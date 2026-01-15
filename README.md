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
- Processing SAGA provider enabled
