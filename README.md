# Tree Distribution & Urban Forestry Analytics Dashboard

This project is an interactive, spatial data visualization dashboard designed to analyze urban forestry distributions and tree health metrics. Built using Plotly Dash, the application processes regional environmental datasets to expose patterns in tree canopy density, species diversity, and geospatial concentration markers, turning raw environmental inventories into actionable ecological insights.

---

## Overview

- Platform: Plotly Dash Framework
- Analytics Engine: Python, Pandas
- Geo-Spatial Rendering: Plotly Express / Mapbox
- Deployment Target: Render.com (WSGI via Gunicorn)

---

## Features
- Dynamic geospatial mapping tracks individual tree coordinates and density clusters across target areas
- Categorical species distribution analysis using high-performance breakdown charts
- Interactive multi-parameter filtering arrays (by location, health condition, and species family)
- Seamless callback orchestration updating statistical matrices instantly upon UI filter changes
- Lightweight cloud deployment architecture configured for continuous delivery via GitHub

---

## Tech Stack
- **Dashboard Framework:** Plotly Dash, Dash Core Components (DCC), Dash HTML Components
- **Data Engineering & Visualization:** Python, Pandas, Plotly Express
- **Production Server:** Gunicorn (WSGI HTTP Server)
- **Deployment Platform:** Render.com

---

## Core Dashboard Callbacks & Views

* **`update_geospatial_map`** – Listens to drop-down selections to filter regional coordinate matrices and update map scatter plots.
* **`render_species_diversity_chart`** – Aggregates raw counts across selected data partitions to compute percentage distributions of species variance.
* **`filter_forestry_metrics`** – Computes real-time inventory summaries (such as total count and condition indexes) across active subset slices.
