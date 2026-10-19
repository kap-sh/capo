"""Generated from Smithy shape ``com.amazonaws.polly#DescribeVoicesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_polly.types.engine
    import capo_polly.types.include_additional_language_codes
    import capo_polly.types.language_code
    import capo_polly.types.next_token


class DescribeVoicesInput(TypedDict, closed=True):
    engine: NotRequired["capo_polly.types.engine.Engine"]
    """<p>Specifies the engine (<code>standard</code>, <code>neural</code>, <code>long-form</code> or <code>generative</code>) used by Amazon Polly when processing input text for speech synthesis. </p>"""
    language_code: NotRequired["capo_polly.types.language_code.LanguageCode"]
    """<p> The language identification tag (ISO 639 code for the language name-ISO 3166 country code) for filtering the list of voices returned. If you don't specify this optional parameter, all available voices are returned. </p>"""
    include_additional_language_codes: NotRequired[
        "capo_polly.types.include_additional_language_codes.IncludeAdditionalLanguageCodes"
    ]
    """<p>Boolean value indicating whether to return any bilingual voices that use the specified language as an additional language. For instance, if you request all languages that use US English (es-US), and there is an Italian voice that speaks both Italian (it-IT) and US English, that voice will be included if you specify <code>yes</code> but not if you specify <code>no</code>.</p>"""
    next_token: NotRequired["capo_polly.types.next_token.NextToken"]
    """<p>An opaque pagination token returned from the previous <code>DescribeVoices</code> operation. If present, this indicates where to continue the listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVoicesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeVoicesInput:
    out: DescribeVoicesInput = {}  # type: ignore[typeddict-item]
    return out
