# SiteWorks API Documentation

This is a technical documentation project for the SiteWorks API, a construction management API.  
A deployment is at [siteworks-api-docs-production.up.railway.app](https://siteworks-api-docs-production.up.railway.app/)

## Technologies & Tools Used

This project leverages the following technologies:

- **[MkDocs](https://www.mkdocs.org/)** – Static site generator for project documentation
- **[Mermaid.js](https://mermaid.js.org/)** – For real-time UML and sequence diagrams
- **[PlantUML](https://plantuml.com/)** – For creating detailed UML diagrams including system modeling
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** – Enhanced styling and features for documentation
- **[Swagger OpenAPI Specification](https://swagger.io/specification/)** – For documenting API endpoints
- **[GitHub](https://github.com/) / [Railway](https://railway.com/)** – For hosting the documentation

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

## Interaction with PlantUML diagrams

When you hover the diagram few buttons appear in the top left corner:

- 📋 copies SVG content of the diagram.
- ⬇️ downloads SVG diagram.
- ➕ zooms in the diagram.
- 🏠 resets the diagram to its default view.
- ➖ zooms out the diagram.

Additionally, mouse events control the zooming and panning of the diagram:

- `Left Button` + `_Mouse Move_` will trigger panning of the diagram.
- `Shift` + `_Scroll_` will trigger zooming of the diagram.

## Resources

The following resources was used to design and implement this project :

- **[Getting Started with MkDocs](https://www.mkdocs.org/getting-started/)** – To build and structure documentation
- **[Mkdocs-Mermaid2 plugin](https://github.com/fralau/mkdocs-mermaid2-plugin)** – An MkDocs plugin that renders Mermaid text descriptions into diagrams
- **[Mkdocs_puml Documentation](https://mikhailkravets.github.io/mkdocs_puml/)** - A package that brings PlantUML diagrams to MkDocs documentation
- **[MkDocs Swagger UI Tag](https://github.com/blueswen/mkdocs-swagger-ui-tag)** - A MkDocs plugin supports adding Swagger UI to the page
- **[Diagram as Code](https://diagrams.mingrammer.com/)** - To draw cloud system architecture in Python code
- **[Markdown Syntax](https://docs.framasoft.org/fr/grav/markdown.html)** - To use markdown syntax to format text

## Contribution

Interested in improving the SiteWorks API documentation? Follow these steps:

1. **Fork the repository**
2. **Create a new branch**:
   ```bash
   git checkout -b feature-name
   ```
3. **Make changes and commit**:
   ```bash
   git commit -m "Add new idea"
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

### Thank you for reading!
