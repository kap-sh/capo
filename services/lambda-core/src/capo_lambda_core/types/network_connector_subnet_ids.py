"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorSubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_core.types.network_connector_subnet_id

NetworkConnectorSubnetIds: TypeAlias = list[
    "capo_lambda_core.types.network_connector_subnet_id.NetworkConnectorSubnetId"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorSubnetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> NetworkConnectorSubnetIds:
    return [item for item in data if item is not None]
