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
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

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
