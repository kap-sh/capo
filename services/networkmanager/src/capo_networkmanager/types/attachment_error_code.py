"""Generated from Smithy shape ``com.amazonaws.networkmanager#AttachmentErrorCode``."""

from typing import Literal, TypeAlias, cast

AttachmentErrorCode: TypeAlias = Literal[
    "VPC_NOT_FOUND",
    "SUBNET_NOT_FOUND",
    "SUBNET_DUPLICATED_IN_AVAILABILITY_ZONE",
    "SUBNET_NO_FREE_ADDRESSES",
    "SUBNET_UNSUPPORTED_AVAILABILITY_ZONE",
    "SUBNET_NO_IPV6_CIDRS",
    "SECURITY_GROUP_REFERENCING_UNSUPPORTED_AVAILABILITY_ZONE",
    "VPN_CONNECTION_NOT_FOUND",
    "MAXIMUM_NO_ENCAP_LIMIT_EXCEEDED",
    "DIRECT_CONNECT_GATEWAY_NOT_FOUND",
    "DIRECT_CONNECT_GATEWAY_EXISTING_ATTACHMENTS",
    "DIRECT_CONNECT_GATEWAY_NO_PRIVATE_VIF",
    "VPN_EXISTING_ASSOCIATIONS",
    "VPN_STATIC_ROUTES_NAT_UNSUPPORTED",
    "VPC_UNSUPPORTED_FEATURES",
    "DIRECT_CONNECT_GATEWAY_TOPOLOGY_RESTRICTIONS",
    "CREATION_FAILED",
    "UPDATE_FAILED",
    "DELETION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentErrorCode) -> str:
    return value


def deserialize_json(data: str) -> AttachmentErrorCode:
    return cast(AttachmentErrorCode, data)
