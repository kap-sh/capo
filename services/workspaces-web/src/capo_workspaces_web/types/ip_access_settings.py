"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IpAccessSettings``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.arn_list
    import capo_workspaces_web.types.description
    import capo_workspaces_web.types.display_name
    import capo_workspaces_web.types.encryption_context_map
    import capo_workspaces_web.types.ip_rule_list
    import capo_workspaces_web.types.key_arn
    import capo_workspaces_web.types.timestamp


class IpAccessSettings(TypedDict, closed=True):
    ip_access_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the IP access settings resource.</p>"""
    associated_portal_arns: NotRequired["capo_workspaces_web.types.arn_list.ArnList"]
    """<p>A list of web portal ARNs that this IP access settings resource is associated with.</p>"""
    ip_rules: NotRequired["capo_workspaces_web.types.ip_rule_list.IpRuleList"]
    """<p>The IP rules of the IP access settings.</p>"""
    display_name: NotRequired["capo_workspaces_web.types.display_name.DisplayName"]
    """<p> The display name of the IP access settings.</p>"""
    description: NotRequired["capo_workspaces_web.types.description.Description"]
    """<p>The description of the IP access settings.</p>"""
    creation_date: NotRequired["capo_workspaces_web.types.timestamp.Timestamp"]
    """<p>The creation date timestamp of the IP access settings.</p>"""
    customer_managed_key: NotRequired["capo_workspaces_web.types.key_arn.keyArn"]
    """<p>The customer managed key used to encrypt sensitive information in the IP access settings.</p>"""
    additional_encryption_context: NotRequired[
        "capo_workspaces_web.types.encryption_context_map.EncryptionContextMap"
    ]
    """<p>The additional encryption context of the IP access settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpAccessSettings) -> dict:
    out: dict = {}
    out["ipAccessSettingsArn"] = value["ip_access_settings_arn"]
    if "associated_portal_arns" in value:
        import capo_workspaces_web.types.arn_list

        out["associatedPortalArns"] = capo_workspaces_web.types.arn_list.serialize_json(
            value["associated_portal_arns"]
        )
    if "ip_rules" in value:
        import capo_workspaces_web.types.ip_rule_list

        out["ipRules"] = capo_workspaces_web.types.ip_rule_list.serialize_json(
            value["ip_rules"]
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "creation_date" in value:
        import capo_workspaces_web.types.timestamp

        out["creationDate"] = capo_workspaces_web.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "customer_managed_key" in value:
        out["customerManagedKey"] = value["customer_managed_key"]
    if "additional_encryption_context" in value:
        import capo_workspaces_web.types.encryption_context_map

        out["additionalEncryptionContext"] = (
            capo_workspaces_web.types.encryption_context_map.serialize_json(
                value["additional_encryption_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> IpAccessSettings:
    out: IpAccessSettings = {}  # type: ignore[typeddict-item]
    if data.get("ipAccessSettingsArn") is not None:
        out["ip_access_settings_arn"] = data["ipAccessSettingsArn"]
    else:
        out["ip_access_settings_arn"] = ""
    if data.get("associatedPortalArns") is not None:
        import capo_workspaces_web.types.arn_list

        out["associated_portal_arns"] = (
            capo_workspaces_web.types.arn_list.deserialize_json(
                data["associatedPortalArns"]
            )
        )
    if data.get("ipRules") is not None:
        import capo_workspaces_web.types.ip_rule_list

        out["ip_rules"] = capo_workspaces_web.types.ip_rule_list.deserialize_json(
            data["ipRules"]
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("creationDate") is not None:
        import capo_workspaces_web.types.timestamp

        out["creation_date"] = capo_workspaces_web.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    if data.get("customerManagedKey") is not None:
        out["customer_managed_key"] = data["customerManagedKey"]
    if data.get("additionalEncryptionContext") is not None:
        import capo_workspaces_web.types.encryption_context_map

        out["additional_encryption_context"] = (
            capo_workspaces_web.types.encryption_context_map.deserialize_json(
                data["additionalEncryptionContext"]
            )
        )
    return out


def redact_sensitive(value: IpAccessSettings) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ip_rules" in value:
        out["ip_rules"] = "*** Sensitive Data Redacted ***"
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
