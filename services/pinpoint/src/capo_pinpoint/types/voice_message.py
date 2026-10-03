"""Generated from Smithy shape ``com.amazonaws.pinpoint#VoiceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.map_of_list_of__string


class VoiceMessage(TypedDict, closed=True):
    body: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The text of the script to use for the voice message.</p>"""
    language_code: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The code for the language to use when synthesizing the text of the message script. For a list of supported languages and the code for each one, see the <a href="https://docs.aws.amazon.com/polly/latest/dg/what-is.html">Amazon Polly Developer Guide</a>.</p>"""
    origination_number: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The long code to send the voice message from. This value should be one of the dedicated long codes that's assigned to your AWS account. Although it isn't required, we recommend that you specify the long code in E.164 format, for example +12065550100, to ensure prompt and accurate delivery of the message.</p>"""
    substitutions: NotRequired[
        "capo_pinpoint.types.map_of_list_of__string.MapOfListOf__string"
    ]
    """<p>The default message variables to use in the voice message. You can override the default variables with individual address variables.</p>"""
    voice_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the voice to use when delivering the message. For a list of supported voices, see the <a href="https://docs.aws.amazon.com/polly/latest/dg/what-is.html">Amazon Polly Developer Guide</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceMessage) -> dict:
    out: dict = {}
    if "body" in value:
        out["Body"] = value["body"]
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    if "origination_number" in value:
        out["OriginationNumber"] = value["origination_number"]
    if "substitutions" in value:
        import capo_pinpoint.types.map_of_list_of__string

        out["Substitutions"] = (
            capo_pinpoint.types.map_of_list_of__string.serialize_json(
                value["substitutions"]
            )
        )
    if "voice_id" in value:
        out["VoiceId"] = value["voice_id"]
    return out


def deserialize_json(data: dict) -> VoiceMessage:
    out: VoiceMessage = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    if data.get("LanguageCode") is not None:
        out["language_code"] = data["LanguageCode"]
    if data.get("OriginationNumber") is not None:
        out["origination_number"] = data["OriginationNumber"]
    if data.get("Substitutions") is not None:
        import capo_pinpoint.types.map_of_list_of__string

        out["substitutions"] = (
            capo_pinpoint.types.map_of_list_of__string.deserialize_json(
                data["Substitutions"]
            )
        )
    if data.get("VoiceId") is not None:
        out["voice_id"] = data["VoiceId"]
    return out
