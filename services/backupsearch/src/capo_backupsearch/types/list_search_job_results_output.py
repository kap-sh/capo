"""Generated from Smithy shape ``com.amazonaws.backupsearch#ListSearchJobResultsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_backupsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backupsearch.types.results


class ListSearchJobResultsOutput(TypedDict, closed=True):
    results: "capo_backupsearch.types.results.Results"
    """<p>The results consist of either EBSResultItem or S3ResultItem.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of search job results.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSearchJobResultsOutput) -> dict:
    out: dict = {}
    import capo_backupsearch.types.results

    out["Results"] = capo_backupsearch.types.results.serialize_json(value["results"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSearchJobResultsOutput:
    out: ListSearchJobResultsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Results") is not None:
        import capo_backupsearch.types.results

        out["results"] = capo_backupsearch.types.results.deserialize_json(
            data["Results"]
        )
    else:
        raise DeserializationError("ListSearchJobResultsOutput.results required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListSearchJobResultsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "results" in value:
        import capo_backupsearch.types.results

        out["results"] = capo_backupsearch.types.results.redact_sensitive(
            value["results"]
        )
    return out
