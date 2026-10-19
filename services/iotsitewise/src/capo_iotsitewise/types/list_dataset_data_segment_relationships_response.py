"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListDatasetDataSegmentRelationshipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.data_segment_relationship_summaries
    import capo_iotsitewise.types.next_token


class ListDatasetDataSegmentRelationshipsResponse(TypedDict, closed=True):
    data_segment_relationship_summaries: "capo_iotsitewise.types.data_segment_relationship_summaries.DataSegmentRelationshipSummaries"
    """<p>A list that summarizes each data segment relationship.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetDataSegmentRelationshipsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.data_segment_relationship_summaries

    out["dataSegmentRelationshipSummaries"] = (
        capo_iotsitewise.types.data_segment_relationship_summaries.serialize_json(
            value["data_segment_relationship_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetDataSegmentRelationshipsResponse:
    out: ListDatasetDataSegmentRelationshipsResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataSegmentRelationshipSummaries") is not None:
        import capo_iotsitewise.types.data_segment_relationship_summaries

        out["data_segment_relationship_summaries"] = (
            capo_iotsitewise.types.data_segment_relationship_summaries.deserialize_json(
                data["dataSegmentRelationshipSummaries"]
            )
        )
    else:
        out["data_segment_relationship_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
