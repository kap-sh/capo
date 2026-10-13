"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateBrowserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_enterprise_policies
    import capo_bedrock_agentcore_control.types.browser_network_configuration
    import capo_bedrock_agentcore_control.types.browser_signing_config_input
    import capo_bedrock_agentcore_control.types.certificates
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.recording_config
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.sandbox_name
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.tools_file_system_configurations


class CreateBrowserRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.sandbox_name.SandboxName"
    """<p>The name of the browser. The name must be unique within your account.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the browser.</p>"""
    execution_role_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the browser to access Amazon Web Services services.</p>"""
    network_configuration: "capo_bedrock_agentcore_control.types.browser_network_configuration.BrowserNetworkConfiguration"
    """<p>The network configuration for the browser. This configuration specifies the network mode for the browser.</p>"""
    recording: NotRequired[
        "capo_bedrock_agentcore_control.types.recording_config.RecordingConfig"
    ]
    """<p>The recording configuration for the browser. When enabled, browser sessions are recorded and stored in the specified Amazon S3 location.</p>"""
    browser_signing: NotRequired[
        "capo_bedrock_agentcore_control.types.browser_signing_config_input.BrowserSigningConfigInput"
    ]
    """<p>The browser signing configuration that enables cryptographic agent identification using HTTP message signatures for web bot authentication.</p>"""
    enterprise_policies: NotRequired[
        "capo_bedrock_agentcore_control.types.browser_enterprise_policies.BrowserEnterprisePolicies"
    ]
    """<p>A list of enterprise policy files for the browser.</p>"""
    certificates: NotRequired[
        "capo_bedrock_agentcore_control.types.certificates.Certificates"
    ]
    """<p>A list of certificates to install in the browser.</p>"""
    filesystem_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
    ]
    """<p>The file system configurations to mount into the browser. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your sessions can then access your data. If you don't specify this field, no file systems are mounted.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to the browser. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrowserRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    import capo_bedrock_agentcore_control.types.browser_network_configuration

    out["networkConfiguration"] = (
        capo_bedrock_agentcore_control.types.browser_network_configuration.serialize_json(
            value["network_configuration"]
        )
    )
    if "recording" in value:
        import capo_bedrock_agentcore_control.types.recording_config

        out["recording"] = (
            capo_bedrock_agentcore_control.types.recording_config.serialize_json(
                value["recording"]
            )
        )
    if "browser_signing" in value:
        import capo_bedrock_agentcore_control.types.browser_signing_config_input

        out["browserSigning"] = (
            capo_bedrock_agentcore_control.types.browser_signing_config_input.serialize_json(
                value["browser_signing"]
            )
        )
    if "enterprise_policies" in value:
        import capo_bedrock_agentcore_control.types.browser_enterprise_policies

        out["enterprisePolicies"] = (
            capo_bedrock_agentcore_control.types.browser_enterprise_policies.serialize_json(
                value["enterprise_policies"]
            )
        )
    if "certificates" in value:
        import capo_bedrock_agentcore_control.types.certificates

        out["certificates"] = (
            capo_bedrock_agentcore_control.types.certificates.serialize_json(
                value["certificates"]
            )
        )
    if "filesystem_configurations" in value:
        import capo_bedrock_agentcore_control.types.tools_file_system_configurations

        out["filesystemConfigurations"] = (
            capo_bedrock_agentcore_control.types.tools_file_system_configurations.serialize_json(
                value["filesystem_configurations"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateBrowserRequest:
    out: CreateBrowserRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateBrowserRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("networkConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.browser_network_configuration

        out["network_configuration"] = (
            capo_bedrock_agentcore_control.types.browser_network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBrowserRequest.network_configuration required"
        )
    if data.get("recording") is not None:
        import capo_bedrock_agentcore_control.types.recording_config

        out["recording"] = (
            capo_bedrock_agentcore_control.types.recording_config.deserialize_json(
                data["recording"]
            )
        )
    if data.get("browserSigning") is not None:
        import capo_bedrock_agentcore_control.types.browser_signing_config_input

        out["browser_signing"] = (
            capo_bedrock_agentcore_control.types.browser_signing_config_input.deserialize_json(
                data["browserSigning"]
            )
        )
    if data.get("enterprisePolicies") is not None:
        import capo_bedrock_agentcore_control.types.browser_enterprise_policies

        out["enterprise_policies"] = (
            capo_bedrock_agentcore_control.types.browser_enterprise_policies.deserialize_json(
                data["enterprisePolicies"]
            )
        )
    if data.get("certificates") is not None:
        import capo_bedrock_agentcore_control.types.certificates

        out["certificates"] = (
            capo_bedrock_agentcore_control.types.certificates.deserialize_json(
                data["certificates"]
            )
        )
    if data.get("filesystemConfigurations") is not None:
        import capo_bedrock_agentcore_control.types.tools_file_system_configurations

        out["filesystem_configurations"] = (
            capo_bedrock_agentcore_control.types.tools_file_system_configurations.deserialize_json(
                data["filesystemConfigurations"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out


def redact_sensitive(value: CreateBrowserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
