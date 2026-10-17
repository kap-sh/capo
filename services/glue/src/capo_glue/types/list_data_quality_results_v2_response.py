"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityResultsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.data_quality_results_v2_description_list
    import capo_glue.types.pagination_token


class ListDataQualityResultsV2Response(TypedDict, closed=True):
    results: "capo_glue.types.data_quality_results_v2_description_list.DataQualityResultsV2DescriptionList"
    """<p>A list of <code>DataQualityResultsV2Description</code> objects.</p>"""
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token, if more results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityResultsV2Response) -> dict:
    out: dict = {}
    import capo_glue.types.data_quality_results_v2_description_list

    out["Results"] = (
        capo_glue.types.data_quality_results_v2_description_list.serialize_aws_json_1_1(
            value["results"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityResultsV2Response:
    out: ListDataQualityResultsV2Response = {}  # type: ignore[typeddict-item]
    if data.get("Results") is not None:
        import capo_glue.types.data_quality_results_v2_description_list

        out["results"] = (
            capo_glue.types.data_quality_results_v2_description_list.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    else:
        raise DeserializationError("ListDataQualityResultsV2Response.results required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
