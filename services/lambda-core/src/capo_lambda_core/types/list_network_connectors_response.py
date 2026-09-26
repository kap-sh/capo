"""Generated from Smithy shape ``com.amazonaws.lambdacore#ListNetworkConnectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_core.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_core.types.network_connectors_list
    import capo_lambda_core.types.string


class ListNetworkConnectorsResponse(TypedDict, closed=True):
    network_connectors: (
        "capo_lambda_core.types.network_connectors_list.NetworkConnectorsList"
    )
    """<p>A list of network connector summaries for the current page of results.</p>"""
    next_marker: NotRequired["capo_lambda_core.types.string.String"]
    """<p>The pagination token to include in a subsequent request to retrieve the next page. This value is null when there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkConnectorsResponse) -> dict:
    out: dict = {}
    import capo_lambda_core.types.network_connectors_list

    out["NetworkConnectors"] = (
        capo_lambda_core.types.network_connectors_list.serialize_json(
            value["network_connectors"]
        )
    )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListNetworkConnectorsResponse:
    out: ListNetworkConnectorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NetworkConnectors") is not None:
        import capo_lambda_core.types.network_connectors_list

        out["network_connectors"] = (
            capo_lambda_core.types.network_connectors_list.deserialize_json(
                data["NetworkConnectors"]
            )
        )
    else:
        raise DeserializationError(
            "ListNetworkConnectorsResponse.network_connectors required"
        )
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
