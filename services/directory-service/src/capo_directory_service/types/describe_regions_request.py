"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeRegionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.next_token
    import capo_directory_service.types.region_name


class DescribeRegionsRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    region_name: NotRequired["capo_directory_service.types.region_name.RegionName"]
    """<p>The name of the Region. For example, <code>us-east-1</code>.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>The <code>DescribeRegionsResult.NextToken</code> value from a previous call to <a>DescribeRegions</a>. Pass null if this is the first call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRegionsRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRegionsRequest:
    out: DescribeRegionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("RegionName") is not None:
        out["region_name"] = data["RegionName"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
