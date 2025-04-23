# 🍃 Li-Fa-Fang-Yao

**`Li-Fa-Fang-Yao`** is a big semantic netowrk dataset of traditional Chinese medicine (TCM).

> Currently, we have open-sourced all semantic types of nodes and publicly available relationship data entries. Due to the large size of the complete entities and relations data, it cannot be uploaded to GitHub. If you need it, please send an email to mc36401@um.edu.mo to explain your purpose.

## 1.Statistics

| Semantic Type| Resource | Total |
| --- | --- | --- |
| Symptoms  | GB/T16751-1-2023-Disease, SymMap | 2444 |
| Diseases  | GB/T16751-1-2023-Disease, UMLS   | 1167 |
| Syndromes | GB/T16751-2-2021-Syndrome | 1648 |
| Therapys  | GB/T16751-3-2023-Therapeutics | 764 |
| Formulaes | GBT31773-2015-Formulae | 1089 |
| Herbs     | GBT31774-2015-Herbs, HERB, ITCM, TCMIO | 1603 |
| Ingredients | PubChem, HERB  | 1283 |
| References  | PubMed  | 6705 |
| Experiments | HERB  | 2231 |
| Relation | References, Literature  | 27185|

## 2.Running

Please run `buildKG.py` to construct `neo4j graph database`, 

Replace with your username and password in the `neo4j_connector` function.

```python
...
def neo4j_connector(
    uri="bolt://localhost:7687", 
    username="neo4j", # Replace with your username
    password="neo4j@soap" # and password
):
    """
    Connect to Neo4j instance.
    """
    driver = GraphDatabase.driver(uri, auth=(username, password))
    return driver
```

## 3.Details

### Symptoms - 2444

- name_cn: standard Chinese name of the symptom (e.g., "头痛" [Headache], "发热" [Fever]).
- name_en: standard English name of the symptom (e.g., "Headache", "Fever").
- name_pinyin: Pinyin spelling of the Chinese symptom name
- clinical_performance: Clinical manifestations or specific characteristics of the symptom (e.g., "paroxysmal stabbing pain", "accompanied by nausea").
- body_part: Anatomical location associated with the symptom (e.g., "head", "abdomen").
- indicator: Relevant clinical biomarkers or diagnostic indicators / Chinese syndrome summary. (e.g., "elevated leukocyte count", "positive CRP").
  
### Diseases - 1167

- name_cn: standard traditional Chinese disease name
- name_en: The translation of the Chinese disease name into English
- pathogenesis: Pathological mechanisms or etiology
- clinical_performance: Typical clinical features
- Disease_name: The official or primary name by which the disease is commonly known.
- Disease_alias_name: A list of alternative names, synonyms, or aliases for the disease, separated by semicolons.
- DisGeNET_disease_type: The type or classification of the disease as categorized in the DisGeNET database.
- UMLS_disease_type: The type of disease as classified in the Unified Medical Language System (UMLS), a comprehensive system for biomedical vocabularies.
- MeSH_disease_class: The class or category of the disease within the Medical Subject Headings (MeSH), which is used for indexing, cataloging, and searching biomedical literature.
- HPO_disease_class: The class or category of the disease within the Human Phenotype Ontology (HPO), which provides a standardized vocabulary for human phenotypic abnormalities.
- DO_disease_class: The class or category of the disease within the Disease Ontology (DO), which offers a classification for human diseases.
- UMLS_disease_type_id: The identifier for the disease type within the UMLS classification system.
- MeSH_disease_class_id: The identifier for the MeSH disease class.
- HPO_disease_class_id: The identifier for the HPO disease class.
- DO_disease_class_id: The identifier for the DO disease class.
- HERB_id: The cross-reference identifier for the disease within the HERB database.
- DisGeNET_id:  The unique identifier for the disease within the DisGeNET database.
- MeSH_id: The cross-reference identifier for the disease within the MeSH database.
- HPO_id: The cross-reference identifier for the disease within the HPO database.
- DO_id: The cross-reference identifier for the disease within the Disease Ontology database.
- ICD10_id: The cross-reference identifier for the disease within the International Classification of Diseases, 10th Revision (ICD-10), which is used for epidemiological purposes and for the clinical coding of diseases.
- OMIM_id: The cross-reference identifier for the disease within the Online Mendelian Inheritance in Man (OMIM) database, which focuses on the genetic aspects of human diseases.

