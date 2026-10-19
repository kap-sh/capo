"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeClientAuthenticationSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.client_authentication_type
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.next_token
    import capo_directory_service.types.page_limit


class DescribeClientAuthenticationSettingsRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for which to retrieve information.</p>"""
    type: NotRequired[
        "capo_directory_service.types.client_authentication_type.ClientAuthenticationType"
    ]
    """<p>The type of client authentication for which to retrieve information. If no type is specified, a list of all client authentication types that are supported for the specified directory is retrieved.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>The <i>DescribeClientAuthenticationSettingsResult.NextToken</i> value from a previous call to <a>DescribeClientAuthenticationSettings</a>. Pass null if this is the first call.</p>"""
    limit: NotRequired["capo_directory_service.types.page_limit.PageLimit"]
    """<p>The maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClientAuthenticationSettingsRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "type" in value:
        import capo_directory_service.types.client_authentication_type

        out["Type"] = (
            capo_directory_service.types.client_authentication_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClientAuthenticationSettingsRequest:
    out: DescribeClientAuthenticationSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("Type") is not None:
        import capo_directory_service.types.client_authentication_type

        out["type"] = (
            capo_directory_service.types.client_authentication_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
