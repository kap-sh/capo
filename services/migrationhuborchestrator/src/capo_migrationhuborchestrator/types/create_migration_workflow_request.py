"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#CreateMigrationWorkflowRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_migrationhuborchestrator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.step_input_parameters
    import capo_migrationhuborchestrator.types.string_list
    import capo_migrationhuborchestrator.types.string_map


class CreateMigrationWorkflowRequest(TypedDict, closed=True):
    name: "str"
    """<p>The name of the migration workflow.</p>"""
    description: NotRequired["str"]
    """<p>The description of the migration workflow.</p>"""
    template_id: "str"
    """<p>The ID of the template.</p>"""
    application_configuration_id: NotRequired["str"]
    """<p>The configuration ID of the application configured in Application Discovery Service.</p>"""
    input_parameters: (
        "capo_migrationhuborchestrator.types.step_input_parameters.StepInputParameters"
    )
    """<p>The input parameters required to create a migration workflow.</p>"""
    step_targets: NotRequired[
        "capo_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The servers on which a step will be run.</p>"""
    tags: NotRequired["capo_migrationhuborchestrator.types.string_map.StringMap"]
    """<p>The tags to add on a migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMigrationWorkflowRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["templateId"] = value["template_id"]
    if "application_configuration_id" in value:
        out["applicationConfigurationId"] = value["application_configuration_id"]
    import capo_migrationhuborchestrator.types.step_input_parameters

    out["inputParameters"] = (
        capo_migrationhuborchestrator.types.step_input_parameters.serialize_json(
            value["input_parameters"]
        )
    )
    if "step_targets" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["stepTargets"] = (
            capo_migrationhuborchestrator.types.string_list.serialize_json(
                value["step_targets"]
            )
        )
    if "tags" in value:
        import capo_migrationhuborchestrator.types.string_map

        out["tags"] = capo_migrationhuborchestrator.types.string_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateMigrationWorkflowRequest:
    out: CreateMigrationWorkflowRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateMigrationWorkflowRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("templateId") is not None:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError(
            "CreateMigrationWorkflowRequest.template_id required"
        )
    if data.get("applicationConfigurationId") is not None:
        out["application_configuration_id"] = data["applicationConfigurationId"]
    if data.get("inputParameters") is not None:
        import capo_migrationhuborchestrator.types.step_input_parameters

        out["input_parameters"] = (
            capo_migrationhuborchestrator.types.step_input_parameters.deserialize_json(
                data["inputParameters"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMigrationWorkflowRequest.input_parameters required"
        )
    if data.get("stepTargets") is not None:
        import capo_migrationhuborchestrator.types.string_list

        out["step_targets"] = (
            capo_migrationhuborchestrator.types.string_list.deserialize_json(
                data["stepTargets"]
            )
        )
    if data.get("tags") is not None:
        import capo_migrationhuborchestrator.types.string_map

        out["tags"] = capo_migrationhuborchestrator.types.string_map.deserialize_json(
            data["tags"]
        )
    return out


def redact_sensitive(value: CreateMigrationWorkflowRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_parameters" in value:
        out["input_parameters"] = "*** Sensitive Data Redacted ***"
    return out
