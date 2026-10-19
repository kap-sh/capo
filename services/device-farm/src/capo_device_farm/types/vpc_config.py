"""Generated from Smithy shape ``com.amazonaws.devicefarm#VpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.non_empty_string
    import capo_device_farm.types.vpc_security_group_ids
    import capo_device_farm.types.vpc_subnet_ids


class VpcConfig(TypedDict, closed=True):
    security_group_ids: (
        "capo_device_farm.types.vpc_security_group_ids.VpcSecurityGroupIds"
    )
    """<p>An array of one or more security groups IDs in your Amazon VPC.</p>"""
    subnet_ids: "capo_device_farm.types.vpc_subnet_ids.VpcSubnetIds"
    """<p>An array of one or more subnet IDs in your Amazon VPC.</p>"""
    vpc_id: "capo_device_farm.types.non_empty_string.NonEmptyString"
    """<p>The ID of the Amazon VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfig) -> dict:
    out: dict = {}
    import capo_device_farm.types.vpc_security_group_ids

    out["securityGroupIds"] = (
        capo_device_farm.types.vpc_security_group_ids.serialize_aws_json_1_1(
            value["security_group_ids"]
        )
    )
    import capo_device_farm.types.vpc_subnet_ids

    out["subnetIds"] = capo_device_farm.types.vpc_subnet_ids.serialize_aws_json_1_1(
        value["subnet_ids"]
    )
    out["vpcId"] = value["vpc_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if data.get("securityGroupIds") is not None:
        import capo_device_farm.types.vpc_security_group_ids

        out["security_group_ids"] = (
            capo_device_farm.types.vpc_security_group_ids.deserialize_aws_json_1_1(
                data["securityGroupIds"]
            )
        )
    else:
        out["security_group_ids"] = []
    if data.get("subnetIds") is not None:
        import capo_device_farm.types.vpc_subnet_ids

        out["subnet_ids"] = (
            capo_device_farm.types.vpc_subnet_ids.deserialize_aws_json_1_1(
                data["subnetIds"]
            )
        )
    else:
        out["subnet_ids"] = []
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    else:
        out["vpc_id"] = ""
    return out
