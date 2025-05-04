import os

def generate_from_text(prompt, output_path='outputs/model.obj'):
    """
    Generates a basic cube-shaped OBJ file as a placeholder for text-to-3D.
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    cube_obj = f"""# OBJ file generated from prompt: {prompt}
o Cube
v 0 0 0
v 1 0 0
v 1 1 0
v 0 1 0
v 0 0 1
v 1 0 1
v 1 1 1
v 0 1 1
f 1 2 3 4
f 5 6 7 8
f 1 2 6 5
f 2 3 7 6
f 3 4 8 7
f 4 1 5 8
"""

    with open(output_path, 'w') as f:
        f.write(cube_obj)
    
    print(f"[✓] Dummy 3D model saved to {output_path}")
