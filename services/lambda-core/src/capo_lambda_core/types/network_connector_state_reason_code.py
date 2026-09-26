"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorStateReasonCode``."""

from typing import Literal, TypeAlias, cast

NetworkConnectorStateReasonCode: TypeAlias = Literal[
    "DisallowedByVpcEncryptionControl",
    "Ec2RequestLimitExceeded",
    "InsufficientRolePermissions",
    "InternalError",
    "InvalidSecurityGroup",
    "InvalidSubnet",
    "SubnetOutOfIPAddresses",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorStateReasonCode) -> str:
    return value


def deserialize_json(data: str) -> NetworkConnectorStateReasonCode:
    return cast(NetworkConnectorStateReasonCode, data)
