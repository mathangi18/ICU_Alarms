This repository contains my solution for the VTAC alarm classification assignment in the course
AI and ML 2011 – Applied Machine Learning and Data Mining (KTH).

The goal of this assignment is to predict whether an ICU alarm corresponds to a True or False ventricular tachycardia event, using structured data and waveform-derived features.

📂 Repository Contents

1. Mathangi_Chandrasekaran_Assignment1.ipynb

The main submission notebook.
Contains:
	Data exploration before cleaning
	Data cleaning and preprocessing (fully documented)
	Missing data analysis and imputation comparison
	Feature engineering from waveform data
	Multiple baseline models and comparisons
	Feature importance analysis
	Clear discussion of results and limitations

2. extract_waveform_features.py

Helper script used to extract simple statistical features from raw waveform files
(included for transparency and reproducibility).

3.README.md
This file.

📊 Dataset

VTAC: A Benchmark Dataset of Ventricular Tachycardia Alarms
Provided via PhysioNet.

The dataset includes:
	Event-level alarm annotations (True / False)
	Predefined train / validation / test splits
	Raw waveform recordings associated with alarm events
	Only data from the provided VTAC dataset was used.
	No external datasets or labels were introduced.

🔬 Methodology Overview

1. Binary classification: True vs False alarm
2. Exploratory data analysis performed before any cleaning
3. Careful documentation of all preprocessing decisions

Comparison of:
	No imputation vs imputation strategies
	Metadata-only features vs waveform-derived features
	Emphasis on interpretability and reproducibility
	No deep learning models were used, in line with dataset size, assignment scope, and course focus

All reasoning and decisions are explained step-by-step in the notebook.

⚠️ Notes on Reproducibility

Raw waveform files are large and not stored in this repository.
The notebook documents how waveform features were extracted and merged.
Paths and assumptions are explicitly stated so the analysis can be reproduced locally if desired.

📚 Citations

1. Lehman, L. H., Moody, B., Deep, H., Wu, F., Saeed, H., McCullum, L., Perry, D., Struja, T., Li, Q., Clifford, G., & Mark, R. (2024).  
   *VTAC: A Benchmark Dataset of Ventricular Tachycardia Alarms from ICU Monitors (version 1.0).*  
   PhysioNet. https://doi.org/10.13026/8td2-g363
2. Goldberger, A. L., Amaral, L. A. N., Glass, L., Hausdorff, J. M., Ivanov, P. C., Mark, R. G., Mietus, J. E., Moody, G. B., Peng, C. K., & Stanley, H. E. (2000).  
   *PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals.*  
   Circulation, 101(23), e215–e220.
3. Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., et al. (2011).  
   *Scikit-learn: Machine Learning in Python.*  
   Journal of Machine Learning Research, 12, 2825–2830.  
   https://scikit-learn.org/
4. Shalev-Shwartz, S., & Ben-David, S. (2014).  
   *Understanding Machine Learning: From Theory to Algorithms.*  
   Cambridge University Press.  
   (Referenced for binary classification, empirical risk minimization, and generalization concepts.)
5. Hastie, T., Tibshirani, R., & Friedman, J. (2009).  
   *The Elements of Statistical Learning.*  
   Springer.  
   (Referenced for logistic regression, bias–variance tradeoff, and model interpretability.)
6. Raschka, S., Mirjalili, V. (2019).  
   *Python Machine Learning (3rd ed.).*  
   Packt Publishing.  
   (Referenced for best practices in model evaluation, feature importance, and handling class imbalance.)
7. Powers, D. M. W. (2011).  
   *Evaluation: From Precision, Recall and F-Measure to ROC, Informedness, Markedness and Correlation.*  
   Journal of Machine Learning Technologies, 2(1), 37–63.  
   (Referenced for the choice of F1-score in imbalanced classification problems.)
8. Marcus, G. (2018).  
   *Deep Learning: A Critical Appraisal.*  
   arXiv:1801.00631.  
   (Referenced to justify avoiding deep learning models given dataset size, interpretability goals, and assignment scope.)
9. KTH Royal Institute of Technology.  
   *AI and ML 2011 – Applied Machine Learning and Data Mining.*  
   Course lectures, syllabus, and assignment materials.

👤 Author

	Mathangi Chandrasekaran
	Course: AI and ML 2011
	MSc Data Driven Health
	KTH Royal Institute of Technology
