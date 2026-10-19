"""Generated from Smithy shape ``com.amazonaws.migrationhub#AssociateCreatedArtifactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migration_hub.types.created_artifact
    import capo_migration_hub.types.dry_run
    import capo_migration_hub.types.migration_task_name
    import capo_migration_hub.types.progress_update_stream


class AssociateCreatedArtifactRequest(TypedDict, closed=True):
    progress_update_stream: (
        "capo_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the ProgressUpdateStream. </p>"""
    migration_task_name: (
        "capo_migration_hub.types.migration_task_name.MigrationTaskName"
    )
    """<p>Unique identifier that references the migration task. <i>Do not store personal data in this field.</i> </p>"""
    created_artifact: "capo_migration_hub.types.created_artifact.CreatedArtifact"
    """<p>An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.) </p>"""
    dry_run: NotRequired["capo_migration_hub.types.dry_run.DryRun"]
    """<p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateCreatedArtifactRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStream"] = value["progress_update_stream"]
    out["MigrationTaskName"] = value["migration_task_name"]
    import capo_migration_hub.types.created_artifact

    out["CreatedArtifact"] = (
        capo_migration_hub.types.created_artifact.serialize_aws_json_1_1(
            value["created_artifact"]
        )
    )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateCreatedArtifactRequest:
    out: AssociateCreatedArtifactRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProgressUpdateStream") is not None:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    else:
        out["progress_update_stream"] = ""
    if data.get("MigrationTaskName") is not None:
        out["migration_task_name"] = data["MigrationTaskName"]
    else:
        out["migration_task_name"] = ""
    if data.get("CreatedArtifact") is not None:
        import capo_migration_hub.types.created_artifact

        out["created_artifact"] = (
            capo_migration_hub.types.created_artifact.deserialize_aws_json_1_1(
                data["CreatedArtifact"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateCreatedArtifactRequest.created_artifact required"
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
