"""Generated from Smithy shape ``com.amazonaws.fms#AwsEc2NetworkInterfaceViolations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.aws_ec2_network_interface_violation

AwsEc2NetworkInterfaceViolations: TypeAlias = list[
    "capo_fms.types.aws_ec2_network_interface_violation.AwsEc2NetworkInterfaceViolation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AwsEc2NetworkInterfaceViolations) -> list:
    import capo_fms.types.aws_ec2_network_interface_violation

    out: list = []
    for item in value:
        out.append(
            capo_fms.types.aws_ec2_network_interface_violation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AwsEc2NetworkInterfaceViolations:
    import capo_fms.types.aws_ec2_network_interface_violation

    out: AwsEc2NetworkInterfaceViolations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_fms.types.aws_ec2_network_interface_violation.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AwsEc2NetworkInterfaceViolations) -> list:
    import capo_fms.types.aws_ec2_network_interface_violation

    out: list = []
    for item in value:
        out.append(
            capo_fms.types.aws_ec2_network_interface_violation.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> AwsEc2NetworkInterfaceViolations:
    import capo_fms.types.aws_ec2_network_interface_violation

    out: AwsEc2NetworkInterfaceViolations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_fms.types.aws_ec2_network_interface_violation.deserialize_cbor(item)
        )
    return out
