"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetIntentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.intent_name
    import capo_lex_model_building_service.types.max_results
    import capo_lex_model_building_service.types.next_token


class GetIntentsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_lex_model_building_service.types.next_token.NextToken"
    ]
    """<p>A pagination token that fetches the next page of intents. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, specify the pagination token in the next request. </p>"""
    max_results: NotRequired[
        "capo_lex_model_building_service.types.max_results.MaxResults"
    ]
    """<p>The maximum number of intents to return in the response. The default is 10.</p>"""
    name_contains: NotRequired[
        "capo_lex_model_building_service.types.intent_name.IntentName"
    ]
    """<p>Substring to match in intent names. An intent will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIntentsRequest:
    out: GetIntentsRequest = {}  # type: ignore[typeddict-item]
    return out
