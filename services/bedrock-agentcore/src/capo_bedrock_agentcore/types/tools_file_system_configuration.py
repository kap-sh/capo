"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolsFileSystemConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.efs_configuration
    import capo_bedrock_agentcore.types.s3_files_configuration


class ToolsFileSystemConfigurationS3FilesConfigurationMember(TypedDict, closed=True):
    s3FilesConfiguration: (
        "capo_bedrock_agentcore.types.s3_files_configuration.S3FilesConfiguration"
    )


class ToolsFileSystemConfigurationEfsConfigurationMember(TypedDict, closed=True):
    efsConfiguration: "capo_bedrock_agentcore.types.efs_configuration.EfsConfiguration"


ToolsFileSystemConfiguration: TypeAlias = (
    ToolsFileSystemConfigurationS3FilesConfigurationMember
    | ToolsFileSystemConfigurationEfsConfigurationMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ToolsFileSystemConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ToolsFileSystemConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3FilesConfiguration" in value:
        import capo_bedrock_agentcore.types.s3_files_configuration

        return {
            "s3FilesConfiguration": capo_bedrock_agentcore.types.s3_files_configuration.serialize_json(
                value["s3FilesConfiguration"]
            )
        }
    elif "efsConfiguration" in value:
        import capo_bedrock_agentcore.types.efs_configuration

        return {
            "efsConfiguration": capo_bedrock_agentcore.types.efs_configuration.serialize_json(
                value["efsConfiguration"]
            )
        }
    else:
        raise SerializationError("ToolsFileSystemConfiguration: no variant present")


def deserialize_json(data: dict) -> ToolsFileSystemConfiguration:
    if data.get("s3FilesConfiguration") is not None:
        import capo_bedrock_agentcore.types.s3_files_configuration

        return {
            "s3FilesConfiguration": capo_bedrock_agentcore.types.s3_files_configuration.deserialize_json(
                data["s3FilesConfiguration"]
            )
        }
    elif data.get("efsConfiguration") is not None:
        import capo_bedrock_agentcore.types.efs_configuration

        return {
            "efsConfiguration": capo_bedrock_agentcore.types.efs_configuration.deserialize_json(
                data["efsConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ToolsFileSystemConfiguration: no recognized variant key"
        )
