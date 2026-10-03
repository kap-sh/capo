"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#GroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service_data.types.group_name
    import capo_directory_service_data.types.group_scope
    import capo_directory_service_data.types.group_type
    import capo_directory_service_data.types.sid


class GroupSummary(TypedDict, closed=True):
    sid: "capo_directory_service_data.types.sid.SID"
    """<p>The unique security identifier (SID) of the group.</p>"""
    sam_account_name: "capo_directory_service_data.types.group_name.GroupName"
    """<p>The name of the group.</p>"""
    group_type: "capo_directory_service_data.types.group_type.GroupType"
    """<p>The AD group type. For details, see <a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work">Active Directory security group type</a>.</p>"""
    group_scope: "capo_directory_service_data.types.group_scope.GroupScope"
    """<p>The scope of the AD group. For details, see <a href="https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope">Active Directory security groups</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupSummary) -> dict:
    out: dict = {}
    out["SID"] = value["sid"]
    out["SAMAccountName"] = value["sam_account_name"]
    import capo_directory_service_data.types.group_type

    out["GroupType"] = capo_directory_service_data.types.group_type.serialize_json(
        value["group_type"]
    )
    import capo_directory_service_data.types.group_scope

    out["GroupScope"] = capo_directory_service_data.types.group_scope.serialize_json(
        value["group_scope"]
    )
    return out


def deserialize_json(data: dict) -> GroupSummary:
    out: GroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("SID") is not None:
        out["sid"] = data["SID"]
    else:
        raise DeserializationError("GroupSummary.sid required")
    if data.get("SAMAccountName") is not None:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError("GroupSummary.sam_account_name required")
    if data.get("GroupType") is not None:
        import capo_directory_service_data.types.group_type

        out["group_type"] = (
            capo_directory_service_data.types.group_type.deserialize_json(
                data["GroupType"]
            )
        )
    else:
        raise DeserializationError("GroupSummary.group_type required")
    if data.get("GroupScope") is not None:
        import capo_directory_service_data.types.group_scope

        out["group_scope"] = (
            capo_directory_service_data.types.group_scope.deserialize_json(
                data["GroupScope"]
            )
        )
    else:
        raise DeserializationError("GroupSummary.group_scope required")
    return out
