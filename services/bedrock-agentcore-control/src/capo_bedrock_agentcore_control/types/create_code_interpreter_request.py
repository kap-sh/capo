"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateCodeInterpreterRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.certificates
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.code_interpreter_network_configuration
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.sandbox_name
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.tools_file_system_configurations


class CreateCodeInterpreterRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.sandbox_name.SandboxName"
    """<p>The name of the code interpreter. The name must be unique within your account.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the code interpreter.</p>"""
    execution_role_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the code interpreter to access Amazon Web Services services.</p>"""
    network_configuration: "capo_bedrock_agentcore_control.types.code_interpreter_network_configuration.CodeInterpreterNetworkConfiguration"
    """<p>The network configuration for the code interpreter. This configuration specifies the network mode for the code interpreter.</p>"""
    certificates: NotRequired[
        "capo_bedrock_agentcore_control.types.certificates.Certificates"
    ]
    """<p>A list of certificates to install in the code interpreter.</p>"""
    filesystem_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
    ]
    """<p>The file system configurations to mount into the code interpreter. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your sessions can then access your data. If you don't specify this field, no file systems are mounted.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to the code interpreter. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeInterpreterRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    import capo_bedrock_agentcore_control.types.code_interpreter_network_configuration

    out["networkConfiguration"] = (
        capo_bedrock_agentcore_control.types.code_interpreter_network_configuration.serialize_json(
            value["network_configuration"]
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


def deserialize_json(data: dict) -> CreateCodeInterpreterRequest:
    out: CreateCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("networkConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.code_interpreter_network_configuration

        out["network_configuration"] = (
            capo_bedrock_agentcore_control.types.code_interpreter_network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCodeInterpreterRequest.network_configuration required"
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


def redact_sensitive(value: CreateCodeInterpreterRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
