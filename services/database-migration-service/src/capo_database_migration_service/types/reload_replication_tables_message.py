"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReloadReplicationTablesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.reload_option_value
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.table_list_to_reload


class ReloadReplicationTablesMessage(TypedDict, closed=True):
    replication_config_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name of the replication config for which to reload tables.</p>"""
    tables_to_reload: (
        "capo_database_migration_service.types.table_list_to_reload.TableListToReload"
    )
    """<p>The list of tables to reload.</p>"""
    reload_option: NotRequired[
        "capo_database_migration_service.types.reload_option_value.ReloadOptionValue"
    ]
    """<p>Options for reload. Specify <code>data-reload</code> to reload the data and re-validate it if validation is enabled. Specify <code>validate-only</code> to re-validate the table. This option applies only when validation is enabled for the replication. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReloadReplicationTablesMessage) -> dict:
    out: dict = {}
    out["ReplicationConfigArn"] = value["replication_config_arn"]
    import capo_database_migration_service.types.table_list_to_reload

    out["TablesToReload"] = (
        capo_database_migration_service.types.table_list_to_reload.serialize_aws_json_1_1(
            value["tables_to_reload"]
        )
    )
    if "reload_option" in value:
        import capo_database_migration_service.types.reload_option_value

        out["ReloadOption"] = (
            capo_database_migration_service.types.reload_option_value.serialize_aws_json_1_1(
                value["reload_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReloadReplicationTablesMessage:
    out: ReloadReplicationTablesMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationConfigArn") is not None:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    else:
        out["replication_config_arn"] = ""
    if data.get("TablesToReload") is not None:
        import capo_database_migration_service.types.table_list_to_reload

        out["tables_to_reload"] = (
            capo_database_migration_service.types.table_list_to_reload.deserialize_aws_json_1_1(
                data["TablesToReload"]
            )
        )
    else:
        out["tables_to_reload"] = []
    if data.get("ReloadOption") is not None:
        import capo_database_migration_service.types.reload_option_value

        out["reload_option"] = (
            capo_database_migration_service.types.reload_option_value.deserialize_aws_json_1_1(
                data["ReloadOption"]
            )
        )
    return out
