"""Generated from Smithy shape ``com.amazonaws.translate#ListLanguagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.display_language_code
    import capo_translate.types.languages_list
    import capo_translate.types.next_token


class ListLanguagesResponse(TypedDict, closed=True):
    languages: NotRequired["capo_translate.types.languages_list.LanguagesList"]
    """<p>The list of supported languages.</p>"""
    display_language_code: NotRequired[
        "capo_translate.types.display_language_code.DisplayLanguageCode"
    ]
    """<p>The language code passed in with the request.</p>"""
    next_token: NotRequired["capo_translate.types.next_token.NextToken"]
    """<p> If the response does not include all remaining results, use the NextToken in the next request to fetch the next group of supported languages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLanguagesResponse) -> dict:
    out: dict = {}
    if "languages" in value:
        import capo_translate.types.languages_list

        out["Languages"] = capo_translate.types.languages_list.serialize_aws_json_1_1(
            value["languages"]
        )
    if "display_language_code" in value:
        import capo_translate.types.display_language_code

        out["DisplayLanguageCode"] = (
            capo_translate.types.display_language_code.serialize_aws_json_1_1(
                value["display_language_code"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLanguagesResponse:
    out: ListLanguagesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Languages") is not None:
        import capo_translate.types.languages_list

        out["languages"] = capo_translate.types.languages_list.deserialize_aws_json_1_1(
            data["Languages"]
        )
    if data.get("DisplayLanguageCode") is not None:
        import capo_translate.types.display_language_code

        out["display_language_code"] = (
            capo_translate.types.display_language_code.deserialize_aws_json_1_1(
                data["DisplayLanguageCode"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListLanguagesResponse) -> dict:
    out: dict = {}
    if "languages" in value:
        import capo_translate.types.languages_list

        out["Languages"] = capo_translate.types.languages_list.serialize_cbor(
            value["languages"]
        )
    if "display_language_code" in value:
        import capo_translate.types.display_language_code

        out["DisplayLanguageCode"] = (
            capo_translate.types.display_language_code.serialize_cbor(
                value["display_language_code"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListLanguagesResponse:
    out: ListLanguagesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Languages") is not None:
        import capo_translate.types.languages_list

        out["languages"] = capo_translate.types.languages_list.deserialize_cbor(
            data["Languages"]
        )
    if data.get("DisplayLanguageCode") is not None:
        import capo_translate.types.display_language_code

        out["display_language_code"] = (
            capo_translate.types.display_language_code.deserialize_cbor(
                data["DisplayLanguageCode"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
