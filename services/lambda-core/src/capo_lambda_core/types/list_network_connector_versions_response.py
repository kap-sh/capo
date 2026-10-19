"""Generated from Smithy shape ``com.amazonaws.lambdacore#ListNetworkConnectorVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.network_connector_versions_list
    import capo_lambda_core.types.string


class ListNetworkConnectorVersionsResponse(TypedDict, closed=True):
    network_connector_versions: "capo_lambda_core.types.network_connector_versions_list.NetworkConnectorVersionsList"
    """<p>A list of connector version summaries for the current page of results.</p>"""
    next_marker: NotRequired["capo_lambda_core.types.string.String"]
    """<p>The pagination token to include in a subsequent request to retrieve the next page. This value is null when there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkConnectorVersionsResponse) -> dict:
    out: dict = {}
    import capo_lambda_core.types.network_connector_versions_list

    out["NetworkConnectorVersions"] = (
        capo_lambda_core.types.network_connector_versions_list.serialize_json(
            value["network_connector_versions"]
        )
    )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListNetworkConnectorVersionsResponse:
    out: ListNetworkConnectorVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NetworkConnectorVersions") is not None:
        import capo_lambda_core.types.network_connector_versions_list

        out["network_connector_versions"] = (
            capo_lambda_core.types.network_connector_versions_list.deserialize_json(
                data["NetworkConnectorVersions"]
            )
        )
    else:
        out["network_connector_versions"] = []
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
