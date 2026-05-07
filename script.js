document.addEventListener("DOMContentLoaded", function () {

    console.log("JS Loaded");

    const predictBtn = document.getElementById("predictBtn");
    const fileInput = document.getElementById("fileInput");

    predictBtn.addEventListener("click", async function () {

        console.log("Button Clicked");

        const file = fileInput.files[0];

        if (!file) {
            alert("Please upload an image first.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await fetch("/predict", {
                method: "POST",
                body: formData
            });

            const data = await response.json();

alert(
    "Hemoglobin Report\n\n" +
    "Estimated Hb: " + data.estimated_hb + " g/dL\n" +
    "Status: " + data.status + "\n" +
    "Severity: " + data.severity + "\n" +
    "Anemia Risk: " + data.anemia_percentage + "%\n\n" +
    "Recommendation:\n" + data.recommendation
);


        } catch (error) {
            console.error("Error:", error);
            alert("Prediction failed.");
        }

    });

});
<script>
function previewImage(event) {
    let reader = new FileReader();
    reader.onload = function(){
        let output = document.getElementById('preview');
        output.src = reader.result;
        output.style.display = "block";
    };
    reader.readAsDataURL(event.target.files[0]);
}


async function predictImage() {

    document.getElementById("result").innerHTML = "Analyzing image...";

    let fileInput = document.getElementById("imageInput");
    let formData = new FormData();
    formData.append("image", fileInput.files[0]);

    let response = await fetch("/predict", {
        method: "POST",
        body: formData
    });

    let data = await response.json();

    document.getElementById("result").innerHTML =
        "Status: " + data.status + "<br>" +
        "Hemoglobin: " + data.hemoglobin + " g/dL<br>" +
        "Severity: " + data.severity + "<br>" +
        "Confidence: " + data.confidence + "%";
}
</script>
