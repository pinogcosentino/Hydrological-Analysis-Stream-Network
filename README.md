# Hydrological-Analysis-Stream-Network
Algorithm for hydrological analysis that generates the drainage network from a digital terrain model (DTM)
Feautures: 
- Vector stream network (raw and smoothed)
- Drainage directions
- Topographic index ln(a/tan(b))
- Half basins

  Main steps:
- Fill sinks (Wang & Liu algorithm)
- Flow calculation and stream delineation
- Raster to vector conversion
- Geometry smoothing

Requirements
Processing SAGA provider enabled.
