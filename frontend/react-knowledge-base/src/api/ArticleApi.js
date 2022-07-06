import { GET_REQUEST, POST_REQUEST } from "./Requests";

const API_URL = "http://localhost:5000";

export const getAllArticles = GET_REQUEST(API_URL + "/articles");
