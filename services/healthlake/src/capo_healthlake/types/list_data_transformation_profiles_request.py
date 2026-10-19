"""Generated from Smithy shape ``com.amazonaws.healthlake#ListDataTransformationProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_next_token
    import capo_healthlake.types.max_results
    import capo_healthlake.types.source_format


class ListDataTransformationProfilesRequest(TypedDict, closed=True):
    source_format: "capo_healthlake.types.source_format.SourceFormat"
    """<p>Filters the results by source data format.</p>"""
    max_results: NotRequired["capo_healthlake.types.max_results.MaxResults"]
    """<p>The maximum number of profiles to return per page. If you don't specify a value, the service returns up to 100 results.</p>"""
    next_token: NotRequired[
        "capo_healthlake.types.data_transformation_next_token.DataTransformationNextToken"
    ]
    """<p>The pagination token from a previous response. Pass this value to retrieve the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDataTransformationProfilesRequest) -> dict:
    out: dict = {}
    import capo_healthlake.types.source_format

    out["SourceFormat"] = capo_healthlake.types.source_format.serialize_aws_json_1_0(
        value["source_format"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDataTransformationProfilesRequest:
    out: ListDataTransformationProfilesRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceFormat") is not None:
        import capo_healthlake.types.source_format

        out["source_format"] = (
            capo_healthlake.types.source_format.deserialize_aws_json_1_0(
                data["SourceFormat"]
            )
        )
    else:
        import typing

        out["source_format"] = typing.cast(
            "capo_healthlake.types.source_format.SourceFormat", ""
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
