"""Generated from Smithy shape ``com.amazonaws.neptunedata#CustomModelTrainingParameters``."""

from typing_extensions import NotRequired, TypedDict


class CustomModelTrainingParameters(TypedDict, closed=True):
    source_s3_directory_path: "str"
    """<p>The path to the Amazon S3 location where the Python module implementing your model is located. This must point to a valid existing Amazon S3 location that contains, at a minimum, a training script, a transform script, and a <code>model-hpo-configuration.json</code> file.</p>"""
    training_entry_point_script: NotRequired["str"]
    """<p>The name of the entry point in your module of a script that performs model training and takes hyperparameters as command-line arguments, including fixed hyperparameters. The default is <code>training.py</code>.</p>"""
    transform_entry_point_script: NotRequired["str"]
    """<p>The name of the entry point in your module of a script that should be run after the best model from the hyperparameter search has been identified, to compute the model artifacts necessary for model deployment. It should be able to run with no command-line arguments.The default is <code>transform.py</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelTrainingParameters) -> dict:
    out: dict = {}
    out["sourceS3DirectoryPath"] = value["source_s3_directory_path"]
    if "training_entry_point_script" in value:
        out["trainingEntryPointScript"] = value["training_entry_point_script"]
    if "transform_entry_point_script" in value:
        out["transformEntryPointScript"] = value["transform_entry_point_script"]
    return out


def deserialize_json(data: dict) -> CustomModelTrainingParameters:
    out: CustomModelTrainingParameters = {}  # type: ignore[typeddict-item]
    if data.get("sourceS3DirectoryPath") is not None:
        out["source_s3_directory_path"] = data["sourceS3DirectoryPath"]
    else:
        out["source_s3_directory_path"] = ""
    if data.get("trainingEntryPointScript") is not None:
        out["training_entry_point_script"] = data["trainingEntryPointScript"]
    if data.get("transformEntryPointScript") is not None:
        out["transform_entry_point_script"] = data["transformEntryPointScript"]
    return out
