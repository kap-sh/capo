"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#CreateTrustAnchorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rolesanywhere.types.notification_settings
    import capo_rolesanywhere.types.resource_name
    import capo_rolesanywhere.types.source
    import capo_rolesanywhere.types.tag_list


class CreateTrustAnchorRequest(TypedDict, closed=True):
    name: "capo_rolesanywhere.types.resource_name.ResourceName"
    """<p>The name of the trust anchor.</p>"""
    source: "capo_rolesanywhere.types.source.Source"
    """<p>The trust anchor type and its related certificate data.</p>"""
    enabled: NotRequired["bool"]
    """<p>Specifies whether the trust anchor is enabled.</p>"""
    tags: NotRequired["capo_rolesanywhere.types.tag_list.TagList"]
    """<p>The tags to attach to the trust anchor.</p>"""
    notification_settings: NotRequired[
        "capo_rolesanywhere.types.notification_settings.NotificationSettings"
    ]
    """<p>A list of notification settings to be associated to the trust anchor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTrustAnchorRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_rolesanywhere.types.source

    out["source"] = capo_rolesanywhere.types.source.serialize_json(value["source"])
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "tags" in value:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.serialize_json(value["tags"])
    if "notification_settings" in value:
        import capo_rolesanywhere.types.notification_settings

        out["notificationSettings"] = (
            capo_rolesanywhere.types.notification_settings.serialize_json(
                value["notification_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateTrustAnchorRequest:
    out: CreateTrustAnchorRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateTrustAnchorRequest.name required")
    if data.get("source") is not None:
        import capo_rolesanywhere.types.source

        out["source"] = capo_rolesanywhere.types.source.deserialize_json(data["source"])
    else:
        raise DeserializationError("CreateTrustAnchorRequest.source required")
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("tags") is not None:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.deserialize_json(data["tags"])
    if data.get("notificationSettings") is not None:
        import capo_rolesanywhere.types.notification_settings

        out["notification_settings"] = (
            capo_rolesanywhere.types.notification_settings.deserialize_json(
                data["notificationSettings"]
            )
        )
    return out


def redact_sensitive(value: CreateTrustAnchorRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.redact_sensitive(value["tags"])
    return out
