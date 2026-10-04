"""Generated from Smithy shape ``com.amazonaws.deadline#StepDetailsEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.dependencies_list
    import capo_deadline.types.document
    import capo_deadline.types.job_id
    import capo_deadline.types.openjd_extension_name_list
    import capo_deadline.types.serialized_symbol_table
    import capo_deadline.types.step_id
    import capo_deadline.types.string


class StepDetailsEntity(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    step_id: "capo_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""
    schema_version: "capo_deadline.types.string.String"
    """<p>The schema version for a step template.</p>"""
    template: "capo_deadline.types.document.Document"
    """<p>The template for a step.</p>"""
    dependencies: "capo_deadline.types.dependencies_list.DependenciesList"
    """<p>The dependencies for a step.</p>"""
    extensions: NotRequired[
        "capo_deadline.types.openjd_extension_name_list.OpenjdExtensionNameList"
    ]
    """<p>The Open Job Description extensions that the step uses. This value is used by the worker agent.</p>"""
    resolved_symbol_table: NotRequired[
        "capo_deadline.types.serialized_symbol_table.SerializedSymbolTable"
    ]
    """<p>The resolved symbol table for the step's expressions, serialized as JSON. This value is used by the worker agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepDetailsEntity) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    out["schemaVersion"] = value["schema_version"]
    out["template"] = value["template"]
    import capo_deadline.types.dependencies_list

    out["dependencies"] = capo_deadline.types.dependencies_list.serialize_json(
        value["dependencies"]
    )
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


def deserialize_json(data: dict) -> StepDetailsEntity:
    out: StepDetailsEntity = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("StepDetailsEntity.job_id required")
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("StepDetailsEntity.step_id required")
    if data.get("schemaVersion") is not None:
        out["schema_version"] = data["schemaVersion"]
    else:
        raise DeserializationError("StepDetailsEntity.schema_version required")
    if data.get("template") is not None:
        out["template"] = data["template"]
    else:
        raise DeserializationError("StepDetailsEntity.template required")
    if data.get("dependencies") is not None:
        import capo_deadline.types.dependencies_list

        out["dependencies"] = capo_deadline.types.dependencies_list.deserialize_json(
            data["dependencies"]
        )
    else:
        raise DeserializationError("StepDetailsEntity.dependencies required")
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
