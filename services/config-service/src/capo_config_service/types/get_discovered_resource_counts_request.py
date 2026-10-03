"""Generated from Smithy shape ``com.amazonaws.configservice#GetDiscoveredResourceCountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.limit
    import capo_config_service.types.next_token
    import capo_config_service.types.resource_types


class GetDiscoveredResourceCountsRequest(TypedDict, closed=True):
    resource_types: NotRequired[
        "capo_config_service.types.resource_types.ResourceTypes"
    ]
    """<p>The comma-separated list that specifies the resource types that you want Config to return (for example, <code>"AWS::EC2::Instance"</code>, <code>"AWS::IAM::User"</code>).</p> <p>If a value for <code>resourceTypes</code> is not specified, Config returns all resource types that Config is recording in the region for your account.</p> <note> <p>If the configuration recorder is turned off, Config returns an empty list of <a>ResourceCount</a> objects. If the configuration recorder is not recording a specific resource type (for example, S3 buckets), that resource type is not returned in the list of <a>ResourceCount</a> objects.</p> </note>"""
    limit: "capo_config_service.types.limit.Limit"
    """<p>The maximum number of <a>ResourceCount</a> objects returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDiscoveredResourceCountsRequest) -> dict:
    out: dict = {}
    if "resource_types" in value:
        import capo_config_service.types.resource_types

        out["resourceTypes"] = (
            capo_config_service.types.resource_types.serialize_aws_json_1_1(
                value["resource_types"]
            )
        )
    out["limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDiscoveredResourceCountsRequest:
    out: GetDiscoveredResourceCountsRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceTypes") is not None:
        import capo_config_service.types.resource_types

        out["resource_types"] = (
            capo_config_service.types.resource_types.deserialize_aws_json_1_1(
                data["resourceTypes"]
            )
        )
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 0
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
