from omni.isaac.lab.app import AppLauncher
import omni.isaac.core.utils.stage as stage_utils
import omni.kit.app

# Headless starten
app_launcher = AppLauncher(headless=True)
simulation_app = app_launcher.app

# Lade deine Szene
stage_utils.open_stage("/workspace/isaaclab/tools/usd/converted/TEEsavR23oF/world_TEEsavR23oF_with_robot.usd")

# Wenn du einen Loop brauchst
app = omni.kit.app.get_app_interface()
while app.is_running():
    app.update()

simulation_app.close()
