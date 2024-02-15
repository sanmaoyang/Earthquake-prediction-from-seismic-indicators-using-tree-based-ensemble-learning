<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="image/logo.png" alt="Logo" width="600" height="300">
  </a>

  <h3 align="center">Earthquake prediction from seismic indicators using tree-based ensemble learning</h3>

  <p align="center">
    Yang Zhao and Denise Gorse
    <br />
    <a href="https://github.com/sanmaoyang/Earthquake-prediction-from-seismic-indicators-using-tree-based-ensemble-learning"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/sanmaoyang/Earthquake-prediction-from-seismic-indicators-using-tree-based-ensemble-learning/issues">Report Bug</a>
    ·
    <a href="https://github.com/sanmaoyang/Earthquake-prediction-from-seismic-indicators-using-tree-based-ensemble-learning/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-repository">About The Repository</a>
      <ul>
        <li><a href="#development-environment">Development Environment</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Repository 

This is the source code for the Natural Hazards paper：

|  | Info |
|-:|:-----|
| Title | Earthquake prediction from seismic indicatorsusing tree-based ensemble learning |
| Author| Yang Zhao & Denise Gorse |
| Corresponding Author | Denise Gorse |
| Link |https://link.springer.com/article/10.1007/s11069-023-06221-5|
| Availability of data | https://figshare.com/articles/Earthquake_Prediction_using_SVR_and_HNN/6406814.|

<p align="right">(<a href="#readme-top">back to top</a>)</p>


###  Development Environment

|  | Info |
|-:|:-----|
| Operating system | Ubuntu (WSL2) |
| CPU| AMD R7-3700x 3.6GHz - 8 core |
|  Programming Language | Python |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Abstract -->
## Abstract
Earthquake prediction is a challenging research area, but the use of a variety of machine learning models, together with a range of seismic indicators as inputs, has over the last decade led to encouraging progress, though the variety of seismic indicator features within any given study has been generally quite small. Recently, however, a multistage, hybrid learning model has used a total of 60 seismic indicators, applying this to data from three well-studied regions, aiming to predict earthquakes of magnitude 5.0 or above, up to 15 days before the event. In order to determine whether the encouraging results of this prior work were due to its learning model or to its expanded feature set we apply a range of tree-based ensemble classifiers to the same three datasets, showing that all these classifiers outperform the original, more complex model (with CatBoost as the best-performing), and hence that the value of this prior approach likely lay mostly in its range of presented features. We then use feature rankings from Boruta-Shap to discover the most valuable of these 60 features for each of the three regions, and challenge our optimized models to predict earthquakes of larger magnitudes, demonstrating their resilience to imbalanced data. Notably, we also address the prevalent issue of inappropriate test data selection and data leakage in earthquake prediction studies, demonstrating our models can continue to deliver effective predictions when the possibility of data leakage is strictly controlled.

### Keywords: 
Earthquake prediction, Seismic indicators, Ensemble learning, Feature selection
<!-- GETTING STARTED -->

## Getting Started

This section provides a quick guide to get you started with the project.

### Prerequisites

Before you begin, make sure you have installed the following:

Anaconda or Miniconda: A cross-platform distribution that includes Python and a package manager，You can download them from here: https://www.anaconda.com/download/ or https://www.anaconda.com. A virtual environment is a sandboxed environment that allows you to install and manage Python packages without affecting the system's Python environment.

### Create a Virtual Environment

To create a virtual environment, open a terminal and run the following command:
   ```sh
   conda create -n myenv python=3.8
   ```
This will create a virtual environment named ```myenv``` with Python 3.8.

### Install Dependencies

To install the required dependencies, activate the virtual environment and run the following command:
   ```sh
conda activate myenv
pip install -r requirements.txt
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
```Earthquake_data_preprocessor```  and ```Model_Tuner``` classes can be found in the earthquake folder.
   ```sh
from Earthquake_data_preprocessor import EarthquakeDataPreprocessor
from Model_Tuner import ModelTuner
import pandas as pd 
from xgboost import XGBClassifier
# Load the data
data = pd.read_csv("SC.csv")

# Create a preprocessor object
preprocessor = EarthquakeDataPreprocessor(data,remove_nan=False, remove_duplicates=False, binarize_magnitude=True, threshold=5, test_size=0.3, validation_size=0.3, n=50, normalize_data=False)

# Get the training, validation, and testing sets
train_data, validation_data, test_data = preprocessor.get_datasets()

