import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const searchMenu = async (query) => {
    try {
        const response = await axios.post(`${API_URL}/search_menu`, { query });
        return response.data;
    } catch (error) {
        console.error("Error searching menu:", error);
        throw error;
    }
};

export const extractEntities = async (query) => {
    try {
        const response = await axios.post(`${API_URL}/extract_entities`, { query });
        return response.data;
    } catch (error) {
        console.error("Error extracting entities:", error);
        throw error;
    }
};