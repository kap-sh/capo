"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLevelResultDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.test_result_match_status


class ConversationLevelResultDetail(TypedDict, closed=True):
    end_to_end_result: (
        "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    )
    """<p>The success or failure of the streaming of the conversation.</p>"""
    speech_transcription_result: NotRequired[
        "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    ]
    """<p>The speech transcription success or failure details of the conversation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLevelResultDetail) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.test_result_match_status

    out["endToEndResult"] = (
        capo_lex_models_v2.types.test_result_match_status.serialize_json(
            value["end_to_end_result"]
        )
    )
    if "speech_transcription_result" in value:
        import capo_lex_models_v2.types.test_result_match_status

        out["speechTranscriptionResult"] = (
            capo_lex_models_v2.types.test_result_match_status.serialize_json(
                value["speech_transcription_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConversationLevelResultDetail:
    out: ConversationLevelResultDetail = {}  # type: ignore[typeddict-item]
    if data.get("endToEndResult") is not None:
        import capo_lex_models_v2.types.test_result_match_status

        out["end_to_end_result"] = (
            capo_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["endToEndResult"]
            )
        )
    else:
        import typing

        out["end_to_end_result"] = typing.cast(
            "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus",
            "",
        )
    if data.get("speechTranscriptionResult") is not None:
        import capo_lex_models_v2.types.test_result_match_status

        out["speech_transcription_result"] = (
            capo_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["speechTranscriptionResult"]
            )
        )
    return out
