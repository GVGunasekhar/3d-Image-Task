from rembg import remove
from PIL import Image
import numpy as np
import trimesh

def process_image(image_path):
    input_img = Image.open(image_path)
    output_img = remove(input_img)  # Removes background
    output_img = output_img.convert("L").resize((64, 64))
    height_map = np.asarray(output_img) / 255.0
    vertices = []
    faces = []

    for i in range(63):
        for j in range(63):
            z1 = height_map[i][j]
            z2 = height_map[i+1][j]
            z3 = height_map[i][j+1]
            z4 = height_map[i+1][j+1]
            v1 = [i, j, z1]
            v2 = [i+1, j, z2]
            v3 = [i, j+1, z3]
            v4 = [i+1, j+1, z4]

            idx = len(vertices)
            vertices.extend([v1, v2, v3, v4])
            faces.extend([[idx, idx+1, idx+2], [idx+1, idx+3, idx+2]])

    mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
    return mesh
