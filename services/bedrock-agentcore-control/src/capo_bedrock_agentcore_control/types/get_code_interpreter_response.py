"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetCodeInterpreterResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.certificates
    import capo_bedrock_agentcore_control.types.code_interpreter_arn
    import capo_bedrock_agentcore_control.types.code_interpreter_id
    import capo_bedrock_agentcore_control.types.code_interpreter_network_configuration
    import capo_bedrock_agentcore_control.types.code_interpreter_status
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.sandbox_name
    import capo_bedrock_agentcore_control.types.tools_file_system_configurations


class GetCodeInterpreterResponse(TypedDict, closed=True):
    code_interpreter_id: (
        "capo_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId"
    )
    """<p>The unique identifier of the code interpreter.</p>"""
    code_interpreter_arn: (
        "capo_bedrock_agentcore_control.types.code_interpreter_arn.CodeInterpreterArn"
    )
    """<p>The Amazon Resource Name (ARN) of the code interpreter.</p>"""
    name: "capo_bedrock_agentcore_control.types.sandbox_name.SandboxName"
    """<p>The name of the code interpreter.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the code interpreter.</p>"""
    execution_role_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    ]
    """<p>The IAM role ARN that provides permissions for the code interpreter.</p>"""
    network_configuration: "capo_bedrock_agentcore_control.types.code_interpreter_network_configuration.CodeInterpreterNetworkConfiguration"
    status: "capo_bedrock_agentcore_control.types.code_interpreter_status.CodeInterpreterStatus"
    """<p>The current status of the code interpreter.</p>"""
    certificates: NotRequired[
        "capo_bedrock_agentcore_control.types.certificates.Certificates"
    ]
    """<p>The list of certificates configured for the code interpreter.</p>"""
    filesystem_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
    ]
    """<p>The file system configurations mounted into the code interpreter. Each entry describes an access point and its mount path.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for failure if the code interpreter is in a failed state.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the code interpreter was created.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the code interpreter was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeInterpreterResponse) -> dict:
    out: dict = {}
    out["codeInterpreterId"] = value["code_interpreter_id"]
    out["codeInterpreterArn"] = value["code_interpreter_arn"]
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
    import capo_bedrock_agentcore_control.types.code_interpreter_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.code_interpreter_status.serialize_json(
            value["status"]
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


def deserialize_json(data: dict) -> GetCodeInterpreterResponse:
    out: GetCodeInterpreterResponse = {}  # type: ignore[typeddict-item]
    if data.get("codeInterpreterId") is not None:
        out["code_interpreter_id"] = data["codeInterpreterId"]
    else:
        raise DeserializationError(
            "GetCodeInterpreterResponse.code_interpreter_id required"
        )
    if data.get("codeInterpreterArn") is not None:
        out["code_interpreter_arn"] = data["codeInterpreterArn"]
    else:
        raise DeserializationError(
            "GetCodeInterpreterResponse.code_interpreter_arn required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetCodeInterpreterResponse.name required")
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
            "GetCodeInterpreterResponse.network_configuration required"
        )
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.code_interpreter_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.code_interpreter_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetCodeInterpreterResponse.status required")
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
        raise DeserializationError("GetCodeInterpreterResponse.created_at required")
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "GetCodeInterpreterResponse.last_updated_at required"
        )
    return out


def redact_sensitive(value: GetCodeInterpreterResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
