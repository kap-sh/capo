"""Generated from Smithy shape ``com.amazonaws.datapipeline#GetPipelineDefinitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.string


class GetPipelineDefinitionInput(TypedDict, closed=True):
    pipeline_id: "capo_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    version: NotRequired["capo_data_pipeline.types.string.string"]
    """<p>The version of the pipeline definition to retrieve. Set this parameter to <code>latest</code> (default) to use the last definition saved to the pipeline or <code>active</code> to use the last definition that was activated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPipelineDefinitionInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPipelineDefinitionInput:
    out: GetPipelineDefinitionInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineId") is not None:
        out["pipeline_id"] = data["pipelineId"]
    else:
        out["pipeline_id"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
