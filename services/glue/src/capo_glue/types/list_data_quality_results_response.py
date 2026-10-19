"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_result_description_list
    import capo_glue.types.pagination_token


class ListDataQualityResultsResponse(TypedDict, closed=True):
    results: "capo_glue.types.data_quality_result_description_list.DataQualityResultDescriptionList"
    """<p>A list of <code>DataQualityResultDescription</code> objects.</p>"""
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token, if more results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityResultsResponse) -> dict:
    out: dict = {}
    import capo_glue.types.data_quality_result_description_list

    out["Results"] = (
        capo_glue.types.data_quality_result_description_list.serialize_aws_json_1_1(
            value["results"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityResultsResponse:
    out: ListDataQualityResultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Results") is not None:
        import capo_glue.types.data_quality_result_description_list

        out["results"] = (
            capo_glue.types.data_quality_result_description_list.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    else:
        out["results"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
