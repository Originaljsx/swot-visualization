# SWOT Data Visualization

Jupyter notebooks for visualizing SWOT (Surface Water and Ocean Topography) satellite data.

## Notebooks

### L4 Product (Gridded)
- **visualize_june1_2024_final.ipynb** - Visualizes SWOT L4 gridded data https://doi.org/10.24400/527896/a01-2025.001

### L3 Product (Swath)
- **swot_l3_complete_global_mosaic.ipynb** - Visualizes all passes from one cycle https://doi.org/10.24400/527896/A01-2023.017


## Requirements

```
xarray
numpy
matplotlib
cartopy
```

## Data

Download SWOT data from AVISO:
- L3: https://doi.org/10.24400/527896/a01-2025.001
- L4: https://doi.org/10.24400/527896/A01-2023.017

Place data files in:
- `swot_l3_cycle016/` for L3 swaths (cycle 16 here)
- `swot_l4_data/` for L4 gridded products
