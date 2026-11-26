from groq import generate_response

import io, streamlit as st

SYSTEM_PROMPT="""You are a Math Mastermind. For every math problem:

1) Show step-by-step solution 2) Explain reasoning 3) Give alternate method if possible

4) Verify answer if possible 5) Use proper notation 6) Break complex problems into parts

Format: Problem → Steps → **Final Answer** → Concepts used. Be precise and educational."""

def math_generate(problem:str,level:str,temperature=0.1,max_tokens=1024) -> str:
    prompt=f"{SYSTEM_PROMPT}\n\nMath Problem ({level}): {problem}"
    return generate_response(prompt, temperature=temperature, max_tokens=1024)

def export_txt(history):
    txt="\n\n".join([f"q{i}: {h['q']}\nA{i}: {h['a']}" for i,h in enumerate(history,1)])
    return io.BytesIO(txt.encode("utf-8"))

def setup_ui():
    st.set_page_config(page_title="Math Mastermind", layout="centered")
    st.title("Math Mastermind")
    st.write("Solve any math problem with detailed step-by-step explanation.")

    with st.expander("Examples"):
        st.markdown(
            '- Algebra: "Solve 2x² + 5x − 3 = 0"\n'

            '- Calculus: "Derivative of sin(x²) + ln(x)"\n'

            '- Geometry: "Area of triangle (0,0),(3,4),(6,0)"\n'

            '- Probability: "P(sum=7 with two dice)"')

        st.session_state.setdefault("history", [])
        st.session_state.setdefault("k", 0)

        c1,c2=st.columns([1,2])
        if c1.button("Clear"):
            st.session_state.history=[]; st.rerun()

        if st.session_state.history:
            c2.download_button("Export", export_txt(st.session_state.history),
                               "Math_Mastermind_solutions.txt", "text/plain")

        with st.form