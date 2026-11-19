"""Generated from Smithy shape ``com.amazonaws.translate#ListTextTranslationJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.max_results_integer
    import capo_translate.types.next_token
    import capo_translate.types.text_translation_job_filter


class ListTextTranslationJobsRequest(TypedDict, closed=True):
    filter: NotRequired[
        "capo_translate.types.text_translation_job_filter.TextTranslationJobFilter"
    ]
    """<p>The parameters that specify which batch translation jobs to retrieve. Filters include job name, job status, and submission time. You can only set one filter at a time.</p>"""
    next_token: NotRequired["capo_translate.types.next_token.NextToken"]
    """<p>The token to request the next page of results.</p>"""
    max_results: NotRequired[
        "capo_translate.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>The maximum number of results to return in each page. The default value is 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTextTranslationJobsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_translate.types.text_translation_job_filter

        out["Filter"] = (
            capo_translate.types.text_translation_job_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTextTranslationJobsRequest:
    out: ListTextTranslationJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filter") is not None:
        import capo_translate.types.text_translation_job_filter

        out["filter"] = (
            capo_translate.types.text_translation_job_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTextTranslationJobsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_translate.types.text_translation_job_filter

        out["Filter"] = capo_translate.types.text_translation_job_filter.serialize_cbor(
            value["filter"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListTextTranslationJobsRequest:
    out: ListTextTranslationJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filter") is not None:
        import capo_translate.types.text_translation_job_filter

        out["filter"] = (
            capo_translate.types.text_translation_job_filter.deserialize_cbor(
                data["Filter"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
