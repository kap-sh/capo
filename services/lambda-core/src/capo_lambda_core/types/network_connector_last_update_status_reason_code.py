"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorLastUpdateStatusReasonCode``."""

from typing import Literal, TypeAlias, cast

"""<p>A machine-readable code indicating why the last update operation reached its current status. Use this for programmatic error handling.</p>"""
NetworkConnectorLastUpdateStatusReasonCode: TypeAlias = Literal[
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
def serialize_json(value: NetworkConnectorLastUpdateStatusReasonCode) -> str:
    return value


def deserialize_json(data: str) -> NetworkConnectorLastUpdateStatusReasonCode:
    return cast(NetworkConnectorLastUpdateStatusReasonCode, data)
