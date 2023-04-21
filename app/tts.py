# Import all the modules that we will need to use
from TTS.utils.synthesizer import Synthesizer

model_path = "best_model_1105653.pth"
config_path = "config.json"

synthesizer = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
)