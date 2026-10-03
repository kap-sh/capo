"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectSyntaxRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.customer_input_string_list
    import capo_comprehend.types.syntax_language_code


class BatchDetectSyntaxRequest(TypedDict, closed=True):
    text_list: (
        "capo_comprehend.types.customer_input_string_list.CustomerInputStringList"
    )
    """<p>A list containing the UTF-8 encoded text of the input documents. The list can contain a maximum of 25 documents. The maximum size for each document is 5 KB.</p>"""
    language_code: "capo_comprehend.types.syntax_language_code.SyntaxLanguageCode"
    """<p>The language of the input documents. You can specify any of the following languages supported by Amazon Comprehend: German ("de"), English ("en"), Spanish ("es"), French ("fr"), Italian ("it"), or Portuguese ("pt"). All documents must be in the same language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectSyntaxRequest) -> dict:
    out: dict = {}
    import capo_comprehend.types.customer_input_string_list

    out["TextList"] = (
        capo_comprehend.types.customer_input_string_list.serialize_aws_json_1_1(
            value["text_list"]
        )
    )
    import capo_comprehend.types.syntax_language_code

    out["LanguageCode"] = (
        capo_comprehend.types.syntax_language_code.serialize_aws_json_1_1(
            value["language_code"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectSyntaxRequest:
    out: BatchDetectSyntaxRequest = {}  # type: ignore[typeddict-item]
    if data.get("TextList") is not None:
        import capo_comprehend.types.customer_input_string_list

        out["text_list"] = (
            capo_comprehend.types.customer_input_string_list.deserialize_aws_json_1_1(
                data["TextList"]
            )
        )
    else:
        raise DeserializationError("BatchDetectSyntaxRequest.text_list required")
    if data.get("LanguageCode") is not None:
        import capo_comprehend.types.syntax_language_code

        out["language_code"] = (
            capo_comprehend.types.syntax_language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("BatchDetectSyntaxRequest.language_code required")
    return out
