# SiteWorks API - Use Cases

## Overview  
The **SiteWorks API** provides powerful tools for managing construction projects, workers, teams, and resources efficiently. Below are common use cases that demonstrate how businesses can integrate our API into their workflows.

---

## **1. Worker & Team Management**

### **Use Case: Registering and Assigning Workers**
**Scenario:**  
A construction company hires new workers and needs to register them in the system while assigning them to specific teams.

**Steps:**  
1. The HR department registers a new worker using the `/workers` endpoint.  
2. The worker is assigned to a team using the `/teams` endpoint.  
3. The project manager retrieves a list of all team members to confirm assignments.  

**Endpoints Used:**  
- `POST /workers`  
- `POST /teams`  
- `GET /teams/{team_id}`  

---  

## **2. Project & Site Management**  

### **Use Case: Creating and Tracking a Construction Project**  
**Scenario:**  
A company starts a new construction project and needs to track its progress.

**Steps:**  
1. The project manager creates a new project using the `/projects` endpoint.  
2. Teams and workers are assigned to the project.  
3. Progress updates are logged periodically.  

**Endpoints Used:**  
- `POST /projects`  
- `GET /projects/{project_id}`  
- `PATCH /projects/{project_id}` (for status updates)  

---  

## **3. Material & Supply Chain Management**  

### **Use Case: Tracking Construction Material Usage**  
**Scenario:**  
A site manager wants to track the usage of materials and ensure stock availability.  

**Steps:**  
1. The warehouse team registers new materials in the system.  
2. Materials are assigned to specific construction projects.  
3. When stock levels are low, an automated alert is triggered.  

**Endpoints Used:**  
- `POST /materials`  
- `GET /materials/{material_id}`  
- `PATCH /materials/{material_id}` (for updating stock levels)  
- `GET /projects/{project_id}/materials`  

---  

## **4. Subcontractor & Client Management**  

### **Use Case: Managing Subcontractors**  
**Scenario:**  
A company hires subcontractors for specific tasks like plumbing and electrical work.  

**Steps:**  
1. The procurement team registers a new subcontractor.  
2. The subcontractor is assigned to a specific project.  
3. Payment details and contract terms are stored.  

**Endpoints Used:**  
- `POST /subcontractors`  
- `GET /subcontractors/{subcontractor_id}`  
- `PATCH /subcontractors/{subcontractor_id}`  
  
---  

## **5. Real-Time Notifications & Reporting**  

### ✅ **Use Case: Receiving Real-Time Project Updates**  
**Scenario:**  
A project manager wants to be notified when critical project milestones are reached.  

**Steps:**  
1. Webhooks are set up to notify the project manager of updates.  
2. The system triggers a notification when a milestone is completed.  
3. A daily summary report is generated.  

**Endpoints Used:**  
- `POST /notifications/webhooks`  
- `GET /projects/{project_id}/progress`  
- `GET /reports/daily-summary`  

---

## **6. Authentication & Security**  

### **Use Case: Secure API Access with JWT**  
**Scenario:**  
A third-party application wants to securely access the SiteWorks API.  

**Steps:**  
1. The application requests an access token using OAuth 2.0.  
2. The token is used to authenticate API requests.  
3. If the token expires, the application renews it.  

**Endpoints Used:**  
- `POST /auth/token`  
- `GET /workers` (with authentication)  
- `GET /projects` (with authentication)  

---

## **Conclusion**  
The **SiteWorks API** simplifies construction project management by offering robust features for worker tracking, project management, material handling, and subcontractor coordination. Whether you're building a small site or managing large-scale infrastructure projects, **SiteWorks API** provides the essential tools for efficient and secure operations.

For more details, explore our [API Authentication Guide](../api-docs/api-authentication.md) and [Swagger API Endpoints](../api-docs/api-endpoints.md).
