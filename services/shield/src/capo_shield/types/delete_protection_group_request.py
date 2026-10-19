"""Generated from Smithy shape ``com.amazonaws.shield#DeleteProtectionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_shield.types.protection_group_id


class DeleteProtectionGroupRequest(TypedDict, closed=True):
    protection_group_id: "capo_shield.types.protection_group_id.ProtectionGroupId"
    """<p>The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProtectionGroupRequest) -> dict:
    out: dict = {}
    out["ProtectionGroupId"] = value["protection_group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProtectionGroupRequest:
    out: DeleteProtectionGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionGroupId") is not None:
        out["protection_group_id"] = data["ProtectionGroupId"]
    else:
        out["protection_group_id"] = ""
    return out
