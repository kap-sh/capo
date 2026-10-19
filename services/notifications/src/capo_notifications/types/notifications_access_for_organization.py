"""Generated from Smithy shape ``com.amazonaws.notifications#NotificationsAccessForOrganization``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.access_status


class NotificationsAccessForOrganization(TypedDict, closed=True):
    access_status: "capo_notifications.types.access_status.AccessStatus"
    """<p>Access Status for the Orgs Service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationsAccessForOrganization) -> dict:
    out: dict = {}
    import capo_notifications.types.access_status

    out["accessStatus"] = capo_notifications.types.access_status.serialize_json(
        value["access_status"]
    )
    return out


def deserialize_json(data: dict) -> NotificationsAccessForOrganization:
    out: NotificationsAccessForOrganization = {}  # type: ignore[typeddict-item]
    if data.get("accessStatus") is not None:
        import capo_notifications.types.access_status

        out["access_status"] = capo_notifications.types.access_status.deserialize_json(
            data["accessStatus"]
        )
    else:
        import typing

        out["access_status"] = typing.cast(
            "capo_notifications.types.access_status.AccessStatus", ""
        )
    return out
