# entityraster

Raster-valued attributes for GeoPandas: one raster per row, handled like any other column. A table with such a column is called a **GeoRasterFrame**.

```python
import entityraster as er

gdf = er.embed(people, "rasters/", on="uid", pattern="p{uid:05d}.tif",
               column="activity_space", index="uid")

gdf.loc[200, "activity_space"].mean()                                  # one person's raster
old = gdf[gdf["age"] > 60]                                             # rasters follow the filter
old.rst.surface("activity_space", by="gender", outside="unknown")      # a mean surface per group
```

## What it does

- **Attach rasters by key** (`embed`): catalogue, file-name pattern, folder or path column. Unmatched rows and unused files are reported.
- **Lazy:** the table holds references and metadata; pixels are read only for the rows an operation needs.
- **Different extents:** rasters are aligned with strict, explained rules; reprojection, resampling and snapping are opt-in.
- **Zero or unknown?** Operations across entities require you to state what a cell outside a raster means.
- **Weighted analysis and land use:** exposure weighted by each entity's raster, and class shares per entity and per polygon.
- **Plain pandas:** filter, groupby, merge and GeoParquet keep working; surfaces export as GeoTIFF.

## Install

```bash
pip install entityraster
```

Python 3.11 or newer. BSD 3-Clause licence.

```{note}
Status: pre-release (0.1). The full user guide, examples and API reference will be published with the first public release.
```

```{toctree}
:hidden:

```
