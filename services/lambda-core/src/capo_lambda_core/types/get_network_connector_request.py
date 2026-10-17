"""Generated from Smithy shape ``com.amazonaws.lambdacore#GetNetworkConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.network_connector_identifier


class GetNetworkConnectorRequest(TypedDict, closed=True):
    identifier: (
        "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier"
    )
    """<p>The identifier of the network connector to retrieve. You can specify the connector ID, name, or ARN. Provide an unqualified ARN (or an ID or name) to retrieve the connector's latest version, or a version-qualified ARN — one that includes the immutable version suffix — to retrieve a specific historical version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNetworkConnectorRequest:
    out: GetNetworkConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
