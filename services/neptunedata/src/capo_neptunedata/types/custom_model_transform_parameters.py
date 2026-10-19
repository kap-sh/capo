"""Generated from Smithy shape ``com.amazonaws.neptunedata#CustomModelTransformParameters``."""

from typing_extensions import NotRequired, TypedDict


class CustomModelTransformParameters(TypedDict, closed=True):
    source_s3_directory_path: "str"
    """<p>The path to the Amazon S3 location where the Python module implementing your model is located. This must point to a valid existing Amazon S3 location that contains, at a minimum, a training script, a transform script, and a <code>model-hpo-configuration.json</code> file.</p>"""
    transform_entry_point_script: NotRequired["str"]
    """<p>The name of the entry point in your module of a script that should be run after the best model from the hyperparameter search has been identified, to compute the model artifacts necessary for model deployment. It should be able to run with no command-line arguments. The default is <code>transform.py</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelTransformParameters) -> dict:
    out: dict = {}
    out["sourceS3DirectoryPath"] = value["source_s3_directory_path"]
    if "transform_entry_point_script" in value:
        out["transformEntryPointScript"] = value["transform_entry_point_script"]
    return out


def deserialize_json(data: dict) -> CustomModelTransformParameters:
    out: CustomModelTransformParameters = {}  # type: ignore[typeddict-item]
    if data.get("sourceS3DirectoryPath") is not None:
        out["source_s3_directory_path"] = data["sourceS3DirectoryPath"]
    else:
        out["source_s3_directory_path"] = ""
    if data.get("transformEntryPointScript") is not None:
        out["transform_entry_point_script"] = data["transformEntryPointScript"]
    return out
