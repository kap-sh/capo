"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ForgetDeviceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.device_key_type
    import capo_cognito_identity_provider.types.token_model_type


class ForgetDeviceRequest(TypedDict, closed=True):
    access_token: NotRequired[
        "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    ]
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""
    device_key: "capo_cognito_identity_provider.types.device_key_type.DeviceKeyType"
    """<p>The unique identifier, or device key, of the device that the user wants to forget.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForgetDeviceRequest) -> dict:
    out: dict = {}
    if "access_token" in value:
        out["AccessToken"] = value["access_token"]
    out["DeviceKey"] = value["device_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ForgetDeviceRequest:
    out: ForgetDeviceRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    if data.get("DeviceKey") is not None:
        out["device_key"] = data["DeviceKey"]
    else:
        out["device_key"] = ""
    return out


def redact_sensitive(value: ForgetDeviceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
