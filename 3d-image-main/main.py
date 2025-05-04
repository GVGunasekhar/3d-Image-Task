import sys
from utils.image_to_3d import process_image
from utils.text_to_3d import generate_from_text
import trimesh
import pyrender
import matplotlib.pyplot as plt
import numpy as np


def render_model(mesh):
    scene = pyrender.Scene()

    # Convert Trimesh to Pyrender Mesh
    render_mesh = pyrender.Mesh.from_trimesh(mesh)
    scene.add(render_mesh)

    # ✅ Add camera
    camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0)
    camera_pose = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, -0.2],
        [0.0, 0.0, 1.0, 1.0],
        [0.0, 0.0, 0.0, 1.0],
    ])
    scene.add(camera, pose=camera_pose)

    # ✅ Add light
    light = pyrender.DirectionalLight(color=np.ones(3), intensity=2.0)
    scene.add(light, pose=camera_pose)

    # Render
    viewer = pyrender.OffscreenRenderer(512, 512)
    color, _ = viewer.render(scene)
    viewer.delete()
    
    # Show
    plt.imshow(color)
    plt.axis('off')
    plt.show()


def main():
    mode = input("Enter input type (image/text): ").strip().lower()
    
    if mode == "image":
        path = input("Enter image path (e.g., assets/toy.jpg): ").strip()
        mesh = process_image(path)
        mesh.export('outputs/model.stl')
        render_model(mesh)
        print("3D model saved to outputs/model.stl")

    elif mode == "text":
        prompt = input("Enter text prompt: ").strip()
        generate_from_text(prompt, output_path='outputs/model.obj')
        print("3D model saved to outputs/model.obj")

    else:
        print("Invalid input type. Use 'image' or 'text'.")

if __name__ == "__main__":
    main()
