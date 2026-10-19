"""Generated from Smithy shape ``com.amazonaws.dax#CreateSubnetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.string
    import capo_dax.types.subnet_identifier_list


class CreateSubnetGroupRequest(TypedDict, closed=True):
    subnet_group_name: "capo_dax.types.string.String"
    """<p>A name for the subnet group. This value is stored as a lowercase string. </p>"""
    description: NotRequired["capo_dax.types.string.String"]
    """<p>A description for the subnet group</p>"""
    subnet_ids: "capo_dax.types.subnet_identifier_list.SubnetIdentifierList"
    """<p>A list of VPC subnet IDs for the subnet group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSubnetGroupRequest) -> dict:
    out: dict = {}
    out["SubnetGroupName"] = value["subnet_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_dax.types.subnet_identifier_list

    out["SubnetIds"] = capo_dax.types.subnet_identifier_list.serialize_aws_json_1_1(
        value["subnet_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSubnetGroupRequest:
    out: CreateSubnetGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubnetGroupName") is not None:
        out["subnet_group_name"] = data["SubnetGroupName"]
    else:
        out["subnet_group_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SubnetIds") is not None:
        import capo_dax.types.subnet_identifier_list

        out["subnet_ids"] = (
            capo_dax.types.subnet_identifier_list.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    else:
        out["subnet_ids"] = []
    return out
