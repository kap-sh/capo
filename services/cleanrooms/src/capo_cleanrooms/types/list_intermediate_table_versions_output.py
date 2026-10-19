"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListIntermediateTableVersionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_version_summary_list
    import capo_cleanrooms.types.pagination_token


class ListIntermediateTableVersionsOutput(TypedDict, closed=True):
    intermediate_table_version_summaries: "capo_cleanrooms.types.intermediate_table_version_summary_list.IntermediateTableVersionSummaryList"
    """<p>The list of intermediate table version summaries.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntermediateTableVersionsOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.intermediate_table_version_summary_list

    out["intermediateTableVersionSummaries"] = (
        capo_cleanrooms.types.intermediate_table_version_summary_list.serialize_json(
            value["intermediate_table_version_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIntermediateTableVersionsOutput:
    out: ListIntermediateTableVersionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("intermediateTableVersionSummaries") is not None:
        import capo_cleanrooms.types.intermediate_table_version_summary_list

        out["intermediate_table_version_summaries"] = (
            capo_cleanrooms.types.intermediate_table_version_summary_list.deserialize_json(
                data["intermediateTableVersionSummaries"]
            )
        )
    else:
        out["intermediate_table_version_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
