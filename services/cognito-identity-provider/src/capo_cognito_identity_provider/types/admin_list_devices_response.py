"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminListDevicesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.device_list_type
    import capo_cognito_identity_provider.types.search_pagination_token_type


class AdminListDevicesResponse(TypedDict, closed=True):
    devices: NotRequired[
        "capo_cognito_identity_provider.types.device_list_type.DeviceListType"
    ]
    """<p>An array of devices and their information. Each entry that's returned includes device information, last-accessed and created dates, and the device key.</p>"""
    pagination_token: NotRequired[
        "capo_cognito_identity_provider.types.search_pagination_token_type.SearchPaginationTokenType"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminListDevicesResponse) -> dict:
    out: dict = {}
    if "devices" in value:
        import capo_cognito_identity_provider.types.device_list_type

        out["Devices"] = (
            capo_cognito_identity_provider.types.device_list_type.serialize_aws_json_1_1(
                value["devices"]
            )
        )
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminListDevicesResponse:
    out: AdminListDevicesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Devices") is not None:
        import capo_cognito_identity_provider.types.device_list_type

        out["devices"] = (
            capo_cognito_identity_provider.types.device_list_type.deserialize_aws_json_1_1(
                data["Devices"]
            )
        )
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    return out


def redact_sensitive(value: AdminListDevicesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "devices" in value:
        import capo_cognito_identity_provider.types.device_list_type

        out["devices"] = (
            capo_cognito_identity_provider.types.device_list_type.redact_sensitive(
                value["devices"]
            )
        )
    return out
