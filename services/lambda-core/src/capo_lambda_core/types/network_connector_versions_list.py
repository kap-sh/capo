"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_core.types.network_connector_version_summary

NetworkConnectorVersionsList: TypeAlias = list[
    "capo_lambda_core.types.network_connector_version_summary.NetworkConnectorVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorVersionsList) -> list:
    import capo_lambda_core.types.network_connector_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_lambda_core.types.network_connector_version_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkConnectorVersionsList:
    import capo_lambda_core.types.network_connector_version_summary

    out: NetworkConnectorVersionsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lambda_core.types.network_connector_version_summary.deserialize_json(
                item
            )
        )
    return out
