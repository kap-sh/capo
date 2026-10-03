"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceBotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.image_response_card
    import capo_lex_models_v2.types.string
    import capo_lex_models_v2.types.utterance_content_type


class UtteranceBotResponse(TypedDict, closed=True):
    content: NotRequired["capo_lex_models_v2.types.string.String"]
    """<p>The text of the response to the utterance from the bot.</p>"""
    content_type: NotRequired[
        "capo_lex_models_v2.types.utterance_content_type.UtteranceContentType"
    ]
    """<p>The type of the response. The following values are possible:</p> <ul> <li> <p> <code>PlainText</code> – A plain text string.</p> </li> <li> <p> <code>CustomPayload</code> – A response string that you can customize to include data or metadata for your application.</p> </li> <li> <p> <code>SSML</code> – A string that includes Speech Synthesis Markup Language to customize the audio response.</p> </li> <li> <p> <code>ImageResponseCard</code> – An image with buttons that the customer can select. See <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_ImageResponseCard.html">ImageResponseCard</a> for more information.</p> </li> </ul>"""
    image_response_card: NotRequired[
        "capo_lex_models_v2.types.image_response_card.ImageResponseCard"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceBotResponse) -> dict:
    out: dict = {}
    if "content" in value:
        out["content"] = value["content"]
    if "content_type" in value:
        import capo_lex_models_v2.types.utterance_content_type

        out["contentType"] = (
            capo_lex_models_v2.types.utterance_content_type.serialize_json(
                value["content_type"]
            )
        )
    if "image_response_card" in value:
        import capo_lex_models_v2.types.image_response_card

        out["imageResponseCard"] = (
            capo_lex_models_v2.types.image_response_card.serialize_json(
                value["image_response_card"]
            )
        )
    return out


def deserialize_json(data: dict) -> UtteranceBotResponse:
    out: UtteranceBotResponse = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        out["content"] = data["content"]
    if data.get("contentType") is not None:
        import capo_lex_models_v2.types.utterance_content_type

        out["content_type"] = (
            capo_lex_models_v2.types.utterance_content_type.deserialize_json(
                data["contentType"]
            )
        )
    if data.get("imageResponseCard") is not None:
        import capo_lex_models_v2.types.image_response_card

        out["image_response_card"] = (
            capo_lex_models_v2.types.image_response_card.deserialize_json(
                data["imageResponseCard"]
            )
        )
    return out
