"""Generated from Smithy shape ``com.amazonaws.simpledbv2#ListExportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simpledbv2.types.export_summaries
    import capo_simpledbv2.types.next_token


class ListExportsResponse(TypedDict, closed=True):
    export_summaries: "capo_simpledbv2.types.export_summaries.ExportSummaries"
    """List of export summaries containing export ARN, status, request timestamp, and associated domain name."""
    next_token: NotRequired["capo_simpledbv2.types.next_token.NextToken"]
    """A pagination token indicating that more results are available. To retrieve the next page of results, provide this token in a subsequent ListExports request. If null or empty, there are no more results to retrieve."""


# --- restJson1 ser/de ---
def serialize_json(value: ListExportsResponse) -> dict:
    out: dict = {}
    import capo_simpledbv2.types.export_summaries

    out["exportSummaries"] = capo_simpledbv2.types.export_summaries.serialize_json(
        value["export_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExportsResponse:
    out: ListExportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("exportSummaries") is not None:
        import capo_simpledbv2.types.export_summaries

        out["export_summaries"] = (
            capo_simpledbv2.types.export_summaries.deserialize_json(
                data["exportSummaries"]
            )
        )
    else:
        out["export_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
