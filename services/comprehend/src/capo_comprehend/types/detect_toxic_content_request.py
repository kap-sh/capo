"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectToxicContentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.language_code
    import capo_comprehend.types.list_of_text_segments


class DetectToxicContentRequest(TypedDict, closed=True):
    text_segments: "capo_comprehend.types.list_of_text_segments.ListOfTextSegments"
    """<p>A list of up to 10 text strings. Each string has a maximum size of 1 KB, and the maximum size of the list is 10 KB.</p>"""
    language_code: "capo_comprehend.types.language_code.LanguageCode"
    """<p>The language of the input text. Currently, English is the only supported language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectToxicContentRequest) -> dict:
    out: dict = {}
    import capo_comprehend.types.list_of_text_segments

    out["TextSegments"] = (
        capo_comprehend.types.list_of_text_segments.serialize_aws_json_1_1(
            value["text_segments"]
        )
    )
    import capo_comprehend.types.language_code

    out["LanguageCode"] = capo_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectToxicContentRequest:
    out: DetectToxicContentRequest = {}  # type: ignore[typeddict-item]
    if data.get("TextSegments") is not None:
        import capo_comprehend.types.list_of_text_segments

        out["text_segments"] = (
            capo_comprehend.types.list_of_text_segments.deserialize_aws_json_1_1(
                data["TextSegments"]
            )
        )
    else:
        out["text_segments"] = []
    if data.get("LanguageCode") is not None:
        import capo_comprehend.types.language_code

        out["language_code"] = (
            capo_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        import typing

        out["language_code"] = typing.cast(
            "capo_comprehend.types.language_code.LanguageCode", ""
        )
    return out


def redact_sensitive(value: DetectToxicContentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text_segments" in value:
        out["text_segments"] = "*** Sensitive Data Redacted ***"
    return out
