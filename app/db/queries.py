from app.db.connection import execute_query

def get_menu_data():
    query = "SELECT id, label AS menuLabel, description AS menuDescription FROM college_menu_items WHERE module ='EXAM_CONTROLLER' AND name LIKE '%REPORT%'"
    return execute_query(query)

def get_entity_data():
    queries = {
        "batches": "SELECT id, name AS batchName FROM `groups` WHERE type ='BATCH'",
        "semesters": "SELECT id, name AS semName FROM academic_term",
        "subjects": "SELECT id, code AS subjectCode, name AS subjectName FROM v4_ams_subject",
        "departments": "SELECT deptID as id, deptName as departmentName, departmentDesc AS departmentDescription FROM department",
        "programs": "SELECT id, name as programName FROM program",
        "course_types": "SELECT courseTypeID as id, typeName as courseType FROM course_type"
    }

    entities = {key: execute_query(query) for key, query in queries.items()}
    return entities