##define the scoring function
score1 = make_scorer(roc_auc_score, needs_proba=True)

##Define model
model = XGBClassifier()

# Create a model tuner
tuner = ModelTuner(model, train_data, validation_data, test_data,scorefunction = score1)

# Define the fixed parameters
fixed_params = {"verbosity":0,"n_jobs":-1}

# Define the model parameters you want to optimase
param_grid = {"learning_rate": [0.1, 0.01, 0.001], "max_depth": [3, 5, 10],"n_estimators":[50,55]}

# Tune the model
best_parameters , best_model = tuner.tune(fixed_params, param_grid)

#Provide an evaluation of the best model’s performance on the test data.
tuner.evaluate()
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Cite
### bib
```
﻿@Article{Zhao2024,
author={Zhao, Yang
and Gorse, Denise},
title={Earthquake prediction from seismic indicators using tree-based ensemble learning},
journal={Natural Hazards},
year={2024},
month={Jan},
day={27},
abstract={Earthquake prediction is a challenging research area, but the use of a variety of machine learning models, together with a range of seismic indicators as inputs, has over the last decade led to encouraging progress, though the variety of seismic indicator features within any given study has been generally quite small. Recently, however, a multistage, hybrid learning model has used a total of 60 seismic indicators, applying this to data from three well-studied regions, aiming to predict earthquakes of magnitude 5.0 or above, up to 15 days before the event. In order to determine whether the encouraging results of this prior work were due to its learning model or to its expanded feature set we apply a range of tree-based ensemble classifiers to the same three datasets, showing that all these classifiers outperform the original, more complex model (with CatBoost as the best-performing), and hence that the value of this prior approach likely lay mostly in its range of presented features. We then use feature rankings from Boruta-Shap to discover the most valuable of these 60 features for each of the three regions, and challenge our optimized models to predict earthquakes of larger magnitudes, demonstrating their resilience to imbalanced data. Notably, we also address the prevalent issue of inappropriate test data selection and data leakage in earthquake prediction studies, demonstrating our models can continue to deliver effective predictions when the possibility of data leakage is strictly controlled.},
issn={1573-0840},
doi={10.1007/s11069-023-06221-5},
url={https://doi.org/10.1007/s11069-023-06221-5}
}

```
### ris
```
TY  - JOUR
AU  - Zhao, Yang
AU  - Gorse, Denise
PY  - 2024
DA  - 2024/01/27
TI  - Earthquake prediction from seismic indicators using tree-based ensemble learning
JO  - Natural Hazards
AB  - Earthquake prediction is a challenging research area, but the use of a variety of machine learning models, together with a range of seismic indicators as inputs, has over the last decade led to encouraging progress, though the variety of seismic indicator features within any given study has been generally quite small. Recently, however, a multistage, hybrid learning model has used a total of 60 seismic indicators, applying this to data from three well-studied regions, aiming to predict earthquakes of magnitude 5.0 or above, up to 15 days before the event. In order to determine whether the encouraging results of this prior work were due to its learning model or to its expanded feature set we apply a range of tree-based ensemble classifiers to the same three datasets, showing that all these classifiers outperform the original, more complex model (with CatBoost as the best-performing), and hence that the value of this prior approach likely lay mostly in its range of presented features. We then use feature rankings from Boruta-Shap to discover the most valuable of these 60 features for each of the three regions, and challenge our optimized models to predict earthquakes of larger magnitudes, demonstrating their resilience to imbalanced data. Notably, we also address the prevalent issue of inappropriate test data selection and data leakage in earthquake prediction studies, demonstrating our models can continue to deliver effective predictions when the possibility of data leakage is strictly controlled.
SN  - 1573-0840
UR  - https://doi.org/10.1007/s11069-023-06221-5
DO  - 10.1007/s11069-023-06221-5
ID  - Zhao2024
ER  - 
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Denise Gorse - d.gorse@cs.ucl.ac.uk

Yang Zhao  - yangzhao1215@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

A list of resources that can be helpful:

* [A comparison of deep and shallow models for the detection of induced seismicity](https://onlinelibrary.wiley.com/doi/full/10.1111/1365-2478.13386)
* [Seismic indicators based earthquake prediction system using support vector regressor and hybrid neural networks](https://figshare.com/articles/dataset/Earthquake_Prediction_using_SVR_and_HNN/6406814/1)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
