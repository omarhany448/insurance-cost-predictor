import gradio as gr
import joblib
import pandas as pd

model = joblib.load("model.pkl")

def predict_cost(age, sex, bmi, children, smoker, region):
    input_data = pd.DataFrame({
        'age': [age],
        'sex_male': [1 if sex == 'male' else 0],
        'bmi': [bmi],
        'children': [children],
        'smoker_yes': [1 if smoker == 'yes' else 0],
        'region_northwest': [1 if region == 'northwest' else 0],
        'region_southeast': [1 if region == 'southeast' else 0],
        'region_southwest': [1 if region == 'southwest' else 0],
    })

    input_data = input_data[model.feature_names_in_]
    prediction = model.predict(input_data)[0]
    return f"Estimated Insurance Cost: ${prediction:,.2f}"

def clear_inputs():
    return 30, None, 25, 1, None, None, ""

custom_css = """
button {
    background-color: #ff7f0e !important;
    color: white !important;
}
"""

with gr.Blocks(title="Health Insurance Cost Prediction", css=custom_css) as demo:
    gr.Markdown("## Health Insurance Cost Prediction")
    gr.Markdown("Enter your personal details to estimate your expected health insurance cost.")

    with gr.Row():
        with gr.Column():
            age = gr.Number(label="Age", value=30)
            sex = gr.Radio(["male", "female"], label="Sex")
            bmi = gr.Number(label="BMI", value=25)
        with gr.Column():
            children = gr.Number(label="Children", value=1)
            smoker = gr.Radio(["yes", "no"], label="Smoker")
            region = gr.Dropdown(["southeast", "southwest", "northwest", "northeast"], label="Region")

    output = gr.Textbox(label="Prediction Result")

    with gr.Row():
        predict_btn = gr.Button("Predict")
        clear_btn = gr.Button("Clear")

    predict_btn.click(fn=predict_cost, inputs=[age, sex, bmi, children, smoker, region], outputs=output)
    clear_btn.click(fn=clear_inputs, inputs=[], outputs=[age, sex, bmi, children, smoker, region, output])

demo.launch()