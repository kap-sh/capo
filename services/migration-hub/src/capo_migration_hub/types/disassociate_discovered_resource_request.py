"""Generated from Smithy shape ``com.amazonaws.migrationhub#DisassociateDiscoveredResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.configuration_id
    import capo_migration_hub.types.dry_run
    import capo_migration_hub.types.migration_task_name
    import capo_migration_hub.types.progress_update_stream


class DisassociateDiscoveredResourceRequest(TypedDict, closed=True):
    progress_update_stream: (
        "capo_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the ProgressUpdateStream.</p>"""
    migration_task_name: (
        "capo_migration_hub.types.migration_task_name.MigrationTaskName"
    )
    """<p>The identifier given to the MigrationTask. <i>Do not store personal data in this field.</i> </p>"""
    configuration_id: "capo_migration_hub.types.configuration_id.ConfigurationId"
    """<p>ConfigurationId of the Application Discovery Service resource to be disassociated.</p>"""
    dry_run: NotRequired["capo_migration_hub.types.dry_run.DryRun"]
    """<p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateDiscoveredResourceRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStream"] = value["progress_update_stream"]
    out["MigrationTaskName"] = value["migration_task_name"]
    out["ConfigurationId"] = value["configuration_id"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateDiscoveredResourceRequest:
    out: DisassociateDiscoveredResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProgressUpdateStream") is not None:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    else:
        out["progress_update_stream"] = ""
    if data.get("MigrationTaskName") is not None:
        out["migration_task_name"] = data["MigrationTaskName"]
    else:
        out["migration_task_name"] = ""
    if data.get("ConfigurationId") is not None:
        out["configuration_id"] = data["ConfigurationId"]
    else:
        out["configuration_id"] = ""
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
