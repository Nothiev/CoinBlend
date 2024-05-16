import pandas as pd
import random
from datetime import datetime, timedelta

def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

def random_score():
    return round(random.uniform(60, 100), 1)

# Data for the initial 10 projects
data = {
    "Nom du projet": ["EcoVille", "TechMed", "EduLearn", "SolarPark", "FoodWasteSolution", "SmartHome", "GreenTransport", "CleanWaterAccess", "DigitalArtGallery", "HealthyAging"],
    "Catégorie": ["Environnement", "Santé", "Éducation", "Énergie", "Environnement", "Technologie", "Transport", "Humanitaire", "Culture", "Santé"],
    "Image": ["eco_ville.png", "tech_med.png", "edu_learn.png", "solar_park.png", "food_waste.png", "smart_home.png", "green_transport.png", "clean_water.png", "digital_art.png", "healthy_aging.png"],
    "Description": [
        "Développement d'une ville éco-responsable avec des énergies renouvelables.",
        "Création d'un dispositif médical connecté pour surveiller les patients.",
        "Plateforme d'apprentissage en ligne pour les enfants défavorisés.",
        "Installation d'un parc solaire pour fournir de l'énergie propre.",
        "Solution pour réduire le gaspillage alimentaire dans les restaurants.",
        "Système domotique pour rendre les maisons intelligentes et économes en énergie.",
        "Développement de véhicules électriques pour le transport en commun.",
        "Projet d'installation de puits d'eau potable dans les zones rurales.",
        "Galerie d'art numérique accessible en ligne pour les artistes émergents.",
        "Programme de santé pour le vieillissement actif et en bonne santé."
    ],
    "Porteur du projet": ["Jean Dupont", "Marie Leblanc", "Ali Ahmed", "Sarah Leroy", "Pierre Martin", "Laura Dupuis", "Karim Nadir", "Emma Smith", "Lucas Moreau", "Sophie Durand"],
    "Niveau d'études": ["Master en Génie Civil", "Doctorat en Biotech", "Master en Éducation", "Licence en Énergie", "Master en Environnement", "Master en Informatique", "Doctorat en Ingénierie", "Master en Développement", "Licence en Arts Numériques", "Master en Santé Publique"],
    "Expérience dans d'autres projets": ["5 projets", "3 projets", "2 projets", "4 projets", "6 projets", "3 projets", "5 projets", "7 projets", "1 projet", "4 projets"],
    "Objectif financier": ["500000 €", "200000 €", "100000 €", "1000000 €", "150000 €", "300000 €", "2000000 €", "250000 €", "50000 €", "120000 €"],
    "Date de fin": ["2025-12-31", "2024-06-30", "2024-09-30", "2026-03-31", "2023-12-31", "2025-08-31", "2027-05-31", "2024-12-31", "2023-11-30", "2024-04-30"],
    "A quoi servira le financement": [
        "Construction de bâtiments écologiques",
        "Développement et commercialisation du dispositif",
        "Développement de la plateforme et création de contenu",
        "Achat de panneaux solaires et installation",
        "Développement de la technologie et campagnes de sensibilisation",
        "Recherche et développement, commercialisation",
        "Production de prototypes, tests et certifications",
        "Achat de matériel et construction des puits",
        "Développement de la plateforme et marketing",
        "Création de programmes, formation de personnel"
    ],
    "Score potentiel de réussite": [75.5, 82.3, 78.4, 80.0, 70.2, 85.1, 90.3, 88.5, 65.4, 78.9],
    "Pays": ["France", "Allemagne", "Inde", "États-Unis", "Canada", "Japon", "Chine", "Brésil", "Royaume-Uni", "Australie"],
    "Nombre de personnes impliquées": [15, 10, 8, 20, 12, 14, 25, 18, 6, 10]
}

