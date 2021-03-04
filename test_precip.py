import argparse
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
import cmocean


def convert_pr_units(darray):
    """Convert kg m-2 s-1 to mm day-1.

    Args:
      darray (xarray.DataArray): Precipitation data

    """

    darray.data = darray.data * 86400
    darray.attrs['units'] = 'mm/day'

    return darray


def create_plot(clim, model, season, gridlines=False):
    """Plot the precipitation climatology.

    Args:
      clim (xarray.DataArray): Precipitation climatology data
      model (str) : Name of the climate model
      season (str): Season 

    Kwargs:  
      gridlines (bool): Select whether to plot gridlines    

    """

    fig = plt.figure(figsize=[12, 5])
    ax = fig.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=180))
    clim.sel(season=season).plot.contourf(ax=ax,
                                          levels=np.arange(0, 13.5, 1.5),
                                          extend='max',
                                          transform=ccrs.PlateCarree(),
                                          cbar_kwargs={'label': clim.units},
                                          cmap=cmocean.cm.haline_r)
    ax.coastlines()
    if gridlines:
        plt.gca().gridlines()

    title = f'{model} precipitation climatology ({season})'
    plt.title(title)


def main(inargs):
    """Run the program."""

    print('Input file: ', inargs.infile)
    print('Output file: ', inargs.outfile)


if __name__ == '__main__':
    description = 'Print the input arguments to the screen.'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("infile", type=str, help="Input file name")
    parser.add_argument("outfile", type=str, help="Output file name")

    args = parser.parse_args()
    main(args)