"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectSentimentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.customer_input_string
    import capo_comprehend.types.language_code


class DetectSentimentRequest(TypedDict, closed=True):
    text: "capo_comprehend.types.customer_input_string.CustomerInputString"
    """<p>A UTF-8 text string. The maximum string size is 5 KB.</p>"""
    language_code: "capo_comprehend.types.language_code.LanguageCode"
    """<p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectSentimentRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    import capo_comprehend.types.language_code

    out["LanguageCode"] = capo_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectSentimentRequest:
    out: DetectSentimentRequest = {}  # type: ignore[typeddict-item]
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


def redact_sensitive(value: DetectSentimentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
