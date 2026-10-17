"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetDataQualityResultV2Response``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.data_quality_result_v2_id_list
    import capo_glue.types.data_quality_result_v2_list


class BatchGetDataQualityResultV2Response(TypedDict, closed=True):
    results: "capo_glue.types.data_quality_result_v2_list.DataQualityResultV2List"
    """<p>A list of <code>DataQualityResultV2Item</code> objects representing the data quality results.</p>"""
    results_not_found: NotRequired[
        "capo_glue.types.data_quality_result_v2_id_list.DataQualityResultV2IdList"
    ]
    """<p>A list of result IDs for which results were not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDataQualityResultV2Response) -> dict:
    out: dict = {}
    import capo_glue.types.data_quality_result_v2_list

    out["Results"] = capo_glue.types.data_quality_result_v2_list.serialize_aws_json_1_1(
        value["results"]
    )
    if "results_not_found" in value:
        import capo_glue.types.data_quality_result_v2_id_list

        out["ResultsNotFound"] = (
            capo_glue.types.data_quality_result_v2_id_list.serialize_aws_json_1_1(
                value["results_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDataQualityResultV2Response:
    out: BatchGetDataQualityResultV2Response = {}  # type: ignore[typeddict-item]
    if data.get("Results") is not None:
        import capo_glue.types.data_quality_result_v2_list

        out["results"] = (
            capo_glue.types.data_quality_result_v2_list.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetDataQualityResultV2Response.results required"
        )
    if data.get("ResultsNotFound") is not None:
        import capo_glue.types.data_quality_result_v2_id_list

        out["results_not_found"] = (
            capo_glue.types.data_quality_result_v2_id_list.deserialize_aws_json_1_1(
                data["ResultsNotFound"]
            )
        )
    return out


def redact_sensitive(value: BatchGetDataQualityResultV2Response) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "results" in value:
        import capo_glue.types.data_quality_result_v2_list

        out["results"] = capo_glue.types.data_quality_result_v2_list.redact_sensitive(
            value["results"]
        )
    return out
