"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeEC2InstanceLimitsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.ec2_instance_type
    import capo_gamelift.types.location_string_model


class DescribeEC2InstanceLimitsInput(TypedDict, closed=True):
    ec2_instance_type: NotRequired[
        "capo_gamelift.types.ec2_instance_type.EC2InstanceType"
    ]
    """<p>Name of an Amazon EC2 instance type that is supported in Amazon GameLift Servers. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Do not specify a value for this parameter to retrieve limits for all instance types.</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The name of a remote location to request instance limits for, in the form of an Amazon Web Services Region code such as <code>us-west-2</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEC2InstanceLimitsInput) -> dict:
    out: dict = {}
    if "ec2_instance_type" in value:
        import capo_gamelift.types.ec2_instance_type

        out["EC2InstanceType"] = (
            capo_gamelift.types.ec2_instance_type.serialize_aws_json_1_1(
                value["ec2_instance_type"]
            )
        )
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEC2InstanceLimitsInput:
    out: DescribeEC2InstanceLimitsInput = {}  # type: ignore[typeddict-item]
    if data.get("EC2InstanceType") is not None:
        import capo_gamelift.types.ec2_instance_type

        out["ec2_instance_type"] = (
            capo_gamelift.types.ec2_instance_type.deserialize_aws_json_1_1(
                data["EC2InstanceType"]
            )
        )
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEC2InstanceLimitsInput) -> dict:
    out: dict = {}
    if "ec2_instance_type" in value:
        import capo_gamelift.types.ec2_instance_type

        out["EC2InstanceType"] = capo_gamelift.types.ec2_instance_type.serialize_cbor(
            value["ec2_instance_type"]
        )
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_cbor(data: dict) -> DescribeEC2InstanceLimitsInput:
    out: DescribeEC2InstanceLimitsInput = {}  # type: ignore[typeddict-item]
    if data.get("EC2InstanceType") is not None:
        import capo_gamelift.types.ec2_instance_type

        out["ec2_instance_type"] = (
            capo_gamelift.types.ec2_instance_type.deserialize_cbor(
                data["EC2InstanceType"]
            )
        )
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out
