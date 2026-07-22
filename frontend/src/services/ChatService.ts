import api from "../api/client";

export const sendMessage = async (message: string) => {

    const response = await api.post(
        `/chat/?query=${encodeURIComponent(message)}`
    );

    return response.data;

};