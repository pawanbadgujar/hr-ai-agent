import { BrowserRouter, Routes, Route } from "react-router-dom";

import DashboardPage from "../pages/DashboardPage";
import AIChatPage from "../pages/AIChatPage";

function AppRoutes() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<DashboardPage />} />
                <Route path="/chat" element={<AIChatPage />} />
            </Routes>
        </BrowserRouter>
    );
}

export default AppRoutes;