### Syndromes - 1648

- name_cn: standard traditional Chinese syndrome name
- name_en: The translation of the Chinese syndrome name into English
- pathogenesis: Pathological mechanisms or etiology
- clinical_performance: Typical clinical features

### Therapys - 764

- name_cn: Standard Chinese therapy name
- name_en: The translation of the Chinese therapy name into English
- description: Technical details or principles of the therapy
- alias: Alternative names or abbreviations 

### Formulaes - 1089

- name_cn: Standard Chinese formula name 
- source: Historical or literary origin 
- efficacy_class: Pharmacological classification
- composition: Herbal ingredients
- function: Primary therapeutic effects
- indications: Indications for use
- alias: Alternative names

### Herbs - 1603

The herb info file includes all detail information of the 1,603 herbs. The detail of each column are as follows:

- name_cn: The official Chinese name of the herb.
- name_en: The common English name of the herb.
- name_pinyin: The pronunciation of the herb's Chinese name using Pinyin.
- name_latin: The scientific Latin name that classifies the species of the herb.
- name_alias: The alternate names or synonyms of the herb.
- property_cn: A description of the inherent characteristics or 'properties' of the herb, often referring to its nature in TCM, such as being warm, cold, sweet, pungent, etc.
- property_en: The common English translation of the 'property_cn' column.
- meridian_cn: The specific pathways or 'meridians' in the body through which the herb is believed to act, according to TCM theory in Chinese.
- meridian_en: The common English translation of the 'meridian_cn' column.
- usepart_cn: The specific part of the herb that is used for medicinal purposes, such as the root, leaf, seed, or bulb in Chinese.
- usepart_en: The common English translation of the 'usepart_cn' column.
- function_cn: A description of the medicinal functions or 'effects' the herb is traditionally believed to have.
- function_en: The common English translation of the 'function_cn' column.
- indication_cn: The conditions or symptoms for which the herb is traditionally used to treat.
- indication_en: The common English translation of the 'indication_cn' column.
- clinical_manifestations: The observed clinical effects or indications that the herb may address or alleviate.
- toxicity_cn: Information regarding the potential toxicity or side effects of the herb in Chinese.
- toxicity_en: The common English translation of the 'toxicity_cn' column.
- therapeutic_cn: The therapeutic category of the herb in Chinese, providing a cultural and linguistic context for its use.
- therapeutic_en: The therapeutic category of the herb in English, which may include terms like 'blood activation and stasis removal' or 'medicinal for detoxification'.
- HERB_ID: A cross-reference identifier linking the herb to the HERB database.
- TCMID_id: A cross-reference identifier linking the herb to the TCMID database.
- TCM-ID_id: A cross-reference identifier for the herb within the TCM-ID database.
- SymMap_id: A cross-reference identifier for the herb within the SymMap database.
- TCMSP_id: A cross-reference identifier for the herb within the TCMSP database.

### Ingredients - 1283

The ingredient info file includes all detail information of the 1,283 ingredients. The detail of each column are as follows:

