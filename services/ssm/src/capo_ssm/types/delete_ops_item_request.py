"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteOpsItemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_id


class DeleteOpsItemRequest(TypedDict, closed=True):
    ops_item_id: "capo_ssm.types.ops_item_id.OpsItemId"
    """<p>The ID of the OpsItem that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOpsItemRequest) -> dict:
    out: dict = {}
    out["OpsItemId"] = value["ops_item_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteOpsItemRequest:
    out: DeleteOpsItemRequest = {}  # type: ignore[typeddict-item]
    if data.get("OpsItemId") is not None:
        out["ops_item_id"] = data["OpsItemId"]
    else:
        out["ops_item_id"] = ""
    return out
