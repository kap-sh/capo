"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#TrustAnchorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rolesanywhere.types.alias_name
    import capo_rolesanywhere.types.notification_setting_details
    import capo_rolesanywhere.types.resource_name
    import capo_rolesanywhere.types.source
    import capo_rolesanywhere.types.trust_anchor_alias_arn
    import capo_rolesanywhere.types.trust_anchor_resource_arn
    import capo_rolesanywhere.types.uuid


class TrustAnchorDetail(TypedDict, closed=True):
    trust_anchor_id: NotRequired["capo_rolesanywhere.types.uuid.Uuid"]
    """<p>The unique identifier of the trust anchor.</p>"""
    trust_anchor_arn: NotRequired[
        "capo_rolesanywhere.types.trust_anchor_resource_arn.TrustAnchorResourceArn"
    ]
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
    alias_name: NotRequired["capo_rolesanywhere.types.alias_name.AliasName"]
    """<p>The alias of the trust anchor. Present only if the trust anchor has an alias.</p>"""
    alias_arn: NotRequired[
        "capo_rolesanywhere.types.trust_anchor_alias_arn.TrustAnchorAliasArn"
    ]
    """<p>The alias ARN of the trust anchor, in the form <code>arn:<i>partition</i>:rolesanywhere:<i>region</i>:<i>account</i>:alias/trust-anchor/<i>alias-name</i> </code>. Present only if the trust anchor has an alias.</p> <p>You can use the alias ARN in place of the resource ID or ARN in the request parameters whose descriptions say that they accept an alias ARN. Don't use the alias ARN in Identity and Access Management (IAM) policies. A policy statement that names an alias ARN doesn't apply to the resource that holds the alias. Write policies with the ARN that contains the resource ID instead.</p>"""
    previous_alias_name: NotRequired["capo_rolesanywhere.types.alias_name.AliasName"]
    """<p>The alias that the resource had before the update request. IAM Roles Anywhere returns this value only in the response to an update request that changed or removed an existing alias. It isn't returned when the alias was unchanged, when the resource had no alias before the request, or by other operations.</p>"""


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
    if "alias_name" in value:
        out["aliasName"] = value["alias_name"]
    if "alias_arn" in value:
        out["aliasArn"] = value["alias_arn"]
    if "previous_alias_name" in value:
        out["previousAliasName"] = value["previous_alias_name"]
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
    if data.get("aliasName") is not None:
        out["alias_name"] = data["aliasName"]
    if data.get("aliasArn") is not None:
        out["alias_arn"] = data["aliasArn"]
    if data.get("previousAliasName") is not None:
        out["previous_alias_name"] = data["previousAliasName"]
    return out
