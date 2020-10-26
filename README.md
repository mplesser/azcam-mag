# azcam-mag

*azcam-mag* is an *azcam* extension for OCIW Magellan CCD controllers (ITL version). See http://instrumentation.obs.carnegiescience.edu/ccd/gcam.html.

## Installation

Download from github: https://github.com/mplesser/azcam-mag.git.

## Example Code

The code below is for example only.

### Controller
    controller = ControllerMag()
    controller.camserver.set_server(guider_address, guider_port)
    controller.timing_file = os.path.join(azcam.db.datafolder, "dspcode/gcam_ccd57.s")

### Exposure
    exposure = ExposureMag()
    filetype = "BIN"
    exposure.filetype = azcam.db.filetypes[filetype]
    exposure.image.filetype = azcam.db.filetypes[filetype]
    exposure.display_image = 1
    exposure.image.remote_imageserver_flag = 0
    exposure.filename.set_name("/azcam/soguider/image.bin")
    exposure.filename.test_image = 0
    exposure.filename.root = "image"
    exposure.display_image = 0
    exposure.image.make_lockfile = 1
