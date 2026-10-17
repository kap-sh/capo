"""Generated from Smithy shape ``com.amazonaws.lambdacore#DeleteNetworkConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.network_connector_identifier


class DeleteNetworkConnectorRequest(TypedDict, closed=True):
    identifier: (
        "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier"
    )


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNetworkConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNetworkConnectorRequest:
    out: DeleteNetworkConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
