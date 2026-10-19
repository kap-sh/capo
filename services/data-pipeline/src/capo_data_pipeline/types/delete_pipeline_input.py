"""Generated from Smithy shape ``com.amazonaws.datapipeline#DeletePipelineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.id


class DeletePipelineInput(TypedDict, closed=True):
    pipeline_id: "capo_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePipelineInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePipelineInput:
    out: DeletePipelineInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineId") is not None:
        out["pipeline_id"] = data["pipelineId"]
    else:
        out["pipeline_id"] = ""
    return out
