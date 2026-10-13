"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectEntitiesRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.customer_input_string_list
    import capo_comprehend.types.language_code


class BatchDetectEntitiesRequest(TypedDict, closed=True):
    text_list: (
        "capo_comprehend.types.customer_input_string_list.CustomerInputStringList"
    )
    """<p>A list containing the UTF-8 encoded text of the input documents. The list can contain a maximum of 25 documents. The maximum size of each document is 5 KB.</p>"""
    language_code: "capo_comprehend.types.language_code.LanguageCode"
    """<p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectEntitiesRequest) -> dict:
    out: dict = {}
    import capo_comprehend.types.customer_input_string_list

    out["TextList"] = (
        capo_comprehend.types.customer_input_string_list.serialize_aws_json_1_1(
            value["text_list"]
        )
    )
    import capo_comprehend.types.language_code

    out["LanguageCode"] = capo_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectEntitiesRequest:
    out: BatchDetectEntitiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("TextList") is not None:
        import capo_comprehend.types.customer_input_string_list

        out["text_list"] = (
            capo_comprehend.types.customer_input_string_list.deserialize_aws_json_1_1(
                data["TextList"]
            )
        )
    else:
        raise DeserializationError("BatchDetectEntitiesRequest.text_list required")
    if data.get("LanguageCode") is not None:
        import capo_comprehend.types.language_code

        out["language_code"] = (
            capo_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("BatchDetectEntitiesRequest.language_code required")
    return out


def redact_sensitive(value: BatchDetectEntitiesRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text_list" in value:
        out["text_list"] = "*** Sensitive Data Redacted ***"
    return out
