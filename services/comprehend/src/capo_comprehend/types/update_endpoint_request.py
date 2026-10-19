"""Generated from Smithy shape ``com.amazonaws.comprehend#UpdateEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_endpoint_arn
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.comprehend_model_arn
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.inference_units_integer


class UpdateEndpointRequest(TypedDict, closed=True):
    endpoint_arn: "capo_comprehend.types.comprehend_endpoint_arn.ComprehendEndpointArn"
    """<p>The Amazon Resource Number (ARN) of the endpoint being updated.</p>"""
    desired_model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The ARN of the new model to use when updating an existing endpoint.</p>"""
    desired_inference_units: NotRequired[
        "capo_comprehend.types.inference_units_integer.InferenceUnitsInteger"
    ]
    """<p> The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.</p>"""
    desired_data_access_role_arn: NotRequired[
        "capo_comprehend.types.iam_role_arn.IamRoleArn"
    ]
    """<p>Data access role ARN to use in case the new model is encrypted with a customer CMK.</p>"""
    flywheel_arn: NotRequired[
        "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEndpointRequest) -> dict:
    out: dict = {}
    out["EndpointArn"] = value["endpoint_arn"]
    if "desired_model_arn" in value:
        out["DesiredModelArn"] = value["desired_model_arn"]
    if "desired_inference_units" in value:
        out["DesiredInferenceUnits"] = value["desired_inference_units"]
    if "desired_data_access_role_arn" in value:
        out["DesiredDataAccessRoleArn"] = value["desired_data_access_role_arn"]
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEndpointRequest:
    out: UpdateEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    else:
        out["endpoint_arn"] = ""
    if data.get("DesiredModelArn") is not None:
        out["desired_model_arn"] = data["DesiredModelArn"]
    if data.get("DesiredInferenceUnits") is not None:
        out["desired_inference_units"] = data["DesiredInferenceUnits"]
    if data.get("DesiredDataAccessRoleArn") is not None:
        out["desired_data_access_role_arn"] = data["DesiredDataAccessRoleArn"]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    return out
