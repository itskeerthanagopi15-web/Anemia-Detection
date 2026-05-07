from flask import Flask, render_template, request, jsonify
import numpy as np
from PIL import Image

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['image']
        image = Image.open(file)

        processed_image = preprocess_image(image)

        prediction = model.predict(processed_image)

        probability = float(prediction[0][0])
        confidence = probability * 100

        if probability > 0.5:
            status = "Anemia Detected"

            if confidence > 90:
                severity = "Severe Anemia"
                hemoglobin = "7.5"
            elif confidence > 70:
                severity = "Moderate Anemia"
                hemoglobin = "9.0"
            else:
                severity = "Mild Anemia"
                hemoglobin = "10.5"
        else:
            status = "Normal"
            severity = "Healthy"
            hemoglobin = "13.5"

        conn = sqlite3.connect("predictions.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO history (date, status, hemoglobin, severity, confidence)
            VALUES (?, ?, ?, ?, ?)
        """, (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status,
            hemoglobin,
            severity,
            round(confidence, 2)
        ))

        conn.commit()
        conn.close()

    
        return jsonify({
            "status": status,
            "hemoglobin": hemoglobin,
            "severity": severity,
            "confidence": round(confidence, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)})


