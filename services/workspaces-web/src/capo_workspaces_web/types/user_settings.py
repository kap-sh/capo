"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UserSettings``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.arn_list
    import capo_workspaces_web.types.branding_configuration
    import capo_workspaces_web.types.cookie_synchronization_configuration
    import capo_workspaces_web.types.disconnect_timeout_in_minutes
    import capo_workspaces_web.types.enabled_type
    import capo_workspaces_web.types.encryption_context_map
    import capo_workspaces_web.types.idle_disconnect_timeout_in_minutes
    import capo_workspaces_web.types.key_arn
    import capo_workspaces_web.types.toolbar_configuration


class UserSettings(TypedDict, closed=True):
    user_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user settings.</p>"""
    associated_portal_arns: NotRequired["capo_workspaces_web.types.arn_list.ArnList"]
    """<p>A list of web portal ARNs that this user settings is associated with.</p>"""
    copy_allowed: NotRequired["capo_workspaces_web.types.enabled_type.EnabledType"]
    """<p>Specifies whether the user can copy text from the streaming session to the local device.</p>"""
    paste_allowed: NotRequired["capo_workspaces_web.types.enabled_type.EnabledType"]
    """<p>Specifies whether the user can paste text from the local device to the streaming session.</p>"""
    download_allowed: NotRequired["capo_workspaces_web.types.enabled_type.EnabledType"]
    """<p>Specifies whether the user can download files from the streaming session to the local device.</p>"""
    upload_allowed: NotRequired["capo_workspaces_web.types.enabled_type.EnabledType"]
    """<p>Specifies whether the user can upload files from the local device to the streaming session.</p>"""
    print_allowed: NotRequired["capo_workspaces_web.types.enabled_type.EnabledType"]
    """<p>Specifies whether the user can print to the local device.</p>"""
    disconnect_timeout_in_minutes: NotRequired[
        "capo_workspaces_web.types.disconnect_timeout_in_minutes.DisconnectTimeoutInMinutes"
    ]
    """<p>The amount of time that a streaming session remains active after users disconnect.</p>"""
    idle_disconnect_timeout_in_minutes: NotRequired[
        "capo_workspaces_web.types.idle_disconnect_timeout_in_minutes.IdleDisconnectTimeoutInMinutes"
    ]
    """<p>The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.</p>"""
    cookie_synchronization_configuration: NotRequired[
        "capo_workspaces_web.types.cookie_synchronization_configuration.CookieSynchronizationConfiguration"
    ]
    """<p>The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.</p>"""
    customer_managed_key: NotRequired["capo_workspaces_web.types.key_arn.keyArn"]
    """<p>The customer managed key used to encrypt sensitive information in the user settings.</p>"""
    additional_encryption_context: NotRequired[
        "capo_workspaces_web.types.encryption_context_map.EncryptionContextMap"
    ]
    """<p>The additional encryption context of the user settings.</p>"""
    deep_link_allowed: NotRequired["capo_workspaces_web.types.enabled_type.EnabledType"]
    """<p>Specifies whether the user can use deep links that open automatically when connecting to a session.</p>"""
    toolbar_configuration: NotRequired[
        "capo_workspaces_web.types.toolbar_configuration.ToolbarConfiguration"
    ]
    """<p>The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.</p>"""
    branding_configuration: NotRequired[
        "capo_workspaces_web.types.branding_configuration.BrandingConfiguration"
    ]
    """<p>The branding configuration output that customizes the appearance of the web portal for end users.</p>"""
    web_authn_allowed: NotRequired["capo_workspaces_web.types.enabled_type.EnabledType"]
    """<p>Specifies whether the user can use WebAuthn redirection for passwordless login to websites within the streaming session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserSettings) -> dict:
    out: dict = {}
    out["userSettingsArn"] = value["user_settings_arn"]
    if "associated_portal_arns" in value:
        import capo_workspaces_web.types.arn_list

        out["associatedPortalArns"] = capo_workspaces_web.types.arn_list.serialize_json(
            value["associated_portal_arns"]
        )
    if "copy_allowed" in value:
        out["copyAllowed"] = value["copy_allowed"]
    if "paste_allowed" in value:
        out["pasteAllowed"] = value["paste_allowed"]
    if "download_allowed" in value:
        out["downloadAllowed"] = value["download_allowed"]
    if "upload_allowed" in value:
        out["uploadAllowed"] = value["upload_allowed"]
    if "print_allowed" in value:
        out["printAllowed"] = value["print_allowed"]
    if "disconnect_timeout_in_minutes" in value:
        out["disconnectTimeoutInMinutes"] = value["disconnect_timeout_in_minutes"]
    if "idle_disconnect_timeout_in_minutes" in value:
        out["idleDisconnectTimeoutInMinutes"] = value[
            "idle_disconnect_timeout_in_minutes"
        ]
    if "cookie_synchronization_configuration" in value:
        import capo_workspaces_web.types.cookie_synchronization_configuration

        out["cookieSynchronizationConfiguration"] = (
            capo_workspaces_web.types.cookie_synchronization_configuration.serialize_json(
                value["cookie_synchronization_configuration"]
            )
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
    if "deep_link_allowed" in value:
        out["deepLinkAllowed"] = value["deep_link_allowed"]
    if "toolbar_configuration" in value:
        import capo_workspaces_web.types.toolbar_configuration

        out["toolbarConfiguration"] = (
            capo_workspaces_web.types.toolbar_configuration.serialize_json(
                value["toolbar_configuration"]
            )
        )
    if "branding_configuration" in value:
        import capo_workspaces_web.types.branding_configuration

        out["brandingConfiguration"] = (
            capo_workspaces_web.types.branding_configuration.serialize_json(
                value["branding_configuration"]
            )
        )
    if "web_authn_allowed" in value:
        out["webAuthnAllowed"] = value["web_authn_allowed"]
    return out


def deserialize_json(data: dict) -> UserSettings:
    out: UserSettings = {}  # type: ignore[typeddict-item]
    if data.get("userSettingsArn") is not None:
        out["user_settings_arn"] = data["userSettingsArn"]
    else:
        out["user_settings_arn"] = ""
    if data.get("associatedPortalArns") is not None:
        import capo_workspaces_web.types.arn_list

        out["associated_portal_arns"] = (
            capo_workspaces_web.types.arn_list.deserialize_json(
                data["associatedPortalArns"]
            )
        )
    if data.get("copyAllowed") is not None:
        out["copy_allowed"] = data["copyAllowed"]
    if data.get("pasteAllowed") is not None:
        out["paste_allowed"] = data["pasteAllowed"]
    if data.get("downloadAllowed") is not None:
        out["download_allowed"] = data["downloadAllowed"]
    if data.get("uploadAllowed") is not None:
        out["upload_allowed"] = data["uploadAllowed"]
    if data.get("printAllowed") is not None:
        out["print_allowed"] = data["printAllowed"]
    if data.get("disconnectTimeoutInMinutes") is not None:
        out["disconnect_timeout_in_minutes"] = data["disconnectTimeoutInMinutes"]
    if data.get("idleDisconnectTimeoutInMinutes") is not None:
        out["idle_disconnect_timeout_in_minutes"] = data[
            "idleDisconnectTimeoutInMinutes"
        ]
    if data.get("cookieSynchronizationConfiguration") is not None:
        import capo_workspaces_web.types.cookie_synchronization_configuration

        out["cookie_synchronization_configuration"] = (
            capo_workspaces_web.types.cookie_synchronization_configuration.deserialize_json(
                data["cookieSynchronizationConfiguration"]
            )
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
    if data.get("deepLinkAllowed") is not None:
        out["deep_link_allowed"] = data["deepLinkAllowed"]
    if data.get("toolbarConfiguration") is not None:
        import capo_workspaces_web.types.toolbar_configuration

        out["toolbar_configuration"] = (
            capo_workspaces_web.types.toolbar_configuration.deserialize_json(
                data["toolbarConfiguration"]
            )
        )
    if data.get("brandingConfiguration") is not None:
        import capo_workspaces_web.types.branding_configuration

        out["branding_configuration"] = (
            capo_workspaces_web.types.branding_configuration.deserialize_json(
                data["brandingConfiguration"]
            )
        )
    if data.get("webAuthnAllowed") is not None:
        out["web_authn_allowed"] = data["webAuthnAllowed"]
    return out


def redact_sensitive(value: UserSettings) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cookie_synchronization_configuration" in value:
        out["cookie_synchronization_configuration"] = "*** Sensitive Data Redacted ***"
    if "branding_configuration" in value:
        import capo_workspaces_web.types.branding_configuration

        out["branding_configuration"] = (
            capo_workspaces_web.types.branding_configuration.redact_sensitive(
                value["branding_configuration"]
            )
        )
    return out
