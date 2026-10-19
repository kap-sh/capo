"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#GetExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.arn
    import capo_bcm_data_exports.types.generic_string


class GetExecutionRequest(TypedDict, closed=True):
    export_arn: "capo_bcm_data_exports.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Export object that generated this specific execution.</p>"""
    execution_id: "capo_bcm_data_exports.types.generic_string.GenericString"
    """<p>The ID for this specific execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExecutionRequest) -> dict:
    out: dict = {}
    out["ExportArn"] = value["export_arn"]
    out["ExecutionId"] = value["execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExecutionRequest:
    out: GetExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExportArn") is not None:
        out["export_arn"] = data["ExportArn"]
    else:
        out["export_arn"] = ""
    if data.get("ExecutionId") is not None:
        out["execution_id"] = data["ExecutionId"]
    else:
        out["execution_id"] = ""
    return out
