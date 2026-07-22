import api from "./api";

export const sendMessage = async (query: string) => {

    const response = await api.post(
        `/chat/?query=${encodeURIComponent(query)}`
    );

    return response.data;
};