"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeAppBlockBuilderAppBlockAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn
    import capo_appstream.types.integer
    import capo_appstream.types.name
    import capo_appstream.types.string


class DescribeAppBlockBuilderAppBlockAssociationsRequest(TypedDict, closed=True):
    app_block_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the app block.</p>"""
    app_block_builder_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the app block builder.</p>"""
    max_results: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The maximum size of each page of results.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeAppBlockBuilderAppBlockAssociationsRequest,
) -> dict:
    out: dict = {}
    if "app_block_arn" in value:
        out["AppBlockArn"] = value["app_block_arn"]
    if "app_block_builder_name" in value:
        out["AppBlockBuilderName"] = value["app_block_builder_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeAppBlockBuilderAppBlockAssociationsRequest:
    out: DescribeAppBlockBuilderAppBlockAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AppBlockArn") is not None:
        out["app_block_arn"] = data["AppBlockArn"]
    if data.get("AppBlockBuilderName") is not None:
        out["app_block_builder_name"] = data["AppBlockBuilderName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAppBlockBuilderAppBlockAssociationsRequest) -> dict:
    out: dict = {}
    if "app_block_arn" in value:
        out["AppBlockArn"] = value["app_block_arn"]
    if "app_block_builder_name" in value:
        out["AppBlockBuilderName"] = value["app_block_builder_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeAppBlockBuilderAppBlockAssociationsRequest:
    out: DescribeAppBlockBuilderAppBlockAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AppBlockArn") is not None:
        out["app_block_arn"] = data["AppBlockArn"]
    if data.get("AppBlockBuilderName") is not None:
        out["app_block_builder_name"] = data["AppBlockBuilderName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
