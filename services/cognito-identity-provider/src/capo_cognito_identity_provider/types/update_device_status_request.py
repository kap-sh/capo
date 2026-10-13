"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateDeviceStatusRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.device_key_type
    import capo_cognito_identity_provider.types.device_remembered_status_type
    import capo_cognito_identity_provider.types.token_model_type


class UpdateDeviceStatusRequest(TypedDict, closed=True):
    access_token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""
    device_key: "capo_cognito_identity_provider.types.device_key_type.DeviceKeyType"
    """<p>The device key of the device you want to update, for example <code>us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>.</p>"""
    device_remembered_status: NotRequired[
        "capo_cognito_identity_provider.types.device_remembered_status_type.DeviceRememberedStatusType"
    ]
    """<p>To enable device authentication with the specified device, set to <code>remembered</code>.To disable, set to <code>not_remembered</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDeviceStatusRequest) -> dict:
    out: dict = {}
    out["AccessToken"] = value["access_token"]
    out["DeviceKey"] = value["device_key"]
    if "device_remembered_status" in value:
        import capo_cognito_identity_provider.types.device_remembered_status_type

        out["DeviceRememberedStatus"] = (
            capo_cognito_identity_provider.types.device_remembered_status_type.serialize_aws_json_1_1(
                value["device_remembered_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDeviceStatusRequest:
    out: UpdateDeviceStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    else:
        raise DeserializationError("UpdateDeviceStatusRequest.access_token required")
    if data.get("DeviceKey") is not None:
        out["device_key"] = data["DeviceKey"]
    else:
        raise DeserializationError("UpdateDeviceStatusRequest.device_key required")
    if data.get("DeviceRememberedStatus") is not None:
        import capo_cognito_identity_provider.types.device_remembered_status_type

        out["device_remembered_status"] = (
            capo_cognito_identity_provider.types.device_remembered_status_type.deserialize_aws_json_1_1(
                data["DeviceRememberedStatus"]
            )
        )
    return out


def redact_sensitive(value: UpdateDeviceStatusRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
