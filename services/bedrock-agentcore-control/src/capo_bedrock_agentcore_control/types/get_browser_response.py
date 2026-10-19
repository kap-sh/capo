"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetBrowserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_arn
    import capo_bedrock_agentcore_control.types.browser_enterprise_policies
    import capo_bedrock_agentcore_control.types.browser_id
    import capo_bedrock_agentcore_control.types.browser_network_configuration
    import capo_bedrock_agentcore_control.types.browser_signing_config_output
    import capo_bedrock_agentcore_control.types.browser_status
    import capo_bedrock_agentcore_control.types.certificates
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.recording_config
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.sandbox_name
    import capo_bedrock_agentcore_control.types.tools_file_system_configurations


class GetBrowserResponse(TypedDict, closed=True):
    browser_id: "capo_bedrock_agentcore_control.types.browser_id.BrowserId"
    """<p>The unique identifier of the browser.</p>"""
    browser_arn: "capo_bedrock_agentcore_control.types.browser_arn.BrowserArn"
    """<p>The Amazon Resource Name (ARN) of the browser.</p>"""
    name: "capo_bedrock_agentcore_control.types.sandbox_name.SandboxName"
    """<p>The name of the browser.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the browser.</p>"""
    execution_role_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    ]
    """<p>The IAM role ARN that provides permissions for the browser.</p>"""
    network_configuration: "capo_bedrock_agentcore_control.types.browser_network_configuration.BrowserNetworkConfiguration"
    recording: NotRequired[
        "capo_bedrock_agentcore_control.types.recording_config.RecordingConfig"
    ]
    browser_signing: NotRequired[
        "capo_bedrock_agentcore_control.types.browser_signing_config_output.BrowserSigningConfigOutput"
    ]
    """<p>The browser signing configuration that shows whether cryptographic agent identification is enabled for web bot authentication.</p>"""
    enterprise_policies: NotRequired[
        "capo_bedrock_agentcore_control.types.browser_enterprise_policies.BrowserEnterprisePolicies"
    ]
    """<p>The list of enterprise policy files configured for the browser.</p>"""
    certificates: NotRequired[
        "capo_bedrock_agentcore_control.types.certificates.Certificates"
    ]
    """<p>The list of certificates configured for the browser.</p>"""
    filesystem_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
    ]
    """<p>The file system configurations mounted into the browser. Each entry describes an access point and its mount path.</p>"""
    status: "capo_bedrock_agentcore_control.types.browser_status.BrowserStatus"
    """<p>The current status of the browser.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for failure if the browser is in a failed state.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser was created.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBrowserResponse) -> dict:
    out: dict = {}
    out["browserId"] = value["browser_id"]
    out["browserArn"] = value["browser_arn"]
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
        import capo_bedrock_agentcore_control.types.browser_signing_config_output

        out["browserSigning"] = (
            capo_bedrock_agentcore_control.types.browser_signing_config_output.serialize_json(
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
    import capo_bedrock_agentcore_control.types.browser_status

    out["status"] = capo_bedrock_agentcore_control.types.browser_status.serialize_json(
        value["status"]
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetBrowserResponse:
    out: GetBrowserResponse = {}  # type: ignore[typeddict-item]
    if data.get("browserId") is not None:
        out["browser_id"] = data["browserId"]
    else:
        out["browser_id"] = ""
    if data.get("browserArn") is not None:
        out["browser_arn"] = data["browserArn"]
    else:
        out["browser_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
        raise DeserializationError("GetBrowserResponse.network_configuration required")
    if data.get("recording") is not None:
        import capo_bedrock_agentcore_control.types.recording_config

        out["recording"] = (
            capo_bedrock_agentcore_control.types.recording_config.deserialize_json(
                data["recording"]
            )
        )
    if data.get("browserSigning") is not None:
        import capo_bedrock_agentcore_control.types.browser_signing_config_output

        out["browser_signing"] = (
            capo_bedrock_agentcore_control.types.browser_signing_config_output.deserialize_json(
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
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.browser_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.browser_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.browser_status.BrowserStatus", ""
        )
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out


def redact_sensitive(value: GetBrowserResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
