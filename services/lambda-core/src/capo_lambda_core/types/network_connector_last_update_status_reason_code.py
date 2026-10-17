"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorLastUpdateStatusReasonCode``."""

from typing import Literal, TypeAlias, cast

NetworkConnectorLastUpdateStatusReasonCode: TypeAlias = Literal[
    "DisallowedByVpcEncryptionControl",
    "Ec2RequestLimitExceeded",
    "InsufficientRolePermissions",
    "InternalError",
    "InvalidSecurityGroup",
    "InvalidSubnet",
    "SubnetOutOfIPAddresses",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorLastUpdateStatusReasonCode) -> str:
    return value


def deserialize_json(data: str) -> NetworkConnectorLastUpdateStatusReasonCode:
    return cast(NetworkConnectorLastUpdateStatusReasonCode, data)
