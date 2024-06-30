# Cartography with Enhanced Statistics

This repository is a modified version of the [Lyft Cartography](https://github.com/lyft/cartography) tool. Cartography is a tool that consolidates infrastructure assets and the relationships between them in an intuitive graph database. This modified version includes additional functionality to collect and export statistics related to the scans performed by Cartography.

## Table of Contents

- [Background](#background)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Statistics Collected](#statistics-collected)
- [Configuration](#configuration)


## Background

Lyft's Cartography is designed to pull information from various infrastructure sources (like AWS, GCP, etc.), consolidate it into a graph database (Neo4j), and provide insights into the security posture of your infrastructure. This modified version builds upon the original by introducing the capability to collect and export detailed statistics regarding the resources scanned during each run.

## Features

- **Collection of Scan Statistics**: Automatically collects statistics such as total resources scanned, time taken for each scan, and regions skipped.
- **Export to JSON**: Exports the collected statistics to a JSON file for further analysis and record-keeping.
- **Singleton Pattern for Statistics Management**: Ensures that the statistics are collected and managed in a centralized manner using a singleton class.

## Installation

- Start [here](https://lyft.github.io/cartography/install.html)

## Usage

1. Configure Cartography as per the original [Cartography documentation](https://github.com/lyft/cartography#installation).

2. Run Cartography with your desired configurations:
    ```bash
    cd cartography
    python3 __main__.py \
    --neo4j-uri bolt://localhost:7687 \
    --neo4j-user "username" \
    --neo4j-password-env-var NEO4J_PASS \
    --neo4j-database neo4j \
    --selected-modules aws \
    --aws-requested-syncs "add desired syncs here" \
    ```

3. After the run, find the statistics summary in the `stats_summary.json` file in the current directory:
    ```bash
    cartography/statistics_file.json
    ```
   For more distributed results, check the directory:
   ```bash
   cartography/intel/aws/recordedStats
   ```

## Statistics Collected

The following statistics are collected during each scan:

- **Resources Scanned**: This parameter can vary for each service, information regarding data relevant to each scan can be found here.
- **Time Taken**: The time taken to scan each service.
- **Skipped Regions**: The regions that were skipped during the scan.
- **Error Messages**: Any errors encountered during the scan.
- **Status**: Whether or not the scan was successfully completed.

## Configuration

The statistics collection is automatically integrated into the Cartography run. No additional configuration is needed beyond the standard Cartography configuration.

## Implementation Details

Learn [here](collecting_carto_scan_statistics.pdf)