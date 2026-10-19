"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.boolean_object
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.organization_id


class UpdateGroupRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization under which the group exists.</p>"""
    group_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier for the group to be updated.</p> <p>The identifier can accept <i>GroupId</i>, <i>Groupname</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Group ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: group@domain.tld</p> </li> <li> <p>Group name: group</p> </li> </ul>"""
    hidden_from_global_address_list: NotRequired[
        "capo_workmail.types.boolean_object.BooleanObject"
    ]
    """<p>If enabled, the group is hidden from the global address list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGroupRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["GroupId"] = value["group_id"]
    if "hidden_from_global_address_list" in value:
        out["HiddenFromGlobalAddressList"] = value["hidden_from_global_address_list"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGroupRequest:
    out: UpdateGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    else:
        out["group_id"] = ""
    if data.get("HiddenFromGlobalAddressList") is not None:
        out["hidden_from_global_address_list"] = data["HiddenFromGlobalAddressList"]
    return out
