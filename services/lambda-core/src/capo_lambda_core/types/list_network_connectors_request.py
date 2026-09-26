"""Generated from Smithy shape ``com.amazonaws.lambdacore#ListNetworkConnectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.max_hundred_list_items
    import capo_lambda_core.types.network_connector_state
    import capo_lambda_core.types.string


class ListNetworkConnectorsRequest(TypedDict, closed=True):
    state: NotRequired[
        "capo_lambda_core.types.network_connector_state.NetworkConnectorState"
    ]
    """<p>Optional filter to return only connectors in the specified state (for example, <code>ACTIVE</code> or <code>FAILED</code>).</p>"""
    marker: NotRequired["capo_lambda_core.types.string.String"]
    """<p>The pagination token from a previous <code>ListNetworkConnectors</code> response. Use this value to retrieve the next page of results.</p>"""
    max_items: NotRequired[
        "capo_lambda_core.types.max_hundred_list_items.MaxHundredListItems"
    ]
    """<p>The maximum number of connectors to return per page. Valid range: 1 to 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkConnectorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNetworkConnectorsRequest:
    out: ListNetworkConnectorsRequest = {}  # type: ignore[typeddict-item]
    return out
