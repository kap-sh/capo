"""Generated from Smithy shape ``com.amazonaws.migrationhub#PutResourceAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migration_hub.types.dry_run
    import capo_migration_hub.types.migration_task_name
    import capo_migration_hub.types.progress_update_stream
    import capo_migration_hub.types.resource_attribute_list


class PutResourceAttributesRequest(TypedDict, closed=True):
    progress_update_stream: (
        "capo_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the ProgressUpdateStream. </p>"""
    migration_task_name: (
        "capo_migration_hub.types.migration_task_name.MigrationTaskName"
    )
    """<p>Unique identifier that references the migration task. <i>Do not store personal data in this field.</i> </p>"""
    resource_attribute_list: (
        "capo_migration_hub.types.resource_attribute_list.ResourceAttributeList"
    )
    """<p>Information about the resource that is being migrated. This data will be used to map the task to a resource in the Application Discovery Service repository.</p> <note> <p>Takes the object array of <code>ResourceAttribute</code> where the <code>Type</code> field is reserved for the following values: <code>IPV4_ADDRESS | IPV6_ADDRESS | MAC_ADDRESS | FQDN | VM_MANAGER_ID | VM_MANAGED_OBJECT_REFERENCE | VM_NAME | VM_PATH | BIOS_ID | MOTHERBOARD_SERIAL_NUMBER</code> where the identifying value can be a string up to 256 characters.</p> </note> <important> <ul> <li> <p>If any "VM" related value is set for a <code>ResourceAttribute</code> object, it is required that <code>VM_MANAGER_ID</code>, as a minimum, is always set. If <code>VM_MANAGER_ID</code> is not set, then all "VM" fields will be discarded and "VM" fields will not be used for matching the migration task to a server in Application Discovery Service repository. See the <a href="https://docs.aws.amazon.com/migrationhub/latest/ug/API_PutResourceAttributes.html#API_PutResourceAttributes_Examples">Example</a> section below for a use case of specifying "VM" related values.</p> </li> <li> <p> If a server you are trying to match has multiple IP or MAC addresses, you should provide as many as you know in separate type/value pairs passed to the <code>ResourceAttributeList</code> parameter to maximize the chances of matching.</p> </li> </ul> </important>"""
    dry_run: "capo_migration_hub.types.dry_run.DryRun"
    """<p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourceAttributesRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStream"] = value["progress_update_stream"]
    out["MigrationTaskName"] = value["migration_task_name"]
    import capo_migration_hub.types.resource_attribute_list

    out["ResourceAttributeList"] = (
        capo_migration_hub.types.resource_attribute_list.serialize_aws_json_1_1(
            value["resource_attribute_list"]
        )
    )
    out["DryRun"] = value.get("dry_run", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourceAttributesRequest:
    out: PutResourceAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProgressUpdateStream") is not None:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    else:
        raise DeserializationError(
            "PutResourceAttributesRequest.progress_update_stream required"
        )
    if data.get("MigrationTaskName") is not None:
        out["migration_task_name"] = data["MigrationTaskName"]
    else:
        raise DeserializationError(
            "PutResourceAttributesRequest.migration_task_name required"
        )
    if data.get("ResourceAttributeList") is not None:
        import capo_migration_hub.types.resource_attribute_list

        out["resource_attribute_list"] = (
            capo_migration_hub.types.resource_attribute_list.deserialize_aws_json_1_1(
                data["ResourceAttributeList"]
            )
        )
    else:
        raise DeserializationError(
            "PutResourceAttributesRequest.resource_attribute_list required"
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    return out
