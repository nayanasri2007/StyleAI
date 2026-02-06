from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["UPLOAD_FOLDER"] = "static/uploads"

@app.route("/", methods=["GET", "POST"])
def index():
    skin_tone = None
    recommendation = None

    if request.method == "POST":
        image = request.files["image"]
        gender = request.form["gender"]

        if image:
            filename = image.filename.lower()
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            # Simple AI-style logic
            if "fair" in filename:
                skin_tone = "Fair"
            elif "dark" in filename or "deep" in filename:
                skin_tone = "Deep"
            elif "olive" in filename:
                skin_tone = "Olive"
            else:
                skin_tone = "Medium"

            if gender == "female":
                recommendation = (
                    "Pastel tops, floral dresses, soft makeup shades, "
                    "silver or pearl accessories."
                )
            else:
                recommendation = (
                    "Neutral shirts, denim jeans, earthy colors, "
                    "leather shoes or sneakers."
                )

    return render_template(
        "index.html",
        skin_tone=skin_tone,
        recommendation=recommendation
    )

if __name__ == "__main__":
    app.run(debug=True)