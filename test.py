# import tensorflow as tf

# print(f"TensorFlow Version: {tf.__version__}")
# print("Available GPUs:", tf.config.list_physical_devices('GPU'))


import tensorflow as tf

# Check TensorFlow version
print(f"TensorFlow Version: {tf.__version__}")

# List physical devices
print("Physical Devices:", tf.config.list_physical_devices())

# Enable GPU growth (optional)
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        print("GPU memory growth set")
    except RuntimeError as e:
        print(e)
else:
    print("No GPU detected")
