# Hydrological-Analysis-Stream-Network
Algorithm for hydrological analysis that generates the drainage network from a digital terrain model (DTM)
# Feautures: 
- Vector stream network (raw and smoothed)
- Drainage directions
- Topographic index ln(a/tan(b))
- Half basins

# Main steps:
1) Fill sinks (Wang & Liu algorithm)
2) Flow calculation and stream delineation
3) Raster to vector conversion
4) Geometry smoothing

# Requirements
- Processing SAGA NextGen provider enabled
- GDAL/Processing are included with QGIS.
- Grass/Processing are included with QGIS.

# Installation
Before installing the "Hydrological Analysis Streams Network" plugin, you must first install the "Processing Saga NextGen Provider".
To do this in QGIS:
1. Go to QGIS -> Plugins → Manage and Install Plugins…
2. Search for "Processing Saga NextGen Provider" and select Install Plugin.
3. Once the installation is complete, repeat the same steps to search for and install the "Hydrological Analysis Streams Network" plugin.
