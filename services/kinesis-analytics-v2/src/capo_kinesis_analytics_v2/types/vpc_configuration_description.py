"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#VpcConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.id
    import capo_kinesis_analytics_v2.types.security_group_ids
    import capo_kinesis_analytics_v2.types.subnet_ids
    import capo_kinesis_analytics_v2.types.vpc_id


class VpcConfigurationDescription(TypedDict, closed=True):
    vpc_configuration_id: "capo_kinesis_analytics_v2.types.id.Id"
    """<p>The ID of the VPC configuration.</p>"""
    vpc_id: "capo_kinesis_analytics_v2.types.vpc_id.VpcId"
    """<p>The ID of the associated VPC.</p>"""
    subnet_ids: "capo_kinesis_analytics_v2.types.subnet_ids.SubnetIds"
    """<p>The array of <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html">Subnet</a> IDs used by the VPC configuration.</p>"""
    security_group_ids: (
        "capo_kinesis_analytics_v2.types.security_group_ids.SecurityGroupIds"
    )
    """<p>The array of <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html">SecurityGroup</a> IDs used by the VPC configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfigurationDescription) -> dict:
    out: dict = {}
    out["VpcConfigurationId"] = value["vpc_configuration_id"]
    out["VpcId"] = value["vpc_id"]
    import capo_kinesis_analytics_v2.types.subnet_ids

    out["SubnetIds"] = (
        capo_kinesis_analytics_v2.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    )
    import capo_kinesis_analytics_v2.types.security_group_ids

    out["SecurityGroupIds"] = (
        capo_kinesis_analytics_v2.types.security_group_ids.serialize_aws_json_1_1(
            value["security_group_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcConfigurationDescription:
    out: VpcConfigurationDescription = {}  # type: ignore[typeddict-item]
    if data.get("VpcConfigurationId") is not None:
        out["vpc_configuration_id"] = data["VpcConfigurationId"]
    else:
        raise DeserializationError(
            "VpcConfigurationDescription.vpc_configuration_id required"
        )
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    else:
        raise DeserializationError("VpcConfigurationDescription.vpc_id required")
    if data.get("SubnetIds") is not None:
        import capo_kinesis_analytics_v2.types.subnet_ids

        out["subnet_ids"] = (
            capo_kinesis_analytics_v2.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    else:
        raise DeserializationError("VpcConfigurationDescription.subnet_ids required")
    if data.get("SecurityGroupIds") is not None:
        import capo_kinesis_analytics_v2.types.security_group_ids

        out["security_group_ids"] = (
            capo_kinesis_analytics_v2.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "VpcConfigurationDescription.security_group_ids required"
        )
    return out