- Ingredient_name: The common name by which the ingredient is widely recognized.
- Ingredient_alias_name: A list of alternative names or aliases for the ingredient, separated by semicolons.
- Molecular_formula: The chemical formula representing the molecule's composition.
- Canonical_smiles: A unique representation of the molecular structure in the SMILES (Simplified Molecular-Input Line-Entry System) format.
- Isomeric_smiles: A SMILES string that may differ from the canonical SMILES due to isomerism in the molecule's structure.
- InChIKey: A hashed version of the InChI, used as a compact and web-friendly identifier for the substance.
- MolWt: The molecular weight of the ingredient, a measure of the mass of one mole of the substance.
- NumHAcceptors: The number of hydrogen bond acceptors in the molecule.
- NumHDonors: The number of hydrogen bond donors in the molecule.
- MolLogP: The logarithm of the octanol-water partition coefficient, a measure of the molecule's hydrophobicity.
- NumRotatableBonds: The number of rotatable bonds in the molecule, which can affect its flexibility and pharmacokinetics.
- Drug_likeness: A quantitative measure estimating how closely the ingredient resembles drugs.
- OB_score: The Oral Bioavailability score, indicating the likelihood of the substance being absorbed in the gastrointestinal tract when taken orally.
- CAS_id: A cross-reference identifier for the ingredient in the Chemical Abstracts Service database.
- SymMap_id: A cross-reference identifier linking the ingredient to the SymMap database, which may provide information on the ingredient's effects on biological systems.
- TCMID_id: A cross-reference identifier for the ingredient in the TCMID database.
- TCMSP_id: A cross-reference identifier for the ingredient in the TCMSP database.
- TCM_ID_id: A cross-reference identifier for the ingredient in the TCM-ID database.
- HERB_id: A cross-reference identifier linking the ingredient to the HERB database.
- PubChem_id: A cross-reference identifier for the ingredient in the PubChem database.
- DrugBank_id: A cross-reference identifier for the ingredient in the DrugBank database.
- NPASS_id: A cross-reference identifier for the ingredient in the NPASS database.
- HIT_id: A cross-reference identifier for the ingredient in the HIT 2.0 database.

### References - 6705

The reference info file includes all detail information of the `6,705 papers` records related to drugs (herbs, ingredients, or formulae) in HERB database. The detail of each column are as follows:

- PubMed_id: The identifier for the reference as recorded in the PubMed database, a public database of biomedical literature.
- Subject_name: The name of the herb, ingredient, or formula that is the focus of the reference.
- Subject_type: The type of the subject, which can be an herb, ingredient, or formula.
- Paper_title: The title of the paper or article that the reference pertains to.
- Paper_abstract: A brief summary of the paper's content, including its aims, methods, and findings.
- Journal: The name of the journal in which the paper was published.
- DOI: A unique alphanumeric string assigned to the paper, which provides a persistent link to its location on the internet.
- Publish_date: The date on which the paper was published.
- Experiment_subject: The entity or model used in the experiments described in the paper, such as cell lines, animals, or human subjects.
- Experiment_type: The type of experiment conducted, which could include in vitro studies, animal experiments, clinical trials, etc.
- Phenotype_related: The disease or phenotype that is relevant to the research presented in the paper.

### Experiments - 2231

The experiment info file includes all detail information of the 2,231 experiments related to drugs (herbs, ingredients, or formulae) and diseases. The detail of each column are as follows:

- Subject_disease_name: The common name of the subject or the disease associated with the experiment.
- Subject_disease_id: The unique identifier for the subject or the disease in HERB database.
- Subject_type: The type of the subject, such as 'Herb', 'Ingredient', 'Disease', or 'Formula'.
- GSE_id: The identifier from the NCBI Gene Expression Omnibus (GEO) database for the experiment.
- Organism: The biological organism used in the experiment, for example, 'Homo sapiens' for humans.
- Experiment_type: The general type of experiment conducted, such as 'Expression profiling by array' or 'Expression profiling by high throughput sequencing'.
- Sequence_type: The type of sequencing used in the experiment, if applicable, such as 'total RNA'.
- Experiment_subject: The class of subjects involved in the experiment, which could be humans, animals, cell lines, or tissues.
- Experiment_detail: Additional details about the subjects involved in the experiment.
- Special_pretreatment: Any special pretreatments or conditions that the subjects were subjected to as part of the experiment.
- Control_condition: The conditions under which the control group was kept.
- Control_samples: The samples that serve as the control group in the experiment.
- Experiment_subject_detail: Further details about the subjects of the experiment, such as specific treatments or conditions.
- Treatment_samples: The samples that received the treatment or intervention in the experiment.
- Drug_delivery: The method by which drugs or other treatments were delivered to the subjects.
- Data_type: The data type of the experiment.
- Data_process_pipeline: The specific pipeline used for data processing.
- Platform: Refers to the specific GPL identifier used in the study to denote the microarray platform or sequencing technology utilized for the gene expression analysis.
- Original_id: The original identifier for the experiment in the source database or study.
- Exp_number: A set of experiment identifiers within the same GSE that correspond to a group of experiments under the same experimental conditions, allowing for the grouping and comparison of similar experimental setups.
- Strain: The specific strain of an animal model used in the experiment, if applicable.
- Tissue: The type of tissue sampled in the experiment, if applicable.
- Cell_type: The type of cells used in the experiment, if applicable.
- Cell_line: The specific cell line used in the experiment, if applicable.