# Additional 90 projects data
additional_projects = {
    "Nom du projet": ["GreenHouse", "MedTechAI", "EduTech", "WindFarm", "UrbanGarden", "HomeSecurity", "ElectricBus", "WaterForAll", "CulturalFest", "HealthCareApp",
                      "BioFarm", "MentalHealthSupport", "OnlineLearning", "SolarEnergy", "EcoTransport", "SmartCity", "RuralHealth", "ArtExhibition", "RenewableEnergy", "EcoConstruction",
                      "HealthMonitor", "EducationForAll", "WindPower", "RecycleProject", "TechInnovation", "GreenCity", "MedicalResearch", "CodingSchool", "BioEnergy", "SafeTransport",
                      "WaterClean", "CulturalExchange", "TeleHealth", "AgriTech", "ElectricCar", "CleanEnergy", "CommunitySupport", "ArtGallery", "CleanWaterTech", "EcoFriendlyPackaging",
                      "RenewableGrid", "SmartFarming", "MarineConservation", "SolarTech", "UrbanRenewal", "EdTech", "Agroecology", "TechForGood", "GreenEnergyStorage", "DigitalHealthcare",
                      "SmartHealthcare", "EcoPark", "RemoteEducation", "SmartIrrigation", "WasteManagement", "GreenBuilding", "PublicHealthApp", "ArtFestival", "CleanAirInitiative", "TechForSeniors",
                      "AgriInnovation", "RenewableTransport", "HealthTech", "CulturalHeritage", "CleanRiverProject", "SolarPowerGrid", "GreenStartup", "InclusiveEducation", "WaterSustainability", "Tech4Kids",
                      "RuralDevelopment", "BioTechResearch", "GreenEnergySolutions", "SmartWasteDisposal", "TeleEducation", "SustainableFarming", "Tech4Health", "DigitalLibrary", "CleanCityInitiative", "HealthcareRobotics",
                      "EcoFriendlyHomes", "SmartGrid", "MarineProtection", "DigitalArtPlatform", "UrbanSustainability", "EdTechSolutions", "GreenInitiative", "RenewableInnovation", "AgriResearch", "Tech4GoodHealth"],
    "Catégorie": ["Environnement", "Santé", "Éducation", "Énergie", "Environnement", "Technologie", "Transport", "Humanitaire", "Culture", "Santé",
                  "Environnement", "Santé", "Éducation", "Énergie", "Environnement", "Technologie", "Santé", "Culture", "Énergie", "Environnement",
                  "Santé", "Éducation", "Énergie", "Environnement", "Technologie", "Environnement", "Santé", "Éducation", "Énergie", "Transport",
                  "Environnement", "Culture", "Santé", "Environnement", "Transport", "Énergie", "Humanitaire", "Culture", "Environnement", "Environnement",
                  "Énergie", "Technologie", "Environnement", "Énergie", "Environnement", "Éducation", "Environnement", "Technologie", "Énergie", "Santé",
                  "Santé", "Environnement", "Éducation", "Énergie", "Environnement", "Environnement", "Santé", "Culture", "Environnement", "Technologie",
                  "Énergie", "Transport", "Santé", "Culture", "Environnement", "Énergie", "Environnement", "Éducation", "Environnement", "Technologie",
                  "Humanitaire", "Santé", "Énergie", "Environnement", "Éducation", "Environnement", "Santé", "Culture", "Environnement", "Technologie",
                  "Environnement", "Énergie", "Environnement", "Culture", "Environnement", "Éducation", "Environnement", "Énergie", "Énergie", "Santé"],
    "Image": ["green_house.png", "medtech_ai.png", "edutech.png", "wind_farm.png", "urban_garden.png", "home_security.png", "electric_bus.png", "water_for_all.png", "cultural_fest.png", "healthcare_app.png",
              "bio_farm.png", "mental_health_support.png", "online_learning.png", "solar_energy.png", "eco_transport.png", "smart_city.png", "rural_health.png", "art_exhibition.png", "renewable_energy.png", "eco_construction.png",
              "health_monitor.png", "education_for_all.png", "wind_power.png", "recycle_project.png", "tech_innovation.png", "green_city.png", "medical_research.png", "coding_school.png", "bio_energy.png", "safe_transport.png",
              "water_clean.png", "cultural_exchange.png", "tele_health.png", "agri_tech.png", "electric_car.png", "clean_energy.png", "community_support.png", "art_gallery.png", "clean_water_tech.png", "eco_friendly_packaging.png",
              "renewable_grid.png", "smart_farming.png", "marine_conservation.png", "solar_tech.png", "urban_renewal.png", "ed_tech.png", "agroecology.png", "tech_for_good.png", "green_energy_storage.png", "digital_healthcare.png",
              "smart_healthcare.png", "eco_park.png", "remote_education.png", "smart_irrigation.png", "waste_management.png", "green_building.png", "public_health_app.png", "art_festival.png", "clean_air_initiative.png", "tech_for_seniors.png",
              "agri_innovation.png", "renewable_transport.png", "health_tech.png", "cultural_heritage.png", "clean_river_project.png", "solar_power_grid.png", "green_startup.png", "inclusive_education.png", "water_sustainability.png", "tech_for_kids.png",
              "rural_development.png", "biotech_research.png", "green_energy_solutions.png", "smart_waste_disposal.png", "tele_education.png", "sustainable_farming.png", "tech_for_health.png", "digital_library.png", "clean_city_initiative.png", "healthcare_robotics.png",
              "eco_friendly_homes.png", "smart_grid.png", "marine_protection.png", "digital_art_platform.png", "urban_sustainability.png", "edtech_solutions.png", "green_initiative.png", "renewable_innovation.png", "agri_research.png", "tech_for_good_health.png"],
    "Description": ["Construction de serres urbaines pour une agriculture durable.", "Développement d'une IA pour diagnostiquer des maladies rares.", "Application pour aider les étudiants à organiser leurs études.",
                    "Installation de fermes éoliennes dans les régions venteuses.", "Création de jardins urbains communautaires.", "Système de sécurité domestique intelligent et connecté.", "Développement d'un bus électrique pour les transports en commun.",
                    "Projet de distribution d'eau potable dans les zones arides.", "Organisation d'un festival culturel international.", "Application pour la gestion de la santé personnelle.", "Ferme biologique avec des pratiques agricoles durables.",
                    "Programme de soutien pour la santé mentale.", "Plateforme d'apprentissage en ligne pour adultes.", "Installation de panneaux solaires pour les habitations.", "Développement de solutions de transport éco-responsables.",
                    "Ville intelligente avec des services connectés.", "Accès aux soins de santé dans les zones rurales.", "Exposition d'art contemporain.", "Développement de sources d'énergie renouvelable.", "Construction de bâtiments avec des matériaux écologiques.",
                    "Dispositif de surveillance de la santé en temps réel.", "Programme éducatif pour les enfants défavorisés.", "Production d'électricité à partir de l'énergie éolienne.", "Programme de recyclage dans les écoles.",
                    "Développement de nouvelles technologies pour l'industrie.", "Transformation urbaine pour une ville verte.", "Recherche médicale pour de nouveaux traitements.", "École de programmation pour les jeunes.",
                    "Production d'énergie à partir de biomasse.", "Amélioration de la sécurité des transports publics.", "Projet de nettoyage des rivières polluées.", "Programme d'échanges culturels internationaux.", "Service de téléconsultation médicale.",
                    "Technologie pour l'agriculture de précision.", "Développement d'une voiture électrique abordable.", "Promotion des énergies propres et renouvelables.", "Soutien aux communautés défavorisées.", "Galerie d'art contemporain en ligne.",
                    "Technologie de purification de l'eau.", "Développement de solutions d'emballage écologiques.", "Développement d'un réseau électrique intelligent utilisant des sources renouvelables.", "Système de gestion agricole intelligent utilisant l'IA et l'IoT.",
                    "Projet de conservation marine pour protéger les écosystèmes sous-marins.", "Innovation technologique pour améliorer l'efficacité des panneaux solaires.", "Projet de rénovation urbaine durable.", "Plateforme éducative utilisant des technologies de pointe.",
                    "Promotion de l'agroécologie pour une agriculture durable.", "Développement de technologies au service du bien commun.", "Solutions de stockage de l'énergie renouvelable.", "Plateforme numérique pour la gestion des dossiers médicaux.",
                    "Solutions de santé connectées", "Développement d'un parc écologique", "Plateforme d'éducation à distance", "Système d'irrigation intelligent", "Gestion des déchets écologiques", "Construction de bâtiments verts",
                    "Application de santé publique", "Organisation d'un festival d'art", "Initiative pour un air propre", "Technologie pour les seniors", "Innovation agricole durable", "Transport renouvelable",
                    "Technologie de la santé", "Préservation du patrimoine culturel", "Projet de nettoyage des rivières", "Réseau solaire", "Startup verte", "Éducation inclusive", "Durabilité de l'eau",
                    "Technologie pour enfants", "Développement rural", "Recherche en biotechnologie", "Solutions énergétiques vertes", "Élimination intelligente des déchets", "Télé-éducation", "Agriculture durable",
                    "Technologie pour la santé", "Bibliothèque numérique", "Initiative pour une ville propre", "Robotique médicale", "Maisons écologiques", "Réseau intelligent", "Protection marine", "Plateforme d'art numérique",
                    "Durabilité urbaine", "Solutions EdTech", "Initiative verte", "Innovation renouvelable", "Recherche agricole", "Technologie pour la bonne santé"],
    "Porteur du projet": ["Nina Dubois", "Paul Henry", "Isabelle Martin", "Jacques Lefevre", "Claire Morel", "Lucas Perrin", "Sophie Bernard", "Aminata Traoré", "Julien Robert", "Emilie Laurent",
                          "Antoine Girard", "Nathalie Dubois", "Amir Rahman", "Laura Richard", "Mehdi Kacem", "Alice Dupont", "Hélène Lefebvre", "Thomas Petit", "Claire Fournier", "Olivier Simon",
                          "Eva Collin", "Léa Marchand", "Matthieu Lefèvre", "Céline Girard", "Vincent Dubois", "Sophie Morel", "Alexandre Roche", "Mohamed Diallo", "François Martin", "Julie Bernard",
                          "Hugo Lefebvre", "Marine Richard", "Julie Moreau", "Antoine Dubois", "Marc Lefèvre", "Camille Leroy", "Nadia Kone", "Lucas Fontaine", "Sophie Marchal", "Maxime Renault",
                          "Caroline Dupont", "Marc Lefevre", "Laura Richard", "Nina Dubois", "Julien Robert", "Karim Nadir", "Sophie Morel", "Emilie Laurent", "Antoine Girard", "Marie Leblanc",
                          "Sarah Martin", "Thomas Leroy", "Emma Bernard", "Maxime Durand", "Elodie Petit", "Lucas Morel", "Paul Fournier", "Sophie Dupuis", "Nicolas Girard", "Julie Lefèvre",
                          "Lucie Dubois", "Antoine Martin", "Hugo Richard", "Eva Moreau", "Claire Petit", "Nathalie Leroy", "Thomas Fournier", "Julien Dupont", "Sarah Leblanc", "Marie Bernard",
                          "Nicolas Leroy", "Paul Morel", "Julie Martin", "Thomas Lefèvre", "Emma Dubois", "Lucas Richard", "Elodie Moreau", "Maxime Petit", "Paul Lefèvre", "Sarah Dupont",
                          "Claire Bernard", "Nicolas Dubois", "Eva Martin", "Antoine Petit", "Sophie Moreau", "Thomas Dupont", "Julie Richard", "Nathalie Lefèvre", "Maxime Morel", "Hugo Leblanc"],
    "Niveau d'études": ["Master en Agronomie", "Doctorat en Intelligence Artificielle", "Licence en Informatique", "Master en Énergie Renouvelable", "Licence en Horticulture", "Master en Cyber Sécurité", "Doctorat en Ingénierie des Transports",
                        "Master en Développement International", "Licence en Gestion d'Événements", "Master en Informatique Médicale", "Master en Agronomie", "Doctorat en Psychologie", "Master en Technologies de l'Éducation", "Licence en Énergie Renouvelable",
                        "Master en Transport Durable", "Doctorat en Urbanisme", "Master en Santé Publique", "Licence en Beaux-Arts", "Master en Énergies Renouvelables", "Master en Architecture Durable", "Doctorat en Bioingénierie", "Master en Sciences de l'Éducation",
                        "Licence en Énergie Renouvelable", "Master en Environnement", "Master en Ingénierie", "Doctorat en Urbanisme Durable", "Doctorat en Médecine", "Licence en Informatique", "Master en Bioénergie", "Doctorat en Sécurité des Transports",
                        "Master en Environnement", "Licence en Relations Internationales", "Master en Télémédecine", "Master en Agritech", "Doctorat en Ingénierie Automobile", "Master en Énergies Renouvelables", "Master en Travail Social", "Licence en Arts Numériques",
                        "Doctorat en Génie Chimique", "Master en Chimie Verte", "Doctorat en Électrotechnique", "Master en Agronomie", "Master en Biologie Marine", "Doctorat en Physique", "Master en Urbanisme", "Master en Technologies Éducatives", "Doctorat en Agronomie",
                        "Master en Informatique", "Doctorat en Énergies Renouvelables", "Master en Informatique Médicale", "Doctorat en Santé Publique", "Master en Environnement", "Licence en Éducation", "Doctorat en Énergies Renouvelables", "Master en Horticulture",
                        "Master en Gestion des Déchets", "Master en Architecture", "Doctorat en Santé Publique", "Licence en Beaux-Arts", "Master en Chimie", "Doctorat en Technologies", "Licence en Énergie Renouvelable", "Master en Sciences Environnementales",
                        "Doctorat en Biotechnologie", "Doctorat en Environnement", "Doctorat en Transports", "Licence en Histoire", "Doctorat en Chimie", "Master en Environnement", "Master en Éducation Inclusive", "Master en Gestion de l'Eau",
                        "Doctorat en Informatique", "Doctorat en Développement", "Doctorat en Biotechnologie", "Doctorat en Énergie Renouvelable", "Doctorat en Gestion des Déchets", "Doctorat en Éducation", "Master en Agriculture Durable",
                        "Master en Santé Publique", "Licence en Bibliothéconomie", "Doctorat en Environnement", "Doctorat en Robotique Médicale", "Master en Architecture", "Doctorat en Génie Électrique", "Doctorat en Biologie Marine", "Licence en Beaux-Arts",
                        "Master en Urbanisme", "Doctorat en Technologies Éducatives", "Doctorat en Environnement", "Master en Chimie"],
    "Expérience dans d'autres projets": ["3 projets", "2 projets", "1 projet", "5 projets", "4 projets", "3 projets", "6 projets", "7 projets", "2 projets", "4 projets", "5 projets", "3 projets", "4 projets", "3 projets", "2 projets", "5 projets", "6 projets", "1 projet", "4 projets", "5 projets",
                                         "3 projets", "6 projets", "4 projets", "3 projets", "5 projets", "4 projets", "6 projets", "2 projets", "4 projets", "5 projets", "3 projets", "2 projets", "4 projets", "3 projets", "6 projets", "5 projets", "4 projets", "1 projet", "4 projets", "5 projets",
                                         "6 projets", "4 projets", "5 projets", "3 projets", "4 projets", "3 projets", "6 projets", "4 projets", "5 projets", "3 projets", "3 projets", "2 projets", "1 projet", "5 projets", "4 projets", "3 projets", "6 projets", "7 projets", "2 projets", "4 projets",
                                         "5 projets", "3 projets", "4 projets", "3 projets", "2 projets", "5 projets", "6 projets", "1 projet", "4 projets", "5 projets", "3 projets", "6 projets", "4 projets", "3 projets", "5 projets", "4 projets", "6 projets", "2 projets", "4 projets", "5 projets",
                                         "3 projets", "2 projets", "4 projets", "3 projets", "6 projets", "5 projets", "4 projets", "1 projet", "4 projets", "5 projets"],
    "Objectif financier": ["600000 €", "800000 €", "100000 €", "1200000 €", "200000 €", "250000 €", "3000000 €", "500000 €", "150000 €", "200000 €", "750000 €", "180000 €", "300000 €", "850000 €", "450000 €", "1500000 €", "400000 €", "50000 €", "900000 €", "1000000 €",
                           "500000 €", "250000 €", "1100000 €", "200000 €", "1200000 €", "800000 €", "1500000 €", "100000 €", "700000 €", "950000 €", "300000 €", "150000 €", "400000 €", "650000 €", "2500000 €", "1300000 €", "350000 €", "60000 €", "800000 €", "550000 €",
                           "1400000 €", "700000 €", "900000 €", "1100000 €", "1200000 €", "500000 €", "850000 €", "700000 €", "1000000 €", "600000 €", "700000 €", "800000 €", "100000 €", "2000000 €", "500000 €", "600000 €", "900000 €", "1500000 €", "1200000 €",
                           "850000 €", "1100000 €", "400000 €", "50000 €", "300000 €", "600000 €", "2500000 €", "1300000 €", "350000 €", "60000 €", "1400000 €", "700000 €", "900000 €", "1100000 €", "1200000 €", "500000 €", "850000 €", "700000 €", "1000000 €", "600000 €",
                           "900000 €", "200000 €", "300000 €", "500000 €", "800000 €", "600000 €", "700000 €", "2000000 €", "300000 €", "2500000 €", "180000"],
    "Date de fin": [random_date(datetime(2023, 1, 1), datetime(2027, 12, 31)).strftime("%Y-%m-%d") for _ in range(90)],
    "A quoi servira le financement": ["Achat de matériel et installation des serres", "Recherche et développement de l'IA", "Développement de l'application et marketing", "Achat et installation des éoliennes", "Achat de matériel et aménagement des jardins", "Développement et commercialisation du système",
                                      "Production et tests des prototypes", "Achat et distribution de matériel", "Organisation et promotion du festival", "Développement de l'application et marketing", "Achat de terrain et matériel agricole", "Création de programmes et formation du personnel",
                                      "Développement de la plateforme et création de contenu", "Achat et installation des panneaux solaires", "Recherche et développement des solutions", "Développement et intégration des services", "Achat de matériel et formation du personnel", "Organisation et promotion de l'exposition",
                                      "Recherche et développement", "Achat de matériaux et construction", "Recherche et développement du dispositif", "Création de contenu éducatif et formation", "Achat et installation des éoliennes", "Achat de matériel de recyclage et campagnes de sensibilisation",
                                      "Recherche et développement", "Aménagement des espaces verts", "Recherche en laboratoire et essais cliniques", "Création de cours et recrutement de formateurs", "Achat de matériel et production", "Recherche et mise en place des solutions", "Achat de matériel et opérations de nettoyage",
                                      "Organisation des échanges et promotion", "Développement de la plateforme et marketing", "Développement de la technologie et commercialisation", "Production et tests des prototypes", "Campagnes de sensibilisation et installations", "Achat de matériel et formation du personnel",
                                      "Développement de la plateforme et marketing", "Recherche et développement de la technologie", "Recherche et développement de matériaux écologiques", "Installation et maintenance du réseau", "Développement du système et tests sur le terrain", "Recherche, protection des habitats et sensibilisation",
                                      "Recherche et développement technologique", "Rénovation des infrastructures et création d'espaces verts", "Développement de la plateforme et création de contenu interactif", "Recherche, développement et formation des agriculteurs", "Recherche et développement, tests utilisateurs",
                                      "Recherche et développement, mise en œuvre des solutions", "Développement de la plateforme et sécurité des données", "R&D et commercialisation", "Aménagement du parc et activités éducatives", "Développement de la plateforme et marketing",
                                      "Installation et maintenance du système", "Développement de la technologie et campagnes de sensibilisation", "Construction et équipements", "Développement de l'application et campagnes de sensibilisation", "Organisation et promotion du festival",
                                      "Développement de la technologie et marketing", "Recherche et développement des solutions agricoles", "Développement de solutions de transport renouvelables", "Recherche et développement des dispositifs de santé",
                                      "Restauration et préservation du patrimoine", "Nettoyage des rivières et campagnes de sensibilisation", "Installation et maintenance des infrastructures solaires", "Recherche et développement de la startup",
                                      "Développement et intégration des services éducatifs", "Installation et maintenance des infrastructures", "Recherche et développement de la technologie pour enfants", "Développement et intégration des services ruraux",
                                      "Recherche et essais en biotechnologie", "Recherche et développement de solutions énergétiques", "Développement et tests des systèmes d'élimination des déchets", "Développement de la plateforme et marketing",
                                      "Recherche et développement des pratiques agricoles durables", "Développement et intégration des services de santé", "Développement et maintenance de la bibliothèque numérique", "Nettoyage et aménagement des villes",
                                      "Recherche et développement de la robotique médicale", "Construction de maisons écologiques", "Recherche et développement du réseau intelligent", "Protection des habitats marins",
                                      "Développement de la plateforme et marketing", "Rénovation et aménagement urbain durable", "Développement de solutions éducatives technologiques", "Recherche et développement d'initiatives vertes",
                                      "Recherche et développement d'innovations renouvelables", "Recherche et développement agricoles", "Développement de technologies pour la bonne santé","?"],
    "Score potentiel de réussite": [random_score() for _ in range(90)],
    "Pays": random.choices(["France", "Allemagne", "États-Unis", "Japon", "Brésil", "Inde", "Canada", "Australie", "Chine", "Royaume-Uni"], k=90),
    "Nombre de personnes impliquées": [random.randint(5, 25) for _ in range(90)]
}

# Ensure all lists in `additional_projects` have the same length
lengths = [len(v) for v in additional_projects.values()]
if len(set(lengths)) != 1:
    raise ValueError(f"All lists in additional_projects must have the same length. Current lengths: {lengths}")

# Convert initial and additional projects to DataFrames
df = pd.DataFrame(data)
additional_df = pd.DataFrame(additional_projects)

# Append the additional projects to the initial DataFrame
full_df = pd.concat([df, additional_df], ignore_index=True)

# Save to CSV in the current directory
csv_path = "projets_imaginaires_100_complet.csv"
full_df.to_csv(csv_path, index=False)

print(f"CSV file saved to {csv_path}")
