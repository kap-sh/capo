"""Generated from Smithy shape ``com.amazonaws.deadline#EnvironmentDetailsEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.document
    import capo_deadline.types.environment_id
    import capo_deadline.types.job_id
    import capo_deadline.types.openjd_extension_name_list
    import capo_deadline.types.serialized_symbol_table
    import capo_deadline.types.string


class EnvironmentDetailsEntity(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    environment_id: "capo_deadline.types.environment_id.EnvironmentId"
    """<p>The environment ID.</p>"""
    schema_version: "capo_deadline.types.string.String"
    """<p>The schema version in the environment.</p>"""
    template: "capo_deadline.types.document.Document"
    """<p>The template used for the environment.</p>"""
    extensions: NotRequired[
        "capo_deadline.types.openjd_extension_name_list.OpenjdExtensionNameList"
    ]
    """<p>The Open Job Description extensions that the environment uses. This value is used by the worker agent.</p>"""
    resolved_symbol_table: NotRequired[
        "capo_deadline.types.serialized_symbol_table.SerializedSymbolTable"
    ]
    """<p>The resolved symbol table for the environment's expressions, serialized as JSON. This value is used by the worker agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentDetailsEntity) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["environmentId"] = value["environment_id"]
    out["schemaVersion"] = value["schema_version"]
    out["template"] = value["template"]
    if "extensions" in value:
        import capo_deadline.types.openjd_extension_name_list

        out["extensions"] = (
            capo_deadline.types.openjd_extension_name_list.serialize_json(
                value["extensions"]
            )
        )
    if "resolved_symbol_table" in value:
        out["resolvedSymbolTable"] = value["resolved_symbol_table"]
    return out


def deserialize_json(data: dict) -> EnvironmentDetailsEntity:
    out: EnvironmentDetailsEntity = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("EnvironmentDetailsEntity.job_id required")
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("EnvironmentDetailsEntity.environment_id required")
    if data.get("schemaVersion") is not None:
        out["schema_version"] = data["schemaVersion"]
    else:
        raise DeserializationError("EnvironmentDetailsEntity.schema_version required")
    if data.get("template") is not None:
        out["template"] = data["template"]
    else:
        raise DeserializationError("EnvironmentDetailsEntity.template required")
    if data.get("extensions") is not None:
        import capo_deadline.types.openjd_extension_name_list

        out["extensions"] = (
            capo_deadline.types.openjd_extension_name_list.deserialize_json(
                data["extensions"]
            )
        )
    if data.get("resolvedSymbolTable") is not None:
        out["resolved_symbol_table"] = data["resolvedSymbolTable"]
    return out
