"""Generated from Smithy shape ``com.amazonaws.qconnect#QueryAssistantResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.next_token
    import capo_qconnect.types.query_results_list


class QueryAssistantResponse(TypedDict, closed=True):
    results: "capo_qconnect.types.query_results_list.QueryResultsList"
    """<p>The results of the query.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryAssistantResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.query_results_list

    out["results"] = capo_qconnect.types.query_results_list.serialize_json(
        value["results"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> QueryAssistantResponse:
    out: QueryAssistantResponse = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_qconnect.types.query_results_list

        out["results"] = capo_qconnect.types.query_results_list.deserialize_json(
            data["results"]
        )
    else:
        raise DeserializationError("QueryAssistantResponse.results required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: QueryAssistantResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "results" in value:
        import capo_qconnect.types.query_results_list

        out["results"] = capo_qconnect.types.query_results_list.redact_sensitive(
            value["results"]
        )
    return out
