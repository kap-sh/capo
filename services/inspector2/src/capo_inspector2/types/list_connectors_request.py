"""Generated from Smithy shape ``com.amazonaws.inspector2#ListConnectorsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.connector_filter_criteria
    import capo_inspector2.types.connector_next_token


class ListConnectorsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another request with the <code>nextToken</code> value returned from this request.</p>"""
    next_token: NotRequired[
        "capo_inspector2.types.connector_next_token.ConnectorNextToken"
    ]
    """<p>A token to use for paginating results. Set this value to null for the first request. For subsequent calls, use the <code>nextToken</code> value returned from the previous request.</p>"""
    filter_criteria: NotRequired[
        "capo_inspector2.types.connector_filter_criteria.ConnectorFilterCriteria"
    ]
    """<p>The filter criteria to apply to the list of connectors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filter_criteria" in value:
        import capo_inspector2.types.connector_filter_criteria

        out["filterCriteria"] = (
            capo_inspector2.types.connector_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListConnectorsRequest:
    out: ListConnectorsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("filterCriteria") is not None:
        import capo_inspector2.types.connector_filter_criteria

        out["filter_criteria"] = (
            capo_inspector2.types.connector_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    return out


def redact_sensitive(value: ListConnectorsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
