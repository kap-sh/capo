"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectTargetedSentimentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.customer_input_string
    import capo_comprehend.types.language_code


class DetectTargetedSentimentRequest(TypedDict, closed=True):
    text: "capo_comprehend.types.customer_input_string.CustomerInputString"
    """<p>A UTF-8 text string. The maximum string length is 5 KB.</p>"""
    language_code: "capo_comprehend.types.language_code.LanguageCode"
    """<p>The language of the input documents. Currently, English is the only supported language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectTargetedSentimentRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    import capo_comprehend.types.language_code

    out["LanguageCode"] = capo_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectTargetedSentimentRequest:
    out: DetectTargetedSentimentRequest = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        out["text"] = ""
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


def redact_sensitive(value: DetectTargetedSentimentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
