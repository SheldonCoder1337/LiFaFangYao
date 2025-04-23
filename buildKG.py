# 
# Created by: Jiale Cai
# Date: 2025-04-01
# 
# you need to run `pip install neo4j, jsonlines` first
#

import sys
import json
import jsonlines
from neo4j import GraphDatabase

def json_loader(file: str) -> list:
    with open(file, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data

def neo4j_connector(
    uri="bolt://localhost:7687", 
    username="neo4j", 
    password="neo4j@soap"
):
    """
    Connect to Neo4j instance.
    """
    driver = GraphDatabase.driver(uri, auth=(username, password))
    return driver

def add_entity(
    tx, 
    entity_name:str, 
    entity_label:str, 
    entity_attributes:dict
):
    """
    Initialize all entity nodes information into the graph database.
    """
    # Add entity attributes
    tx.run(
        f"""
        MERGE (e:`Entity`:`{entity_label}` {{name:$name}})
        SET e += $attributes
        """,
        name=entity_name,
        attributes=entity_attributes,
    )

def add_relation(
    tx, 
    relation:dict,
):
    """
    Create relation between two nodes with given relation files
    """
    relation = list(relation.items())
    source_label = relation[0][0]
    source_name = relation[0][1]
    target_label = relation[1][0]
    target_name = relation[1][1]
    relation_label = relation[2][0]
    relation_name = relation[2][1]

    cypher = f"""
    MERGE (s:`Entity`:`{source_label}` {{name: $source_name}})
    MERGE (t:`Entity`:`{target_label}` {{name: $target_name}})
    MERGE (s)-[:`{relation_name}`]->(t)
    """
    tx.run(cypher, source_name=source_name, target_name=target_name)


if __name__ == "__main__":
    # Neo4j connection
    try:
        driver = neo4j_connector()
    except Exception as e:
        print(f"ERROR: Failed to connect to Neo4j database: {str(e)}", file=sys.stderr)
        sys.exit(1)

    # Data loading
    def load_data(file_path, data_type):
        try:
            return json_loader(file_path)
        except FileNotFoundError:
            print(f"ERROR: {data_type} file not found: {file_path}", file=sys.stderr)
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON format in {data_type} file: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"ERROR: Failed to load {data_type} data: {e}", file=sys.stderr)
            sys.exit(1)

    try:
        symptoms = load_data("./data/symptom.json", "Symptom")
        diseases = load_data("./data/disease.json", "Disease")
        syndromes = load_data("./data/syndrome.json", "Syndrome")
        therapies = load_data("./data/therapy.json", "Therapy")
        formulae = load_data("./data/formulae.json", "Formulae")
        herbs = load_data("./data/herbs.json", "Herbs")
        ingredients = load_data("./data/ingredients.json", "Ingredients")
        references = load_data("./data/reference.json", "References")
        experiments = load_data("./data/experiments.json", "Experiments")
        metas = load_data("./data/metas.json", "Metas")
    except SystemExit:
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Critical data loading failure: {e}", file=sys.stderr)
        sys.exit(1)

    # Entity creation with error resilience
    def batch_create_entities(session, entities, entity_type):
        success = 0
        for entity in entities:
            try:
                session.execute_write(
                    add_entity,
                    entity["name"],
                    entity["label"],
                    entity["attributes"]
                )
                success += 1
            except KeyError as e:
                print(f"WARNING: Skipping invalid {entity_type} entry - missing field: {str(e)}", file=sys.stderr)
            except Exception as e:
                print(f"WARNING: Failed to create {entity_type} node '{entity.get('name','unnamed')}': {str(e)}", file=sys.stderr)
        print(f"STATUS: Processed {entity_type}s - {success} successful / {len(entities)} total")

    with driver.session() as session:
        entity_types = [
            (symptoms, "Symptom"),
            (diseases, "Disease"),
            (syndromes, "Syndrome"),
            (therapies, "Therapy"),
            (formulae, "Formulae"),
            (herbs, "Herb"),
            (ingredients, "Ingredient"),
            (references, "Reference"),
            (experiments, "Experiment"),
            (metas, "Meta")
        ]
        
        for data, label in entity_types:
            batch_create_entities(session, data, label)

    # Relationship processing
    try:
        with open("data/relation.jsonl", "r", encoding="utf-8") as f:
            reader = jsonlines.Reader(f)
            processed = 0
            success = 0
            
            with driver.session() as session:
                for idx, relation in enumerate(reader, 1):
                    try:
                        session.execute_write(add_relation, relation)
                        success += 1
                    except KeyError as e:
                        print(f"WARNING: Invalid relation entry (line {idx}) - missing field: {str(e)}", file=sys.stderr)
                    except Exception as e:
                        print(f"WARNING: Failed to create relation (line {idx}): {str(e)}", file=sys.stderr)
                    processed = idx
                
                print(f"STATUS: Relationship processing - {success} successful / {processed} total")
                
    except FileNotFoundError:
        print("ERROR: Relation file not found: data/relation.jsonl", file=sys.stderr)
        sys.exit(1)
    except jsonlines.JSONDecodeError as e:
        print(f"ERROR: Invalid JSONL format at line {e.lineno}: {e.msg}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Failed to process relations: {str(e)}", file=sys.stderr)
        sys.exit(1)

    # Cleanup
    driver.close()
    print("STATUS: Database initialization completed successfully")

# STATUS: Processed Symptoms - 2444 successful / 2444 total
# STATUS: Processed Diseases - 1167 successful / 1167 total
# STATUS: Processed Syndromes - 1648 successful / 1648 total
# STATUS: Processed Therapys - 764 successful / 764 total
# STATUS: Processed Formulaes - 1089 successful / 1089 total
# STATUS: Processed Herbs - 1603 successful / 1603 total
# STATUS: Processed Ingredients - 1283 successful / 1283 total
# STATUS: Processed References - 6705 successful / 6705 total
# STATUS: Processed Experiments - 2231 successful / 2231 total
# STATUS: Processed Metas - 8032 successful / 8032 total
# STATUS: Relationship processing - 27185 successful / 27185 total
# STATUS: Database initialization completed successfully
