"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeUpdateDirectoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.next_token
    import capo_directory_service.types.region_name
    import capo_directory_service.types.update_type


class DescribeUpdateDirectoryRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p> The unique identifier of the directory. </p>"""
    update_type: "capo_directory_service.types.update_type.UpdateType"
    """<p> The type of updates you want to describe for the directory. </p>"""
    region_name: NotRequired["capo_directory_service.types.region_name.RegionName"]
    """<p> The name of the Region. </p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p> The <code>DescribeUpdateDirectoryResult</code>. NextToken value from a previous call to <a>DescribeUpdateDirectory</a>. Pass null if this is the first call. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUpdateDirectoryRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import capo_directory_service.types.update_type

    out["UpdateType"] = capo_directory_service.types.update_type.serialize_aws_json_1_1(
        value["update_type"]
    )
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUpdateDirectoryRequest:
    out: DescribeUpdateDirectoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("UpdateType") is not None:
        import capo_directory_service.types.update_type

        out["update_type"] = (
            capo_directory_service.types.update_type.deserialize_aws_json_1_1(
                data["UpdateType"]
            )
        )
    else:
        import typing

        out["update_type"] = typing.cast(
            "capo_directory_service.types.update_type.UpdateType", ""
        )
    if data.get("RegionName") is not None:
        out["region_name"] = data["RegionName"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
