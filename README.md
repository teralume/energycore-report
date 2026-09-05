<div align="center">

<img src="assets/front-matter/upc-logo.png" width="72" alt="Logo de la Universidad Peruana de Ciencias Aplicadas">

**Universidad Peruana de Ciencias Aplicadas**<br>
**Carrera de Ingeniería de Software**<br>
**Ciclo académico 2026-20**

**1ASI0732**<br>
**Diseño de Experimentos de Ingeniería de Software**

**NRC 9100**

**Profesor**<br>
**Alex Humberto Sánchez Ponce**

# Informe de Trabajo Final

**Startup: Teralume**<br>
**Producto: EnergyCore**

## Integrantes

| Código | Apellidos y nombres |
|:--:|:--|
| U20241E406 | Loa Rojas, Jean Franck |

**Septiembre de 2026**

</div>

<div style="page-break-after: always;"></div>

## Registro de Versiones del Informe

| Versión | Fecha | Autor | Descripción de la modificación |
|:--:|:--:|:--|:--|
| AV1 | 05/09/2026 | Loa Rojas, Jean Franck | Creación de la estructura del informe conforme al enunciado del curso, incorporación de la carátula, los enlaces de los repositorios, el perfil individual y el sustento inicial del Student Outcome 4. |

<div style="page-break-after: always;"></div>

## Project Report Collaboration Insights

EnergyCore se desarrolla mediante cinco repositorios independientes dentro de la organización Teralume. Esta separación permite mantener trazabilidad específica para el informe, la Landing Page, la aplicación web, la aplicación móvil y los servicios de backend.

### Repositorios del proyecto

