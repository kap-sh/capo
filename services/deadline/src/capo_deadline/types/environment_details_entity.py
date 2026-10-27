"""Generated from Smithy shape ``com.amazonaws.deadline#EnvironmentDetailsEntity``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.document
    import capo_deadline.types.environment_id
    import capo_deadline.types.job_id
    import capo_deadline.types.openjd_extension_name_list
    import capo_deadline.types.serialized_symbol_table
    import capo_deadline.types.string


class EnvironmentDetailsEntity(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID."""
    environment_id: "capo_deadline.types.environment_id.EnvironmentId"
    """The environment ID."""
    schema_version: "capo_deadline.types.string.String"
    """The schema version in the environment."""
    template: "capo_deadline.types.document.Document"
    """The template used for the environment."""
    extensions: NotRequired[
        "capo_deadline.types.openjd_extension_name_list.OpenjdExtensionNameList"
    ]
    """The Open Job Description extensions that the environment uses. This value is used by the worker agent."""
    resolved_symbol_table: NotRequired[
        "capo_deadline.types.serialized_symbol_table.SerializedSymbolTable"
    ]
    """The resolved symbol table for the environment's expressions, serialized as JSON. This value is used by the worker agent."""


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
        out["job_id"] = ""
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("schemaVersion") is not None:
        out["schema_version"] = data["schemaVersion"]
    else:
        out["schema_version"] = ""
    if data.get("template") is not None:
        out["template"] = data["template"]
    else:
        out["template"] = None
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


def redact_sensitive(value: EnvironmentDetailsEntity) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "template" in value:
        out["template"] = "*** Sensitive Data Redacted ***"
    return out
