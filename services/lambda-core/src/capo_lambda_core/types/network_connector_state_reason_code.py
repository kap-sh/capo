"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorStateReasonCode``."""

from typing import Literal, TypeAlias, cast

"""<p>A machine-readable code indicating why the connector reached its current state. Use this for programmatic error handling.</p>"""
NetworkConnectorStateReasonCode: TypeAlias = Literal[
    "DisallowedByVpcEncryptionControl",
    "Ec2RequestLimitExceeded",
    "InsufficientRolePermissions",
    "InternalError",
    "InvalidSecurityGroup",
    "InvalidSubnet",
    "SecurityGroupsPerInterfaceLimitExceeded",
    "SubnetOutOfIPAddresses",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorStateReasonCode) -> str:
    return value


def deserialize_json(data: str) -> NetworkConnectorStateReasonCode:
    return cast(NetworkConnectorStateReasonCode, data)
