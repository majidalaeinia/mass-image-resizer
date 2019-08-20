# Mass Image Resizer


## What is this?
This repository can resize all your images with a specific extension to a certain size.

## How to use this code?
Suppose you have a folder with a bunch of `.png` images in it and this folder is called `your_images_folder`. Just `cd` (change directory) to that folder, then, run this command:

### 1. Installing the Pillow
```
pip install Pillow==6.1.0
```

### 2. Running the command
Copy [mass_image_resizer.py](https://github.com/MajidAlaeinia/mass-image-resizer/blob/master/mass_image_resizer.py) to `your_images_folder` and run this command:

```
python mass_image_resizer.py <image_extension_without_dot> <your_desired_width_in_pixels> <your_desired_height_in_pixels>
```

##### Example

Let's suppose your images are in the `png` format, and you want your `width` to be **600** and the `height` to be **800**. You can run this command to resize all the images in that folder to your desired size.

```
python mass_image_resizer.py png 800 600
```

That's it.