"""Generated from Smithy shape ``com.amazonaws.notifications#DisassociateOrganizationalUnitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.notification_configuration_arn
    import capo_notifications.types.organizational_unit_id


class DisassociateOrganizationalUnitRequest(TypedDict, closed=True):
    organizational_unit_id: (
        "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
    )
    """<p>The unique identifier of the organizational unit to disassociate.</p>"""
    notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the notification configuration to disassociate from the organizational unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateOrganizationalUnitRequest) -> dict:
    out: dict = {}
    out["notificationConfigurationArn"] = value["notification_configuration_arn"]
    return out


def deserialize_json(data: dict) -> DisassociateOrganizationalUnitRequest:
    out: DisassociateOrganizationalUnitRequest = {}  # type: ignore[typeddict-item]
    if data.get("notificationConfigurationArn") is not None:
        out["notification_configuration_arn"] = data["notificationConfigurationArn"]
    else:
        out["notification_configuration_arn"] = ""
    return out
