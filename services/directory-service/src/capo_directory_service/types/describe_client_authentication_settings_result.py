"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeClientAuthenticationSettingsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.client_authentication_settings_info
    import capo_directory_service.types.next_token


class DescribeClientAuthenticationSettingsResult(TypedDict, closed=True):
    client_authentication_settings_info: NotRequired[
        "capo_directory_service.types.client_authentication_settings_info.ClientAuthenticationSettingsInfo"
    ]
    """<p>Information about the type of client authentication for the specified directory. The following information is retrieved: The date and time when the status of the client authentication type was last updated, whether the client authentication type is enabled or disabled, and the type of client authentication.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>The next token used to retrieve the client authentication settings if the number of setting types exceeds page limit and there is another page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClientAuthenticationSettingsResult) -> dict:
    out: dict = {}
    if "client_authentication_settings_info" in value:
        import capo_directory_service.types.client_authentication_settings_info

        out["ClientAuthenticationSettingsInfo"] = (
            capo_directory_service.types.client_authentication_settings_info.serialize_aws_json_1_1(
                value["client_authentication_settings_info"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClientAuthenticationSettingsResult:
    out: DescribeClientAuthenticationSettingsResult = {}  # type: ignore[typeddict-item]
    if data.get("ClientAuthenticationSettingsInfo") is not None:
        import capo_directory_service.types.client_authentication_settings_info

        out["client_authentication_settings_info"] = (
            capo_directory_service.types.client_authentication_settings_info.deserialize_aws_json_1_1(
                data["ClientAuthenticationSettingsInfo"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeClientAuthenticationSettingsResult) -> dict:
    out: dict = {}
    if "client_authentication_settings_info" in value:
        import capo_directory_service.types.client_authentication_settings_info

        out["ClientAuthenticationSettingsInfo"] = (
            capo_directory_service.types.client_authentication_settings_info.serialize_cbor(
                value["client_authentication_settings_info"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeClientAuthenticationSettingsResult:
    out: DescribeClientAuthenticationSettingsResult = {}  # type: ignore[typeddict-item]
    if data.get("ClientAuthenticationSettingsInfo") is not None:
        import capo_directory_service.types.client_authentication_settings_info

        out["client_authentication_settings_info"] = (
            capo_directory_service.types.client_authentication_settings_info.deserialize_cbor(
                data["ClientAuthenticationSettingsInfo"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
