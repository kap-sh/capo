"""Generated from Smithy shape ``com.amazonaws.translate#ListLanguagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.display_language_code
    import capo_translate.types.max_results_integer
    import capo_translate.types.next_token


class ListLanguagesRequest(TypedDict, closed=True):
    display_language_code: NotRequired[
        "capo_translate.types.display_language_code.DisplayLanguageCode"
    ]
    """<p>The language code for the language to use to display the language names in the response. The language code is <code>en</code> by default. </p>"""
    next_token: NotRequired["capo_translate.types.next_token.NextToken"]
    """<p>Include the NextToken value to fetch the next group of supported languages. </p>"""
    max_results: NotRequired[
        "capo_translate.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>The maximum number of results to return in each response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLanguagesRequest) -> dict:
    out: dict = {}
    if "display_language_code" in value:
        import capo_translate.types.display_language_code

        out["DisplayLanguageCode"] = (
            capo_translate.types.display_language_code.serialize_aws_json_1_1(
                value["display_language_code"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLanguagesRequest:
    out: ListLanguagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("DisplayLanguageCode") is not None:
        import capo_translate.types.display_language_code

        out["display_language_code"] = (
            capo_translate.types.display_language_code.deserialize_aws_json_1_1(
                data["DisplayLanguageCode"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListLanguagesRequest) -> dict:
    out: dict = {}
    if "display_language_code" in value:
        import capo_translate.types.display_language_code

        out["DisplayLanguageCode"] = (
            capo_translate.types.display_language_code.serialize_cbor(
                value["display_language_code"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListLanguagesRequest:
    out: ListLanguagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("DisplayLanguageCode") is not None:
        import capo_translate.types.display_language_code

        out["display_language_code"] = (
            capo_translate.types.display_language_code.deserialize_cbor(
                data["DisplayLanguageCode"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
