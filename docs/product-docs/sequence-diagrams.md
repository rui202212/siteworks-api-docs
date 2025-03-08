# SiteWorks API - Sequence Diagrams

## 1. Authentication & Security

### Sequence Diagram - Obtaining a JWT Token

```mermaid
sequenceDiagram
    participant Client
    participant API Gateway
    participant Auth Server

    Client->>API Gateway: POST /auth/token (client_id, client_secret)
    API Gateway->>Auth Server: Validate credentials
    Auth Server-->>API Gateway: JWT Token (access_token)
    API Gateway-->>Client: JWT Token (access_token)
```

## 2. Worker & Team Management

### Sequence Diagram - Registering and Assigning a Worker

```mermaid
sequenceDiagram
    participant HR
    participant API Gateway
    participant Worker Service
    participant Team Service

    HR->>API Gateway: POST /workers (worker data)
    API Gateway->>Worker Service: Create worker
    Worker Service-->>API Gateway: Worker created (worker_id)
    API Gateway-->>HR: Worker registered (worker_id)

    HR->>API Gateway: POST /teams (team data)
    API Gateway->>Team Service: Create team
    Team Service-->>API Gateway: Team created (team_id)

    HR->>API Gateway: Assign worker to team
    API Gateway->>Team Service: Update team members
    Team Service-->>API Gateway: Assignment successful
    API Gateway-->>HR: Worker assigned to team
```

## 3. Project Management

### Sequence Diagram - Creating and Tracking a Project

```mermaid
sequenceDiagram
    participant Project Manager
    participant API Gateway
    participant Project Service

    Project Manager->>API Gateway: POST /projects (project details)
    API Gateway->>Project Service: Create project
    Project Service-->>API Gateway: Project created (project_id)
    API Gateway-->>Project Manager: Project registered (project_id)

    Project Manager->>API Gateway: GET /projects/{project_id}
    API Gateway->>Project Service: Retrieve project details
    Project Service-->>API Gateway: Project details
    API Gateway-->>Project Manager: Project details
```

## 4. Material & Supply Chain Management

### Sequence Diagram - Tracking Material Stock Levels

```mermaid
sequenceDiagram
    participant Site Manager
    participant API Gateway
    participant Material Service

    Site Manager->>API Gateway: POST /materials (material details)
    API Gateway->>Material Service: Register material
    Material Service-->>API Gateway: Material registered (material_id)
    API Gateway-->>Site Manager: Material added (material_id)

    Site Manager->>API Gateway: PATCH /materials/{material_id} (update stock)
    API Gateway->>Material Service: Update stock level
    Material Service-->>API Gateway: Stock updated
    API Gateway-->>Site Manager: Confirmation
```

## 5. Notifications & Webhooks

### Sequence Diagram - Receiving Real-Time Project Updates

```mermaid
sequenceDiagram
    participant API Gateway
    participant Webhook System
    participant Project Service
    participant Client System

    Client System->>API Gateway: POST /notifications/webhooks (subscribe)
    API Gateway->>Webhook System: Register webhook
    Webhook System-->>API Gateway: Webhook registered

    Project Service->>API Gateway: Project milestone reached
    API Gateway->>Webhook System: Trigger webhook
    Webhook System-->>Client System: Send notification
```
