import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Home = () => {
    const [country, setCountry] = useState("germany");
    const navigate = useNavigate();

    const handleStart = () => {
        navigate(`/upload/${country}`);  //uploading files page
    };

    return (
        <div style={{ textAlign: "center", marginTop: "50px" }}>
            <h1>Welcome to Traffic Sign Classifier</h1>
            <p>Select a country to begin</p>
            <select value={country} onChange={(e) => setCountry(e.target.value)}>
                <option value="germany">Germany</option>
                <option value="usa">USA</option>
            </select>
            <br /><br />
            <button onClick={handleStart} style={{ padding: "10px 20px" }}>
                Continue
            </button>
        </div>
    );
};

export default Home;
