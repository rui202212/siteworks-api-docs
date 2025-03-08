# Error Handling in SiteWorks API

## Introduction

The SiteWorks API follows a consistent error-handling strategy to help developers understand and resolve issues effectively. Errors are returned in a structured JSON format, including an HTTP status code, an error message, and an optional error code for reference.

## Error Response Format

All error responses follow this JSON structure:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "A human-readable explanation of the error.",
    "details": "Additional context or guidance on resolving the issue."
  }
}
```

- `code`: a unique identifier for the error type.
- `message`: a brief explanation of what went wrong.
- `details`: (optional) additional information or troubleshooting tips.

## Common HTTP Status Codes and Error Messages

| Status Code                   | Error Code            | Description                                                              |
| ----------------------------- | --------------------- | ------------------------------------------------------------------------ |
| **400 Bad Request**           | `INVALID_REQUEST`     | The request is malformed or missing required parameters.                 |
| **401 Unauthorized**          | `AUTH_REQUIRED`       | Authentication is required but missing or invalid.                       |
| **403 Forbidden**             | `ACCESS_DENIED`       | The client does not have permission to access the resource.              |
| **404 Not Found**             | `RESOURCE_NOT_FOUND`  | The requested resource does not exist.                                   |
| **409 Conflict**              | `RESOURCE_CONFLICT`   | The request conflicts with an existing resource (e.g., duplicate entry). |
| **422 Unprocessable Entity**  | `VALIDATION_FAILED`   | The input data is syntactically correct but semantically invalid.        |
| **429 Too Many Requests**     | `RATE_LIMIT_EXCEEDED` | The client has exceeded the allowed request rate.                        |
| **500 Internal Server Error** | `INTERNAL_ERROR`      | A server-side issue occurred. Contact support if the problem persists.   |

---

## Example Error Responses

### 400 Bad Request – Invalid Input

#### Scenario: Missing required parameters in a worker registration request.

**Request:**

```http
POST /workers
Content-Type: application/json
Authorization: Bearer <your_token>
```

**Request Body:**

```json
{
  "name": "",
  "role": "Electrician"
}
```

**Response:**

```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "The 'name' field is required."
  }
}
```

### 401 Unauthorized – Invalid Token

#### Scenario: Accessing an endpoint without a valid token.

**Request:**

```http
GET /projects
Content-Type: application/json
```

**Response:**

```json
{
  "error": {
    "code": "AUTH_REQUIRED",
    "message": "You must provide a valid authentication token."
  }
}
```

### 404 Not Found – Resource Does Not Exist

#### Scenario: Fetching a non-existent project.

**Request:**

```http
GET /projects/99999
Authorization: Bearer <your_token>
```

**Response:**

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Project with ID 99999 does not exist."
  }
}
```

### 429 Too Many Requests – Rate Limit Exceeded

#### Scenario: The client exceeds API request limits.

**Response:**

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests. Please wait and try again later."
  }
}
```

---

## Best Practices for Handling Errors

- **Check HTTP status codes** before processing the response.
- **Use the error code** to determine the cause of the failure.
- **Implement retries** for **429 Too Many Requests** with exponential backoff.
- **Validate inputs** before sending API requests to avoid **400 Bad Request** errors.
- **Refresh expired tokens** when encountering **401 Unauthorized**.

---

## Need Help?

If you encounter unexpected errors, please refer to the [API FAQ](api-faq.md) or contact [support@siteworks.com](mailto:support@siteworks.com).
