"""Generated from Smithy shape ``com.amazonaws.rekognition#DescribeProjectVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.extended_pagination_token
    import capo_rekognition.types.project_arn
    import capo_rekognition.types.project_versions_page_size
    import capo_rekognition.types.version_names


class DescribeProjectVersionsRequest(TypedDict, closed=True):
    project_arn: "capo_rekognition.types.project_arn.ProjectArn"
    """<p>The Amazon Resource Name (ARN) of the project that contains the model/adapter you want to describe.</p>"""
    version_names: NotRequired["capo_rekognition.types.version_names.VersionNames"]
    """<p>A list of model or project version names that you want to describe. You can add up to 10 model or project version names to the list. If you don't specify a value, all project version descriptions are returned. A version name is part of a project version ARN. For example, <code>my-model.2020-01-21T09.10.15</code> is the version name in the following ARN. <code>arn:aws:rekognition:us-east-1:123456789012:project/getting-started/version/<i>my-model.2020-01-21T09.10.15</i>/1234567890123</code>.</p>"""
    next_token: NotRequired[
        "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>"""
    max_results: NotRequired[
        "capo_rekognition.types.project_versions_page_size.ProjectVersionsPageSize"
    ]
    """<p>The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProjectVersionsRequest) -> dict:
    out: dict = {}
    out["ProjectArn"] = value["project_arn"]
    if "version_names" in value:
        import capo_rekognition.types.version_names

        out["VersionNames"] = (
            capo_rekognition.types.version_names.serialize_aws_json_1_1(
                value["version_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProjectVersionsRequest:
    out: DescribeProjectVersionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProjectArn") is not None:
        out["project_arn"] = data["ProjectArn"]
    else:
        out["project_arn"] = ""
    if data.get("VersionNames") is not None:
        import capo_rekognition.types.version_names

        out["version_names"] = (
            capo_rekognition.types.version_names.deserialize_aws_json_1_1(
                data["VersionNames"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
