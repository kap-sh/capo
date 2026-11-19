"""Generated from Smithy shape ``com.amazonaws.translate#DescribeTextTranslationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.text_translation_job_properties


class DescribeTextTranslationJobResponse(TypedDict, closed=True):
    text_translation_job_properties: NotRequired[
        "capo_translate.types.text_translation_job_properties.TextTranslationJobProperties"
    ]
    """<p>An object that contains the properties associated with an asynchronous batch translation job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTextTranslationJobResponse) -> dict:
    out: dict = {}
    if "text_translation_job_properties" in value:
        import capo_translate.types.text_translation_job_properties

        out["TextTranslationJobProperties"] = (
            capo_translate.types.text_translation_job_properties.serialize_aws_json_1_1(
                value["text_translation_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTextTranslationJobResponse:
    out: DescribeTextTranslationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("TextTranslationJobProperties") is not None:
        import capo_translate.types.text_translation_job_properties

        out["text_translation_job_properties"] = (
            capo_translate.types.text_translation_job_properties.deserialize_aws_json_1_1(
                data["TextTranslationJobProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeTextTranslationJobResponse) -> dict:
    out: dict = {}
    if "text_translation_job_properties" in value:
        import capo_translate.types.text_translation_job_properties

        out["TextTranslationJobProperties"] = (
            capo_translate.types.text_translation_job_properties.serialize_cbor(
                value["text_translation_job_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeTextTranslationJobResponse:
    out: DescribeTextTranslationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("TextTranslationJobProperties") is not None:
        import capo_translate.types.text_translation_job_properties

        out["text_translation_job_properties"] = (
            capo_translate.types.text_translation_job_properties.deserialize_cbor(
                data["TextTranslationJobProperties"]
            )
        )
    return out
