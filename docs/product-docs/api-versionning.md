# API Versioning Guide

## Introduction

The SiteWorks API follows a structured versioning strategy to ensure backward compatibility while allowing continuous improvements. This document explains how API versions are managed, best practices for developers, and how to migrate between versions.

## Why Versioning?

Versioning is crucial for:

- **Backward Compatibility**: Preventing breaking changes for existing clients.
- **Incremental Improvements**: Allowing enhancements without disrupting services.
- **Deprecation Management**: Providing a smooth transition between versions.

## Versioning Strategy

The SiteWorks API uses **URL-based versioning** with **semantic versioning principles**:

- **Major Versions (`v1`, `v2`, etc.)**
  - Introduce breaking changes (e.g., removing fields, altering authentication mechanisms).
  - Indicated in the API base URL:
    ```
    https://api.siteworks.com/v1/projects
    ```
- **Minor Versions (`v1.1`, `v1.2`, etc.)**
  - Introduce new features or optional parameters without breaking existing functionality.
  - Typically not reflected in the base URL but communicated via headers.
- **Patch Versions (`v1.0.1`, `v1.0.2`, etc.)**
  - Contain bug fixes and security updates.
  - Do not introduce new features or breaking changes.

## How to Specify an API Version?

### 1️. URL Path Versioning (Recommended)

Each major version is included in the API base URL:

```http
GET https://api.siteworks.com/v1/workers
```

This ensures clear, explicit versioning.

### 2️. Accept Header Versioning (Alternative)

Clients can request a specific minor version using the `Accept` header:

```http
GET /workers
Accept: application/vnd.siteworks.v1+json
```

This method allows greater flexibility but requires clients to manage headers correctly.

## Handling Deprecation

When an API version is deprecated:

- **Advanced Notice:** A deprecation announcement will be made in the [Release Notes](release-notes.md).
- **Deprecation Period:** Old versions remain functional for a period before retirement.
- **Deprecation Warnings:** Clients using deprecated versions may receive warnings in API responses.

```json
{
  "warning": "This API version (v1) will be deprecated on 2026-01-01. Please upgrade to v2."
}
```

**Migration Guides:** Provided in the [Changelog](changelog.md).

## Best Practices for API Consumers

🔹 **Always use the latest stable version** to benefit from security fixes and new features.  
🔹 **Check the API documentation** before upgrading to a new version.  
🔹 **Monitor deprecation notices** to plan migration in advance.  
🔹 **Use feature detection** rather than relying on version numbers when possible.

## Example: Upgrading from v1 to v2

### Breaking Change Example

In **v1**, a worker’s role was stored under `job_title`:

```json
{
  "id": 123,
  "name": "John Doe",
  "job_title": "Electrician"
}
```

In **v2**, it has been renamed to `role`:

```json
{
  "id": 123,
  "name": "John Doe",
  "role": "Electrician"
}
```

**Migration Tip:** Update your client code to handle `role` instead of `job_title`.

---

## Need Help?

For questions or migration support, check the [API FAQ](../api-docs/api-faq.md) or contact [support@siteworks.com](mailto:support@siteworks.com).
