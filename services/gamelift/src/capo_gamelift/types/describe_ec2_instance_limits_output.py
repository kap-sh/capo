"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeEC2InstanceLimitsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.ec2_instance_limit_list


class DescribeEC2InstanceLimitsOutput(TypedDict, closed=True):
    ec2_instance_limits: NotRequired[
        "capo_gamelift.types.ec2_instance_limit_list.EC2InstanceLimitList"
    ]
    """<p>The maximum number of instances for the specified instance type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEC2InstanceLimitsOutput) -> dict:
    out: dict = {}
    if "ec2_instance_limits" in value:
        import capo_gamelift.types.ec2_instance_limit_list

        out["EC2InstanceLimits"] = (
            capo_gamelift.types.ec2_instance_limit_list.serialize_aws_json_1_1(
                value["ec2_instance_limits"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEC2InstanceLimitsOutput:
    out: DescribeEC2InstanceLimitsOutput = {}  # type: ignore[typeddict-item]
    if data.get("EC2InstanceLimits") is not None:
        import capo_gamelift.types.ec2_instance_limit_list

        out["ec2_instance_limits"] = (
            capo_gamelift.types.ec2_instance_limit_list.deserialize_aws_json_1_1(
                data["EC2InstanceLimits"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEC2InstanceLimitsOutput) -> dict:
    out: dict = {}
    if "ec2_instance_limits" in value:
        import capo_gamelift.types.ec2_instance_limit_list

        out["EC2InstanceLimits"] = (
            capo_gamelift.types.ec2_instance_limit_list.serialize_cbor(
                value["ec2_instance_limits"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeEC2InstanceLimitsOutput:
    out: DescribeEC2InstanceLimitsOutput = {}  # type: ignore[typeddict-item]
    if data.get("EC2InstanceLimits") is not None:
        import capo_gamelift.types.ec2_instance_limit_list

        out["ec2_instance_limits"] = (
            capo_gamelift.types.ec2_instance_limit_list.deserialize_cbor(
                data["EC2InstanceLimits"]
            )
        )
    return out
