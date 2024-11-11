import gradio as gr

# Define the function that will handle the conversion
def nep_inr(nep_val):
    x = nep_val * 0.63
    return x

# Create a Gradio interface
interface = gr.Interface(fn=nep_inr, 
                         inputs=gr.Number(label="Enter the amount in Nepalese currency (NPR)"),
                         outputs=gr.Number(label="Converted amount in INR"))

# Launch the interface
interface.launch(share=True)
