"""Generated from Smithy shape ``com.amazonaws.connect#DeletePushNotificationRegistrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.registration_id


class DeletePushNotificationRegistrationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    registration_id: "capo_connect.types.registration_id.RegistrationId"
    """<p>The identifier for the registration.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact within the Connect Customer instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePushNotificationRegistrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePushNotificationRegistrationRequest:
    out: DeletePushNotificationRegistrationRequest = {}  # type: ignore[typeddict-item]
    return out
