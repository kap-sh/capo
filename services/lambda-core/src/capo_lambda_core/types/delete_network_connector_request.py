"""Generated from Smithy shape ``com.amazonaws.lambdacore#DeleteNetworkConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.network_connector_identifier


class DeleteNetworkConnectorRequest(TypedDict, closed=True):
    identifier: (
        "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier"
    )
    """<p>The identifier of the network connector to delete. Provide an unqualified ARN (or an ID or name) to delete the entire connector and all of its versions, or a version-qualified ARN — one that includes the immutable version suffix — to delete a specific historical version. You can't delete the latest version with a version-qualified identifier; delete the connector instead.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNetworkConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNetworkConnectorRequest:
    out: DeleteNetworkConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
