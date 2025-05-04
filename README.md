# 3D Model Generator

This project provides a simple framework for generating 3D models from either text prompts or images. It includes utilities for creating basic 3D models and rendering them using Python libraries.

## Features

- **Text-to-3D**: Generates a basic cube-shaped 3D model in OBJ format based on a text prompt.
- **Image-to-3D**: Converts an image into a height-map-based 3D model in STL format.
- **Rendering**: Renders the generated 3D models using `pyrender` and displays them.

## Project Structure

```
3dmodel/
├── main.py                  # Entry point for the application
├── utils/
│   ├── text_to_3d.py        # Utility for generating 3D models from text
│   ├── image_to_3d.py       # Utility for generating 3D models from images
├── requirements.txt         # List of dependencies
```

## Requirements

The project requires Python 3.8 or higher. Install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

Run the application using:

```bash
python main.py
```

### Modes

1. **Image Mode**:
   - Enter `image` when prompted.
   - Provide the path to an image file (e.g., `assets/toy.jpg`).
   - The program will generate a 3D model in STL format and save it to `outputs/model.stl`.

2. **Text Mode**:
   - Enter `text` when prompted.
   - Provide a text prompt.
   - The program will generate a basic cube-shaped 3D model in OBJ format and save it to `outputs/model.obj`.

## File Descriptions

### `main.py`

The main script that handles user input and coordinates the 3D model generation and rendering process.

### `utils/text_to_3d.py`

Contains the `generate_from_text` function, which creates a basic cube-shaped 3D model in OBJ format based on a text prompt.

### `utils/image_to_3d.py`

Contains the `process_image` function, which:
- Removes the background from an image.
- Converts the image into a grayscale height map.
- Generates a 3D mesh using the height map.

### `requirements.txt`

Lists the Python libraries required for the project:
- `torch`, `transformers`, `diffusers`: For potential AI-based extensions.
- `pillow`: For image processing.
- `numpy`: For numerical computations.
- `pyrender`, `trimesh`: For 3D model creation and rendering.
- `opencv-python`, `rembg`: For image manipulation.

## Output

- **Text Mode**: Generates a file `outputs/model.obj` containing a cube-shaped 3D model.
- **Image Mode**: Generates a file `outputs/model.stl` containing a height-map-based 3D model.

## Example

### Text Mode
Input:
```
Enter input type (image/text): text
Enter text prompt: A simple cube
```
Output:
```
[✓] Dummy 3D model saved to outputs/model.obj
```

### Image Mode
Input:
```
Enter input type (image/text): image
Enter image path (e.g., assets/toy.jpg): assets/toy.jpg
```
Output:
```
3D model saved to outputs/model.stl
```

## Future Enhancements

- Add support for more complex 3D model generation using AI-based techniques.
- Improve the rendering pipeline for better visualization.
- Extend text-to-3D functionality to generate models based on semantic understanding of the text.
