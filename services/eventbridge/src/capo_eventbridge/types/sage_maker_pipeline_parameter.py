"""Generated from Smithy shape ``com.amazonaws.eventbridge#SageMakerPipelineParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.sage_maker_pipeline_parameter_name
    import capo_eventbridge.types.sage_maker_pipeline_parameter_value


class SageMakerPipelineParameter(TypedDict, closed=True):
    name: "capo_eventbridge.types.sage_maker_pipeline_parameter_name.SageMakerPipelineParameterName"
    """<p>Name of parameter to start execution of a SageMaker AI Model Building Pipeline.</p>"""
    value: "capo_eventbridge.types.sage_maker_pipeline_parameter_value.SageMakerPipelineParameterValue"
    """<p>Value of parameter to start execution of a SageMaker AI Model Building Pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SageMakerPipelineParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SageMakerPipelineParameter:
    out: SageMakerPipelineParameter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
