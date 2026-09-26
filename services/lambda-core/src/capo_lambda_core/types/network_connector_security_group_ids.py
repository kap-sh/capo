"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorSecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_core.types.network_connector_security_group_id

NetworkConnectorSecurityGroupIds: TypeAlias = list[
    "capo_lambda_core.types.network_connector_security_group_id.NetworkConnectorSecurityGroupId"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorSecurityGroupIds) -> list:
    return list(value)


def deserialize_json(data: list) -> NetworkConnectorSecurityGroupIds:
    return [item for item in data if item is not None]
