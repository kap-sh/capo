"""Generated from Smithy shape ``com.amazonaws.workmail#CreateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.boolean
    import capo_workmail.types.group_name
    import capo_workmail.types.organization_id


class CreateGroupRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The organization under which the group is to be created.</p>"""
    name: "capo_workmail.types.group_name.GroupName"
    """<p>The name of the group.</p>"""
    hidden_from_global_address_list: NotRequired["capo_workmail.types.boolean.Boolean"]
    """<p>If this parameter is enabled, the group will be hidden from the address book.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGroupRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["Name"] = value["name"]
    if "hidden_from_global_address_list" in value:
        out["HiddenFromGlobalAddressList"] = value["hidden_from_global_address_list"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGroupRequest:
    out: CreateGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("CreateGroupRequest.organization_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateGroupRequest.name required")
    if data.get("HiddenFromGlobalAddressList") is not None:
        out["hidden_from_global_address_list"] = data["HiddenFromGlobalAddressList"]
    return out
