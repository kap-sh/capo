"""Generated from Smithy shape ``com.amazonaws.healthlake#ListDataTransformationProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_next_token
    import capo_healthlake.types.data_transformation_profile_summary_list


class ListDataTransformationProfilesResponse(TypedDict, closed=True):
    items: "capo_healthlake.types.data_transformation_profile_summary_list.DataTransformationProfileSummaryList"
    """<p>The list of data transformation profile summaries.</p>"""
    next_token: NotRequired[
        "capo_healthlake.types.data_transformation_next_token.DataTransformationNextToken"
    ]
    """<p>The pagination token to use in the next request. If this value is <code>null</code>, there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDataTransformationProfilesResponse) -> dict:
    out: dict = {}
    import capo_healthlake.types.data_transformation_profile_summary_list

    out["Items"] = (
        capo_healthlake.types.data_transformation_profile_summary_list.serialize_aws_json_1_0(
            value["items"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDataTransformationProfilesResponse:
    out: ListDataTransformationProfilesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_healthlake.types.data_transformation_profile_summary_list

        out["items"] = (
            capo_healthlake.types.data_transformation_profile_summary_list.deserialize_aws_json_1_0(
                data["Items"]
            )
        )
    else:
        out["items"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
