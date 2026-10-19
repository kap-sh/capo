"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartBrowserSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_enterprise_policies
    import capo_bedrock_agentcore.types.browser_extensions
    import capo_bedrock_agentcore.types.browser_profile_configuration
    import capo_bedrock_agentcore.types.browser_session_timeout
    import capo_bedrock_agentcore.types.certificates
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.name
    import capo_bedrock_agentcore.types.proxy_configuration
    import capo_bedrock_agentcore.types.tools_file_system_configurations
    import capo_bedrock_agentcore.types.view_port


class StartBrowserSessionRequest(TypedDict, closed=True):
    trace_id: NotRequired["str"]
    """<p>The trace identifier for request tracking.</p>"""
    trace_parent: NotRequired["str"]
    """<p>The parent trace information for distributed tracing.</p>"""
    browser_identifier: "str"
    """<p>The unique identifier of the browser to use for this session. This identifier specifies which browser environment to initialize for the session.</p>"""
    name: NotRequired["capo_bedrock_agentcore.types.name.Name"]
    """<p>The name of the browser session. This name helps you identify and manage the session. The name does not need to be unique.</p>"""
    session_timeout_seconds: NotRequired[
        "capo_bedrock_agentcore.types.browser_session_timeout.BrowserSessionTimeout"
    ]
    """<p>The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 3600 seconds (1 hour). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).</p>"""
    view_port: NotRequired["capo_bedrock_agentcore.types.view_port.ViewPort"]
    """<p>The dimensions of the browser viewport for this session. This determines the visible area of the web content and affects how web pages are rendered. If not specified, Amazon Bedrock AgentCore uses a default viewport size.</p>"""
    extensions: NotRequired[
        "capo_bedrock_agentcore.types.browser_extensions.BrowserExtensions"
    ]
    """<p>A list of browser extensions to load into the browser session.</p>"""
    profile_configuration: NotRequired[
        "capo_bedrock_agentcore.types.browser_profile_configuration.BrowserProfileConfiguration"
    ]
    """<p>The browser profile configuration to use for this session. A browser profile contains persistent data such as cookies and local storage that can be reused across multiple browser sessions. If specified, the session initializes with the profile's stored data, enabling continuity for tasks that require authentication or personalized settings.</p>"""
    proxy_configuration: NotRequired[
        "capo_bedrock_agentcore.types.proxy_configuration.ProxyConfiguration"
    ]
    """<p>Optional proxy configuration for routing browser traffic through customer-specified proxy servers. When provided, enables HTTP Basic authentication via Amazon Web Services Secrets Manager and domain-based routing rules. Requires <code>secretsmanager:GetSecretValue</code> IAM permission for the specified secret ARNs.</p>"""
    enterprise_policies: NotRequired[
        "capo_bedrock_agentcore.types.browser_enterprise_policies.BrowserEnterprisePolicies"
    ]
    """<p>A list of files containing enterprise policies for the browser.</p>"""
    certificates: NotRequired["capo_bedrock_agentcore.types.certificates.Certificates"]
    """<p>A list of certificates to install in the browser session.</p>"""
    filesystem_configurations: NotRequired[
        "capo_bedrock_agentcore.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
    ]
    """<p>The file system configurations to mount into the browser session. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your session can then read and write your data. If you don't specify this field, no additional file systems are mounted.</p>"""
    client_token: NotRequired["capo_bedrock_agentcore.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBrowserSessionRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "session_timeout_seconds" in value:
        out["sessionTimeoutSeconds"] = value["session_timeout_seconds"]
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
    if "profile_configuration" in value:
        import capo_bedrock_agentcore.types.browser_profile_configuration

        out["profileConfiguration"] = (
            capo_bedrock_agentcore.types.browser_profile_configuration.serialize_json(
                value["profile_configuration"]
            )
        )
    if "proxy_configuration" in value:
        import capo_bedrock_agentcore.types.proxy_configuration

        out["proxyConfiguration"] = (
            capo_bedrock_agentcore.types.proxy_configuration.serialize_json(
                value["proxy_configuration"]
            )
        )
    if "enterprise_policies" in value:
        import capo_bedrock_agentcore.types.browser_enterprise_policies

        out["enterprisePolicies"] = (
            capo_bedrock_agentcore.types.browser_enterprise_policies.serialize_json(
                value["enterprise_policies"]
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartBrowserSessionRequest:
    out: StartBrowserSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("sessionTimeoutSeconds") is not None:
        out["session_timeout_seconds"] = data["sessionTimeoutSeconds"]
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
    if data.get("profileConfiguration") is not None:
        import capo_bedrock_agentcore.types.browser_profile_configuration

        out["profile_configuration"] = (
            capo_bedrock_agentcore.types.browser_profile_configuration.deserialize_json(
                data["profileConfiguration"]
            )
        )
    if data.get("proxyConfiguration") is not None:
        import capo_bedrock_agentcore.types.proxy_configuration

        out["proxy_configuration"] = (
            capo_bedrock_agentcore.types.proxy_configuration.deserialize_json(
                data["proxyConfiguration"]
            )
        )
    if data.get("enterprisePolicies") is not None:
        import capo_bedrock_agentcore.types.browser_enterprise_policies

        out["enterprise_policies"] = (
            capo_bedrock_agentcore.types.browser_enterprise_policies.deserialize_json(
                data["enterprisePolicies"]
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
