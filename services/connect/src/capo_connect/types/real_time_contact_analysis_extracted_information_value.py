"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisExtractedInformationValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_extracted_information_content
    import capo_connect.types.real_time_contact_analysis_transcript_items_with_character_offsets


class RealTimeContactAnalysisExtractedInformationValue(TypedDict, closed=True):
    content: "capo_connect.types.real_time_contact_analysis_extracted_information_content.RealTimeContactAnalysisExtractedInformationContent"
    """<p>The text content of the extracted value.</p>"""
    points_of_interest: "capo_connect.types.real_time_contact_analysis_transcript_items_with_character_offsets.RealTimeContactAnalysisTranscriptItemsWithCharacterOffsets"
    """<p>The sections in the conversation that indicate where the extracted value was found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisExtractedInformationValue) -> dict:
    out: dict = {}
    out["Content"] = value["content"]
    import capo_connect.types.real_time_contact_analysis_transcript_items_with_character_offsets

    out["PointsOfInterest"] = (
        capo_connect.types.real_time_contact_analysis_transcript_items_with_character_offsets.serialize_json(
            value["points_of_interest"]
        )
    )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisExtractedInformationValue:
    out: RealTimeContactAnalysisExtractedInformationValue = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        out["content"] = ""
    if data.get("PointsOfInterest") is not None:
        import capo_connect.types.real_time_contact_analysis_transcript_items_with_character_offsets

        out["points_of_interest"] = (
            capo_connect.types.real_time_contact_analysis_transcript_items_with_character_offsets.deserialize_json(
                data["PointsOfInterest"]
            )
        )
    else:
        out["points_of_interest"] = []
    return out
