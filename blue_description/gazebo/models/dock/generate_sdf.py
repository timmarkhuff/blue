MATERIAL = '''
        <material>
            <ambient>0.54 0.27 0.07 1</ambient> <!-- Brown color -->
            <diffuse>0.54 0.27 0.07 1</diffuse> <!-- Brown color -->
            <specular>1 1 1 1</specular>
        </material>
'''

SPACE_BETWEEN_PILINGS = 1.5
DOCK_HEIGHT = 0.1
DOCK_WIDTH = 2
DOCK_LENGTH = 10
PILING_OFFSET = 0.25
PILING_RADIUS = 0.1
PILING_HEIGHT = 4

DOCK_X = 0
DOCK_Y = 5
DOCK_Z = 0.25

def create_box(name, size, pose):
    return f'''
    <link name="{name}">
      <pose>{pose}</pose>
      <collision name="{name}_collision">
        <geometry>
          <box><size>{size}</size></box>
        </geometry>
      </collision>
      <visual name="{name}_visual">
        <geometry>
          <box><size>{size}</size></box>
        </geometry>
        {MATERIAL}
      </visual>
    </link>
    '''

def create_cylinder(name, radius, length, pose):
    return f'''
    <link name="{name}">
      <pose>{pose}</pose>
      <collision name="{name}_collision">
        <geometry>
          <cylinder><radius>{radius}</radius><length>{length}</length></cylinder>
        </geometry>
      </collision>
      <visual name="{name}_visual">
        <geometry>
          <cylinder><radius>{radius}</radius><length>{length}</length></cylinder>
        </geometry>
        {MATERIAL}
      </visual>
    </link>
    '''

# create the dock platform
dock_platform = create_box("dock_platform", 
                           f"{DOCK_WIDTH} {DOCK_LENGTH} {DOCK_HEIGHT}", 
                           f"{DOCK_X} {DOCK_Y} {DOCK_Z} 0 0 0")

# Create the dock pilings
PILING_SPAN = DOCK_LENGTH - 2 * PILING_OFFSET # the length of the dock that can contain pilings
NUM_PILINGS = int(PILING_SPAN / SPACE_BETWEEN_PILINGS)
SPACE_BETWEEN_PILINGS_ADJUSTED = PILING_SPAN / NUM_PILINGS 

x1 = DOCK_WIDTH / 2 - PILING_OFFSET
x2 = - DOCK_WIDTH / 2 + PILING_OFFSET
y = DOCK_Y - DOCK_LENGTH/2 + PILING_OFFSET
z = - PILING_HEIGHT / 2 + DOCK_Z

cylinders = ''
piling_num = 0
for _ in range(NUM_PILINGS):
    poses = (
        f'{x1} {y} {z} 0 0 0',
        f'{x2} {y} {z} 0 0 0',
             )
    for pose in poses:
        cylinders += create_cylinder(f"cylinder{piling_num}", f"{PILING_RADIUS}", f"{PILING_HEIGHT}", pose) + '\n'
        piling_num += 1

    y += SPACE_BETWEEN_PILINGS_ADJUSTED

sdf_model_content = f'''<?xml version="1.0" ?>
<sdf version="1.6">
  <model name="custom_model">
    <static>true</static>
    {dock_platform}
    {cylinders}
    <!-- Add more links (boxes/cylinders) here -->
  </model>
</sdf>'''

print(sdf_model_content)

with open("model.sdf", "w") as file:
    file.write(sdf_model_content)
