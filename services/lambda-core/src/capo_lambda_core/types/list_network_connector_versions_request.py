"""Generated from Smithy shape ``com.amazonaws.lambdacore#ListNetworkConnectorVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.max_hundred_list_items
    import capo_lambda_core.types.network_connector_identifier
    import capo_lambda_core.types.network_connector_state
    import capo_lambda_core.types.string


class ListNetworkConnectorVersionsRequest(TypedDict, closed=True):
    identifier: (
        "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier"
    )
    """<p>The identifier of the network connector whose versions you want to list. You can specify the connector ID, name, or full ARN. Specify an unqualified identifier — this operation lists all versions of the connector, not a specific version.</p>"""
    state: NotRequired[
        "capo_lambda_core.types.network_connector_state.NetworkConnectorState"
    ]
    """<p>Optional filter to return only versions in the specified state (for example, <code>ACTIVE</code> or <code>FAILED</code>).</p>"""
    marker: NotRequired["capo_lambda_core.types.string.String"]
    """<p>The pagination token from a previous <code>ListNetworkConnectorVersions</code> response. Use this value to retrieve the next page of results.</p>"""
    max_items: NotRequired[
        "capo_lambda_core.types.max_hundred_list_items.MaxHundredListItems"
    ]
    """<p>The maximum number of versions to return per page. Valid range: 1 to 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkConnectorVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNetworkConnectorVersionsRequest:
    out: ListNetworkConnectorVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