## benchmark

In order to further effectively and accurately assess the performance of large models in the field of traditional Chinese medicine (TCM), we have now established a standardized and comprehensive TCM evaluation framework. This evaluation framework will fully take into account the complexity and professionalism of the TCM field, covering multiple aspects to ensure the practicality and applicability of large language models in real-world scenarios.

### Dataset

The dataset includes three categories of multiple-choice questions: Traditional Chinese Medicine (TCM) Diagnosis, TCM Pediatrics, and Internal Medicine. Each category contains up to 100 questions for each of the 16 knowledge points. We will gradually release more test questions and expand this dataset in the future. By collecting, organizing, and annotating these data, we aim to provide a comprehensive, accurate, and representative TCM testing benchmark to help evaluate and improve the performance of large language models in the field of TCM.

### Question Types

- **Best Choice Questions or Single-Choice Questions (Type A)**: Each question consists of a stem and five optional answers labeled A, B, C, D, and E. The stem comes first, followed by the five options. Only one of the five options is the correct answer. Type A questions are divided into two subtypes: Type A1 and Type A2.
- **Single-Sentence Best Choice Questions (Type A1)**: The stem is presented in the form of a statement, which can be affirmative or negative.
- **Case Summary Best Choice Questions (Type A2)**: The stem is a brief case description.
Case Group Best Choice Questions (Type A3): The stem begins with a clinical scenario centered on a patient, followed by several (more than one) related questions. Each question is connected to the initial clinical scenario but tests different key points. The focus of these questions is on clinical application.
- **Standard Matching Questions (Type B1)**: Each question consists of five optional answers labeled A, B, C, D, and E, followed by two or more stems. When answering, one option must be selected for each stem. Each optional answer can be used zero, one, or multiple times.

💥 Note: Since single-sentence best choice questions and case summary best choice questions have similar answer structures, they are combined into one type during testing and labeled as Single-Stem Single-Best-Choice Questions (Type A1/A2).

The statistics of benchmark are as follows:

| Question Type          | Single-Stem Single-Best-Choice Questions (Type A1/A2)| Case Group Best Choice Questions (Type A3)|Standard Matching Questions (Type B1)|
| ------------------ | -------------- | -------------- |-------------- |
| **Number of Questions**           | 1600           | 198         |1481         |
| **Sub-questions**             | \           | 642          | 3231          |

### Data Processing

The questions are transformed into structured evaluation data, with the format shown below:
Single-Stem Single-Best-Choice Questions (Type A1/A2):

```json
 {
      "question": "《素问·咳论》：“五脏六腑皆令人咳”，但关系最密切的是（  ）。\nA．心肺\nB．肺肾\nC．肺脾\nD．肺胃\nE．肺大肠",
      "answer": [
        "D"
      ],
      "analysis": "根据《素问·咳论》“此皆聚于胃，关于肺，使人多涕唾而面浮肿气逆也”可知与五脏六腑皆令人咳关系最密切的脏腑为肺胃。手太阴肺经起于中焦，还循胃口，上膈属肺。寒凉饮食入胃，导致中焦寒，寒气循手太阴肺经上入于肺中，导致肺寒，肺为娇脏，不耐寒热，外内寒邪并聚于肺，则肺失宣降，肺气上逆发生咳嗽。因此答案选D。",
      "knowledge_point": "中医经典",
      "index": 8196,
      "score": 1
    }
```

