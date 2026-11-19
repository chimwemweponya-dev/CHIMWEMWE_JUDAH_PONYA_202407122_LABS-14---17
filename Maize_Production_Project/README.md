# Maize Production Analysis

## Project Description
This project analyses maize production using Python.

## Requirements
pip install -r requirements.txt

## How to Run
1. Open the project folder.
2. Open the notebooks folder.
3. Open maize_analysis.ipynb.
4. Run all notebook cells.

## Project Consultation Questions

1. **What problem are you investigating?**
   Maize is Zambia's staple crop, and production varies widely between districts and seasons. This project analyses those patterns and what drives them.

2. **Why did you choose this topic?**
   Maize is important for food security and the economy, data is available, and the topic lets me apply the whole course: descriptive statistics, modelling, visualization and a dashboard.

3. **What are your research objectives?**
   - Collect and clean maize production data.
   - Calculate descriptive statistics.
   - Analyse production patterns.
   - Build a statistical model.
   - Visualize the results.
   - Develop an interactive dashboard.
   - Present findings and recommendations.

4. **Where will you obtain your data?**
   From the Zambia Statistics Agency (ZamStats), Ministry of Agriculture crop forecast surveys, or FAOSTAT. If real data is not available, I will use a simulated dataset with a fixed random seed.

5. **Which statistical methods will you use?**
   Descriptive statistics, regression (production against factors such as rainfall), and bootstrapping for uncertainty. Optionally Monte Carlo simulation or a Gaussian Mixture Model to group districts.

6. **Which Python libraries will you require?**
   NumPy, Pandas, Matplotlib, SciPy, Scikit-learn and Streamlit (PyMC and ArviZ if Bayesian methods are used).

7. **How will you evaluate your results?**
   Model fit (R² and residuals), bootstrap confidence intervals, and train/test performance. I will also check that the findings agree with known agricultural patterns.

8. **How will you make your research reproducible?**
   Fixed random seeds, a clean notebook, an organized folder (`data/`, `notebooks/`, `src/`, `dashboard/`, `outputs/`), a README, `requirements.txt`, and an nbconvert HTML export.

9. **What challenges do you expect?**
   Missing or inconsistent data, few years of records per district, outliers from drought years, and the time needed to build the dashboard.

10. **What contribution will your project make?**
    A clear, reproducible analysis of district maize production and an interactive dashboard that makes the results easy for farmers, planners and students to explore.

## Author
Chimwemwe Judah Ponya
