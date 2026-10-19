"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RestoreTableFromSnapshotRequest``."""

from typing_extensions import NotRequired, TypedDict


class RestoreTableFromSnapshotRequest(TypedDict, closed=True):
    namespace_name: "str"
    """<p>The namespace of the snapshot to restore from.</p>"""
    workgroup_name: "str"
    """<p>The workgroup to restore the table to.</p>"""
    snapshot_name: "str"
    """<p>The name of the snapshot to restore the table from.</p>"""
    source_database_name: "str"
    """<p>The name of the source database that contains the table being restored.</p>"""
    source_schema_name: NotRequired["str"]
    """<p>The name of the source schema that contains the table being restored.</p>"""
    source_table_name: "str"
    """<p>The name of the source table being restored.</p>"""
    target_database_name: NotRequired["str"]
    """<p>The name of the database to restore the table to.</p>"""
    target_schema_name: NotRequired["str"]
    """<p>The name of the schema to restore the table to.</p>"""
    new_table_name: "str"
    """<p>The name of the table to create from the restore operation.</p>"""
    activate_case_sensitive_identifier: NotRequired["bool"]
    """<p>Indicates whether name identifiers for database, schema, and table are case sensitive. If true, the names are case sensitive. If false, the names are not case sensitive. The default is false.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreTableFromSnapshotRequest) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    out["workgroupName"] = value["workgroup_name"]
    out["snapshotName"] = value["snapshot_name"]
    out["sourceDatabaseName"] = value["source_database_name"]
    if "source_schema_name" in value:
        out["sourceSchemaName"] = value["source_schema_name"]
    out["sourceTableName"] = value["source_table_name"]
    if "target_database_name" in value:
        out["targetDatabaseName"] = value["target_database_name"]
    if "target_schema_name" in value:
        out["targetSchemaName"] = value["target_schema_name"]
    out["newTableName"] = value["new_table_name"]
    if "activate_case_sensitive_identifier" in value:
        out["activateCaseSensitiveIdentifier"] = value[
            "activate_case_sensitive_identifier"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreTableFromSnapshotRequest:
    out: RestoreTableFromSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    else:
        out["namespace_name"] = ""
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    else:
        out["workgroup_name"] = ""
    if data.get("snapshotName") is not None:
        out["snapshot_name"] = data["snapshotName"]
    else:
        out["snapshot_name"] = ""
    if data.get("sourceDatabaseName") is not None:
        out["source_database_name"] = data["sourceDatabaseName"]
    else:
        out["source_database_name"] = ""
    if data.get("sourceSchemaName") is not None:
        out["source_schema_name"] = data["sourceSchemaName"]
    if data.get("sourceTableName") is not None:
        out["source_table_name"] = data["sourceTableName"]
    else:
        out["source_table_name"] = ""
    if data.get("targetDatabaseName") is not None:
        out["target_database_name"] = data["targetDatabaseName"]
    if data.get("targetSchemaName") is not None:
        out["target_schema_name"] = data["targetSchemaName"]
    if data.get("newTableName") is not None:
        out["new_table_name"] = data["newTableName"]
    else:
        out["new_table_name"] = ""
    if data.get("activateCaseSensitiveIdentifier") is not None:
        out["activate_case_sensitive_identifier"] = data[
            "activateCaseSensitiveIdentifier"
        ]
    return out
