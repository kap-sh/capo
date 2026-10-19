"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetBrowserSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_enterprise_policies
    import capo_bedrock_agentcore.types.browser_extensions
    import capo_bedrock_agentcore.types.browser_profile_configuration
    import capo_bedrock_agentcore.types.browser_session_id
    import capo_bedrock_agentcore.types.browser_session_status
    import capo_bedrock_agentcore.types.browser_session_stream
    import capo_bedrock_agentcore.types.browser_session_timeout
    import capo_bedrock_agentcore.types.certificates
    import capo_bedrock_agentcore.types.date_timestamp
    import capo_bedrock_agentcore.types.name
    import capo_bedrock_agentcore.types.proxy_configuration
    import capo_bedrock_agentcore.types.tools_file_system_configurations
    import capo_bedrock_agentcore.types.view_port


class GetBrowserSessionResponse(TypedDict, closed=True):
    browser_identifier: "str"
    """<p>The identifier of the browser.</p>"""
    session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The identifier of the browser session.</p>"""
    name: NotRequired["capo_bedrock_agentcore.types.name.Name"]
    """<p>The name of the browser session.</p>"""
    created_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The time at which the browser session was created.</p>"""
    view_port: NotRequired["capo_bedrock_agentcore.types.view_port.ViewPort"]
    extensions: NotRequired[
        "capo_bedrock_agentcore.types.browser_extensions.BrowserExtensions"
    ]
    """<p>The list of browser extensions that are configured in the browser session.</p>"""
    enterprise_policies: NotRequired[
        "capo_bedrock_agentcore.types.browser_enterprise_policies.BrowserEnterprisePolicies"
    ]
    """<p>A list of files containing enterprise policies for the browser session.</p>"""
    profile_configuration: NotRequired[
        "capo_bedrock_agentcore.types.browser_profile_configuration.BrowserProfileConfiguration"
    ]
    """<p>The browser profile configuration associated with this session. Contains the profile identifier that links to persistent browser data such as cookies and local storage.</p>"""
    session_timeout_seconds: NotRequired[
        "capo_bedrock_agentcore.types.browser_session_timeout.BrowserSessionTimeout"
    ]
    """<p>The timeout period for the browser session in seconds.</p>"""
    status: NotRequired[
        "capo_bedrock_agentcore.types.browser_session_status.BrowserSessionStatus"
    ]
    """<p>The current status of the browser session. Possible values include ACTIVE, STOPPING, and STOPPED.</p>"""
    streams: NotRequired[
        "capo_bedrock_agentcore.types.browser_session_stream.BrowserSessionStream"
    ]
    """<p>The streams associated with this browser session. These include the automation stream and live view stream.</p>"""
    proxy_configuration: NotRequired[
        "capo_bedrock_agentcore.types.proxy_configuration.ProxyConfiguration"
    ]
    """<p>The active proxy configuration for this browser session. This field is only present if proxy configuration was provided when the session was started using <code>StartBrowserSession</code>. The configuration includes proxy servers, domain bypass rules and the proxy authentication credentials.</p>"""
    certificates: NotRequired["capo_bedrock_agentcore.types.certificates.Certificates"]
    """<p>The list of certificates installed in the browser session.</p>"""
    filesystem_configurations: NotRequired[
        "capo_bedrock_agentcore.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
    ]
    """<p>The file system configurations for the browser session. Each entry describes an access point and its mount path.</p>"""
    session_replay_artifact: NotRequired["str"]
    """<p>The artifact containing the session replay information.</p>"""
    last_updated_at: NotRequired[
        "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time at which the browser session was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBrowserSessionResponse) -> dict:
    out: dict = {}
    out["browserIdentifier"] = value["browser_identifier"]
    out["sessionId"] = value["session_id"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    if "view_port" in value:
        import capo_bedrock_agentcore.types.view_port

        out["viewPort"] = capo_bedrock_agentcore.types.view_port.serialize_json(
            value["view_port"]
        )
    if "extensions" in value:
        import capo_bedrock_agentcore.types.browser_extensions

        out["extensions"] = (
            capo_bedrock_agentcore.types.browser_extensions.serialize_json(
                value["extensions"]
            )
        )
    if "enterprise_policies" in value:
        import capo_bedrock_agentcore.types.browser_enterprise_policies

        out["enterprisePolicies"] = (
            capo_bedrock_agentcore.types.browser_enterprise_policies.serialize_json(
                value["enterprise_policies"]
            )
        )
    if "profile_configuration" in value:
        import capo_bedrock_agentcore.types.browser_profile_configuration

        out["profileConfiguration"] = (
            capo_bedrock_agentcore.types.browser_profile_configuration.serialize_json(
                value["profile_configuration"]
            )
        )
    if "session_timeout_seconds" in value:
        out["sessionTimeoutSeconds"] = value["session_timeout_seconds"]
    if "status" in value:
        import capo_bedrock_agentcore.types.browser_session_status

        out["status"] = (
            capo_bedrock_agentcore.types.browser_session_status.serialize_json(
                value["status"]
            )
        )
    if "streams" in value:
        import capo_bedrock_agentcore.types.browser_session_stream

        out["streams"] = (
            capo_bedrock_agentcore.types.browser_session_stream.serialize_json(
                value["streams"]
            )
        )
    if "proxy_configuration" in value:
        import capo_bedrock_agentcore.types.proxy_configuration

        out["proxyConfiguration"] = (
            capo_bedrock_agentcore.types.proxy_configuration.serialize_json(
                value["proxy_configuration"]
            )
        )
    if "certificates" in value:
        import capo_bedrock_agentcore.types.certificates

        out["certificates"] = capo_bedrock_agentcore.types.certificates.serialize_json(
            value["certificates"]
        )
    if "filesystem_configurations" in value:
        import capo_bedrock_agentcore.types.tools_file_system_configurations

        out["filesystemConfigurations"] = (
            capo_bedrock_agentcore.types.tools_file_system_configurations.serialize_json(
                value["filesystem_configurations"]
            )
        )
    if "session_replay_artifact" in value:
        out["sessionReplayArtifact"] = value["session_replay_artifact"]
    if "last_updated_at" in value:
        import capo_bedrock_agentcore.types.date_timestamp

        out["lastUpdatedAt"] = (
            capo_bedrock_agentcore.types.date_timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetBrowserSessionResponse:
    out: GetBrowserSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("browserIdentifier") is not None:
        out["browser_identifier"] = data["browserIdentifier"]
    else:
        out["browser_identifier"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("viewPort") is not None:
        import capo_bedrock_agentcore.types.view_port

        out["view_port"] = capo_bedrock_agentcore.types.view_port.deserialize_json(
            data["viewPort"]
        )
    if data.get("extensions") is not None:
        import capo_bedrock_agentcore.types.browser_extensions

        out["extensions"] = (
            capo_bedrock_agentcore.types.browser_extensions.deserialize_json(
                data["extensions"]
            )
        )
    if data.get("enterprisePolicies") is not None:
        import capo_bedrock_agentcore.types.browser_enterprise_policies

        out["enterprise_policies"] = (
            capo_bedrock_agentcore.types.browser_enterprise_policies.deserialize_json(
                data["enterprisePolicies"]
            )
        )
    if data.get("profileConfiguration") is not None:
        import capo_bedrock_agentcore.types.browser_profile_configuration

        out["profile_configuration"] = (
            capo_bedrock_agentcore.types.browser_profile_configuration.deserialize_json(
                data["profileConfiguration"]
            )
        )
    if data.get("sessionTimeoutSeconds") is not None:
        out["session_timeout_seconds"] = data["sessionTimeoutSeconds"]
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.browser_session_status

        out["status"] = (
            capo_bedrock_agentcore.types.browser_session_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("streams") is not None:
        import capo_bedrock_agentcore.types.browser_session_stream

        out["streams"] = (
            capo_bedrock_agentcore.types.browser_session_stream.deserialize_json(
                data["streams"]
            )
        )
    if data.get("proxyConfiguration") is not None:
        import capo_bedrock_agentcore.types.proxy_configuration

        out["proxy_configuration"] = (
            capo_bedrock_agentcore.types.proxy_configuration.deserialize_json(
                data["proxyConfiguration"]
            )
        )
    if data.get("certificates") is not None:
        import capo_bedrock_agentcore.types.certificates

        out["certificates"] = (
            capo_bedrock_agentcore.types.certificates.deserialize_json(
                data["certificates"]
            )
        )
    if data.get("filesystemConfigurations") is not None:
        import capo_bedrock_agentcore.types.tools_file_system_configurations

        out["filesystem_configurations"] = (
            capo_bedrock_agentcore.types.tools_file_system_configurations.deserialize_json(
                data["filesystemConfigurations"]
            )
        )
    if data.get("sessionReplayArtifact") is not None:
        out["session_replay_artifact"] = data["sessionReplayArtifact"]
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    return out
