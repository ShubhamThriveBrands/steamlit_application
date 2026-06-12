import streamlit as st
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path
import pandas as pd
import time

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="DataHive Notebook Runner",
    layout="wide"
)

st.title("🚀 DataHive Notebook Runner")

# =====================================================
# NOTEBOOK FOLDER
# =====================================================

NOTEBOOK_FOLDER = Path("notebooks")

notebooks = sorted(
    list(NOTEBOOK_FOLDER.glob("*.ipynb"))
)

if not notebooks:
    st.error("❌ No notebooks found in notebooks folder.")
    st.stop()

# =====================================================
# NOTEBOOK SELECTION
# =====================================================

selected_notebooks = st.multiselect(
    "Select Notebooks",
    notebooks,
    format_func=lambda x: x.name
)

col1, col2 = st.columns(2)

run_selected = col1.button("▶ Run Selected")
run_all = col2.button("🚀 Run All")

# =====================================================
# EXECUTION
# =====================================================

if run_selected or run_all:

    notebooks_to_run = (
        selected_notebooks
        if run_selected
        else notebooks
    )

    if len(notebooks_to_run) == 0:
        st.warning("Please select at least one notebook.")
        st.stop()

    # Live widgets
    progress_bar = st.progress(0)
    current_notebook = st.empty()
    live_logs = st.empty()

    logs = []

    results = []

    total_notebooks = len(notebooks_to_run)

    start_pipeline = time.time()

    for idx, notebook in enumerate(notebooks_to_run):

        notebook_name = notebook.name

        current_notebook.info(
            f"🔄 Running Notebook {idx+1}/{total_notebooks}\n\n"
            f"📒 {notebook_name}"
        )

        logs.append(
            f"\n{'='*70}"
        )

        logs.append(
            f"Notebook {idx+1}/{total_notebooks}"
        )

        logs.append(
            f"Started: {notebook_name}"
        )

        live_logs.text("\n".join(logs))

        notebook_start = time.time()

        try:

            with open(
                notebook,
                "r",
                encoding="utf-8"
            ) as f:

                nb = nbformat.read(
                    f,
                    as_version=4
                )

            ep = ExecutePreprocessor(
                timeout=7200,
                kernel_name="python3"
            )

            ep.preprocess(
                nb,
                {
                    "metadata": {
                        "path": notebook.parent
                    }
                }
            )

            runtime = round(
                time.time() - notebook_start,
                2
            )

            logs.append(
                f"✅ SUCCESS ({runtime}s)"
            )

            results.append({
                "Notebook": notebook_name,
                "Status": "SUCCESS",
                "Runtime (sec)": runtime
            })

        except Exception as e:

            runtime = round(
                time.time() - notebook_start,
                2
            )

            logs.append(
                f"❌ FAILED ({runtime}s)"
            )

            logs.append(
                f"Error: {str(e)}"
            )

            results.append({
                "Notebook": notebook_name,
                "Status": "FAILED",
                "Runtime (sec)": runtime
            })

        progress_bar.progress(
            (idx + 1) / total_notebooks
        )

        live_logs.text(
            "\n".join(logs)
        )

    # =====================================================
    # FINAL SUMMARY
    # =====================================================

    total_runtime = round(
        time.time() - start_pipeline,
        2
    )

    current_notebook.success(
        "🎉 All Notebook Execution Finished"
    )

    st.divider()

    st.subheader("📊 Execution Summary")

    results_df = pd.DataFrame(results)

    st.dataframe(
        results_df,
        use_container_width=True
    )

    success_count = (
        results_df["Status"] == "SUCCESS"
    ).sum()

    fail_count = (
        results_df["Status"] == "FAILED"
    ).sum()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Notebooks",
        len(results_df)
    )

    col2.metric(
        "Successful",
        success_count
    )

    col3.metric(
        "Failed",
        fail_count
    )

    st.success(
        f"⏱ Total Pipeline Runtime: {total_runtime} seconds"
    )