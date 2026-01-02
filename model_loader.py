import numpy as np
import tflite_runtime.interpreter as tflite


class TFLiteModel:
    def __init__(self, model_path):
        # Load TFLite model
        self.interpreter = tflite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()

        # Get input & output details
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def predict(self, img):
        """
        Run inference on a single image
        """
        # Add batch dimension and ensure float32
        img = np.expand_dims(img, axis=0).astype(np.float32)

        # Set input tensor
        self.interpreter.set_tensor(
            self.input_details[0]["index"], img
        )

        # Run inference
        self.interpreter.invoke()

        # Get output
        output = self.interpreter.get_tensor(
            self.output_details[0]["index"]
        )

        return output[0][0]
