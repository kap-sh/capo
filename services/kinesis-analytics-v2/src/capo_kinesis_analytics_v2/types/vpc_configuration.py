"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#VpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.security_group_ids
    import capo_kinesis_analytics_v2.types.subnet_ids


class VpcConfiguration(TypedDict, closed=True):
    subnet_ids: "capo_kinesis_analytics_v2.types.subnet_ids.SubnetIds"
    """<p>The array of <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html">Subnet</a> IDs used by the VPC configuration.</p>"""
    security_group_ids: (
        "capo_kinesis_analytics_v2.types.security_group_ids.SecurityGroupIds"
    )
    """<p>The array of <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html">SecurityGroup</a> IDs used by the VPC configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfiguration) -> dict:
    out: dict = {}
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


def deserialize_aws_json_1_1(data: dict) -> VpcConfiguration:
    out: VpcConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SubnetIds") is not None:
        import capo_kinesis_analytics_v2.types.subnet_ids

        out["subnet_ids"] = (
            capo_kinesis_analytics_v2.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    else:
        raise DeserializationError("VpcConfiguration.subnet_ids required")
    if data.get("SecurityGroupIds") is not None:
        import capo_kinesis_analytics_v2.types.security_group_ids

        out["security_group_ids"] = (
            capo_kinesis_analytics_v2.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError("VpcConfiguration.security_group_ids required")
    return out
