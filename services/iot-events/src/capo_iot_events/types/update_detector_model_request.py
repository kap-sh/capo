"""Generated from Smithy shape ``com.amazonaws.iotevents#UpdateDetectorModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events.types.amazon_resource_name
    import capo_iot_events.types.detector_model_definition
    import capo_iot_events.types.detector_model_description
    import capo_iot_events.types.detector_model_name
    import capo_iot_events.types.evaluation_method


class UpdateDetectorModelRequest(TypedDict, closed=True):
    detector_model_name: "capo_iot_events.types.detector_model_name.DetectorModelName"
    """<p>The name of the detector model that is updated.</p>"""
    detector_model_definition: (
        "capo_iot_events.types.detector_model_definition.DetectorModelDefinition"
    )
    """<p>Information that defines how a detector operates.</p>"""
    detector_model_description: NotRequired[
        "capo_iot_events.types.detector_model_description.DetectorModelDescription"
    ]
    """<p>A brief description of the detector model.</p>"""
    role_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</p>"""
    evaluation_method: NotRequired[
        "capo_iot_events.types.evaluation_method.EvaluationMethod"
    ]
    """<p>Information about the order in which events are evaluated and how actions are executed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDetectorModelRequest) -> dict:
    out: dict = {}
    import capo_iot_events.types.detector_model_definition

    out["detectorModelDefinition"] = (
        capo_iot_events.types.detector_model_definition.serialize_json(
            value["detector_model_definition"]
        )
    )
    if "detector_model_description" in value:
        out["detectorModelDescription"] = value["detector_model_description"]
    out["roleArn"] = value["role_arn"]
    if "evaluation_method" in value:
        import capo_iot_events.types.evaluation_method

        out["evaluationMethod"] = (
            capo_iot_events.types.evaluation_method.serialize_json(
                value["evaluation_method"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDetectorModelRequest:
    out: UpdateDetectorModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("detectorModelDefinition") is not None:
        import capo_iot_events.types.detector_model_definition

        out["detector_model_definition"] = (
            capo_iot_events.types.detector_model_definition.deserialize_json(
                data["detectorModelDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDetectorModelRequest.detector_model_definition required"
        )
    if data.get("detectorModelDescription") is not None:
        out["detector_model_description"] = data["detectorModelDescription"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("evaluationMethod") is not None:
        import capo_iot_events.types.evaluation_method

        out["evaluation_method"] = (
            capo_iot_events.types.evaluation_method.deserialize_json(
                data["evaluationMethod"]
            )
        )
    return out
