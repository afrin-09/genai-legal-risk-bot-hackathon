import streamlit as st
from backend.parser import extract_text
from backend.clause_extractor import split_into_clauses
from backend.risk_engine import assess_risk
from backend.llm_engine import explain_clause_simple
from backend.pdf_exporter import generate_pdf_summary


st.set_page_config(
    page_title="GenAI Legal Assistant",
    layout="wide"
)

st.title("📄 GenAI Contract Analysis & Risk Assessment Bot")

st.write("""
Welcome!  
Upload a contract document (PDF, DOCX, or TXT) to:
- Identify risky clauses  
- Understand them in simple business language  
- Get SME-friendly insights  
""")

uploaded_file = st.file_uploader(
    "Upload a contract file",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:
    st.success(f"File uploaded successfully: {uploaded_file.name}")

    file_type = uploaded_file.name.split(".")[-1].lower()

    # -------- TEXT EXTRACTION --------
    with st.spinner("Extracting text from contract..."):
        contract_text = extract_text(uploaded_file, file_type)

    st.success("Contract text extracted successfully!")

    st.subheader("📃 Extracted Contract Text")
    st.text_area(
        "Contract Content",
        contract_text,
        height=300
    )

    # -------- CLAUSE DETECTION --------
    st.subheader("📌 Detected Clauses")

    clauses = split_into_clauses(contract_text)

    if not clauses:
        st.warning("No clauses detected. Please try another document.")
    else:
        for clause in clauses:
            risk = assess_risk(clause["text"])

            if risk == "High":
                color = "🔴"
            elif risk == "Medium":
                color = "🟠"
            else:
                color = "🟢"

            with st.expander(
                f"{color} Clause {clause['id']} — {clause['type']} — Risk: {risk}"
            ):
                st.write("**Original Clause Text:**")
                st.write(clause["text"])

                if risk in ["High", "Medium"]:
                    st.info("🧠 AI Explanation (sample output shown due to API limits)")
                    st.markdown("""
                - This clause gives one party more control than the other.
                - It may expose the business to unexpected penalties or obligations.
                - Small businesses should consider negotiating clearer or balanced terms.
                - Legal review is recommended before signing.
                """)

        # -------- CONTRACT RISK SUMMARY (ADD HERE) --------
        st.subheader("📊 Contract Risk Summary")

        total_clauses = len(clauses)
        high_risk = sum(1 for c in clauses if assess_risk(c["text"]) == "High")
        medium_risk = sum(1 for c in clauses if assess_risk(c["text"]) == "Medium")

        overall_risk = "Low"
        if high_risk >= 2:
            overall_risk = "High"
        elif medium_risk >= 2:
            overall_risk = "Medium"

        st.markdown(f"""
**Total Clauses:** {total_clauses}  
🔴 **High Risk:** {high_risk}  
🟠 **Medium Risk:** {medium_risk}  
🟢 **Overall Contract Risk:** **{overall_risk}**
""")

        if st.button("📄 Download Risk Summary as PDF"):
            summary_data = {
                "Total Clauses": total_clauses,
                "High Risk Clauses": high_risk,
                "Medium Risk Clauses": medium_risk,
                "Overall Risk Level": overall_risk
            }

            pdf_file = "contract_risk_summary.pdf"
            generate_pdf_summary(pdf_file, summary_data)

            with open(pdf_file, "rb") as f:
                st.download_button(
                    label="⬇️ Download PDF",
                    data=f,
                    file_name=pdf_file,
                    mime="application/pdf"
                )

