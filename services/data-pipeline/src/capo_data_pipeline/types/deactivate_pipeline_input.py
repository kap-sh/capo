"""Generated from Smithy shape ``com.amazonaws.datapipeline#DeactivatePipelineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.cancel_active
    import capo_data_pipeline.types.id


class DeactivatePipelineInput(TypedDict, closed=True):
    pipeline_id: "capo_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    cancel_active: NotRequired["capo_data_pipeline.types.cancel_active.cancelActive"]
    """<p>Indicates whether to cancel any running objects. The default is true, which sets the state of any running objects to <code>CANCELED</code>. If this value is false, the pipeline is deactivated after all running objects finish.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeactivatePipelineInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    if "cancel_active" in value:
        out["cancelActive"] = value["cancel_active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeactivatePipelineInput:
    out: DeactivatePipelineInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineId") is not None:
        out["pipeline_id"] = data["pipelineId"]
    else:
        out["pipeline_id"] = ""
    if data.get("cancelActive") is not None:
        out["cancel_active"] = data["cancelActive"]
    return out
