"""Generated from Smithy shape ``com.amazonaws.datazone#ListConnectionsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.connection_summaries
    import capo_datazone.types.pagination_token


class ListConnectionsOutput(TypedDict, closed=True):
    items: "capo_datazone.types.connection_summaries.ConnectionSummaries"
    """<p>The results of the ListConnections action.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of connections is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of connections, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListConnections to list the next set of connections.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectionsOutput) -> dict:
    out: dict = {}
    import capo_datazone.types.connection_summaries

    out["items"] = capo_datazone.types.connection_summaries.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectionsOutput:
    out: ListConnectionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_datazone.types.connection_summaries

        out["items"] = capo_datazone.types.connection_summaries.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListConnectionsOutput.items required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListConnectionsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_datazone.types.connection_summaries

        out["items"] = capo_datazone.types.connection_summaries.redact_sensitive(
            value["items"]
        )
    return out
