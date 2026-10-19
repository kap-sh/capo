"""Generated from Smithy shape ``com.amazonaws.ssm#GetExecutionPreviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.execution_preview_id


class GetExecutionPreviewRequest(TypedDict, closed=True):
    execution_preview_id: "capo_ssm.types.execution_preview_id.ExecutionPreviewId"
    """<p>The ID of the existing execution preview.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExecutionPreviewRequest) -> dict:
    out: dict = {}
    out["ExecutionPreviewId"] = value["execution_preview_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExecutionPreviewRequest:
    out: GetExecutionPreviewRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExecutionPreviewId") is not None:
        out["execution_preview_id"] = data["ExecutionPreviewId"]
    else:
        out["execution_preview_id"] = ""
    return out
