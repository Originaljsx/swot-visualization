# SWOT Data Visualization

Jupyter notebooks for visualizing SWOT (Surface Water and Ocean Topography) satellite data.

## Notebooks

### L4 Product (Gridded)
- **visualize_june1_2024_final.ipynb** - Visualizes SWOT L4 gridded data at 0.125° resolution with MIOST interpolation

### L3 Product (Swath)
- **swot_l3_complete_global_mosaic.ipynb** - Basic L3 swath visualization
- **visualize_swot_l3_global_mosaic.ipynb** - Complete L3 global mosaic merging 567 swaths at 2 km resolution

## Requirements

```
xarray
numpy
matplotlib
cartopy
```

## Data

Download SWOT data from:
- L3: https://podaac.jpl.nasa.gov/dataset/SWOT_L3_LR_SSH
- L4: https://podaac.jpl.nasa.gov/dataset/SWOT_L4_LR_SSH

Place data files in:
- `swot_l3_cycle016/` for L3 swaths
- `swot_l4_data/` for L4 gridded products

## Usage

```bash
jupyter notebook visualize_june1_2024_final.ipynb
```

or

```bash
jupyter notebook visualize_swot_l3_global_mosaic.ipynb
```
