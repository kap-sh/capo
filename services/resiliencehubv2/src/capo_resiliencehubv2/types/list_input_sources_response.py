"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListInputSourcesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.input_source_summary_list
    import capo_resiliencehubv2.types.next_token


class ListInputSourcesResponse(TypedDict, closed=True):
    input_source_summaries: (
        "capo_resiliencehubv2.types.input_source_summary_list.InputSourceSummaryList"
    )
    """<p>The list of input source summaries.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListInputSourcesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.input_source_summary_list

    out["inputSourceSummaries"] = (
        capo_resiliencehubv2.types.input_source_summary_list.serialize_json(
            value["input_source_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInputSourcesResponse:
    out: ListInputSourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("inputSourceSummaries") is not None:
        import capo_resiliencehubv2.types.input_source_summary_list

        out["input_source_summaries"] = (
            capo_resiliencehubv2.types.input_source_summary_list.deserialize_json(
                data["inputSourceSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListInputSourcesResponse.input_source_summaries required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListInputSourcesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_source_summaries" in value:
        import capo_resiliencehubv2.types.input_source_summary_list

        out["input_source_summaries"] = (
            capo_resiliencehubv2.types.input_source_summary_list.redact_sensitive(
                value["input_source_summaries"]
            )
        )
    return out
