site_name: SiteWorks API Docs
nav:

- Home: index.md
- API Docs:
  - API Authentication: api-docs/api-authentication.md
  - Swagger API Endpoints: api-docs/api-endpoints.md
  - API FAQ: api-docs/api-faq.md
- Product Docs:
  - API Features: product-docs/api-features.md
  - API Use Cases: product-docs/api-use-cases.md
  - Changelog: product-docs/changelog.md
  - Roadmap Overview: product-docs/roadmap-overview.md
- System Docs:
  - API Architecture: system-docs/api-architecture.md
  - API Tech Stack: system-docs/api-teck-stack.md
- Annex:
  - Glossary references: annex/glossary-references.md
- About: - About: about/about.md - License: about/license.md
  theme:
  name: mkdocs
  user_color_mode_toggle: true
  locale: en
  logo: images/logo.jpeg
  plugins:
- swagger-ui-tag
- search
- mermaid2
