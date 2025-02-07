import faiss
import numpy as np
from app.db.queries import get_menu_data, get_entity_data
from app.services.nlp_service import create_embeddings

# FAISS index for menu data
menu_index = faiss.IndexFlatL2(384)
# FAISS index for entity data
entity_index = faiss.IndexFlatL2(384)

def load_data_into_faiss():
    menu_data = get_menu_data()
    entity_data = get_entity_data()

    menu_descriptions = [row[2] for row in menu_data]
    entity_descriptions = [item[1] for key, value in entity_data.items() for item in value]

    menu_embeddings = create_embeddings(menu_descriptions)
    entity_embeddings = create_embeddings(entity_descriptions)

    menu_index.add(menu_embeddings)
    entity_index.add(entity_embeddings)

def search_faiss_index(query_embedding, index_type="menu"):
    if index_type == "menu":
        D, I = menu_index.search(np.array([query_embedding]), k=1)
        if len(I) > 0 and len(I[0]) > 0:
            menu_rows = get_menu_data()
            menu_result = menu_rows[I[0][0]]
            return {
                "id": menu_result[0],
                "menuLabel": menu_result[1],
                "menuDescription": menu_result[2]
            }
    elif index_type == "entity":
        D, I = entity_index.search(np.array([query_embedding]), k=5)
        if len(I) > 0 and len(I[0]) > 0:
            entity_data = get_entity_data()
            extracted_entities = []
            for idx in I[0]:
                if idx < len(entity_data["batches"]):
                    extracted_entities.append({"batchName": entity_data["batches"][idx][1]})
                elif idx < len(entity_data["batches"]) + len(entity_data["semesters"]):
                    extracted_entities.append({"semName": entity_data["semesters"][idx - len(entity_data["batches"])][1]})
                elif idx < len(entity_data["batches"]) + len(entity_data["semesters"]) + len(entity_data["subjects"]):
                    extracted_entities.append({"subjectName": entity_data["subjects"][idx - len(entity_data["batches"]) - len(entity_data["semesters"])][2]})
                elif idx < len(entity_data["batches"]) + len(entity_data["semesters"]) + len(entity_data["subjects"]) + len(entity_data["departments"]):
                    extracted_entities.append({"departmentName": entity_data["departments"][idx - len(entity_data["batches"]) - len(entity_data["semesters"]) - len(entity_data["subjects"])][1]})
                elif idx < len(entity_data["batches"]) + len(entity_data["semesters"]) + len(entity_data["subjects"]) + len(entity_data["departments"]) + len(entity_data["programs"]):
                    extracted_entities.append({"programName": entity_data["programs"][idx - len(entity_data["batches"]) - len(entity_data["semesters"]) - len(entity_data["subjects"]) - len(entity_data["departments"])][1]})
                elif idx < len(entity_data["batches"]) + len(entity_data["semesters"]) + len(entity_data["subjects"]) + len(entity_data["departments"]) + len(entity_data["programs"]) + len(entity_data["course_types"]):
                    extracted_entities.append({"courseType": entity_data["course_types"][idx - len(entity_data["batches"]) - len(entity_data["semesters"]) - len(entity_data["subjects"]) - len(entity_data["departments"]) - len(entity_data["programs"])][1]})
            return extracted_entities
    return None