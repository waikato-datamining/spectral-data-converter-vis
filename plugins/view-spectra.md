# view-spectra

* accepts: sdc.api.Spectrum2D

Displays the spectra in a plot.

```
usage: view-spectra [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                    [-N LOGGER_NAME] [--skip] [-t TITLE] [--legend]
                    [--legend_loc {best,upper right,upper left,lower left,lower right,right,center left,center right,lower center,upper center,center}]

Displays the spectra in a plot.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --skip                Disables the plugin, removing it from the pipeline.
                        (default: False)
  -t TITLE, --title TITLE
                        The title for the plot. (default: None)
  --legend              Whether to display the legend. (default: False)
  --legend_loc {best,upper right,upper left,lower left,lower right,right,center left,center right,lower center,upper center,center}
                        The location for the legend. (default: best)
```
