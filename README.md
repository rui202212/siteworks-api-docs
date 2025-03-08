# SiteWorks API Documentation

This is a technical documentation project for the SiteWorks API, a construction management API.  
A deployment is at [siteworks-api-docs-production.up.railway.app](https://siteworks-api-docs-production.up.railway.app/)

## Project Objectives

This project was created to achieve the following **learning goals**:

- **Structuring and writing** complete and well-organized technical documentation
- **Using MkDocs** to generate documentation dynamically
- **Integrating dynamic diagrams** with **Mermaid** and **PlantUML**
- **Documenting an API** using **Swagger (OpenAPI)**
- etc.

## Technologies & Tools Used

This project leverages the following technologies:

- **[MkDocs](https://www.mkdocs.org/)** – Static site generator for project documentation
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** – Enhanced styling and features for documentation
- **Mermaid.js** – For real-time UML and sequence diagrams
- **PlantUML** – For advanced system modeling
- **Swagger (OpenAPI)** – For documenting API endpoints
- **GitHub Pages / Railway** – For hosting the documentation

## Installation & Deployment

This section explains how to **install, run, and deploy the SiteWorks API documentation** on **Railway** from a GitHub repository.

### 1️. Prerequisites

Before you begin, make sure you have:

- **Python 3.8+** installed
- **pip** (Python package manager) installed
- **Git** installed on your machine

### 2️. Install MkDocs

Clone the repository and install dependencies:

```bash
git clone https://github.com/rui202212/siteworks-api-docs.git
cd siteworks-api-docs
pip install -r requirements.txt
```

### 3️. Run Documentation Locally

To preview the documentation locally:

```bash
mkdocs serve
```

Then, open **http://127.0.0.1:8000/** in a browser.

---

## Deploying to Railway

Railway is a cloud deployment platform that supports MkDocs. Followrd steps to deploy this documentation from GitHub.

### 1️. Create a Railway Account & Link GitHub

- Go to **[Railway.app](https://railway.app/)**
- Sign up and **connect the GitHub account**
- Click **New Project** → **Deploy from GitHub**
- Select the repository

### 2️. Configure Railway for MkDocs

After linking the GitHub repo:

1. **Set up a new service**

   - Add `PORT = 8000` in Variables
   - Choose **"Python"** as the environment
   - Set the **build command**:
     ```bash
     pip install -r requirements.txt
     ```
   - Set the **start command**:
     ```bash
     mkdocs serve --dev-addr=0.0.0.0:8000
     ```
     or
     ```bash
     mkdocs build && mkdocs serve --dev-addr=0.0.0.0:8000
     ```

2. **Set up a deployment trigger**

   - Enable **automatic deployments** on Railway
   - Railway will redeploy the site whenever they push updates to GitHub

3. **Get the public URL**
   - Once deployed, Railway will provide a **public URL** where the documentation is hosted

## Resources

The following resources was used to design and implement this project :

- **[MkDocs Documentation](https://www.mkdocs.org/)** – For building and structuring documentation
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** – A powerful theme for MkDocs
- **[Mermaid.js Documentation](https://mermaid.js.org/)** – To create dynamic diagrams
- **[Diagram as Code](https://diagrams.mingrammer.com/)** - To draw cloud system architecture in Python code
- **[Swagger OpenAPI Specification](https://swagger.io/specification/)** – To document API endpoints
- **[PlantUML Documentation](https://plantuml.com/)** – For creating detailed UML diagrams
- \*\*[mkdocs_puml Documentation](https://mikhailkravets.github.io/mkdocs_puml/) - A package that brings PlantUML diagrams to MkDocs documentation

## Contribution

Interested in improving the SiteWorks API documentation? Follow these steps:

1. **Fork the repository**
2. **Create a new branch**:
   ```bash
   git checkout -b feature-name
   ```
3. **Make changes and commit**:
   ```bash
   git commit -m "Added new idea"
   ```
4. **Push your changes**:
   ```bash
   git push origin feature-name
   ```
5. **Submit a Pull Request (PR)**

---

## License

This project is open-source under the **MIT License**.

---

### Happy Documentation!
