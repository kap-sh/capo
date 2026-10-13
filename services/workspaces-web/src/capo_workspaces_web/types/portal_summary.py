"""Generated from Smithy shape ``com.amazonaws.workspacesweb#PortalSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.authentication_type
    import capo_workspaces_web.types.browser_type
    import capo_workspaces_web.types.display_name
    import capo_workspaces_web.types.instance_type
    import capo_workspaces_web.types.max_concurrent_sessions
    import capo_workspaces_web.types.portal_custom_domain
    import capo_workspaces_web.types.portal_endpoint
    import capo_workspaces_web.types.portal_status
    import capo_workspaces_web.types.renderer_type
    import capo_workspaces_web.types.timestamp


class PortalSummary(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    renderer_type: NotRequired["capo_workspaces_web.types.renderer_type.RendererType"]
    """<p>The renderer that is used in streaming sessions.</p>"""
    browser_type: NotRequired["capo_workspaces_web.types.browser_type.BrowserType"]
    """<p>The browser type of the web portal.</p>"""
    portal_status: NotRequired["capo_workspaces_web.types.portal_status.PortalStatus"]
    """<p>The status of the web portal.</p>"""
    portal_endpoint: NotRequired[
        "capo_workspaces_web.types.portal_endpoint.PortalEndpoint"
    ]
    """<p>The endpoint URL of the web portal that users access in order to start streaming sessions.</p>"""
    display_name: NotRequired["capo_workspaces_web.types.display_name.DisplayName"]
    """<p>The name of the web portal.</p>"""
    creation_date: NotRequired["capo_workspaces_web.types.timestamp.Timestamp"]
    """<p>The creation date of the web portal.</p>"""
    browser_settings_arn: NotRequired["capo_workspaces_web.types.arn.ARN"]
    """<p>The ARN of the browser settings that is associated with the web portal.</p>"""
    data_protection_settings_arn: NotRequired["capo_workspaces_web.types.arn.ARN"]
    """<p>The ARN of the data protection settings.</p>"""
    user_settings_arn: NotRequired["capo_workspaces_web.types.arn.ARN"]
    """<p>The ARN of the user settings that is associated with the web portal.</p>"""
    network_settings_arn: NotRequired["capo_workspaces_web.types.arn.ARN"]
    """<p>The ARN of the network settings that is associated with the web portal.</p>"""
    session_logger_arn: NotRequired["capo_workspaces_web.types.arn.ARN"]
    """<p>The ARN of the session logger that is assocaited with the portal.</p>"""
    trust_store_arn: NotRequired["capo_workspaces_web.types.arn.ARN"]
    """<p>The ARN of the trust that is associated with this web portal.</p>"""
    user_access_logging_settings_arn: NotRequired["capo_workspaces_web.types.arn.ARN"]
    """<p>The ARN of the user access logging settings that is associated with the web portal.</p>"""
    authentication_type: NotRequired[
        "capo_workspaces_web.types.authentication_type.AuthenticationType"
    ]
    """<p>The type of authentication integration points used when signing into the web portal. Defaults to <code>Standard</code>.</p> <p> <code>Standard</code> web portals are authenticated directly through your identity provider. You need to call <code>CreateIdentityProvider</code> to integrate your identity provider with your web portal. User and group access to your web portal is controlled through your identity provider.</p> <p> <code>IAM Identity Center</code> web portals are authenticated through IAM Identity Center. Identity sources (including external identity provider integration), plus user and group access to your web portal, can be configured in the IAM Identity Center.</p>"""
    ip_access_settings_arn: NotRequired["capo_workspaces_web.types.arn.ARN"]
    """<p>The ARN of the IP access settings.</p>"""
    instance_type: NotRequired["capo_workspaces_web.types.instance_type.InstanceType"]
    """<p>The type and resources of the underlying instance.</p>"""
    max_concurrent_sessions: NotRequired[
        "capo_workspaces_web.types.max_concurrent_sessions.MaxConcurrentSessions"
    ]
    """<p>The maximum number of concurrent sessions for the portal.</p>"""
    portal_custom_domain: NotRequired[
        "capo_workspaces_web.types.portal_custom_domain.PortalCustomDomain"
    ]
    """<p>The custom domain of the web portal that users access in order to start streaming sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortalSummary) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    if "renderer_type" in value:
        out["rendererType"] = value["renderer_type"]
    if "browser_type" in value:
        out["browserType"] = value["browser_type"]
    if "portal_status" in value:
        out["portalStatus"] = value["portal_status"]
    if "portal_endpoint" in value:
        out["portalEndpoint"] = value["portal_endpoint"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "creation_date" in value:
        import capo_workspaces_web.types.timestamp

        out["creationDate"] = capo_workspaces_web.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "browser_settings_arn" in value:
        out["browserSettingsArn"] = value["browser_settings_arn"]
    if "data_protection_settings_arn" in value:
        out["dataProtectionSettingsArn"] = value["data_protection_settings_arn"]
    if "user_settings_arn" in value:
        out["userSettingsArn"] = value["user_settings_arn"]
    if "network_settings_arn" in value:
        out["networkSettingsArn"] = value["network_settings_arn"]
    if "session_logger_arn" in value:
        out["sessionLoggerArn"] = value["session_logger_arn"]
    if "trust_store_arn" in value:
        out["trustStoreArn"] = value["trust_store_arn"]
    if "user_access_logging_settings_arn" in value:
        out["userAccessLoggingSettingsArn"] = value["user_access_logging_settings_arn"]
    if "authentication_type" in value:
        out["authenticationType"] = value["authentication_type"]
    if "ip_access_settings_arn" in value:
        out["ipAccessSettingsArn"] = value["ip_access_settings_arn"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "max_concurrent_sessions" in value:
        out["maxConcurrentSessions"] = value["max_concurrent_sessions"]
    if "portal_custom_domain" in value:
        out["portalCustomDomain"] = value["portal_custom_domain"]
    return out


def deserialize_json(data: dict) -> PortalSummary:
    out: PortalSummary = {}  # type: ignore[typeddict-item]
    if data.get("portalArn") is not None:
        out["portal_arn"] = data["portalArn"]
    else:
        raise DeserializationError("PortalSummary.portal_arn required")
    if data.get("rendererType") is not None:
        out["renderer_type"] = data["rendererType"]
    if data.get("browserType") is not None:
        out["browser_type"] = data["browserType"]
    if data.get("portalStatus") is not None:
        out["portal_status"] = data["portalStatus"]
    if data.get("portalEndpoint") is not None:
        out["portal_endpoint"] = data["portalEndpoint"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("creationDate") is not None:
        import capo_workspaces_web.types.timestamp

        out["creation_date"] = capo_workspaces_web.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    if data.get("browserSettingsArn") is not None:
        out["browser_settings_arn"] = data["browserSettingsArn"]
    if data.get("dataProtectionSettingsArn") is not None:
        out["data_protection_settings_arn"] = data["dataProtectionSettingsArn"]
    if data.get("userSettingsArn") is not None:
        out["user_settings_arn"] = data["userSettingsArn"]
    if data.get("networkSettingsArn") is not None:
        out["network_settings_arn"] = data["networkSettingsArn"]
    if data.get("sessionLoggerArn") is not None:
        out["session_logger_arn"] = data["sessionLoggerArn"]
    if data.get("trustStoreArn") is not None:
        out["trust_store_arn"] = data["trustStoreArn"]
    if data.get("userAccessLoggingSettingsArn") is not None:
        out["user_access_logging_settings_arn"] = data["userAccessLoggingSettingsArn"]
    if data.get("authenticationType") is not None:
        out["authentication_type"] = data["authenticationType"]
    if data.get("ipAccessSettingsArn") is not None:
        out["ip_access_settings_arn"] = data["ipAccessSettingsArn"]
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("maxConcurrentSessions") is not None:
        out["max_concurrent_sessions"] = data["maxConcurrentSessions"]
    if data.get("portalCustomDomain") is not None:
        out["portal_custom_domain"] = data["portalCustomDomain"]
    return out


def redact_sensitive(value: PortalSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    return out
