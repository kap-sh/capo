"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#CreateTrustAnchorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rolesanywhere.types.alias_name
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
    crl_dp_revocation_enabled: NotRequired["bool"]
    """<p>Specifies whether the trust anchor checks certificate revocation status against CRL distribution points.</p>"""
    tags: NotRequired["capo_rolesanywhere.types.tag_list.TagList"]
    """<p>The tags to attach to the trust anchor.</p>"""
    notification_settings: NotRequired[
        "capo_rolesanywhere.types.notification_settings.NotificationSettings"
    ]
    """<p>A list of notification settings to be associated to the trust anchor.</p>"""
    alias_name: NotRequired["capo_rolesanywhere.types.alias_name.AliasName"]
    """<p>An alias for the trust anchor. When you set an alias, the response includes the alias ARN of the trust anchor in <code>aliasArn</code>.</p> <p>An alias name contains 1 to 256 characters. It must begin with a letter (A-Z or a-z). It can contain only letters (A-Z and a-z), numbers (0-9), underscores (_), hyphens (-), and forward slashes (/). A forward slash can appear only between two other characters, so an alias name can't end with a forward slash or contain two in a row. Alias names that begin with <code>aws/</code>, in any combination of uppercase and lowercase letters, are reserved. Alias names are case sensitive.</p> <p>The alias name must be unique among resources of the same type in your account and Region. If another resource of the same type already has the alias, the request fails with a <code>ValidationException</code>. An invalid or reserved alias name also causes a <code>ValidationException</code>.</p> <p>If you omit this parameter or specify an empty string, the resource is created without an alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTrustAnchorRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_rolesanywhere.types.source

    out["source"] = capo_rolesanywhere.types.source.serialize_json(value["source"])
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "crl_dp_revocation_enabled" in value:
        out["crlDpRevocationEnabled"] = value["crl_dp_revocation_enabled"]
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
    if "alias_name" in value:
        out["aliasName"] = value["alias_name"]
    return out


def deserialize_json(data: dict) -> CreateTrustAnchorRequest:
    out: CreateTrustAnchorRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("source") is not None:
        import capo_rolesanywhere.types.source

        out["source"] = capo_rolesanywhere.types.source.deserialize_json(data["source"])
    else:
        raise DeserializationError("CreateTrustAnchorRequest.source required")
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("crlDpRevocationEnabled") is not None:
        out["crl_dp_revocation_enabled"] = data["crlDpRevocationEnabled"]
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
    if data.get("aliasName") is not None:
        out["alias_name"] = data["aliasName"]
    return out


def redact_sensitive(value: CreateTrustAnchorRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.redact_sensitive(value["tags"])
    return out
