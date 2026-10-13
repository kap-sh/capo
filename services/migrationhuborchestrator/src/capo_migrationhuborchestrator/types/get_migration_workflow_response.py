"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetMigrationWorkflowResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_migrationhuborchestrator.types.migration_workflow_id
    import capo_migrationhuborchestrator.types.migration_workflow_status_enum
    import capo_migrationhuborchestrator.types.step_input_parameters
    import capo_migrationhuborchestrator.types.string_map
    import capo_migrationhuborchestrator.types.tools_list


class GetMigrationWorkflowResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    ]
    """<p>The ID of the migration workflow.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the migration workflow.</p>"""
    name: NotRequired["str"]
    """<p>The name of the migration workflow.</p>"""
    description: NotRequired["str"]
    """<p>The description of the migration workflow.</p>"""
    template_id: NotRequired["str"]
    """<p>The ID of the template.</p>"""
    ads_application_configuration_id: NotRequired["str"]
    """<p>The configuration ID of the application configured in Application Discovery Service.</p>"""
    ads_application_name: NotRequired["str"]
    """<p>The name of the application configured in Application Discovery Service.</p>"""
    status: NotRequired[
        "capo_migrationhuborchestrator.types.migration_workflow_status_enum.MigrationWorkflowStatusEnum"
    ]
    """<p>The status of the migration workflow.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message of the migration workflow.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was created.</p>"""
    last_start_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was last started.</p>"""
    last_stop_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was last stopped.</p>"""
    last_modified_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow was last modified.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the migration workflow ended.</p>"""
    tools: NotRequired["capo_migrationhuborchestrator.types.tools_list.ToolsList"]
    """<p>List of AWS services utilized in a migration workflow.</p>"""
    total_steps: NotRequired["int"]
    """<p>The total number of steps in the migration workflow.</p>"""
    completed_steps: NotRequired["int"]
    """<p>Get a list of completed steps in the migration workflow.</p>"""
    workflow_inputs: NotRequired[
        "capo_migrationhuborchestrator.types.step_input_parameters.StepInputParameters"
    ]
    """<p>The inputs required for creating the migration workflow.</p>"""
    tags: NotRequired["capo_migrationhuborchestrator.types.string_map.StringMap"]
    """<p>The tags added to the migration workflow.</p>"""
    workflow_bucket: NotRequired["str"]
    """<p>The Amazon S3 bucket where the migration logs are stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMigrationWorkflowResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "template_id" in value:
        out["templateId"] = value["template_id"]
    if "ads_application_configuration_id" in value:
        out["adsApplicationConfigurationId"] = value["ads_application_configuration_id"]
    if "ads_application_name" in value:
        out["adsApplicationName"] = value["ads_application_name"]
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "creation_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creationTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "last_start_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["lastStartTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_start_time"]
            )
        )
    if "last_stop_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["lastStopTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_stop_time"]
            )
        )
    if "last_modified_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["lastModifiedTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    if "end_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["endTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["end_time"]
            )
        )
    if "tools" in value:
        import capo_migrationhuborchestrator.types.tools_list

        out["tools"] = capo_migrationhuborchestrator.types.tools_list.serialize_json(
            value["tools"]
        )
    if "total_steps" in value:
        out["totalSteps"] = value["total_steps"]
    if "completed_steps" in value:
        out["completedSteps"] = value["completed_steps"]
    if "workflow_inputs" in value:
        import capo_migrationhuborchestrator.types.step_input_parameters

        out["workflowInputs"] = (
            capo_migrationhuborchestrator.types.step_input_parameters.serialize_json(
                value["workflow_inputs"]
            )
        )
    if "tags" in value:
        import capo_migrationhuborchestrator.types.string_map

        out["tags"] = capo_migrationhuborchestrator.types.string_map.serialize_json(
            value["tags"]
        )
    if "workflow_bucket" in value:
        out["workflowBucket"] = value["workflow_bucket"]
    return out


def deserialize_json(data: dict) -> GetMigrationWorkflowResponse:
    out: GetMigrationWorkflowResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("templateId") is not None:
        out["template_id"] = data["templateId"]
    if data.get("adsApplicationConfigurationId") is not None:
        out["ads_application_configuration_id"] = data["adsApplicationConfigurationId"]
    if data.get("adsApplicationName") is not None:
        out["ads_application_name"] = data["adsApplicationName"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("creationTime") is not None:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creation_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if data.get("lastStartTime") is not None:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["last_start_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastStartTime"]
            )
        )
    if data.get("lastStopTime") is not None:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["last_stop_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastStopTime"]
            )
        )
    if data.get("lastModifiedTime") is not None:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["last_modified_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    if data.get("endTime") is not None:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["end_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    if data.get("tools") is not None:
        import capo_migrationhuborchestrator.types.tools_list

        out["tools"] = capo_migrationhuborchestrator.types.tools_list.deserialize_json(
            data["tools"]
        )
    if data.get("totalSteps") is not None:
        out["total_steps"] = data["totalSteps"]
    if data.get("completedSteps") is not None:
        out["completed_steps"] = data["completedSteps"]
    if data.get("workflowInputs") is not None:
        import capo_migrationhuborchestrator.types.step_input_parameters

        out["workflow_inputs"] = (
            capo_migrationhuborchestrator.types.step_input_parameters.deserialize_json(
                data["workflowInputs"]
            )
        )
    if data.get("tags") is not None:
        import capo_migrationhuborchestrator.types.string_map

        out["tags"] = capo_migrationhuborchestrator.types.string_map.deserialize_json(
            data["tags"]
        )
    if data.get("workflowBucket") is not None:
        out["workflow_bucket"] = data["workflowBucket"]
    return out


def redact_sensitive(value: GetMigrationWorkflowResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "workflow_inputs" in value:
        out["workflow_inputs"] = "*** Sensitive Data Redacted ***"
    return out
