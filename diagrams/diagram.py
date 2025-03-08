from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ingress
from diagrams.k8s.group import Namespace
from diagrams.k8s.storage import PV
from diagrams.onprem.ci import GithubActions
from diagrams.aws.security import IAM
from diagrams.generic.network import Firewall
from diagrams.elastic.elasticsearch import Elasticsearch

# Création du diagramme
with Diagram("SiteWorks API Architecture", show=False):

    # Cluster des Utilisateurs
    with Cluster("Users"):
        worker = User("Worker")
        team_manager = User("Team Manager")
        site_manager = User("Site Manager")

    # Sécurité et Load Balancer
    with Cluster("Security & Load Balancer"):
        waf = Firewall("Web Application Firewall")
        load_balancer = Nginx("NGINX Load Balancer")

    # Kubernetes Cluster
    with Cluster("Kubernetes Cluster"):
        with Cluster("Backend Services"):
            backend = [
                Pod("Auth Service"),
                Pod("Project Service"),
                Pod("Worker Service"),
                Pod("Material Service")
            ]

        with Cluster("Data Layer"):
            db = PostgreSQL("PostgreSQL")
            storage = PV("Persistent Storage")

        with Cluster("Message Queue"):
            kafka = Kafka("Apache Kafka")

    # Monitoring & Logging
    with Cluster("Monitoring & Logging"):
        prometheus = Prometheus("Monitoring")
        grafana = Grafana("Dashboard")
        elk = Elasticsearch("ELK Logging")

    # CI/CD Pipeline
    github_actions = GithubActions("CI/CD Pipeline")

    # IAM & Auth
    iam = IAM("OAuth 2.0 & JWT")

    # Connexions entre les composants
    [worker, team_manager, site_manager] >> waf >> load_balancer >> backend
    backend >> Edge(color="black", style="bold") >> db
    backend >> Edge(color="darkblue") >> kafka
    backend >> Edge(color="firebrick", style="dashed") >> prometheus
    backend >> Edge(color="purple") >> elk
    github_actions >> Edge(color="darkgreen") >> backend
    iam >> Edge(color="darkred") >> waf
