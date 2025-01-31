import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./Home";
import UploadForm from "./UploadForm";

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/upload/:country" element={<UploadForm />} />
            </Routes>
        </Router>
    );
};

export default App;