- [Project Report](https://github.com/teralume/energycore-report)
- [Landing Page](https://github.com/teralume/energycore-website)
- [Frontend Web Application](https://github.com/teralume/energycore-webapp)
- [Native Mobile Application](https://github.com/teralume/energycore-mobile)
- [RESTful API](https://github.com/teralume/energycore-platform)

### Entrega AV1

Durante AV1 se preparó la plataforma EnergyCore a partir de un proyecto académico anterior cuya reutilización fue autorizada por el profesor. El trabajo no se limitó a cambiar el nombre del producto: se separaron los entregables en repositorios propios, se actualizó la identidad a Teralume y EnergyCore, se revisaron los contratos entre frontend y backend, se desarrolló una nueva experiencia visual y se incorporó una aplicación móvil en Flutter conectada a la misma API.

#### Participación de Loa Rojas Jean Franck

- Creó y vinculó los cinco repositorios de EnergyCore con la organización Teralume.
- Adaptó la solución previamente desarrollada a la identidad y alcance de EnergyCore.
- Implementó y corrigió la aplicación web Angular y su integración con la API REST.
- Desarrolló la Landing Page y alineó su navegación con el inicio de sesión de la aplicación.
- Implementó la aplicación móvil Flutter para Android, con autenticación, consumo energético, gestión de dispositivos y adaptación responsiva.
- Revisó la estructura DDD del backend y la conexión de los bounded contexts del producto.
- Preparó la estructura inicial del informe de acuerdo con el enunciado de Diseño de Experimentos de Ingeniería de Software.

#### Evidencias de colaboración y commits

Los siguientes commits locales organizan el trabajo existente en bloques verificables. Se generaron con la fecha real de incorporación al control de versiones y no pretenden simular una cronología anterior.

| Repositorio | Commits preparados para AV1 |
|:--|:--|
| Report | `1a0eced` - estructura del informe y Student Outcome |
| Platform | `63d5a7a` - inicialización; `6f7f47e` - bounded contexts; `250517e` - pruebas |
| WebApp | `d3b1c79` - inicialización; `eb76229` - experiencia web; `85ee2eb` - referencias de diseño |
| Mobile | `1fe1a80` - inicialización Flutter; `24cf286` - experiencia móvil; `0f545f0` - pruebas y paridad web |
| Website | `b3adb4e` - Landing Page; `268de90` - sistema de diseño |

_Las capturas de commits y GitHub Insights permanecen pendientes hasta publicar las ramas en los repositorios remotos._

<div style="page-break-after: always;"></div>

## Contenido

- [Student Outcome](#student-outcome)
  - [Loa Rojas Jean Franck](#loa-rojas-jean-franck)
- [Part I As Is Software Project](#part-i-as-is-software-project)
  - [Capítulo I Introducción](#capítulo-i-introducción)
    - [1.1 Startup Profile](#11-startup-profile)
      - [1.1.1 Descripción de la Startup](#111-descripción-de-la-startup)
      - [1.1.2 Perfiles de integrantes del equipo](#112-perfiles-de-integrantes-del-equipo)
    - [1.2 Solution Profile](#12-solution-profile)
      - [1.2.1 Antecedentes y problemática](#121-antecedentes-y-problemática)
      - [1.2.2 Lean UX Process](#122-lean-ux-process)
      - [1.2.2.3 Lean UX Hypothesis Statements](#1223-lean-ux-hypothesis-statements)
      - [1.2.2.4 Lean UX Canvas](#1224-lean-ux-canvas)
    - [1.3 Segmentos objetivo](#13-segmentos-objetivo)
  - [Capítulo II Requirements Elicitation and Analysis](#capítulo-ii-requirements-elicitation-and-analysis)
    - [2.1 Competidores](#21-competidores)
      - [2.1.1 Análisis competitivo](#211-análisis-competitivo)
      - [2.1.2 Estrategias y tácticas frente a competidores](#212-estrategias-y-tácticas-frente-a-competidores)
    - [2.2 Entrevistas](#22-entrevistas)
      - [2.2.1 Diseño de entrevistas](#221-diseño-de-entrevistas)
      - [2.2.2 Registro de entrevistas](#222-registro-de-entrevistas)
      - [2.2.3 Análisis de entrevistas](#223-análisis-de-entrevistas)
    - [2.3 Needfinding](#23-needfinding)
      - [2.3.1 User Personas](#231-user-personas)
      - [2.3.2 User Task Matrix](#232-user-task-matrix)
      - [2.3.3 User Journey Mapping](#233-user-journey-mapping)
      - [2.3.4 Empathy Mapping](#234-empathy-mapping)
      - [2.3.5 As Is Scenario Mapping](#235-as-is-scenario-mapping)
    - [2.4 Ubiquitous Language](#24-ubiquitous-language)
  - [Capítulo III Requirements Specification](#capítulo-iii-requirements-specification)
    - [3.1 To Be Scenario Mapping](#31-to-be-scenario-mapping)
    - [3.2 User Stories](#32-user-stories)
    - [3.3 Product Backlog](#33-product-backlog)
    - [3.4 Impact Mapping](#34-impact-mapping)
  - [Capítulo IV Product Design](#capítulo-iv-product-design)
    - [4.1 Style Guidelines](#41-style-guidelines)
      - [4.1.1 General Style Guidelines](#411-general-style-guidelines)
      - [4.1.2 Web Style Guidelines](#412-web-style-guidelines)
      - [4.1.3 Mobile Style Guidelines](#413-mobile-style-guidelines)
        - [4.1.3.1 iOS Mobile Style Guidelines](#4131-ios-mobile-style-guidelines)
        - [4.1.3.2 Android Mobile Style Guidelines](#4132-android-mobile-style-guidelines)
    - [4.2 Information Architecture](#42-information-architecture)
      - [4.2.1 Organization Systems](#421-organization-systems)
      - [4.2.2 Labeling Systems](#422-labeling-systems)
      - [4.2.3 SEO Tags and Meta Tags](#423-seo-tags-and-meta-tags)
      - [4.2.4 Searching Systems](#424-searching-systems)
      - [4.2.5 Navigation Systems](#425-navigation-systems)
    - [4.3 Landing Page UI Design](#43-landing-page-ui-design)
      - [4.3.1 Landing Page Wireframe](#431-landing-page-wireframe)
      - [4.3.2 Landing Page Mockup](#432-landing-page-mockup)
    - [4.4 Mobile Applications UX UI Design](#44-mobile-applications-ux-ui-design)
      - [4.4.1 Mobile Applications Wireframes](#441-mobile-applications-wireframes)
      - [4.4.2 Mobile Applications Wireflow Diagrams](#442-mobile-applications-wireflow-diagrams)
      - [4.4.3 Mobile Applications Mockups](#443-mobile-applications-mockups)
      - [4.4.4 Mobile Applications User Flow Diagrams](#444-mobile-applications-user-flow-diagrams)
    - [4.5 Mobile Applications Prototyping](#45-mobile-applications-prototyping)
      - [4.5.1 Android Mobile Applications Prototyping](#451-android-mobile-applications-prototyping)
      - [4.5.2 iOS Mobile Applications Prototyping](#452-ios-mobile-applications-prototyping)
    - [4.6 Web Applications UX UI Design](#46-web-applications-ux-ui-design)
      - [4.6.1 Web Applications Wireframes](#461-web-applications-wireframes)
      - [4.6.2 Web Applications Wireflow Diagrams](#462-web-applications-wireflow-diagrams)
      - [4.6.3 Web Applications Mockups](#463-web-applications-mockups)
      - [4.6.4 Web Applications User Flow Diagrams](#464-web-applications-user-flow-diagrams)
    - [4.7 Web Applications Prototyping](#47-web-applications-prototyping)
    - [4.8 Domain Driven Software Architecture](#48-domain-driven-software-architecture)
      - [4.8.1 Software Architecture Context Diagram](#481-software-architecture-context-diagram)
      - [4.8.2 Software Architecture Container Diagrams](#482-software-architecture-container-diagrams)
      - [4.8.3 Software Architecture Components Diagrams](#483-software-architecture-components-diagrams)
    - [4.9 Software Object Oriented Design](#49-software-object-oriented-design)
      - [4.9.1 Class Diagrams](#491-class-diagrams)
      - [4.9.2 Class Dictionary](#492-class-dictionary)
    - [4.10 Database Design](#410-database-design)
      - [4.10.1 Relational Non Relational Database Diagram](#4101-relational-non-relational-database-diagram)
  - [Capítulo V Product Implementation](#capítulo-v-product-implementation)
    - [5.1 Software Configuration Management](#51-software-configuration-management)
      - [5.1.1 Software Development Environment Configuration](#511-software-development-environment-configuration)
      - [5.1.2 Source Code Management](#512-source-code-management)
      - [5.1.3 Source Code Style Guide and Conventions](#513-source-code-style-guide-and-conventions)
      - [5.1.4 Software Deployment Configuration](#514-software-deployment-configuration)
    - [5.2 Product Implementation and Deployment](#52-product-implementation-and-deployment)
      - [5.2.1 Sprint Backlogs](#521-sprint-backlogs)
      - [5.2.2 Implemented Landing Page Evidence](#522-implemented-landing-page-evidence)
      - [5.2.3 Implemented Frontend Web Application Evidence](#523-implemented-frontend-web-application-evidence)
      - [5.2.4 Acuerdo de Servicio SaaS](#524-acuerdo-de-servicio-saas)
      - [5.2.5 Implemented Native Mobile Application Evidence](#525-implemented-native-mobile-application-evidence)
      - [5.2.6 Implemented RESTful API and Serverless Backend Evidence](#526-implemented-restful-api-and-serverless-backend-evidence)
      - [5.2.7 RESTful API Documentation](#527-restful-api-documentation)
      - [5.2.8 Team Collaboration Insights](#528-team-collaboration-insights)
    - [5.3 Video About the Product](#53-video-about-the-product)
- [Part II Verification Validation and Pipeline](#part-ii-verification-validation-and-pipeline)
  - [Capítulo VI Product Verification and Validation](#capítulo-vi-product-verification-and-validation)
    - [6.1 Testing Suites and Validation](#61-testing-suites-and-validation)
      - [6.1.1 Core Entities Unit Tests](#611-core-entities-unit-tests)
      - [6.1.2 Core Integration Tests](#612-core-integration-tests)
      - [6.1.3 Core Behavior Driven Development](#613-core-behavior-driven-development)
      - [6.1.4 Core System Tests](#614-core-system-tests)
    - [6.2 Static Testing and Verification](#62-static-testing-and-verification)
      - [6.2.1 Static Code Analysis](#621-static-code-analysis)
        - [6.2.1.1 Coding Standard and Code Conventions](#6211-coding-standard-and-code-conventions)
        - [6.2.1.2 Code Quality and Code Security](#6212-code-quality-and-code-security)
      - [6.2.2 Reviews](#622-reviews)
    - [6.3 Validation Interviews](#63-validation-interviews)
      - [6.3.1 Diseño de Entrevistas](#631-diseño-de-entrevistas)
      - [6.3.2 Registro de Entrevistas](#632-registro-de-entrevistas)
      - [6.3.3 Evaluaciones según heurísticas](#633-evaluaciones-según-heurísticas)
    - [6.4 Auditoría de Experiencias de Usuario](#64-auditoría-de-experiencias-de-usuario)
      - [6.4.1 Auditoría realizada](#641-auditoría-realizada)
        - [6.4.1.1 Información del grupo auditado](#6411-información-del-grupo-auditado)
        - [6.4.1.2 Cronograma de auditoría realizada](#6412-cronograma-de-auditoría-realizada)
        - [6.4.1.3 Contenido de auditoría realizada](#6413-contenido-de-auditoría-realizada)
      - [6.4.2 Auditoría recibida](#642-auditoría-recibida)
        - [6.4.2.1 Información del grupo auditor](#6421-información-del-grupo-auditor)
        - [6.4.2.2 Cronograma de auditoría recibida](#6422-cronograma-de-auditoría-recibida)
        - [6.4.2.3 Contenido de auditoría recibida](#6423-contenido-de-auditoría-recibida)
        - [6.4.2.4 Resumen de modificaciones para subsanar hallazgos](#6424-resumen-de-modificaciones-para-subsanar-hallazgos)
  - [Capítulo VII DevOps Practices](#capítulo-vii-devops-practices)
    - [7.1 Continuous Integration](#71-continuous-integration)
      - [7.1.1 Tools and Practices](#711-tools-and-practices)
      - [7.1.2 Build and Test Suite Pipeline Components](#712-build-and-test-suite-pipeline-components)
    - [7.2 Continuous Delivery](#72-continuous-delivery)
      - [7.2.1 Tools and Practices](#721-tools-and-practices)
      - [7.2.2 Stages Deployment Pipeline Components](#722-stages-deployment-pipeline-components)
    - [7.3 Continuous Deployment](#73-continuous-deployment)
      - [7.3.1 Tools and Practices](#731-tools-and-practices)
      - [7.3.2 Production Deployment Pipeline Components](#732-production-deployment-pipeline-components)
    - [7.4 Continuous Monitoring](#74-continuous-monitoring)
      - [7.4.1 Tools and Practices](#741-tools-and-practices)
      - [7.4.2 Monitoring Pipeline Components](#742-monitoring-pipeline-components)
      - [7.4.3 Alerting Pipeline Components](#743-alerting-pipeline-components)
      - [7.4.4 Notification Pipeline Components](#744-notification-pipeline-components)
- [Part III Experiment Driven Lifecycle](#part-iii-experiment-driven-lifecycle)
  - [Capítulo VIII Experiment Driven Development](#capítulo-viii-experiment-driven-development)
    - [8.1 Experiment Planning](#81-experiment-planning)
      - [8.1.1 As Is Summary](#811-as-is-summary)
      - [8.1.2 Raw Material Assumptions Knowledge Gaps Ideas Claims](#812-raw-material-assumptions-knowledge-gaps-ideas-claims)
      - [8.1.3 Experiment Ready Questions](#813-experiment-ready-questions)
      - [8.1.4 Question Backlog](#814-question-backlog)
      - [8.1.5 Experiment Cards](#815-experiment-cards)
    - [8.2 Experiment Design](#82-experiment-design)
      - [8.2.1 Hypotheses](#821-hypotheses)
      - [8.2.2 Domain Business Metrics](#822-domain-business-metrics)
      - [8.2.3 Measures](#823-measures)
      - [8.2.4 Conditions](#824-conditions)
      - [8.2.5 Scale Calculations and Decisions](#825-scale-calculations-and-decisions)
      - [8.2.6 Methods Selection](#826-methods-selection)
      - [8.2.7 Data Analytics Goals KPIs and Metrics Selection](#827-data-analytics-goals-kpis-and-metrics-selection)
      - [8.2.8 Web and Mobile Tracking Plan](#828-web-and-mobile-tracking-plan)
    - [8.3 Experimentation](#83-experimentation)
      - [8.3.1 To Be User Stories](#831-to-be-user-stories)
      - [8.3.2 To Be Product Backlog](#832-to-be-product-backlog)
      - [8.3.3 Pipeline Supported Experiment Driven To Be Software Platform Lifecycle](#833-pipeline-supported-experiment-driven-to-be-software-platform-lifecycle)
        - [8.3.3.1 To Be Sprint Backlogs](#8331-to-be-sprint-backlogs)
        - [8.3.3.2 Implemented To Be Landing Page Evidence](#8332-implemented-to-be-landing-page-evidence)
        - [8.3.3.3 Implemented To Be Frontend Web Application Evidence](#8333-implemented-to-be-frontend-web-application-evidence)
        - [8.3.3.4 Implemented To Be Native Mobile Application Evidence](#8334-implemented-to-be-native-mobile-application-evidence)
        - [8.3.3.5 Implemented To Be RESTful API and Serverless Backend Evidence](#8335-implemented-to-be-restful-api-and-serverless-backend-evidence)
        - [8.3.3.6 Team Collaboration Insights](#8336-team-collaboration-insights)
      - [8.3.4 To Be Validation Interviews](#834-to-be-validation-interviews)
        - [8.3.4.1 Diseño de Entrevistas](#8341-diseño-de-entrevistas)
        - [8.3.4.2 Registro de Entrevistas](#8342-registro-de-entrevistas)
    - [8.4 Experiment Aftermath and Analysis](#84-experiment-aftermath-and-analysis)
      - [8.4.1 Analysis and Interpretation of Results](#841-analysis-and-interpretation-of-results)
      - [8.4.2 Re Scored and Re Prioritized Question Backlog](#842-re-scored-and-re-prioritized-question-backlog)
    - [8.5 Continuous Learning](#85-continuous-learning)
      - [8.5.1 Shareback Session Artifacts Learning Workflow](#851-shareback-session-artifacts-learning-workflow)
    - [8.6 To Be Software Platform Pre Launch](#86-to-be-software-platform-pre-launch)
      - [8.6.1 About the Product Intro Video](#861-about-the-product-intro-video)
      - [8.6.2 Resumen usando GEES Framework](#862-resumen-usando-gees-framework)
- [Conclusiones](#conclusiones)
- [Video App Validation](#video-app-validation)
- [Video About the Team](#video-about-the-team)
- [Bibliografía](#bibliografía)
- [Anexos](#anexos)

<div style="page-break-after: always;"></div>

## Student Outcome

Cada participante del equipo debe sustentar evidencia de cómo las actividades realizadas en el trabajo final han ayudado a desarrollar las dimensiones del student outcome. Por ello en esta sección debe haber una subsección por cada alumno donde éste describa por escrito la relación entre el outcome, sus dimensiones y el trabajo que ha realizado. Esto se complementa con lo reflejado en los testimonios expuestos que forman parte del video About The Team.

El curso contribuye al cumplimiento del Student Outcome ABET:

**ABET EAC Student Outcome 4**

**Criterio:** La capacidad de reconocer responsabilidades éticas y profesionales en situaciones de ingeniería y hacer juicios informados, que deben considerar el impacto de las soluciones de ingeniería en contextos globales, económicos, ambientales y sociales.

En el siguiente cuadro se describen las acciones realizadas y los enunciados de conclusiones que permiten sustentar el logro del ABET EAC Student Outcome 4.

### Loa Rojas Jean Franck

| Criterio específico | Acciones realizadas | Conclusiones |
|:--|:--|:--|
| **4.c.1 Reconoce responsabilidad ética y profesional en situaciones de ingeniería de software** | **AV1:** Reutilicé un proyecto académico anterior con autorización expresa del profesor y documenté su adaptación bajo una nueva identidad, evitando presentarlo como un producto creado íntegramente desde cero para este curso. Organicé EnergyCore en repositorios independientes para conservar trazabilidad y revisé que los componentes reutilizados no mantuvieran nombres, cachés o referencias funcionales de ElectroCorp. En la solución técnica consideré la autenticación con JWT, el cifrado de contraseñas con BCrypt, el almacenamiento del token móvil mediante Android Keystore y AES-GCM, la separación de responsabilidades mediante bounded contexts y la comunicación honesta de las verificaciones que todavía requieren evidencia. También incorporé una experiencia accesible mediante tema claro y oscuro, diseño responsivo, navegación de retorno en autenticación y mensajes explícitos cuando no existe conexión a Internet. | **Pendiente de consenso grupal para AV1.** |
| **4.c.2 Emite juicios informados considerando el impacto de las soluciones de ingeniería de software en contextos globales, económicos, ambientales y sociales** | **AV1:** Evalué EnergyCore como una solución multiplataforma que debe funcionar en web y Android sin mantener fuentes de datos separadas, por lo que ambas aplicaciones consumen una única API y base de datos. Consideré el impacto económico mediante el seguimiento de consumo, costos, metas y planes; el impacto ambiental mediante herramientas que permiten identificar consumos elevados, programar dispositivos y promover decisiones de ahorro energético; y el impacto social mediante una interfaz responsiva, soporte en español, inglés y portugués, y avisos de conectividad comprensibles. La adaptación de la solución busca que hogares y pequeños negocios puedan tomar decisiones informadas sin depender de una infraestructura distinta para cada cliente. | **Pendiente de consenso grupal para AV1.** |

#### Evidencias individuales

- Código de estudiante: **U20241E406**.
- Repositorios trabajados: Report, Website, WebApp, Mobile y Platform.
- Capturas de commits e Insights: **pendientes de incorporar después de la publicación de AV1**.
- Testimonio para el video About The Team: **pendiente de grabación**.

<div style="page-break-after: always;"></div>

# Part I As Is Software Project

# Capítulo I Introducción

## 1.1 Startup Profile

### 1.1.1 Descripción de la Startup

_Pendiente de desarrollo por el equipo._

### 1.1.2 Perfiles de integrantes del equipo

| Nombre completo | Código | Carrera | Fotografía | Conocimientos y habilidades |
|:--|:--:|:--|:--:|:--|
| Loa Rojas, Jean Franck | U20241E406 | Ingeniería de Software, Universidad Peruana de Ciencias Aplicadas | <img src="assets/team/jean-loa.jpg" width="120" alt="Jean Franck Loa Rojas"> | Soy Jean Franck Loa Rojas, estudiante de séptimo ciclo de Ingeniería de Software. Aporto experiencia en desarrollo de aplicaciones web con Angular, servicios backend con Java y Spring Boot, aplicaciones móviles con Flutter, modelado de soluciones mediante Domain-Driven Design y administración de repositorios con Git. Me interesa construir productos integrados, documentar las decisiones técnicas y evaluar sus efectos sobre las personas, los costos y el uso responsable de los recursos. |

_Los perfiles de los demás integrantes se incorporarán cuando el equipo confirme sus datos._

## 1.2 Solution Profile

### 1.2.1 Antecedentes y problemática

_Pendiente de desarrollo por el equipo mediante la técnica de las 5W y 2H._

### 1.2.2 Lean UX Process

#### 1.2.2.1 Lean UX Problem Statements

_Pendiente de desarrollo por el equipo._

#### 1.2.2.2 Lean UX Assumptions

_Pendiente de desarrollo por el equipo._

#### 1.2.2.3 Lean UX Hypothesis Statements

_Pendiente de desarrollo por el equipo._

#### 1.2.2.4 Lean UX Canvas

_Pendiente de desarrollo por el equipo._

## 1.3 Segmentos objetivo

_Pendiente de desarrollo por el equipo con información demográfica y fuentes estadísticas._

# Capítulo II Requirements Elicitation and Analysis

## 2.1 Competidores

### 2.1.1 Análisis competitivo

_Pendiente de desarrollo por el equipo._

### 2.1.2 Estrategias y tácticas frente a competidores

_Pendiente de desarrollo por el equipo._

## 2.2 Entrevistas

### 2.2.1 Diseño de entrevistas

_Pendiente de desarrollo por el equipo._

### 2.2.2 Registro de entrevistas

_Pendiente de entrevistas y evidencias audiovisuales._

### 2.2.3 Análisis de entrevistas

_Pendiente de desarrollo después de realizar las entrevistas._

## 2.3 Needfinding

### 2.3.1 User Personas

_Pendiente de desarrollo por el equipo._

### 2.3.2 User Task Matrix

_Pendiente de desarrollo por el equipo._

### 2.3.3 User Journey Mapping

_Pendiente de desarrollo por el equipo._

### 2.3.4 Empathy Mapping

_Pendiente de desarrollo por el equipo._

### 2.3.5 As Is Scenario Mapping

_Pendiente de desarrollo por el equipo._

## 2.4 Ubiquitous Language

_Pendiente de desarrollo por el equipo._

# Capítulo III Requirements Specification

## 3.1 To Be Scenario Mapping

_Pendiente de desarrollo por el equipo._

## 3.2 User Stories

_Pendiente de desarrollo por el equipo._

## 3.3 Product Backlog

_Pendiente de desarrollo por el equipo._

## 3.4 Impact Mapping

_Pendiente de desarrollo por el equipo._

# Capítulo IV Product Design

## 4.1 Style Guidelines

### 4.1.1 General Style Guidelines

_Pendiente de desarrollo por el equipo._

### 4.1.2 Web Style Guidelines

_Pendiente de desarrollo por el equipo._

### 4.1.3 Mobile Style Guidelines

#### 4.1.3.1 iOS Mobile Style Guidelines

_Pendiente de confirmar si corresponde una implementación iOS._

#### 4.1.3.2 Android Mobile Style Guidelines

_Pendiente de desarrollo por el equipo._

## 4.2 Information Architecture

### 4.2.1 Organization Systems

_Pendiente de desarrollo por el equipo._

### 4.2.2 Labeling Systems

_Pendiente de desarrollo por el equipo._

### 4.2.3 SEO Tags and Meta Tags

_Pendiente de desarrollo por el equipo._

### 4.2.4 Searching Systems

_Pendiente de desarrollo por el equipo._

### 4.2.5 Navigation Systems

_Pendiente de desarrollo por el equipo._

## 4.3 Landing Page UI Design

### 4.3.1 Landing Page Wireframe

_Pendiente de incorporar evidencia._

### 4.3.2 Landing Page Mockup

_Pendiente de incorporar evidencia._

## 4.4 Mobile Applications UX UI Design

### 4.4.1 Mobile Applications Wireframes

_Pendiente de incorporar evidencia._

### 4.4.2 Mobile Applications Wireflow Diagrams

_Pendiente de incorporar evidencia._

### 4.4.3 Mobile Applications Mockups

_Pendiente de incorporar evidencia._

### 4.4.4 Mobile Applications User Flow Diagrams

_Pendiente de incorporar evidencia._

## 4.5 Mobile Applications Prototyping

### 4.5.1 Android Mobile Applications Prototyping

_Pendiente de incorporar el enlace y la evidencia del prototipo._

### 4.5.2 iOS Mobile Applications Prototyping

_Pendiente de confirmar su aplicación al alcance del equipo._

## 4.6 Web Applications UX UI Design

### 4.6.1 Web Applications Wireframes

_Pendiente de incorporar evidencia._

### 4.6.2 Web Applications Wireflow Diagrams

_Pendiente de incorporar evidencia._

### 4.6.3 Web Applications Mockups

_Pendiente de incorporar evidencia._

### 4.6.4 Web Applications User Flow Diagrams

_Pendiente de incorporar evidencia._

## 4.7 Web Applications Prototyping

_Pendiente de incorporar el enlace y la evidencia del prototipo._

## 4.8 Domain Driven Software Architecture

### 4.8.1 Software Architecture Context Diagram

_Pendiente de incorporar el diagrama._

### 4.8.2 Software Architecture Container Diagrams

_Pendiente de incorporar los diagramas._

### 4.8.3 Software Architecture Components Diagrams

_Pendiente de incorporar los diagramas._

## 4.9 Software Object Oriented Design

### 4.9.1 Class Diagrams

_Pendiente de incorporar los diagramas por bounded context._

### 4.9.2 Class Dictionary

_Pendiente de desarrollo por el equipo._

## 4.10 Database Design

### 4.10.1 Relational Non Relational Database Diagram

_Pendiente de incorporar el diagrama correspondiente a la base de datos del backend._

# Capítulo V Product Implementation

## 5.1 Software Configuration Management

### 5.1.1 Software Development Environment Configuration

_Pendiente para la entrega correspondiente._

### 5.1.2 Source Code Management

_Pendiente para la entrega correspondiente._

### 5.1.3 Source Code Style Guide and Conventions

_Pendiente para la entrega correspondiente._

### 5.1.4 Software Deployment Configuration

_Pendiente para la entrega correspondiente._

## 5.2 Product Implementation and Deployment

### 5.2.1 Sprint Backlogs

_Pendiente para la entrega correspondiente._

### 5.2.2 Implemented Landing Page Evidence

_Pendiente de incorporar evidencia._

### 5.2.3 Implemented Frontend Web Application Evidence

_Pendiente de incorporar evidencia._

### 5.2.4 Acuerdo de Servicio SaaS

_Pendiente para la entrega correspondiente._

### 5.2.5 Implemented Native Mobile Application Evidence

_Pendiente de incorporar evidencia._

### 5.2.6 Implemented RESTful API and Serverless Backend Evidence

_Pendiente de incorporar evidencia._

### 5.2.7 RESTful API Documentation

_Pendiente de incorporar evidencia._

### 5.2.8 Team Collaboration Insights

_Pendiente para la entrega correspondiente._

## 5.3 Video About the Product

_Pendiente para la entrega correspondiente._

# Part II Verification Validation and Pipeline

# Capítulo VI Product Verification and Validation

## 6.1 Testing Suites and Validation

### 6.1.1 Core Entities Unit Tests

_Pendiente para la entrega correspondiente._

### 6.1.2 Core Integration Tests

_Pendiente para la entrega correspondiente._

### 6.1.3 Core Behavior Driven Development

_Pendiente para la entrega correspondiente._

### 6.1.4 Core System Tests

_Pendiente para la entrega correspondiente._

## 6.2 Static Testing and Verification

### 6.2.1 Static Code Analysis

#### 6.2.1.1 Coding Standard and Code Conventions

_Pendiente para la entrega correspondiente._

#### 6.2.1.2 Code Quality and Code Security

_Pendiente para la entrega correspondiente._

### 6.2.2 Reviews

_Pendiente para la entrega correspondiente._

## 6.3 Validation Interviews

### 6.3.1 Diseño de Entrevistas

_Pendiente para la entrega correspondiente._

### 6.3.2 Registro de Entrevistas

_Pendiente para la entrega correspondiente._

### 6.3.3 Evaluaciones según heurísticas

_Pendiente para la entrega correspondiente._

## 6.4 Auditoría de Experiencias de Usuario

### 6.4.1 Auditoría realizada

#### 6.4.1.1 Información del grupo auditado

_Pendiente para la entrega correspondiente._

#### 6.4.1.2 Cronograma de auditoría realizada

_Pendiente para la entrega correspondiente._

#### 6.4.1.3 Contenido de auditoría realizada

_Pendiente para la entrega correspondiente._

### 6.4.2 Auditoría recibida

#### 6.4.2.1 Información del grupo auditor

_Pendiente para la entrega correspondiente._

#### 6.4.2.2 Cronograma de auditoría recibida

_Pendiente para la entrega correspondiente._

#### 6.4.2.3 Contenido de auditoría recibida

_Pendiente para la entrega correspondiente._

#### 6.4.2.4 Resumen de modificaciones para subsanar hallazgos

_Pendiente para la entrega correspondiente._

# Capítulo VII DevOps Practices

## 7.1 Continuous Integration

### 7.1.1 Tools and Practices

_Pendiente para la entrega correspondiente._

### 7.1.2 Build and Test Suite Pipeline Components

_Pendiente para la entrega correspondiente._

## 7.2 Continuous Delivery

### 7.2.1 Tools and Practices

_Pendiente para la entrega correspondiente._

### 7.2.2 Stages Deployment Pipeline Components

_Pendiente para la entrega correspondiente._

## 7.3 Continuous Deployment

### 7.3.1 Tools and Practices

_Pendiente para la entrega correspondiente._

### 7.3.2 Production Deployment Pipeline Components

_Pendiente para la entrega correspondiente._

## 7.4 Continuous Monitoring

### 7.4.1 Tools and Practices

_Pendiente para la entrega correspondiente._

### 7.4.2 Monitoring Pipeline Components

_Pendiente para la entrega correspondiente._

### 7.4.3 Alerting Pipeline Components

_Pendiente para la entrega correspondiente._

### 7.4.4 Notification Pipeline Components

_Pendiente para la entrega correspondiente._

# Part III Experiment Driven Lifecycle

# Capítulo VIII Experiment Driven Development

## 8.1 Experiment Planning

### 8.1.1 As Is Summary

_Pendiente para AV2._

### 8.1.2 Raw Material Assumptions Knowledge Gaps Ideas Claims

_Pendiente para AV2._

### 8.1.3 Experiment Ready Questions

_Pendiente para AV2._

### 8.1.4 Question Backlog

_Pendiente para AV2._

### 8.1.5 Experiment Cards

_Pendiente para AV2._

## 8.2 Experiment Design

### 8.2.1 Hypotheses

_Pendiente para AV2._

### 8.2.2 Domain Business Metrics

_Pendiente para AV2._

### 8.2.3 Measures

_Pendiente para AV2._

### 8.2.4 Conditions

_Pendiente para AV2._

### 8.2.5 Scale Calculations and Decisions

_Pendiente para AV2._

### 8.2.6 Methods Selection

_Pendiente para AV2._

### 8.2.7 Data Analytics Goals KPIs and Metrics Selection

_Pendiente para AV2._

### 8.2.8 Web and Mobile Tracking Plan

_Pendiente para AV2._

## 8.3 Experimentation

### 8.3.1 To Be User Stories

_Pendiente para AV2._

### 8.3.2 To Be Product Backlog

_Pendiente para AV2._

### 8.3.3 Pipeline Supported Experiment Driven To Be Software Platform Lifecycle

#### 8.3.3.1 To Be Sprint Backlogs

_Pendiente para AV2._

#### 8.3.3.2 Implemented To Be Landing Page Evidence

_Pendiente para AV2._

#### 8.3.3.3 Implemented To Be Frontend Web Application Evidence

_Pendiente para AV2._

#### 8.3.3.4 Implemented To Be Native Mobile Application Evidence

_Pendiente para AV2._

#### 8.3.3.5 Implemented To Be RESTful API and Serverless Backend Evidence

_Pendiente para AV2._

#### 8.3.3.6 Team Collaboration Insights

_Pendiente para AV2._

### 8.3.4 To Be Validation Interviews

#### 8.3.4.1 Diseño de Entrevistas

_Pendiente para AV2._

#### 8.3.4.2 Registro de Entrevistas

_Pendiente para AV2._

## 8.4 Experiment Aftermath and Analysis

### 8.4.1 Analysis and Interpretation of Results

_Pendiente para TB2._

### 8.4.2 Re Scored and Re Prioritized Question Backlog

_Pendiente para TB2._

## 8.5 Continuous Learning

### 8.5.1 Shareback Session Artifacts Learning Workflow

_Pendiente para TB2._

## 8.6 To Be Software Platform Pre Launch

### 8.6.1 About the Product Intro Video

_Pendiente para TB2._

### 8.6.2 Resumen usando GEES Framework

_Pendiente para TB2._

### Matriz de Evaluación Ética y de Impacto

_Pendiente para TB2._

# Conclusiones

## Conclusiones y recomendaciones

_Pendiente de elaboración grupal acumulativa._

# Video App Validation

_Pendiente de incorporar enlace._

# Video About the Team

_Pendiente de incorporar enlace y testimonio individual._

# Bibliografía

- Universidad Peruana de Ciencias Aplicadas. (2026). _Enunciado del Trabajo Final del curso Diseño de Experimentos de Ingeniería de Software, 1ASI0732_.
- Las fuentes académicas, estadísticas y técnicas empleadas en los capítulos se incorporarán conforme se desarrolle el informe.

# Anexos

## Enlaces importantes

- [Project Report](https://github.com/teralume/energycore-report)
- [Landing Page](https://github.com/teralume/energycore-website)
- [Frontend Web Application](https://github.com/teralume/energycore-webapp)
- [Native Mobile Application](https://github.com/teralume/energycore-mobile)
- [RESTful API](https://github.com/teralume/energycore-platform)

## Evidencias pendientes

- Capturas de GitHub Insights y commits de AV1.
- Evidencias visuales de la Landing Page, WebApp y aplicación móvil.
- Diagramas, entrevistas, prototipos y videos requeridos por el enunciado.
- Enlaces de despliegue y documentación de la API cuando correspondan a la entrega.
