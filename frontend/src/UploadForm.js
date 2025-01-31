import React, { useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const UploadForm = () => {
    const { country } = useParams();  // Get country from URL
    const [image, setImage] = useState(null);
    const [result, setResult] = useState(null);
    const navigate = useNavigate();

    const handleFileChange = (event) => {
        setImage(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!image) return;

        const formData = new FormData();
        formData.append("image", image);

        try {
            const response = await axios.post(`http://127.0.0.1:5000/predict/${country}`, formData);
            setResult(response.data);
        } catch (error) {
            console.error("Error:", error);
        }
    };

    return (
        <div style={{ textAlign: "center", marginTop: "50px" }}>
            <h2>Upload a Traffic Sign Image for {country.toUpperCase()}</h2>
            <input type="file" onChange={handleFileChange} />
            <br /><br />
            <button onClick={handleSubmit} style={{ padding: "10px 20px" }}>
                Predict
            </button>
            <br /><br />
            {result && (
                <div>
                    <h3>Predicted Sign: {result.predicted_sign}</h3>
                    <p>Confidence: {result.confidence.toFixed(2)}</p>
                </div>
            )}
            <br />
            <button onClick={() => navigate("/")} style={{ padding: "10px 20px" }}>
                Back to Home
            </button>
        </div>
    );
};

export default UploadForm;
