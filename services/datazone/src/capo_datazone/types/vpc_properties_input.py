"""Generated from Smithy shape ``com.amazonaws.datazone#VpcPropertiesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.security_group_id
    import capo_datazone.types.vpc_connection_subnet_id_list
    import capo_datazone.types.vpc_id


class VpcPropertiesInput(TypedDict, closed=True):
    vpc_id: "capo_datazone.types.vpc_id.VpcId"
    """<p>The identifier of the VPC. Must match the pattern <code>^vpc-[a-z0-9]+$</code>. Maximum length of 32.</p>"""
    subnet_ids: (
        "capo_datazone.types.vpc_connection_subnet_id_list.VpcConnectionSubnetIdList"
    )
    """<p>The subnet IDs of the VPC connection. You can specify between 1 and 16 subnet IDs.</p>"""
    security_group_id: NotRequired[
        "capo_datazone.types.security_group_id.SecurityGroupId"
    ]
    """<p>The security group ID of the VPC connection. Must match the pattern <code>^sg-[a-z0-9]+$</code>. Maximum length of 32.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcPropertiesInput) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    import capo_datazone.types.vpc_connection_subnet_id_list

    out["subnetIds"] = capo_datazone.types.vpc_connection_subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    if "security_group_id" in value:
        out["securityGroupId"] = value["security_group_id"]
    return out


def deserialize_json(data: dict) -> VpcPropertiesInput:
    out: VpcPropertiesInput = {}  # type: ignore[typeddict-item]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("subnetIds") is not None:
        import capo_datazone.types.vpc_connection_subnet_id_list

        out["subnet_ids"] = (
            capo_datazone.types.vpc_connection_subnet_id_list.deserialize_json(
                data["subnetIds"]
            )
        )
    else:
        out["subnet_ids"] = []
    if data.get("securityGroupId") is not None:
        out["security_group_id"] = data["securityGroupId"]
    return out
