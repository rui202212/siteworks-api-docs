# Changelog - SiteWorks API

## Version 1.1.0 - 2025-03-04

### Added

- New endpoint `/projects/{project_id}/status` to update project progress.
- Support for PATCH requests on `/workers/{worker_id}` to update worker status.

### Fixed

- Authentication issue with expired tokens (#342).
- Improved response times for `/teams` endpoint.

## Version 1.0.1 - 2025-02-22

### Added

- New features: Clients, Reports, Notifications.
- Authentication with JWT token.

## Version 1.0.0 - 2025-02-20

### Initial Release

- Core features: Workers, Teams, Projects, Materials, Subcontractors.
- Authentication via OAuth 2.0.

---  

_Last update : 2025-03-08_