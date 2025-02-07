# AI-Powered Semantic Search for Academic Management System

## Objective

Develop an industry standard AI-powered semantic search that enables intelligent, typo-tolerant, and context-aware menu navigation in our academic management system. The AI will dynamically process user queries, extract structured data, and provide accurate menu suggestions while maintaining scalability and adaptability to future changes.

## System Overview

**Existing Stack:** PHP, Vue.js, MySQL

**AI Backend:** Python (FastAPI) communicating via API

**Database:** MySQL (Existing Academic System), AI will synchronize with it

**Search Type:** AI-powered natural language processing (NLP) with semantic understanding

**Data Handling:** Continuous sync with dynamic datasets like menus, subjects, degrees, course types, batch names, semesters, departments, etc.

## Phase 1: AI-Powered Menu Search

### Requirements

1. **User Query Understanding:** AI should allow users to search in a meaningful way, even with typos or misspellings.
2. **Dynamic Menu Recognition:** AI should map search queries to the most relevant system menu based on provided menu descriptions and aliases.
3. **Independent of Fixed Data:** The system must not hardcode menu names; it should dynamically fetch data from the database.
4. **Scalability:** The AI should scale efficiently as new menus and terms are introduced.

### Sample Menu Data (for training)

| ID  | Menu Description       | Alias                    | Department        |
|-----|------------------------|--------------------------|-------------------|
| 158 | Revaluation Report     | REVALUATION_REPORT       | EXAM_CONTROLLER   |
| 170 | Grace Mark Report      | GRACE_MARK_REPORT        | EXAM_CONTROLLER   |
| 176 | Supplementary Report   | SUPPLEMENTARY_REPORT     | EXAM_CONTROLLER   |

## Phase 2: AI-Powered Entity Extraction

### Example Use Case

**User searches:** "BCOMA 2022 6th Sem Regular Markcard"

**AI should intelligently extract:**
- **Menu:** Regular Semester Mark Card
- **Batch:** BCOMA
- **Batch Start Year:** 2022
- **Semester:** 6th Semester

**AI should confirm intent:**
"Are you looking for BCOMA 2022 Batch Regular Semester Mark Card?"

**On confirmation, generate the required report.**

### Required Capabilities

1. **Entity Recognition:** Extract meaningful batch names, semesters, degrees, departments, etc., from queries.
2. **Data Synchronization:** The AI system must fetch real-time updates from MySQL.
3. **Handling Variations:** AI must recognize variations like:
   - "Sixth Sem" → "6th Semester"
   - "BComA 2022" → "BCOMA 2022"
   - "Reval report" → "Revaluation Report"

### Data Sources

- **Menus:** Dynamic List from System
- **Departments:** `department.csv` Sample Data
- **Semesters:** `semesters.csv` Sample Data
- **Batch Names:** `batchnames.csv` Sample Data

### Example Data Extracted from System

- **Departments:** "Computer Science", "Commerce", "Library and Information Center"
- **Semesters:** "S1", "First Year", "Fourth Year", "Passout Students"
- **Batch Names:** "BSC-BCMZ-2024", "BBA-REG-2025 (SHIFT III)"

## Technical Considerations

### Scalability

- AI must handle thousands of queries daily with low latency.
- API-first approach for seamless integration with PHP & Vue.js.

### AI Model Selection

- Use sentence-transformers for semantic search.
- Implement FAISS for fast vector search indexing.

### Error Handling & Query Refinement

- Implement fuzzy matching for typos and spelling mistakes.
- Use context-awareness to refine incorrect queries.

### Deployment & Performance Optimization

- Run FastAPI with Uvicorn for high-speed API responses.
- Optimize embedding models to balance speed vs accuracy.

## Next Steps

1. **Develop AI Model:**
   - Train on existing menu and academic data.
   - Implement semantic search using FAISS & transformers.
2. **Build API Layer:**
   - Develop endpoints for menu search & entity extraction.
3. **Sync Data with MySQL:**
   - Ensure automatic updates as data grows dynamically.
4. **Test & Optimize:**
   - Validate AI predictions with real user queries.
   - Fine-tune for accuracy & speed.

## Final Goal

A fast, AI-powered semantic search engine for the academic system that:
- Accurately understands user queries (even with typos).
- Handles dynamic data updates without code modifications.
- Seamlessly integrates with the existing PHP & Vue.js web application.
- Follows scalable, industry-standard best practices (as of 2025).