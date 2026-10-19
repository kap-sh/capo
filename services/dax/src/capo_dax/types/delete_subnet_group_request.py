"""Generated from Smithy shape ``com.amazonaws.dax#DeleteSubnetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dax.types.string


class DeleteSubnetGroupRequest(TypedDict, closed=True):
    subnet_group_name: "capo_dax.types.string.String"
    """<p>The name of the subnet group to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSubnetGroupRequest) -> dict:
    out: dict = {}
    out["SubnetGroupName"] = value["subnet_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSubnetGroupRequest:
    out: DeleteSubnetGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubnetGroupName") is not None:
        out["subnet_group_name"] = data["SubnetGroupName"]
    else:
        out["subnet_group_name"] = ""
    return out
