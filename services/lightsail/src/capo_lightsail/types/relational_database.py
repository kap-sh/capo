"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.pending_maintenance_action_list
    import capo_lightsail.types.pending_modified_relational_database_values
    import capo_lightsail.types.relational_database_endpoint
    import capo_lightsail.types.relational_database_hardware
    import capo_lightsail.types.resource_location
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_type
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list


class RelationalDatabase(TypedDict, closed=True):
    name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The unique name of the database resource in Lightsail.</p>"""
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the database.</p>"""
    support_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The support code for the database. Include this code in your email to support when you have questions about a database in Lightsail. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the database was created. Formatted in Unix time.</p>"""
    location: NotRequired["capo_lightsail.types.resource_location.ResourceLocation"]
    """<p>The Region name and Availability Zone where the database is located.</p>"""
    resource_type: NotRequired["capo_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type for the database (for example, <code>RelationalDatabase</code>).</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Amazon Lightsail Developer Guide</a>.</p>"""
    relational_database_blueprint_id: NotRequired[
        "capo_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The blueprint ID for the database. A blueprint describes the major engine version of a database.</p>"""
    relational_database_bundle_id: NotRequired[
        "capo_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The bundle ID for the database. A bundle describes the performance specifications for your database.</p>"""
    master_database_name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The name of the master database created when the Lightsail database resource is created.</p>"""
    hardware: NotRequired[
        "capo_lightsail.types.relational_database_hardware.RelationalDatabaseHardware"
    ]
    """<p>Describes the hardware of the database.</p>"""
    state: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>Describes the current state of the database.</p>"""
    secondary_availability_zone: NotRequired["capo_lightsail.types.string.string"]
    """<p>Describes the secondary Availability Zone of a high availability database.</p> <p>The secondary database is used for failover support of a high availability database.</p>"""
    backup_retention_enabled: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether automated backup retention is enabled for the database.</p>"""
    pending_modified_values: NotRequired[
        "capo_lightsail.types.pending_modified_relational_database_values.PendingModifiedRelationalDatabaseValues"
    ]
    """<p>Describes pending database value modifications.</p>"""
    engine: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The database software (for example, <code>MySQL</code>).</p>"""
    engine_version: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The database engine version (for example, <code>5.7.23</code>).</p>"""
    latest_restorable_time: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The latest point in time to which the database can be restored. Formatted in Unix time.</p>"""
    master_username: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The master user name of the database.</p>"""
    parameter_apply_status: NotRequired[
        "capo_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of parameter updates for the database.</p>"""
    preferred_backup_window: NotRequired[
        "capo_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The daily time range during which automated backups are created for the database (for example, <code>16:00-16:30</code>).</p>"""
    preferred_maintenance_window: NotRequired[
        "capo_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The weekly time range during which system maintenance can occur on the database.</p> <p>In the format <code>ddd:hh24:mi-ddd:hh24:mi</code>. For example, <code>Tue:17:00-Tue:17:30</code>.</p>"""
    publicly_accessible: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the database is publicly accessible.</p>"""
    master_endpoint: NotRequired[
        "capo_lightsail.types.relational_database_endpoint.RelationalDatabaseEndpoint"
    ]
    """<p>The master endpoint for the database.</p>"""
    pending_maintenance_actions: NotRequired[
        "capo_lightsail.types.pending_maintenance_action_list.PendingMaintenanceActionList"
    ]
    """<p>Describes the pending maintenance actions for the database.</p>"""
    ca_certificate_identifier: NotRequired["capo_lightsail.types.string.string"]
    """<p>The certificate associated with the database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabase) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import capo_lightsail.types.resource_location

        out["location"] = capo_lightsail.types.resource_location.serialize_aws_json_1_1(
            value["location"]
        )
    if "resource_type" in value:
        import capo_lightsail.types.resource_type

        out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "relational_database_blueprint_id" in value:
        out["relationalDatabaseBlueprintId"] = value["relational_database_blueprint_id"]
    if "relational_database_bundle_id" in value:
        out["relationalDatabaseBundleId"] = value["relational_database_bundle_id"]
    if "master_database_name" in value:
        out["masterDatabaseName"] = value["master_database_name"]
    if "hardware" in value:
        import capo_lightsail.types.relational_database_hardware

        out["hardware"] = (
            capo_lightsail.types.relational_database_hardware.serialize_aws_json_1_1(
                value["hardware"]
            )
        )
    if "state" in value:
        out["state"] = value["state"]
    if "secondary_availability_zone" in value:
        out["secondaryAvailabilityZone"] = value["secondary_availability_zone"]
    if "backup_retention_enabled" in value:
        out["backupRetentionEnabled"] = value["backup_retention_enabled"]
    if "pending_modified_values" in value:
        import capo_lightsail.types.pending_modified_relational_database_values

        out["pendingModifiedValues"] = (
            capo_lightsail.types.pending_modified_relational_database_values.serialize_aws_json_1_1(
                value["pending_modified_values"]
            )
        )
    if "engine" in value:
        out["engine"] = value["engine"]
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "latest_restorable_time" in value:
        import capo_lightsail.types.iso_date

        out["latestRestorableTime"] = (
            capo_lightsail.types.iso_date.serialize_aws_json_1_1(
                value["latest_restorable_time"]
            )
        )
    if "master_username" in value:
        out["masterUsername"] = value["master_username"]
    if "parameter_apply_status" in value:
        out["parameterApplyStatus"] = value["parameter_apply_status"]
    if "preferred_backup_window" in value:
        out["preferredBackupWindow"] = value["preferred_backup_window"]
    if "preferred_maintenance_window" in value:
        out["preferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "master_endpoint" in value:
        import capo_lightsail.types.relational_database_endpoint

        out["masterEndpoint"] = (
            capo_lightsail.types.relational_database_endpoint.serialize_aws_json_1_1(
                value["master_endpoint"]
            )
        )
    if "pending_maintenance_actions" in value:
        import capo_lightsail.types.pending_maintenance_action_list

        out["pendingMaintenanceActions"] = (
            capo_lightsail.types.pending_maintenance_action_list.serialize_aws_json_1_1(
                value["pending_maintenance_actions"]
            )
        )
    if "ca_certificate_identifier" in value:
        out["caCertificateIdentifier"] = value["ca_certificate_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RelationalDatabase:
    out: RelationalDatabase = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("supportCode") is not None:
        out["support_code"] = data["supportCode"]
    if data.get("createdAt") is not None:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("location") is not None:
        import capo_lightsail.types.resource_location

        out["location"] = (
            capo_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("relationalDatabaseBlueprintId") is not None:
        out["relational_database_blueprint_id"] = data["relationalDatabaseBlueprintId"]
    if data.get("relationalDatabaseBundleId") is not None:
        out["relational_database_bundle_id"] = data["relationalDatabaseBundleId"]
    if data.get("masterDatabaseName") is not None:
        out["master_database_name"] = data["masterDatabaseName"]
    if data.get("hardware") is not None:
        import capo_lightsail.types.relational_database_hardware

        out["hardware"] = (
            capo_lightsail.types.relational_database_hardware.deserialize_aws_json_1_1(
                data["hardware"]
            )
        )
    if data.get("state") is not None:
        out["state"] = data["state"]
    if data.get("secondaryAvailabilityZone") is not None:
        out["secondary_availability_zone"] = data["secondaryAvailabilityZone"]
    if data.get("backupRetentionEnabled") is not None:
        out["backup_retention_enabled"] = data["backupRetentionEnabled"]
    if data.get("pendingModifiedValues") is not None:
        import capo_lightsail.types.pending_modified_relational_database_values

        out["pending_modified_values"] = (
            capo_lightsail.types.pending_modified_relational_database_values.deserialize_aws_json_1_1(
                data["pendingModifiedValues"]
            )
        )
    if data.get("engine") is not None:
        out["engine"] = data["engine"]
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    if data.get("latestRestorableTime") is not None:
        import capo_lightsail.types.iso_date

        out["latest_restorable_time"] = (
            capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
                data["latestRestorableTime"]
            )
        )
    if data.get("masterUsername") is not None:
        out["master_username"] = data["masterUsername"]
    if data.get("parameterApplyStatus") is not None:
        out["parameter_apply_status"] = data["parameterApplyStatus"]
    if data.get("preferredBackupWindow") is not None:
        out["preferred_backup_window"] = data["preferredBackupWindow"]
    if data.get("preferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["preferredMaintenanceWindow"]
    if data.get("publiclyAccessible") is not None:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if data.get("masterEndpoint") is not None:
        import capo_lightsail.types.relational_database_endpoint

        out["master_endpoint"] = (
            capo_lightsail.types.relational_database_endpoint.deserialize_aws_json_1_1(
                data["masterEndpoint"]
            )
        )
    if data.get("pendingMaintenanceActions") is not None:
        import capo_lightsail.types.pending_maintenance_action_list

        out["pending_maintenance_actions"] = (
            capo_lightsail.types.pending_maintenance_action_list.deserialize_aws_json_1_1(
                data["pendingMaintenanceActions"]
            )
        )
    if data.get("caCertificateIdentifier") is not None:
        out["ca_certificate_identifier"] = data["caCertificateIdentifier"]
    return out
