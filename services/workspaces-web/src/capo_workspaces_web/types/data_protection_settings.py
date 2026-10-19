"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DataProtectionSettings``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.arn_list
    import capo_workspaces_web.types.description_safe
    import capo_workspaces_web.types.display_name_safe
    import capo_workspaces_web.types.encryption_context_map
    import capo_workspaces_web.types.inline_redaction_configuration
    import capo_workspaces_web.types.key_arn
    import capo_workspaces_web.types.timestamp


class DataProtectionSettings(TypedDict, closed=True):
    data_protection_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the data protection settings resource.</p>"""
    inline_redaction_configuration: NotRequired[
        "capo_workspaces_web.types.inline_redaction_configuration.InlineRedactionConfiguration"
    ]
    """<p>The inline redaction configuration for the data protection settings.</p>"""
    associated_portal_arns: NotRequired["capo_workspaces_web.types.arn_list.ArnList"]
    """<p>A list of web portal ARNs that this data protection settings resource is associated with.</p>"""
    display_name: NotRequired[
        "capo_workspaces_web.types.display_name_safe.DisplayNameSafe"
    ]
    """<p>The display name of the data protection settings.</p>"""
    description: NotRequired[
        "capo_workspaces_web.types.description_safe.DescriptionSafe"
    ]
    """<p>The description of the data protection settings.</p>"""
    creation_date: NotRequired["capo_workspaces_web.types.timestamp.Timestamp"]
    """<p>The creation date timestamp of the data protection settings.</p>"""
    customer_managed_key: NotRequired["capo_workspaces_web.types.key_arn.keyArn"]
    """<p>The customer managed key used to encrypt sensitive information in the data protection settings.</p>"""
    additional_encryption_context: NotRequired[
        "capo_workspaces_web.types.encryption_context_map.EncryptionContextMap"
    ]
    """<p>The additional encryption context of the data protection settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProtectionSettings) -> dict:
    out: dict = {}
    out["dataProtectionSettingsArn"] = value["data_protection_settings_arn"]
    if "inline_redaction_configuration" in value:
        import capo_workspaces_web.types.inline_redaction_configuration

        out["inlineRedactionConfiguration"] = (
            capo_workspaces_web.types.inline_redaction_configuration.serialize_json(
                value["inline_redaction_configuration"]
            )
        )
    if "associated_portal_arns" in value:
        import capo_workspaces_web.types.arn_list

        out["associatedPortalArns"] = capo_workspaces_web.types.arn_list.serialize_json(
            value["associated_portal_arns"]
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


def deserialize_json(data: dict) -> DataProtectionSettings:
    out: DataProtectionSettings = {}  # type: ignore[typeddict-item]
    if data.get("dataProtectionSettingsArn") is not None:
        out["data_protection_settings_arn"] = data["dataProtectionSettingsArn"]
    else:
        out["data_protection_settings_arn"] = ""
    if data.get("inlineRedactionConfiguration") is not None:
        import capo_workspaces_web.types.inline_redaction_configuration

        out["inline_redaction_configuration"] = (
            capo_workspaces_web.types.inline_redaction_configuration.deserialize_json(
                data["inlineRedactionConfiguration"]
            )
        )
    if data.get("associatedPortalArns") is not None:
        import capo_workspaces_web.types.arn_list

        out["associated_portal_arns"] = (
            capo_workspaces_web.types.arn_list.deserialize_json(
                data["associatedPortalArns"]
            )
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


def redact_sensitive(value: DataProtectionSettings) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inline_redaction_configuration" in value:
        import capo_workspaces_web.types.inline_redaction_configuration

        out["inline_redaction_configuration"] = (
            capo_workspaces_web.types.inline_redaction_configuration.redact_sensitive(
                value["inline_redaction_configuration"]
            )
        )
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
