# SiteWorks API - Frequently Asked Questions (FAQ)

## General Questions

### What is SiteWorks API?

SiteWorks API is a construction management API that helps businesses manage workers, teams, projects, materials, subcontractors, clients, and more. It provides a secure and scalable way to integrate construction workflows into digital platforms.

### Who can use SiteWorks API?

SiteWorks API is designed for construction companies, project managers, subcontractors, and software developers who need to integrate construction management features into their applications.

## Authentication & Security

### How do I authenticate with SiteWorks API?

SiteWorks API uses **OAuth 2.0 with JWT authentication**. To make a request, you need to obtain an **access token** by sending your _**client_id**_ and _**client_secret**_ to the `/auth/token` endpoint.

### How can I get an API key?

You can request an API key by signing up on our developer portal at [https://developers.siteworks.com](https://developers.siteworks.com). Once registered, you will receive your _**client_id**_ and _**client_secret**_.

### How do I use a JWT token in API requests?

Once you receive your JWT token, include it in your request headers:

```http
Authorization: Bearer your-access-token
```

### What should I do if my token expires?

Access tokens expire after a set period.  
When your token expires, request a new one using the `/auth/token` endpoint.

### Can I revoke an access token?

Yes, you can revoke a token via the API or by contacting support.

## API Usage

### How do I create a new worker/team/project?

You can send a POST request to the respective endpoint with the required data. Example:

```http
POST /workers
Content-Type: application/json
Authorization: Bearer your-access-token

{
  "name": "Nicola TESLA",
  "role": "Electrician",
  "team_id": 123
}
```

### How do I retrieve a list of workers, teams, or projects?

You can send a **GET request** to the respective endpoints:

- `/workers` → Get all workers
- `/teams` → Get all teams
- `/projects` → Get all projects

### How do I update a worker’s information?

Use a **PUT request** to update an existing worker:

```http
PUT /workers/{worker_id}
Content-Type: application/json
Authorization: Bearer your-access-token

{
  "name": "Zaha HADID",
  "role": "Supervisor"
}
```

## Errors & Troubleshooting

### What should I do if I get a 401 Unauthorized error?

Ensure that:

- You are including the **correct** access token in the request headers.
- Your token has not expired.
- You have the necessary permissions.

### What should I do if I get a 403 Forbidden error?

This means you do not have the required permissions to access the resource. Check your **role-based access control (RBAC)** settings.

### What should I do if I get a 404 Not Found error?

- Check if the requested resource exists.
- Ensure you are using the correct **ID** in the request URL.
- Verify that the endpoint URL is correct.

### What should I do if I get a 500 Internal Server Error?

This usually indicates a problem on our end. Please try again later or contact support.

## Support

### How can I contact support?

If you need further assistance, you can:

- Visit our documentation at [https://docs.siteworks.com](../index.md)
- Email our support team at [support@siteworks.com](mailto:support@siteworks.com)
- Open a support ticket in our developer portal

---

This FAQ will be regularly updated based on user feedback. If you have additional questions, feel free to contact us!
