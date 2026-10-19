"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetCodeInterpreterSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.certificates
    import capo_bedrock_agentcore.types.code_interpreter_session_id
    import capo_bedrock_agentcore.types.code_interpreter_session_status
    import capo_bedrock_agentcore.types.code_interpreter_session_timeout
    import capo_bedrock_agentcore.types.date_timestamp
    import capo_bedrock_agentcore.types.name
    import capo_bedrock_agentcore.types.tools_file_system_configurations


class GetCodeInterpreterSessionResponse(TypedDict, closed=True):
    code_interpreter_identifier: "str"
    """<p>The identifier of the code interpreter.</p>"""
    session_id: "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
    """<p>The identifier of the code interpreter session.</p>"""
    name: NotRequired["capo_bedrock_agentcore.types.name.Name"]
    """<p>The name of the code interpreter session.</p>"""
    created_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The time at which the code interpreter session was created.</p>"""
    session_timeout_seconds: NotRequired[
        "capo_bedrock_agentcore.types.code_interpreter_session_timeout.CodeInterpreterSessionTimeout"
    ]
    """<p>The timeout period for the code interpreter session in seconds.</p>"""
    status: NotRequired[
        "capo_bedrock_agentcore.types.code_interpreter_session_status.CodeInterpreterSessionStatus"
    ]
    """<p>The current status of the code interpreter session. Possible values include ACTIVE, STOPPING, and STOPPED.</p>"""
    certificates: NotRequired["capo_bedrock_agentcore.types.certificates.Certificates"]
    """<p>The list of certificates installed in the code interpreter session.</p>"""
    filesystem_configurations: NotRequired[
        "capo_bedrock_agentcore.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
    ]
    """<p>The file system configurations for the code interpreter session. Each entry describes an access point and its mount path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeInterpreterSessionResponse) -> dict:
    out: dict = {}
    out["codeInterpreterIdentifier"] = value["code_interpreter_identifier"]
    out["sessionId"] = value["session_id"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    if "session_timeout_seconds" in value:
        out["sessionTimeoutSeconds"] = value["session_timeout_seconds"]
    if "status" in value:
        import capo_bedrock_agentcore.types.code_interpreter_session_status

        out["status"] = (
            capo_bedrock_agentcore.types.code_interpreter_session_status.serialize_json(
                value["status"]
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
    return out


def deserialize_json(data: dict) -> GetCodeInterpreterSessionResponse:
    out: GetCodeInterpreterSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("codeInterpreterIdentifier") is not None:
        out["code_interpreter_identifier"] = data["codeInterpreterIdentifier"]
    else:
        out["code_interpreter_identifier"] = ""
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
    if data.get("sessionTimeoutSeconds") is not None:
        out["session_timeout_seconds"] = data["sessionTimeoutSeconds"]
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.code_interpreter_session_status

        out["status"] = (
            capo_bedrock_agentcore.types.code_interpreter_session_status.deserialize_json(
                data["status"]
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
    return out
