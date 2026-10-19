"""Generated from Smithy shape ``com.amazonaws.translate#Language``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_translate.types.language_code_string
    import capo_translate.types.localized_name_string


class Language(TypedDict, closed=True):
    language_name: "capo_translate.types.localized_name_string.LocalizedNameString"
    """<p>Language name of the supported language.</p>"""
    language_code: "capo_translate.types.language_code_string.LanguageCodeString"
    """<p>Language code for the supported language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Language) -> dict:
    out: dict = {}
    out["LanguageName"] = value["language_name"]
    out["LanguageCode"] = value["language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Language:
    out: Language = {}  # type: ignore[typeddict-item]
    if data.get("LanguageName") is not None:
        out["language_name"] = data["LanguageName"]
    else:
        out["language_name"] = ""
    if data.get("LanguageCode") is not None:
        out["language_code"] = data["LanguageCode"]
    else:
        out["language_code"] = ""
    return out
