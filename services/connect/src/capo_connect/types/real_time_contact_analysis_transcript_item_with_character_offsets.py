"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisTranscriptItemWithCharacterOffsets``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_character_interval
    import capo_connect.types.real_time_contact_analysis_id256


class RealTimeContactAnalysisTranscriptItemWithCharacterOffsets(TypedDict, closed=True):
    id: "capo_connect.types.real_time_contact_analysis_id256.RealTimeContactAnalysisId256"
    """<p>Transcript identifier. Matches the identifier from one of the TranscriptSegments.</p>"""
    character_offsets: NotRequired[
        "capo_connect.types.real_time_contact_analysis_character_interval.RealTimeContactAnalysisCharacterInterval"
    ]
    """<p>List of character intervals within transcript content/text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: RealTimeContactAnalysisTranscriptItemWithCharacterOffsets,
) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "character_offsets" in value:
        import capo_connect.types.real_time_contact_analysis_character_interval

        out["CharacterOffsets"] = (
            capo_connect.types.real_time_contact_analysis_character_interval.serialize_json(
                value["character_offsets"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> RealTimeContactAnalysisTranscriptItemWithCharacterOffsets:
    out: RealTimeContactAnalysisTranscriptItemWithCharacterOffsets = {}  # type: ignore[typeddict-item]
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
