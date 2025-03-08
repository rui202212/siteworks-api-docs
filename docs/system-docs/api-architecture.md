# SiteWorks API Architecture

```uml
@startuml
skinparam backgroundColor white
skinparam componentStyle rectangle
skinparam shadowing false

skinparam defaultFontColor black
skinparam component {
    BackgroundColor LightBlue
    BorderColor DarkBlue
}
skinparam queue {
    BackgroundColor LightGrey
    BorderColor Black
}
skinparam database {
    BackgroundColor LightYellow
    BorderColor DarkRed
}
skinparam cloud {
    BackgroundColor LightGreen
    BorderColor DarkGreen
}
skinparam actor {
    BackgroundColor White
    BorderColor Black
}

title SiteWorks API Architecture

'=== Cluster des utilisateurs
rectangle "Users" as Users #lightgrey {
    actor Worker as W #Yellow
    actor "Team Manager" as TM #Blue
    actor "Site Manager" as SM
    actor "HSE Manager" as HSE #Red
}

'=== Security & Load Balancer
rectangle "Security & Load Balancer" as Security #LightPink {
    cloud "Web Application Firewall\n(WAF)" as WAF #red
    cloud "NGINX Load Balancer" as LB #orange
}

'=== Kubernetes Cluster
rectangle "Kubernetes Cluster" as Kubernetes #LightBlue {

    '=== Backend Services
    rectangle "Backend Services" as Backend #lightblue {
        [Auth Service] as Auth
        [Project Service] as Project
        [Worker Service] as WorkerService
        [Material Service] as Material
    }

    '=== Data Layer
    database "PostgreSQL" as DB #yellow
    storage "Persistent Storage" as Storage #gray

    '=== Message Queue
    queue "Apache Kafka" as Kafka #lightgray
}

'=== Monitoring & Logging
rectangle "Monitoring & Logging" as Monitoring #lightgreen {
    [Prometheus (Monitoring)] as Prometheus
    [Grafana (Dashboard)] as Grafana
    cloud "ELK Logging" as ELK #darkgreen
}

'=== CI/CD Pipeline & IAM
rectangle "CI/CD & IAM" as CICD #lightyellow {
    component "GitHub Actions\n(CI/CD Pipeline)" as GitHubActions
    component "OAuth 2.0 & JWT" as IAM
}

'=== Connexions entre les composants
W --> WAF
TM --> WAF
SM --> WAF
HSE --> WAF
WAF --> LB
LB --> Backend

Backend --> DB
Backend --> Storage
Backend --> Kafka
Backend --> Prometheus
Backend --> ELK

GitHubActions --> Backend
IAM --> WAF
@enduml
```
