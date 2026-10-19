"""Generated from Smithy shape ``com.amazonaws.connect#WebNotificationContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.content_attributes
    import capo_connect.types.notification_type
    import capo_connect.types.view_arn


class WebNotificationContent(TypedDict, closed=True):
    type: "capo_connect.types.notification_type.NotificationType"
    """<p>The type of web notification to send.</p>"""
    view_arn: NotRequired["capo_connect.types.view_arn.ViewArn"]
    """<p>The Amazon Resource Name (ARN) of the view to render for the notification.</p>"""
    attributes: NotRequired["capo_connect.types.content_attributes.ContentAttributes"]
    """<p>Optional attributes used to populate the notification content, such as recommender configuration for personalized content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebNotificationContent) -> dict:
    out: dict = {}
    import capo_connect.types.notification_type

    out["Type"] = capo_connect.types.notification_type.serialize_json(value["type"])
    if "view_arn" in value:
        out["ViewArn"] = value["view_arn"]
    if "attributes" in value:
        import capo_connect.types.content_attributes

        out["Attributes"] = capo_connect.types.content_attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> WebNotificationContent:
    out: WebNotificationContent = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_connect.types.notification_type

        out["type"] = capo_connect.types.notification_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_connect.types.notification_type.NotificationType", ""
        )
    if data.get("ViewArn") is not None:
        out["view_arn"] = data["ViewArn"]
    if data.get("Attributes") is not None:
        import capo_connect.types.content_attributes

        out["attributes"] = capo_connect.types.content_attributes.deserialize_json(
            data["Attributes"]
        )
    return out
