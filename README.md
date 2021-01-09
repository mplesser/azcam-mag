# azcam-mag

*azcam-mag* is an *azcam* extension for OCIW Magellan CCD controllers (ITL version). See http://instrumentation.obs.carnegiescience.edu/ccd/gcam.html.

## Installation

`pip install azcam-mag`

Or download from github: https://github.com/mplesser/azcam-mag.git.

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
    exposure.set_name("/azcam/soguider/image.bin")
    exposure.test_image = 0
    exposure.root = "image"
    exposure.display_image = 0
    exposure.image.make_lockfile = 1

## Camera Server
*Camera servers* are separate executable programs which manage direct interaction with 
controller hardware on some systems. Communication with a CameraServer takes place over sockets via 
communication protocols defined between *azcam* and a specific CameraServer program. These 
CameraServers are necessary when specialized drivers for the camera hardware are required.  They are 
usually written in C/C++. 

## DSP Code
The DSP code which runs in the ARC and Magellan controllers is assembled and linked with
Motorola software tools. These tools should be installed in *../MotorolaDSPtools/* on a
Windows machine, as required by the batch files which assemble and link the DSP source code.

For the Magellan systems, there is only one DSP file which must be downloaded during 
initialization. Note that *xxx.s* files are loaded for the Magellan systems.
