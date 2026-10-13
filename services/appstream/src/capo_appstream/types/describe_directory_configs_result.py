"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeDirectoryConfigsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.directory_config_list
    import capo_appstream.types.string


class DescribeDirectoryConfigsResult(TypedDict, closed=True):
    directory_configs: NotRequired[
        "capo_appstream.types.directory_config_list.DirectoryConfigList"
    ]
    """<p>Information about the directory configurations. Note that although the response syntax in this topic includes the account password, this password is not returned in the actual response. </p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDirectoryConfigsResult) -> dict:
    out: dict = {}
    if "directory_configs" in value:
        import capo_appstream.types.directory_config_list

        out["DirectoryConfigs"] = (
            capo_appstream.types.directory_config_list.serialize_aws_json_1_1(
                value["directory_configs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDirectoryConfigsResult:
    out: DescribeDirectoryConfigsResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryConfigs") is not None:
        import capo_appstream.types.directory_config_list

        out["directory_configs"] = (
            capo_appstream.types.directory_config_list.deserialize_aws_json_1_1(
                data["DirectoryConfigs"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeDirectoryConfigsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "directory_configs" in value:
        import capo_appstream.types.directory_config_list

        out["directory_configs"] = (
            capo_appstream.types.directory_config_list.redact_sensitive(
                value["directory_configs"]
            )
        )
    return out
