"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#TrustAnchorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rolesanywhere.types.notification_setting_details
    import capo_rolesanywhere.types.resource_name
    import capo_rolesanywhere.types.source
    import capo_rolesanywhere.types.uuid


class TrustAnchorDetail(TypedDict, closed=True):
    trust_anchor_id: NotRequired["capo_rolesanywhere.types.uuid.Uuid"]
    """<p>The unique identifier of the trust anchor.</p>"""
    trust_anchor_arn: NotRequired["str"]
    """<p>The ARN of the trust anchor.</p>"""
    name: NotRequired["capo_rolesanywhere.types.resource_name.ResourceName"]
    """<p>The name of the trust anchor.</p>"""
    source: NotRequired["capo_rolesanywhere.types.source.Source"]
    """<p>The trust anchor type and its related certificate data.</p>"""
    enabled: NotRequired["bool"]
    """<p>Indicates whether the trust anchor is enabled.</p>"""
    crl_dp_revocation_enabled: NotRequired["bool"]
    """<p>Specifies whether the trust anchor checks certificate revocation status against CRL distribution points.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the trust anchor was created. </p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the trust anchor was last updated. </p>"""
    notification_settings: NotRequired[
        "capo_rolesanywhere.types.notification_setting_details.NotificationSettingDetails"
    ]
    """<p>A list of notification settings to be associated to the trust anchor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrustAnchorDetail) -> dict:
    out: dict = {}
    if "trust_anchor_id" in value:
        out["trustAnchorId"] = value["trust_anchor_id"]
    if "trust_anchor_arn" in value:
        out["trustAnchorArn"] = value["trust_anchor_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "source" in value:
        import capo_rolesanywhere.types.source

        out["source"] = capo_rolesanywhere.types.source.serialize_json(value["source"])
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "crl_dp_revocation_enabled" in value:
        out["crlDpRevocationEnabled"] = value["crl_dp_revocation_enabled"]
    if "created_at" in value:
        import capo_rolesanywhere._protocol.serialize

        out["createdAt"] = capo_rolesanywhere._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_rolesanywhere._protocol.serialize

        out["updatedAt"] = capo_rolesanywhere._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    if "notification_settings" in value:
        import capo_rolesanywhere.types.notification_setting_details

        out["notificationSettings"] = (
            capo_rolesanywhere.types.notification_setting_details.serialize_json(
                value["notification_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> TrustAnchorDetail:
    out: TrustAnchorDetail = {}  # type: ignore[typeddict-item]
    if data.get("trustAnchorId") is not None:
        out["trust_anchor_id"] = data["trustAnchorId"]
    if data.get("trustAnchorArn") is not None:
        out["trust_anchor_arn"] = data["trustAnchorArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("source") is not None:
        import capo_rolesanywhere.types.source

        out["source"] = capo_rolesanywhere.types.source.deserialize_json(data["source"])
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("crlDpRevocationEnabled") is not None:
        out["crl_dp_revocation_enabled"] = data["crlDpRevocationEnabled"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("notificationSettings") is not None:
        import capo_rolesanywhere.types.notification_setting_details

        out["notification_settings"] = (
            capo_rolesanywhere.types.notification_setting_details.deserialize_json(
                data["notificationSettings"]
            )
        )
    return out
