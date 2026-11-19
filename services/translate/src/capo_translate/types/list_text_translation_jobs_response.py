"""Generated from Smithy shape ``com.amazonaws.translate#ListTextTranslationJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.next_token
    import capo_translate.types.text_translation_job_properties_list


class ListTextTranslationJobsResponse(TypedDict, closed=True):
    text_translation_job_properties_list: NotRequired[
        "capo_translate.types.text_translation_job_properties_list.TextTranslationJobPropertiesList"
    ]
    """<p>A list containing the properties of each job that is returned.</p>"""
    next_token: NotRequired["capo_translate.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTextTranslationJobsResponse) -> dict:
    out: dict = {}
    if "text_translation_job_properties_list" in value:
        import capo_translate.types.text_translation_job_properties_list

        out["TextTranslationJobPropertiesList"] = (
            capo_translate.types.text_translation_job_properties_list.serialize_aws_json_1_1(
                value["text_translation_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTextTranslationJobsResponse:
    out: ListTextTranslationJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("TextTranslationJobPropertiesList") is not None:
        import capo_translate.types.text_translation_job_properties_list

        out["text_translation_job_properties_list"] = (
            capo_translate.types.text_translation_job_properties_list.deserialize_aws_json_1_1(
                data["TextTranslationJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTextTranslationJobsResponse) -> dict:
    out: dict = {}
    if "text_translation_job_properties_list" in value:
        import capo_translate.types.text_translation_job_properties_list

        out["TextTranslationJobPropertiesList"] = (
            capo_translate.types.text_translation_job_properties_list.serialize_cbor(
                value["text_translation_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListTextTranslationJobsResponse:
    out: ListTextTranslationJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("TextTranslationJobPropertiesList") is not None:
        import capo_translate.types.text_translation_job_properties_list

        out["text_translation_job_properties_list"] = (
            capo_translate.types.text_translation_job_properties_list.deserialize_cbor(
                data["TextTranslationJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
