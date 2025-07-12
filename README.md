## VEX-for-containers

Study setup for VEX-tools evaluation and end-to-end pipeline to generate, parse, and analyze SBOMs and VEX data for container images using multiple scanners.

## Table of Contents

- [Repository Structure](#repository-structure)  
- [Scripts](#scripts)  
- [JSON Parsers](#json-parsers)  
- [Data Analysis Notebooks](#data-analysis-notebooks)
- [Covariances based on Jaccard and Tversky indices](#Covariances)


## Scripts

- **`scan_script.py`**  
  Orchestrates scanning of GitHub repositories or container images using VEX-generation tools (and placeholders for other tools). Outputs raw VEX JSON files under `jsons/`.

## JSON Parsers

Each of these transforms raw scanner JSON into a pandas DataFrame summary:

- `json_parser_depscan.py`  
- `json_parser_depscan_sboms.py`  
- `json_parser_docker.py`  
- `json_parser_grype.py`  
- `json_parser_grype_sboms.py`  
- `json_parser_osv.py`  
- `json_parser_osv_sboms.py`  
- `json_parser_snyk.py`  
- `json_parser_trivy.py`  
- `json_parser_trivy_sboms.py`  
- `json_parser_vexy.py`  

Run as modules to extract vulnerability metadata for analysis.

## Data Analysis Notebooks

A suite of Jupyter notebooks for exploratory and comparative analyses:

- `data_analytics_depscan.ipynb`  
- `data_analytics_docker.ipynb`  
- `data_analytics_grype.ipynb`  
- `data_analytics_grype_oci.ipynb`  
- `data_analytics_osv.ipynb`  
- `data_analytics_same_sbom.ipynb`  
- `data_analytics_snyk.ipynb`  
- `data_analytics_trivy.ipynb`  
- `data_analytics_trivy_depscan.ipynb`  
- `data_analytics_trivy_docker.ipynb`  
- `data_analytics_trivy_syft.ipynb`  
- `data_analytics_trivy_trivy.ipynb`  
- `data_analytics_vexy.ipynb`  

These read parser outputs to generate visualizations, statistical comparisons, and SBOM consistency checks.

## Covariances
- Computes the Jaccard index between vulnerability sets via `covariances/jaccard_index.py`.