Case Group Best Choice Questions (Type A3):

```json
    {
      "share_content": "刘×，男，46岁，刻下眩晕而见头重如蒙。胸闷恶心，食少多寐，苔白腻，脉濡滑。",
      "question": [
        {
          "sub_question": "1)．证属（  ）。\nA．肝阳上亢\nB．气血亏虚\nC．肾精不足\nD．痰浊中阻\nE．以上都不是\n",
          "answer": [
            "D"
          ],
          "analysis": ""
        },
        {
          "sub_question": "2)．治法宜选（  ）。\nA．燥湿祛痰，健脾和胃\nB．补肾滋阴\nC．补肾助阳\nD．补养气血，健运脾胃\nE．平肝潜阳，滋养肝肾\n",
          "answer": [
            "A"
          ],
          "analysis": ""
        },
        {
          "sub_question": "3)．方药宜选（  ）。\nA．右归丸\nB．左归丸\nC．半夏白术天麻汤\nD．归脾汤\nE．天麻钩藤饮\n",
          "answer": [
            "C"
          ],
          "analysis": ""
        }
      ],
      "knowledge_point": "中医内科学",
      "index": 334,
      "score": 1
    }
```

Standard Matching Questions (Type B1):

```json
  {
      "share_content": "（共用备选答案）\nA.化痰息风，健脾祛湿\nB.清肺化痰，散结排脓\nC.疏风宣肺，化痰止咳\nD.清热化痰，平肝息风\nE.润肺清热，理气化痰\n",
      "question": [
        {
          "sub_question": "1)．贝母瓜蒌散的功用是（  ）。",
          "answer": [
            "E"
          ],
          "analysis": ""
        },
        {
          "sub_question": "2)．半夏白术天麻汤的功用是（  ）。",
          "answer": [
            "A"
          ],
          "analysis": ""
        }
      ],
      "knowledge_point": "方剂学",
      "index": 1938,
      "score": 1
    }
```

### Prompt Evaluation

We have designed different prompts for each question type, requiring the LLM to answer the questions and provide answers and analyses. The evaluation framework consists of the following components:

| File Name| Description|
| ---| --- |
| /evaluate/A12_bench.py     | Generates answers for single-stem single-best-choice questions |
| /evaluate/A3-B1_bench.py      | Generates answers for case-based best-choice questions and standard matching questions|
| /evaluate/bench_function.py   | Test-related functions |
| /evaluate/correct_analyse.py  | Calculates accuracy |
| /prompt/A1-2_prompt.json| Instruction file for single-stem single-best-choice questions (A1/A2 type)|
| /prompt/A3-4_prompt.json| Instruction file for case-based best-choice questions (A3 type)|
| /prompt/B1_prompt.json| Instruction file for standard matching questions (B1 type)| 
| /models/Openai.py| Calls the OpenAI API |

The fields in the instruction files are as follows:

| Field           | Description|
| --- | --- |
| **type** |Question type|
| **keyword** |Dataset search keyword|
| **prefix_prompt**| Instruction information|

You can generate answers for the three types of questions by running `A12_bench.py` and `A3-B1_bench.py` using different model APIs. We have provided the OpenAI API in the `/models` folder. Other custom model APIs can be placed in this folder for calling.

```python
# First, if necessary, set up a proxy:
os.environ['HTTPS_PROXY']="your proxy"
# Next, fill in your OpenAI Key in the designated location:
openai_api_key = "your key"
# Then, call different models by setting different model_type and model_name.
# The following commands have been run:
python A12_bench.py
python A3-B1_bench.py
```

Finally, you can run `correct_analyse.py` to obtain the model's accuracy score.

```
python correct_analyse.py
```

## Citation

If you use the data from this project, please cite it as follows:

```bash
@misc{cai2025 SOAP,
      title={SOAP:Semantic-Oriented Alignment for Prescription Generation}, 
      author={Jiale Cai},
      year={2025},
      publisher = {GitHub},
      journal = {GitHub repository},
      howpublished = {\url{https://github.com/sheldoncoder1337/SOAP}},
}
```
