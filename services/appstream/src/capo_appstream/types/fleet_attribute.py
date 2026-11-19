"""Generated from Smithy shape ``com.amazonaws.appstream#FleetAttribute``."""

from typing import Literal, TypeAlias, cast

"""<p>The fleet attribute.</p>"""
FleetAttribute: TypeAlias = Literal[
    "VPC_CONFIGURATION",
    "VPC_CONFIGURATION_SECURITY_GROUP_IDS",
    "DOMAIN_JOIN_INFO",
    "IAM_ROLE_ARN",
    "USB_DEVICE_FILTER_STRINGS",
    "SESSION_SCRIPT_S3_LOCATION",
    "MAX_SESSIONS_PER_INSTANCE",
    "VOLUME_CONFIGURATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetAttribute:
    return cast(FleetAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> FleetAttribute:
    return cast(FleetAttribute, data)
