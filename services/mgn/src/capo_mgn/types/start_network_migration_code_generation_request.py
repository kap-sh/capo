"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationCodeGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.code_generation_output_format_types
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_execution_id


class StartNetworkMigrationCodeGenerationRequest(TypedDict, closed=True):
    network_migration_execution_id: (
        "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: (
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    code_generation_output_format_types: NotRequired[
        "capo_mgn.types.code_generation_output_format_types.CodeGenerationOutputFormatTypes"
    ]
    """<p>The output format types for code generation, such as CloudFormation or Terraform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationCodeGenerationRequest) -> dict:
    out: dict = {}
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "code_generation_output_format_types" in value:
        import capo_mgn.types.code_generation_output_format_types

        out["codeGenerationOutputFormatTypes"] = (
            capo_mgn.types.code_generation_output_format_types.serialize_json(
                value["code_generation_output_format_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationCodeGenerationRequest:
    out: StartNetworkMigrationCodeGenerationRequest = {}  # type: ignore[typeddict-item]
    if data.get("networkMigrationExecutionID") is not None:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    else:
        out["network_migration_execution_id"] = ""
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        out["network_migration_definition_id"] = ""
    if data.get("codeGenerationOutputFormatTypes") is not None:
        import capo_mgn.types.code_generation_output_format_types

        out["code_generation_output_format_types"] = (
            capo_mgn.types.code_generation_output_format_types.deserialize_json(
                data["codeGenerationOutputFormatTypes"]
            )
        )
    return out
