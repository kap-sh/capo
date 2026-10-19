"""Generated from Smithy shape ``com.amazonaws.rekognition#StartProjectVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.inference_units
    import capo_rekognition.types.project_version_arn


class StartProjectVersionRequest(TypedDict, closed=True):
    project_version_arn: "capo_rekognition.types.project_version_arn.ProjectVersionArn"
    """<p>The Amazon Resource Name(ARN) of the model version that you want to start.</p>"""
    min_inference_units: "capo_rekognition.types.inference_units.InferenceUnits"
    """<p>The minimum number of inference units to use. A single inference unit represents 1 hour of processing. </p> <p>Use a higher number to increase the TPS throughput of your model. You are charged for the number of inference units that you use. </p>"""
    max_inference_units: NotRequired[
        "capo_rekognition.types.inference_units.InferenceUnits"
    ]
    """<p>The maximum number of inference units to use for auto-scaling the model. If you don't specify a value, Amazon Rekognition Custom Labels doesn't auto-scale the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartProjectVersionRequest) -> dict:
    out: dict = {}
    out["ProjectVersionArn"] = value["project_version_arn"]
    out["MinInferenceUnits"] = value["min_inference_units"]
    if "max_inference_units" in value:
        out["MaxInferenceUnits"] = value["max_inference_units"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartProjectVersionRequest:
    out: StartProjectVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProjectVersionArn") is not None:
        out["project_version_arn"] = data["ProjectVersionArn"]
    else:
        out["project_version_arn"] = ""
    if data.get("MinInferenceUnits") is not None:
        out["min_inference_units"] = data["MinInferenceUnits"]
    else:
        out["min_inference_units"] = 0
    if data.get("MaxInferenceUnits") is not None:
        out["max_inference_units"] = data["MaxInferenceUnits"]
    return out
