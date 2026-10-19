"""Generated from Smithy shape ``com.amazonaws.pipes#SageMakerPipelineParameter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.sage_maker_pipeline_parameter_name
    import capo_pipes.types.sage_maker_pipeline_parameter_value


class SageMakerPipelineParameter(TypedDict, closed=True):
    name: "capo_pipes.types.sage_maker_pipeline_parameter_name.SageMakerPipelineParameterName"
    """<p>Name of parameter to start execution of a SageMaker Model Building Pipeline.</p>"""
    value: "capo_pipes.types.sage_maker_pipeline_parameter_value.SageMakerPipelineParameterValue"
    """<p>Value of parameter to start execution of a SageMaker Model Building Pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerPipelineParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SageMakerPipelineParameter:
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


def redact_sensitive(value: SageMakerPipelineParameter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
