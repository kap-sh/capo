"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.notification_resource_type


class NotificationResource(TypedDict, closed=True):
    type: "capo_datazone.types.notification_resource_type.NotificationResourceType"
    """<p>The type of the resource mentioned in a notification.</p>"""
    id: "str"
    """<p>The ID of the resource mentioned in a notification.</p>"""
    name: NotRequired["str"]
    """<p>The name of the resource mentioned in a notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationResource) -> dict:
    out: dict = {}
    import capo_datazone.types.notification_resource_type

    out["type"] = capo_datazone.types.notification_resource_type.serialize_json(
        value["type"]
    )
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> NotificationResource:
    out: NotificationResource = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_datazone.types.notification_resource_type

        out["type"] = capo_datazone.types.notification_resource_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_datazone.types.notification_resource_type.NotificationResourceType",
            "",
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
