# API Sequence Diagrams

## 1️. Authentication Flow

The authentication process follows OAuth 2.0 with JWT to ensure secure access.

```mermaid
sequenceDiagram
    participant Client
    participant SiteWorksAPI
    Client->>SiteWorksAPI: POST /auth/token (client_id, client_secret)
    SiteWorksAPI-->>Client: 200 OK (access_token)
    Client->>SiteWorksAPI: GET /projects (Authorization: Bearer access_token)
    SiteWorksAPI-->>Client: 200 OK (Project List)
```

## 2️. Creating a New Project

A **Project Manager** creates a new project, and the API validates and stores it.

```mermaid
sequenceDiagram
    participant ProjectManager
    participant SiteWorksAPI
    ProjectManager->>SiteWorksAPI: POST /projects (project details)
    SiteWorksAPI-->>ProjectManager: 201 Created (Project ID)
```

## 3️. Assigning Workers to a Project

A **Project Manager** assigns workers to a construction project.

```mermaid
sequenceDiagram
    participant ProjectManager
    participant SiteWorksAPI
    participant Worker

    ProjectManager->>SiteWorksAPI: PATCH /projects/{id} (assign workers)
    SiteWorksAPI-->>Worker: Notify Assignment
    SiteWorksAPI-->>ProjectManager: 200 OK
```

## 4️. Worker Submitting a Report

A **Worker** submits a daily progress report, and the **Site Manager** reviews it.

```mermaid
sequenceDiagram
    participant Worker
    participant SiteWorksAPI
    participant SiteManager

    Worker->>SiteWorksAPI: POST /reports (report data)
    SiteWorksAPI-->>SiteManager: Notify new report
    SiteWorksAPI-->>Worker: 201 Created
```

## 5️. Fetching Material Inventory

A **Team Manager** requests the current material stock.

```mermaid
sequenceDiagram
    participant TeamManager
    participant SiteWorksAPI

    TeamManager->>SiteWorksAPI: GET /materials
    SiteWorksAPI-->>TeamManager: 200 OK (Material List)
```

For more details, refer to the [API Authentication Guide](api-authentication.md) and [API Endpoints](api-endpoints.md).
