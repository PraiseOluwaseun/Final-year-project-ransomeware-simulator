from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import matplotlib.pyplot as plt
import os

def generate_report(logs, features, prediction, lime, shap):
    file_name = "reports/ransomware_report.pdf"
    styles = getSampleStyleSheet()
    story = []

    # 1. Title & Prediction
    story.append(Paragraph("Ransomware Detection Report", styles['Heading1']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Final Prediction: {prediction}", styles['Heading2']))
    story.append(Spacer(1, 12))

    # 2. Generate Graph Image for PDF
    plt.figure(figsize=(6, 4))
    labels = ["CPU", "Mem", "Disk", "Proc", "Net", "Susp"]
    plt.bar(labels, features, color='skyblue')
    plt.title("System Behaviour Snapshot")
    graph_path = "reports/temp_graph.png"
    plt.savefig(graph_path)
    plt.close()

    story.append(Paragraph("System Behaviour Graph:", styles['Heading2']))
    story.append(Image(graph_path, width=400, height=250))
    story.append(Spacer(1, 12))

    # 3. Features & Logs
    story.append(Paragraph("Activity Logs:", styles['Heading2']))
    for log in logs:
        story.append(Paragraph(f"• {log}", styles['Normal']))
    
    story.append(Spacer(1, 12))

    # 4. Explanations (LIME & SHAP)
    story.append(Paragraph("LIME Explanation:", styles['Heading2']))
    for item in lime:
        story.append(Paragraph(str(item), styles['Normal']))

    story.append(Spacer(1, 12))
    story.append(Paragraph("SHAP Values:", styles['Heading2']))
    story.append(Paragraph(str(shap), styles['Normal']))

    # Build PDF
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    doc.build(story)
    
    # Cleanup temp graph
    if os.path.exists(graph_path):
        os.remove(graph_path)

    return file_name