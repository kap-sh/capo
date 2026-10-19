"""Generated from Smithy shape ``com.amazonaws.datazone#VpcPropertiesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.connection_status
    import capo_datazone.types.glue_connection_names
    import capo_datazone.types.security_group_id
    import capo_datazone.types.vpc_connection_subnet_id_list
    import capo_datazone.types.vpc_id


class VpcPropertiesOutput(TypedDict, closed=True):
    vpc_id: "capo_datazone.types.vpc_id.VpcId"
    """<p>The identifier of the VPC.</p>"""
    subnet_ids: (
        "capo_datazone.types.vpc_connection_subnet_id_list.VpcConnectionSubnetIdList"
    )
    """<p>The subnet IDs of the VPC connection.</p>"""
    status: "capo_datazone.types.connection_status.ConnectionStatus"
    """<p>The status of the VPC connection.</p>"""
    security_group_id: NotRequired[
        "capo_datazone.types.security_group_id.SecurityGroupId"
    ]
    """<p>The security group ID of the VPC connection.</p>"""
    glue_connection_names: NotRequired[
        "capo_datazone.types.glue_connection_names.GlueConnectionNames"
    ]
    """<p>The Amazon Web Services Glue connection names associated with the VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcPropertiesOutput) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    import capo_datazone.types.vpc_connection_subnet_id_list

    out["subnetIds"] = capo_datazone.types.vpc_connection_subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    import capo_datazone.types.connection_status

    out["status"] = capo_datazone.types.connection_status.serialize_json(
        value["status"]
    )
    if "security_group_id" in value:
        out["securityGroupId"] = value["security_group_id"]
    if "glue_connection_names" in value:
        import capo_datazone.types.glue_connection_names

        out["glueConnectionNames"] = (
            capo_datazone.types.glue_connection_names.serialize_json(
                value["glue_connection_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> VpcPropertiesOutput:
    out: VpcPropertiesOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("status") is not None:
        import capo_datazone.types.connection_status

        out["status"] = capo_datazone.types.connection_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.connection_status.ConnectionStatus", ""
        )
    if data.get("securityGroupId") is not None:
        out["security_group_id"] = data["securityGroupId"]
    if data.get("glueConnectionNames") is not None:
        import capo_datazone.types.glue_connection_names

        out["glue_connection_names"] = (
            capo_datazone.types.glue_connection_names.deserialize_json(
                data["glueConnectionNames"]
            )
        )
    return out
