"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReloadTablesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.reload_option_value
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.table_list_to_reload


class ReloadTablesMessage(TypedDict, closed=True):
    replication_task_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the replication task. </p>"""
    tables_to_reload: (
        "capo_database_migration_service.types.table_list_to_reload.TableListToReload"
    )
    """<p>The name and schema of the table to be reloaded. </p>"""
    reload_option: NotRequired[
        "capo_database_migration_service.types.reload_option_value.ReloadOptionValue"
    ]
    """<p>Options for reload. Specify <code>data-reload</code> to reload the data and re-validate it if validation is enabled. Specify <code>validate-only</code> to re-validate the table. This option applies only when validation is enabled for the task. </p> <p>Valid values: data-reload, validate-only</p> <p>Default value is data-reload.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReloadTablesMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskArn"] = value["replication_task_arn"]
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


def deserialize_aws_json_1_1(data: dict) -> ReloadTablesMessage:
    out: ReloadTablesMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationTaskArn") is not None:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    else:
        out["replication_task_arn"] = ""
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
