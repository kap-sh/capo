"""Generated from Smithy shape ``com.amazonaws.connect#CreatePushNotificationRegistrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.client_token
    import capo_connect.types.contact_configuration
    import capo_connect.types.device_token
    import capo_connect.types.device_type
    import capo_connect.types.instance_id


class CreatePushNotificationRegistrationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    pinpoint_app_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the Pinpoint application.</p>"""
    device_token: "capo_connect.types.device_token.DeviceToken"
    """<p>The push notification token issued by the Apple or Google gateways.</p>"""
    device_type: "capo_connect.types.device_type.DeviceType"
    """<p>The device type to use when sending the message.</p>"""
    contact_configuration: (
        "capo_connect.types.contact_configuration.ContactConfiguration"
    )
    """<p>The contact configuration for push notification registration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePushNotificationRegistrationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["PinpointAppArn"] = value["pinpoint_app_arn"]
    out["DeviceToken"] = value["device_token"]
    import capo_connect.types.device_type

    out["DeviceType"] = capo_connect.types.device_type.serialize_json(
        value["device_type"]
    )
    import capo_connect.types.contact_configuration

    out["ContactConfiguration"] = (
        capo_connect.types.contact_configuration.serialize_json(
            value["contact_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreatePushNotificationRegistrationRequest:
    out: CreatePushNotificationRegistrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("PinpointAppArn") is not None:
        out["pinpoint_app_arn"] = data["PinpointAppArn"]
    else:
        raise DeserializationError(
            "CreatePushNotificationRegistrationRequest.pinpoint_app_arn required"
        )
    if data.get("DeviceToken") is not None:
        out["device_token"] = data["DeviceToken"]
    else:
        raise DeserializationError(
            "CreatePushNotificationRegistrationRequest.device_token required"
        )
    if data.get("DeviceType") is not None:
        import capo_connect.types.device_type

        out["device_type"] = capo_connect.types.device_type.deserialize_json(
            data["DeviceType"]
        )
    else:
        raise DeserializationError(
            "CreatePushNotificationRegistrationRequest.device_type required"
        )
    if data.get("ContactConfiguration") is not None:
        import capo_connect.types.contact_configuration

        out["contact_configuration"] = (
            capo_connect.types.contact_configuration.deserialize_json(
                data["ContactConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePushNotificationRegistrationRequest.contact_configuration required"
        )
    return out
