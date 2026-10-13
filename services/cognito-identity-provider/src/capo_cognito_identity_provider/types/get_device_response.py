"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetDeviceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.device_type


class GetDeviceResponse(TypedDict, closed=True):
    device: "capo_cognito_identity_provider.types.device_type.DeviceType"
    """<p>Details of the requested device. Includes device information, last-accessed and created dates, and the device key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeviceResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.device_type

    out["Device"] = (
        capo_cognito_identity_provider.types.device_type.serialize_aws_json_1_1(
            value["device"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeviceResponse:
    out: GetDeviceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Device") is not None:
        import capo_cognito_identity_provider.types.device_type

        out["device"] = (
            capo_cognito_identity_provider.types.device_type.deserialize_aws_json_1_1(
                data["Device"]
            )
        )
    else:
        raise DeserializationError("GetDeviceResponse.device required")
    return out


def redact_sensitive(value: GetDeviceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "device" in value:
        import capo_cognito_identity_provider.types.device_type

        out["device"] = (
            capo_cognito_identity_provider.types.device_type.redact_sensitive(
                value["device"]
            )
        )
    return out
