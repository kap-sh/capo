"""Generated from Smithy shape ``com.amazonaws.ssm#GetOpsItemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_arn
    import capo_ssm.types.ops_item_id


class GetOpsItemRequest(TypedDict, closed=True):
    ops_item_id: "capo_ssm.types.ops_item_id.OpsItemId"
    """<p>The ID of the OpsItem that you want to get.</p>"""
    ops_item_arn: NotRequired["capo_ssm.types.ops_item_arn.OpsItemArn"]
    """<p>The OpsItem Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOpsItemRequest) -> dict:
    out: dict = {}
    out["OpsItemId"] = value["ops_item_id"]
    if "ops_item_arn" in value:
        out["OpsItemArn"] = value["ops_item_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOpsItemRequest:
    out: GetOpsItemRequest = {}  # type: ignore[typeddict-item]
    if data.get("OpsItemId") is not None:
        out["ops_item_id"] = data["OpsItemId"]
    else:
        out["ops_item_id"] = ""
    if data.get("OpsItemArn") is not None:
        out["ops_item_arn"] = data["OpsItemArn"]
    return out
