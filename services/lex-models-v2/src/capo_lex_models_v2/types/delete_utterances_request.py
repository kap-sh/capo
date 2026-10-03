"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteUtterancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.session_id


class DeleteUtterancesRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot that contains the utterances.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The identifier of the language and locale where the utterances were collected. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>"""
    session_id: NotRequired["capo_lex_models_v2.types.session_id.SessionId"]
    """<p>The unique identifier of the session with the user. The ID is returned in the response from the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html">RecognizeText</a> and <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html">RecognizeUtterance</a> operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUtterancesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteUtterancesRequest:
    out: DeleteUtterancesRequest = {}  # type: ignore[typeddict-item]
    return out
