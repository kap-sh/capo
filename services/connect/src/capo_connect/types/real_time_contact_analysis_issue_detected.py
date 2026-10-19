"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisIssueDetected``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_transcript_items_with_content


class RealTimeContactAnalysisIssueDetected(TypedDict, closed=True):
    transcript_items: "capo_connect.types.real_time_contact_analysis_transcript_items_with_content.RealTimeContactAnalysisTranscriptItemsWithContent"
    """<p>List of the transcript items (segments) that are associated with a given issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisIssueDetected) -> dict:
    out: dict = {}
    import capo_connect.types.real_time_contact_analysis_transcript_items_with_content

    out["TranscriptItems"] = (
        capo_connect.types.real_time_contact_analysis_transcript_items_with_content.serialize_json(
            value["transcript_items"]
        )
    )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisIssueDetected:
    out: RealTimeContactAnalysisIssueDetected = {}  # type: ignore[typeddict-item]
    if data.get("TranscriptItems") is not None:
        import capo_connect.types.real_time_contact_analysis_transcript_items_with_content

        out["transcript_items"] = (
            capo_connect.types.real_time_contact_analysis_transcript_items_with_content.deserialize_json(
                data["TranscriptItems"]
            )
        )
    else:
        out["transcript_items"] = []
    return out
