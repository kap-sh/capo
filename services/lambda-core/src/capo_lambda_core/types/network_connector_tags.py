"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_core.types.network_connector_tag_key
    import capo_lambda_core.types.network_connector_tag_value

NetworkConnectorTags: TypeAlias = dict[
    "capo_lambda_core.types.network_connector_tag_key.NetworkConnectorTagKey",
    "capo_lambda_core.types.network_connector_tag_value.NetworkConnectorTagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: NetworkConnectorTags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> NetworkConnectorTags:
    out: NetworkConnectorTags = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
