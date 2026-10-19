"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListDatasetDataSegmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.data_segment_summaries
    import capo_iotsitewise.types.next_token


class ListDatasetDataSegmentsResponse(TypedDict, closed=True):
    data_segments: "capo_iotsitewise.types.data_segment_summaries.DataSegmentSummaries"
    """<p>A list that summarizes each data segment.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetDataSegmentsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.data_segment_summaries

    out["dataSegments"] = capo_iotsitewise.types.data_segment_summaries.serialize_json(
        value["data_segments"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetDataSegmentsResponse:
    out: ListDatasetDataSegmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataSegments") is not None:
        import capo_iotsitewise.types.data_segment_summaries

        out["data_segments"] = (
            capo_iotsitewise.types.data_segment_summaries.deserialize_json(
                data["dataSegments"]
            )
        )
    else:
        out["data_segments"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
