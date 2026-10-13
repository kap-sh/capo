"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationExecution``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mgn.types.execution_stage
    import capo_mgn.types.execution_stage_activity
    import capo_mgn.types.execution_status
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_execution_id
    import capo_mgn.types.tags_map


class NetworkMigrationExecution(TypedDict, closed=True):
    network_migration_definition_id: NotRequired[
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    ]
    """<p>The unique identifier of the network migration definition used by this execution.</p>"""
    network_migration_execution_id: NotRequired[
        "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    ]
    """<p>The unique identifier of the execution.</p>"""
    status: NotRequired["capo_mgn.types.execution_status.ExecutionStatus"]
    """<p>The current status of the execution.</p>"""
    stage: NotRequired["capo_mgn.types.execution_stage.ExecutionStage"]
    """<p>The current stage of the execution in the migration workflow.</p>"""
    activity: NotRequired[
        "capo_mgn.types.execution_stage_activity.ExecutionStageActivity"
    ]
    """<p>The current activity being performed in the execution.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the execution was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the execution was last updated.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Tags assigned to the execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationExecution) -> dict:
    out: dict = {}
    if "network_migration_definition_id" in value:
        out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "network_migration_execution_id" in value:
        out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "stage" in value:
        out["stage"] = value["stage"]
    if "activity" in value:
        out["activity"] = value["activity"]
    if "created_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["createdAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["updatedAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> NetworkMigrationExecution:
    out: NetworkMigrationExecution = {}  # type: ignore[typeddict-item]
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    if data.get("networkMigrationExecutionID") is not None:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("stage") is not None:
        out["stage"] = data["stage"]
    if data.get("activity") is not None:
        out["activity"] = data["activity"]
    if data.get("createdAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["created_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["updated_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: NetworkMigrationExecution) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
