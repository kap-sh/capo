"""Generated from Smithy shape ``com.amazonaws.ssm#RelatedOpsItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.string


class RelatedOpsItem(TypedDict, closed=True):
    ops_item_id: "capo_ssm.types.string.String"
    """<p>The ID of an OpsItem related to the current OpsItem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelatedOpsItem) -> dict:
    out: dict = {}
    out["OpsItemId"] = value["ops_item_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RelatedOpsItem:
    out: RelatedOpsItem = {}  # type: ignore[typeddict-item]
    if data.get("OpsItemId") is not None:
        out["ops_item_id"] = data["OpsItemId"]
    else:
        out["ops_item_id"] = ""
    return out
