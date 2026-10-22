"""Generated from Smithy shape ``com.amazonaws.datazone#ListDesignationsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.designation_summaries
    import capo_datazone.types.pagination_token


class ListDesignationsOutput(TypedDict, closed=True):
    items: NotRequired["capo_datazone.types.designation_summaries.DesignationSummaries"]
    """<p>The designation summaries that <code>ListDesignations</code> returned. Each item contains summary information about a designation in the domain.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>A pagination token that indicates that more results are available. Pass this token to a subsequent call to <code>ListDesignations</code> to retrieve the next page of results. If there are no more results, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDesignationsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_datazone.types.designation_summaries

        out["items"] = capo_datazone.types.designation_summaries.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDesignationsOutput:
    out: ListDesignationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_datazone.types.designation_summaries

        out["items"] = capo_datazone.types.designation_summaries.deserialize_json(
            data["items"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListDesignationsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_datazone.types.designation_summaries

        out["items"] = capo_datazone.types.designation_summaries.redact_sensitive(
            value["items"]
        )
    return out
