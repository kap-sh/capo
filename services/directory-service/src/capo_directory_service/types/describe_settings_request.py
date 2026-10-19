"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_configuration_status
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.next_token


class DescribeSettingsRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for which to retrieve information.</p>"""
    status: NotRequired[
        "capo_directory_service.types.directory_configuration_status.DirectoryConfigurationStatus"
    ]
    """<p>The status of the directory settings for which to retrieve information.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>The <code>DescribeSettingsResult.NextToken</code> value from a previous call to <a>DescribeSettings</a>. Pass null if this is the first call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSettingsRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "status" in value:
        import capo_directory_service.types.directory_configuration_status

        out["Status"] = (
            capo_directory_service.types.directory_configuration_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSettingsRequest:
    out: DescribeSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("Status") is not None:
        import capo_directory_service.types.directory_configuration_status

        out["status"] = (
            capo_directory_service.types.directory_configuration_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
