"""Generated from Smithy shape ``com.amazonaws.workspaces#DisassociateIpGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.ip_group_id_list


class DisassociateIpGroupsRequest(TypedDict, closed=True):
    directory_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    group_ids: "capo_workspaces.types.ip_group_id_list.IpGroupIdList"
    """<p>The identifiers of one or more IP access control groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateIpGroupsRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import capo_workspaces.types.ip_group_id_list

    out["GroupIds"] = capo_workspaces.types.ip_group_id_list.serialize_aws_json_1_1(
        value["group_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateIpGroupsRequest:
    out: DisassociateIpGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("GroupIds") is not None:
        import capo_workspaces.types.ip_group_id_list

        out["group_ids"] = (
            capo_workspaces.types.ip_group_id_list.deserialize_aws_json_1_1(
                data["GroupIds"]
            )
        )
    else:
        out["group_ids"] = []
    return out
