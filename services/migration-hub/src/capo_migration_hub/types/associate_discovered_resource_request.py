"""Generated from Smithy shape ``com.amazonaws.migrationhub#AssociateDiscoveredResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migration_hub.types.discovered_resource
    import capo_migration_hub.types.dry_run
    import capo_migration_hub.types.migration_task_name
    import capo_migration_hub.types.progress_update_stream


class AssociateDiscoveredResourceRequest(TypedDict, closed=True):
    progress_update_stream: (
        "capo_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the ProgressUpdateStream.</p>"""
    migration_task_name: (
        "capo_migration_hub.types.migration_task_name.MigrationTaskName"
    )
    """<p>The identifier given to the MigrationTask. <i>Do not store personal data in this field.</i> </p>"""
    discovered_resource: (
        "capo_migration_hub.types.discovered_resource.DiscoveredResource"
    )
    """<p>Object representing a Resource.</p>"""
    dry_run: NotRequired["capo_migration_hub.types.dry_run.DryRun"]
    """<p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateDiscoveredResourceRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStream"] = value["progress_update_stream"]
    out["MigrationTaskName"] = value["migration_task_name"]
    import capo_migration_hub.types.discovered_resource

    out["DiscoveredResource"] = (
        capo_migration_hub.types.discovered_resource.serialize_aws_json_1_1(
            value["discovered_resource"]
        )
    )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateDiscoveredResourceRequest:
    out: AssociateDiscoveredResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProgressUpdateStream") is not None:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    else:
        raise DeserializationError(
            "AssociateDiscoveredResourceRequest.progress_update_stream required"
        )
    if data.get("MigrationTaskName") is not None:
        out["migration_task_name"] = data["MigrationTaskName"]
    else:
        raise DeserializationError(
            "AssociateDiscoveredResourceRequest.migration_task_name required"
        )
    if data.get("DiscoveredResource") is not None:
        import capo_migration_hub.types.discovered_resource

        out["discovered_resource"] = (
            capo_migration_hub.types.discovered_resource.deserialize_aws_json_1_1(
                data["DiscoveredResource"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateDiscoveredResourceRequest.discovered_resource required"
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
