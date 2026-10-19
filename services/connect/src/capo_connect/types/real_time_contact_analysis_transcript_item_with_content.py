"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisTranscriptItemWithContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_character_interval
    import capo_connect.types.real_time_contact_analysis_id256
    import capo_connect.types.real_time_contact_analysis_transcript_content


class RealTimeContactAnalysisTranscriptItemWithContent(TypedDict, closed=True):
    content: NotRequired[
        "capo_connect.types.real_time_contact_analysis_transcript_content.RealTimeContactAnalysisTranscriptContent"
    ]
    """<p>Part of the transcript content that contains identified issue. Can be redacted</p>"""
    id: "capo_connect.types.real_time_contact_analysis_id256.RealTimeContactAnalysisId256"
    """<p>Transcript identifier. Matches the identifier from one of the TranscriptSegments.</p>"""
    character_offsets: NotRequired[
        "capo_connect.types.real_time_contact_analysis_character_interval.RealTimeContactAnalysisCharacterInterval"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisTranscriptItemWithContent) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    out["Id"] = value["id"]
    if "character_offsets" in value:
        import capo_connect.types.real_time_contact_analysis_character_interval

        out["CharacterOffsets"] = (
            capo_connect.types.real_time_contact_analysis_character_interval.serialize_json(
                value["character_offsets"]
            )
        )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisTranscriptItemWithContent:
    out: RealTimeContactAnalysisTranscriptItemWithContent = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("CharacterOffsets") is not None:
        import capo_connect.types.real_time_contact_analysis_character_interval

        out["character_offsets"] = (
            capo_connect.types.real_time_contact_analysis_character_interval.deserialize_json(
                data["CharacterOffsets"]
            )
        )
    return out
