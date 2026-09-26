"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_core.types.network_connector_summary

NetworkConnectorsList: TypeAlias = list[
    "capo_lambda_core.types.network_connector_summary.NetworkConnectorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorsList) -> list:
    import capo_lambda_core.types.network_connector_summary

    out: list = []
    for item in value:
        out.append(
            capo_lambda_core.types.network_connector_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkConnectorsList:
    import capo_lambda_core.types.network_connector_summary

    out: NetworkConnectorsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lambda_core.types.network_connector_summary.deserialize_json(item)
        )
    return out
