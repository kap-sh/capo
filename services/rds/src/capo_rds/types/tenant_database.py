"""Generated from Smithy shape ``com.amazonaws.rds#TenantDatabase``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.master_user_secret
    import capo_rds.types.string
    import capo_rds.types.t_stamp
    import capo_rds.types.tag_list
    import capo_rds.types.tenant_database_pending_modified_values


class TenantDatabase(TypedDict, closed=True):
    tenant_database_create_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The creation time of the tenant database.</p>"""
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The ID of the DB instance that contains the tenant database.</p>"""
    tenant_db_name: NotRequired["capo_rds.types.string.String"]
    """<p>The database name of the tenant database.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of the tenant database.</p>"""
    master_username: NotRequired["capo_rds.types.string.String"]
    """<p>The master username of the tenant database.</p>"""
    dbi_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services Region-unique, immutable identifier for the DB instance.</p>"""
    tenant_database_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services Region-unique, immutable identifier for the tenant database.</p>"""
    tenant_database_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the tenant database.</p>"""
    character_set_name: NotRequired["capo_rds.types.string.String"]
    """<p>The character set of the tenant database.</p>"""
    nchar_character_set_name: NotRequired["capo_rds.types.string.String"]
    """<p>The <code>NCHAR</code> character set name of the tenant database.</p>"""
    deletion_protection: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether deletion protection is enabled for the DB instance.</p>"""
    pending_modified_values: NotRequired[
        "capo_rds.types.tenant_database_pending_modified_values.TenantDatabasePendingModifiedValues"
    ]
    """<p>Information about pending changes for a tenant database.</p>"""
    master_user_secret: NotRequired[
        "capo_rds.types.master_user_secret.MasterUserSecret"
    ]
    tag_list: NotRequired["capo_rds.types.tag_list.TagList"]


# --- awsQuery ser/de ---
def serialize_query(
    value: TenantDatabase, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "tenant_database_create_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["tenant_database_create_time"],
            pairs,
            f"{key_prefix}TenantDatabaseCreateTime",
        )
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "tenant_db_name" in value:
        pairs.append((f"{key_prefix}TenantDBName", str(value["tenant_db_name"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "dbi_resource_id" in value:
        pairs.append((f"{key_prefix}DbiResourceId", str(value["dbi_resource_id"])))
    if "tenant_database_resource_id" in value:
        pairs.append(
            (
                f"{key_prefix}TenantDatabaseResourceId",
                str(value["tenant_database_resource_id"]),
            )
        )
    if "tenant_database_arn" in value:
        pairs.append(
            (f"{key_prefix}TenantDatabaseARN", str(value["tenant_database_arn"]))
        )
    if "character_set_name" in value:
        pairs.append(
            (f"{key_prefix}CharacterSetName", str(value["character_set_name"]))
        )
    if "nchar_character_set_name" in value:
        pairs.append(
            (
                f"{key_prefix}NcharCharacterSetName",
                str(value["nchar_character_set_name"]),
            )
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "pending_modified_values" in value:
        import capo_rds.types.tenant_database_pending_modified_values

        capo_rds.types.tenant_database_pending_modified_values.serialize_query(
            value["pending_modified_values"],
            pairs,
            f"{key_prefix}PendingModifiedValues",
        )
    if "master_user_secret" in value:
        import capo_rds.types.master_user_secret

        capo_rds.types.master_user_secret.serialize_query(
            value["master_user_secret"], pairs, f"{key_prefix}MasterUserSecret"
        )
    if "tag_list" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{key_prefix}TagList"
        )


def deserialize_query(el: Element) -> TenantDatabase:
    out: TenantDatabase = {}  # type: ignore[typeddict-item]
    child_tenant_database_create_time = el.find("TenantDatabaseCreateTime")
    if child_tenant_database_create_time is not None:
        import capo_rds.types.t_stamp

        out["tenant_database_create_time"] = capo_rds.types.t_stamp.deserialize_query(
            child_tenant_database_create_time
        )
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_tenant_db_name = el.find("TenantDBName")
    if child_tenant_db_name is not None:
        out["tenant_db_name"] = str(child_tenant_db_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_dbi_resource_id = el.find("DbiResourceId")
    if child_dbi_resource_id is not None:
        out["dbi_resource_id"] = str(child_dbi_resource_id.text or "")
    child_tenant_database_resource_id = el.find("TenantDatabaseResourceId")
    if child_tenant_database_resource_id is not None:
        out["tenant_database_resource_id"] = str(
            child_tenant_database_resource_id.text or ""
        )
    child_tenant_database_arn = el.find("TenantDatabaseARN")
    if child_tenant_database_arn is not None:
        out["tenant_database_arn"] = str(child_tenant_database_arn.text or "")
    child_character_set_name = el.find("CharacterSetName")
    if child_character_set_name is not None:
        out["character_set_name"] = str(child_character_set_name.text or "")
    child_nchar_character_set_name = el.find("NcharCharacterSetName")
    if child_nchar_character_set_name is not None:
        out["nchar_character_set_name"] = str(child_nchar_character_set_name.text or "")
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_pending_modified_values = el.find("PendingModifiedValues")
    if child_pending_modified_values is not None:
        import capo_rds.types.tenant_database_pending_modified_values

        out["pending_modified_values"] = (
            capo_rds.types.tenant_database_pending_modified_values.deserialize_query(
                child_pending_modified_values
            )
        )
    child_master_user_secret = el.find("MasterUserSecret")
    if child_master_user_secret is not None:
        import capo_rds.types.master_user_secret

        out["master_user_secret"] = capo_rds.types.master_user_secret.deserialize_query(
            child_master_user_secret
        )
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_rds.types.tag_list

        out["tag_list"] = capo_rds.types.tag_list.deserialize_query(child_tag_list)
    return out


def redact_sensitive(value: TenantDatabase) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pending_modified_values" in value:
        import capo_rds.types.tenant_database_pending_modified_values

        out["pending_modified_values"] = (
            capo_rds.types.tenant_database_pending_modified_values.redact_sensitive(
                value["pending_modified_values"]
            )
        )
    return out
