"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetDataQualityResultV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.data_quality_result_v2_id_list


class BatchGetDataQualityResultV2Request(TypedDict, closed=True):
    result_ids: (
        "capo_glue.types.data_quality_result_v2_id_list.DataQualityResultV2IdList"
    )
    """<p>A list of unique result IDs for the data quality results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDataQualityResultV2Request) -> dict:
    out: dict = {}
    import capo_glue.types.data_quality_result_v2_id_list

    out["ResultIds"] = (
        capo_glue.types.data_quality_result_v2_id_list.serialize_aws_json_1_1(
            value["result_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDataQualityResultV2Request:
    out: BatchGetDataQualityResultV2Request = {}  # type: ignore[typeddict-item]
    if data.get("ResultIds") is not None:
        import capo_glue.types.data_quality_result_v2_id_list

        out["result_ids"] = (
            capo_glue.types.data_quality_result_v2_id_list.deserialize_aws_json_1_1(
                data["ResultIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetDataQualityResultV2Request.result_ids required"
        )
    return out
