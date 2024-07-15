# Gps Toll based system simulation using Python

This project simulates a GPS toll-based system using Python, designed for data analytics and visualization. It models vehicle movements along predefined routes with GPS coordinates, defines toll zones, calculates distances, computes toll charges, and simulates payment processes. The project  leverages various Python libraries for simulation, geospatial analysis, distance calculation, data handling, and visualization.

## Component of simulation:

1. **Vehicle Movement Simulation**: Simulates vehicles moving along predefined routes using GPS coordinates.
2. **Toll Zone Definition**: Defines toll zones or points with GPS coordinates.
3. **Distance Calculation**: Calculates the distance traveled by each vehicle within toll zones.
4. **Toll Calculation**: Computes toll charges based on distance traveled or zones passed.
5. **Payment Simulation**: Simulates the process of deducting toll charges from user accounts.

## Python Libraries and Framework:
- **Simulation Frameworks**: 
  - [SimPy](https://simpy.readthedocs.io/) for event-driven simulation to model vehicle movements and interactions within the system.
- **Geospatial Analysis**: 
  - [GeoPandas](https://geopandas.org/) and [Shapely](https://shapely.readthedocs.io/) for defining toll zones and calculating intersections between vehicle paths and these zones.
- **Distance Calculation**: 
  - [GeoPy](https://geopy.readthedocs.io/) for distance calculations between GPS coordinates.
- **Data Handling**: 
  - [pandas](https://pandas.pydata.org/) for managing and analyzing data related to vehicles, toll transactions, and user accounts.
- **Visualization**: 
  - [Matplotlib](https://matplotlib.org/) and [Folium](https://python-visualization.github.io/folium/) for visualizing the simulation, including vehicle movements and toll zone locations on maps.
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/tanupriya21/GPS-Toll-Based-System
    ```
2. Navigate to the project directory:
    ```bash
    cd repository
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
```
    
## Usage
1. Run the simulation:
    ```bash
    python simulate.py
    ```



## Contributing
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.


## Contact
For any questions or feedback, please contact the project maintainers at [om.lakshkar_cs.h23@gla.ac.in].
