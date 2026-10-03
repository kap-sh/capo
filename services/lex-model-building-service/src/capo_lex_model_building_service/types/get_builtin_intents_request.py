"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBuiltinIntentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.locale
    import capo_lex_model_building_service.types.max_results
    import capo_lex_model_building_service.types.next_token
    import capo_lex_model_building_service.types.string


class GetBuiltinIntentsRequest(TypedDict, closed=True):
    locale: NotRequired["capo_lex_model_building_service.types.locale.Locale"]
    """<p>A list of locales that the intent supports.</p>"""
    signature_contains: NotRequired[
        "capo_lex_model_building_service.types.string.String"
    ]
    """<p>Substring to match in built-in intent signatures. An intent will be returned if any part of its signature matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz." To find the signature for an intent, see <a href="https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.</p>"""
    next_token: NotRequired[
        "capo_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token that fetches the next page of intents. If this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, use the pagination token in the next request.</p>"""
    max_results: NotRequired[
        "capo_lex_model_building_service.types.max_results.MaxResults"
    ]
    """<p>The maximum number of intents to return in the response. The default is 10.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBuiltinIntentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBuiltinIntentsRequest:
    out: GetBuiltinIntentsRequest = {}  # type: ignore[typeddict-item]
    return out
