"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineVariable``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_variable_name
    import capo_codepipeline.types.pipeline_variable_value


class PipelineVariable(TypedDict, closed=True):
    name: "capo_codepipeline.types.pipeline_variable_name.PipelineVariableName"
    """<p>The name of a pipeline-level variable.</p>"""
    value: "capo_codepipeline.types.pipeline_variable_value.PipelineVariableValue"
    """<p>The value of a pipeline-level variable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineVariable) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineVariable:
    out: PipelineVariable = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
