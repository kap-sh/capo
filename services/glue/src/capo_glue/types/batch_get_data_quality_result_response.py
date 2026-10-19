"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetDataQualityResultResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_result_ids
    import capo_glue.types.data_quality_results_list


class BatchGetDataQualityResultResponse(TypedDict, closed=True):
    results: "capo_glue.types.data_quality_results_list.DataQualityResultsList"
    """<p>A list of <code>DataQualityResult</code> objects representing the data quality results.</p>"""
    results_not_found: NotRequired[
        "capo_glue.types.data_quality_result_ids.DataQualityResultIds"
    ]
    """<p>A list of result IDs for which results were not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDataQualityResultResponse) -> dict:
    out: dict = {}
    import capo_glue.types.data_quality_results_list

    out["Results"] = capo_glue.types.data_quality_results_list.serialize_aws_json_1_1(
        value["results"]
    )
    if "results_not_found" in value:
        import capo_glue.types.data_quality_result_ids

        out["ResultsNotFound"] = (
            capo_glue.types.data_quality_result_ids.serialize_aws_json_1_1(
                value["results_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDataQualityResultResponse:
    out: BatchGetDataQualityResultResponse = {}  # type: ignore[typeddict-item]
    if data.get("Results") is not None:
        import capo_glue.types.data_quality_results_list

        out["results"] = (
            capo_glue.types.data_quality_results_list.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    else:
        out["results"] = []
    if data.get("ResultsNotFound") is not None:
        import capo_glue.types.data_quality_result_ids

        out["results_not_found"] = (
            capo_glue.types.data_quality_result_ids.deserialize_aws_json_1_1(
                data["ResultsNotFound"]
            )
        )
    return out


def redact_sensitive(value: BatchGetDataQualityResultResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "results" in value:
        import capo_glue.types.data_quality_results_list

        out["results"] = capo_glue.types.data_quality_results_list.redact_sensitive(
            value["results"]
        )
    return out
