# FHIR for Research Resources

[![pipeline status](https://gitlab.mitre.org/fhir-for-research/web/badges/main/pipeline.svg)](https://gitlab.mitre.org/fhir-for-research/web/-/commits/main)
[![Latest Release](https://gitlab.mitre.org/fhir-for-research/web/-/badges/release.svg)](https://gitlab.mitre.org/fhir-for-research/web/-/releases)

## Dependencies

- [Quarto](https://quarto.org/docs/get-started/)
- R (if you use RMarkdown)
- Jupyter and Python3 (if you use embedded Python)

Python uses `venv` (https://quarto.org/docs/projects/virtual-environments.html):

You will need to create a `venv` in `python_env/`:

    python3 -m venv python_env

Then run `source python_env/bin/activate` to activate the `venv`, and the following command to install dependencies:

    pip install -r requirements.txt

If you add a dependency, run `pip freeze > requirements.txt` to update the requirements file.

## Quick start

- Clone this repository
- Run `quarto preview` (this will compile everthing into _site, start a server, and launch web browser to load localhost server)

### To add a page

- create a `.qmd` file
- add the file to _quarto.yml under navbar, for example:

    ```yaml
    # ... (snipped for brevity)

    website:
      navbar:
        left:
          - about.qmd
          - NEW_FILE.qmd
    ```

- In `NEW_FILE.qmd`:

      ---
      title: NEW_FILE
      ---
      Markdown or HTML goes here

      ```{r}
      # R code goes here
      ```

      ```{python}
      # Python code goes here, but you can't embed R and Python code in the same file
      ```

 - run `quarto preview`

### To view pages by branch

 - on gitlab sidebar navigate to Deployments -> Environments

### To view failed deployments

 - on gitlab sidebar navigate to CI/CD -> Pipelines


## Documentation

 - [Quarto Guides](https://quarto.org/docs/guide/)

The GitLab pipeline is setup to re-compute and re-render everything on CI Server. If you use Python libraries you need to add a requirements.txt, and if you use R libraries you need whatever R uses for package management.
