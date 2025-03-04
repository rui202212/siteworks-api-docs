# API Authentication Guide

## Overview

SiteWorks API uses **OAuth 2.0** and **JWT (JSON Web Token)** for secure authentication and authorization. This ensures safe access to the API while allowing granular control over user permissions through **Role-Based Access Control (RBAC)**.

---

## 1. Obtaining API Keys

To access SiteWorks API, you need an API key, which is required to authenticate your requests.

### Steps to Get an API Key:

1. **Sign Up:** Register an account on the SiteWorks Developer Portal.
2. **Create an Application:** Navigate to the API Keys section and create a new application.
3. **Generate API Key:** The system will provide a unique API key for authentication.
4. **Store Securely:** Keep the API key safe, as it grants access to SiteWorks API.

---

## 2. Obtaining a JWT Token

JWT tokens are used for authenticating API requests after obtaining an API key.

### Requesting a JWT Token

Make a `POST` request to the authentication endpoint with your API key and credentials:

**Endpoint:**

```
POST /auth/token
```

**Request Body:**

```json
{
  "client_id": "your-client-id",
  "client_secret": "your-client-secret",
  "grant_type": "client_credentials"
}
```

**Response:**

```json
{
  "access_token": "your-jwt-token",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

### Token Expiration

- The JWT token is valid for **1 hour**.
- After expiration, you must request a new token.

---

## 3. Using JWT in API Requests

Once you have obtained a JWT token, include it in the `Authorization` header of your API requests.

**Example Request:**

```
GET /projects
Authorization: Bearer your-jwt-token
```

---

## 4. OAuth 2.0 Authorization Flow

For advanced security and third-party integrations, SiteWorks API supports **OAuth 2.0 Authorization Code Flow**.

### Steps:

1. **Redirect User to Authorization Endpoint**
   ```
   GET /oauth/authorize?response_type=code&client_id=your-client-id&redirect_uri=your-redirect-url
   ```
2. **User Grants Permissions**
3. **Receive Authorization Code**
4. **Exchange Authorization Code for Access Token**
   ```
   POST /oauth/token
   {
      "grant_type": "authorization_code",
      "code": "your-authorization-code",
      "redirect_uri": "your-redirect-url",
      "client_id": "your-client-id",
      "client_secret": "your-client-secret"
   }
   ```

---

## 5. Role-Based Access Control (RBAC)

SiteWorks API uses RBAC to restrict access based on user roles.

### Example Roles:

- **Admin:** Full access to all API endpoints.
- **Project Manager:** Can manage projects and teams.
- **Worker:** Limited access to assigned tasks.

### Checking User Permissions

Use the `/auth/me` endpoint to retrieve user roles and permissions:

```
GET /auth/me
Authorization: Bearer your-jwt-token
```

**Response:**

```json
{
  "user_id": "12345",
  "role": "Project Manager",
  "permissions": ["view_projects", "assign_tasks"]
}
```

---

## 6. Security Best Practices

- **Keep API keys and tokens secure** (do not expose them in frontend code).
- **Use HTTPS** for all requests.
- **Rotate API keys and tokens periodically**.
- **Implement refresh tokens** for long-lived sessions.

For further details, refer to [SiteWorks API Documentation](../index.md) or contact support at [**support@siteworks.com**](mailto:support@siteworks.com).
