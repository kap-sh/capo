"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListConnectorsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.connector_next_token
    import capo_observabilityadmin.types.list_connectors_max_results


class ListConnectorsInput(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_observabilityadmin.types.list_connectors_max_results.ListConnectorsMaxResults"
    ]
    """<p>The maximum number of connectors to return in one call. The default is 100.</p>"""
    next_token: NotRequired[
        "capo_observabilityadmin.types.connector_next_token.ConnectorNextToken"
    ]
    """<p>The token for the next page of results, returned by a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorsInput:
    out: ListConnectorsInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListConnectorsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
