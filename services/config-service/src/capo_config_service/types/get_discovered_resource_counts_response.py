"""Generated from Smithy shape ``com.amazonaws.configservice#GetDiscoveredResourceCountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.long
    import capo_config_service.types.next_token
    import capo_config_service.types.resource_counts


class GetDiscoveredResourceCountsResponse(TypedDict, closed=True):
    total_discovered_resources: "capo_config_service.types.long.Long"
    """<p>The total number of resources that Config is recording in the region for your account. If you specify resource types in the request, Config returns only the total number of resources for those resource types.</p> <p class="title"> <b>Example</b> </p> <ol> <li> <p>Config is recording three resource types in the US East (Ohio) Region for your account: 25 EC2 instances, 20 IAM users, and 15 S3 buckets, for a total of 60 resources.</p> </li> <li> <p>You make a call to the <code>GetDiscoveredResourceCounts</code> action and specify the resource type, <code>"AWS::EC2::Instances"</code>, in the request.</p> </li> <li> <p>Config returns 25 for <code>totalDiscoveredResources</code>.</p> </li> </ol>"""
    resource_counts: NotRequired[
        "capo_config_service.types.resource_counts.ResourceCounts"
    ]
    """<p>The list of <code>ResourceCount</code> objects. Each object is listed in descending order by the number of resources.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The string that you use in a subsequent request to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDiscoveredResourceCountsResponse) -> dict:
    out: dict = {}
    out["totalDiscoveredResources"] = value.get("total_discovered_resources", 0)
    if "resource_counts" in value:
        import capo_config_service.types.resource_counts

        out["resourceCounts"] = (
            capo_config_service.types.resource_counts.serialize_aws_json_1_1(
                value["resource_counts"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDiscoveredResourceCountsResponse:
    out: GetDiscoveredResourceCountsResponse = {}  # type: ignore[typeddict-item]
    if data.get("totalDiscoveredResources") is not None:
        out["total_discovered_resources"] = data["totalDiscoveredResources"]
    else:
        out["total_discovered_resources"] = 0
    if data.get("resourceCounts") is not None:
        import capo_config_service.types.resource_counts

        out["resource_counts"] = (
            capo_config_service.types.resource_counts.deserialize_aws_json_1_1(
                data["resourceCounts"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
