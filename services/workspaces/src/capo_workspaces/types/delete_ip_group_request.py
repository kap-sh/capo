"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteIpGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.ip_group_id


class DeleteIpGroupRequest(TypedDict, closed=True):
    group_id: "capo_workspaces.types.ip_group_id.IpGroupId"
    """<p>The identifier of the IP access control group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIpGroupRequest) -> dict:
    out: dict = {}
    out["GroupId"] = value["group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIpGroupRequest:
    out: DeleteIpGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    else:
        out["group_id"] = ""
    return out
