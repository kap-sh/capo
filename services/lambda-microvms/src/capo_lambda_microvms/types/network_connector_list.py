"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#NetworkConnectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_microvms.types.network_connector

NetworkConnectorList: TypeAlias = list[
    "capo_lambda_microvms.types.network_connector.NetworkConnector"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorList) -> list:
    return list(value)


def deserialize_json(data: list) -> NetworkConnectorList:
    return [item for item in data if item is not None]
