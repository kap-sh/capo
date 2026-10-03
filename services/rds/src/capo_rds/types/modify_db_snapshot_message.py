"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class ModifyDBSnapshotMessage(TypedDict, closed=True):
    db_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the DB snapshot to modify.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The engine version to upgrade the DB snapshot to.</p> <p>The following are the database engines and engine versions that are available when you upgrade a DB snapshot.</p> <p> <b>MariaDB</b> </p> <p>For the list of engine versions that are available for upgrading a DB snapshot, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mariadb-upgrade-snapshot.html"> Upgrading a MariaDB DB snapshot engine version</a> in the <i>Amazon RDS User Guide.</i> </p> <p> <b>MySQL</b> </p> <p>For the list of engine versions that are available for upgrading a DB snapshot, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-upgrade-snapshot.html"> Upgrading a MySQL DB snapshot engine version</a> in the <i>Amazon RDS User Guide.</i> </p> <p> <b>Oracle</b> </p> <ul> <li> <p> <code>21.0.0.0.ru-2025-04.rur-2025-04.r1</code> (supported for 21.0.0.0.ru-2022-01.rur-2022-01.r1, 21.0.0.0.ru-2022-04.rur-2022-04.r1, 21.0.0.0.ru-2022-07.rur-2022-07.r1, 21.0.0.0.ru-2022-10.rur-2022-10.r1, 21.0.0.0.ru-2023-01.rur-2023-01.r1 and 21.0.0.0.ru-2023-01.rur-2023-01.r2 DB snapshots)</p> </li> <li> <p> <code>19.0.0.0.ru-2025-04.rur-2025-04.r1</code> (supported for 19.0.0.0.ru-2019-07.rur-2019-07.r1, 19.0.0.0.ru-2019-10.rur-2019-10.r1 and 0.0.0.ru-2020-01.rur-2020-01.r1 DB snapshots)</p> </li> <li> <p> <code>19.0.0.0.ru-2022-01.rur-2022-01.r1</code> (supported for 12.2.0.1 DB snapshots)</p> </li> <li> <p> <code>19.0.0.0.ru-2022-07.rur-2022-07.r1</code> (supported for 12.1.0.2 DB snapshots)</p> </li> <li> <p> <code>12.1.0.2.v8</code> (supported for 12.1.0.1 DB snapshots)</p> </li> <li> <p> <code>11.2.0.4.v12</code> (supported for 11.2.0.2 DB snapshots)</p> </li> <li> <p> <code>11.2.0.4.v11</code> (supported for 11.2.0.3 DB snapshots)</p> </li> </ul> <p> <b>PostgreSQL</b> </p> <p>For the list of engine versions that are available for upgrading a DB snapshot, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBSnapshot.PostgreSQL.html"> Upgrading a PostgreSQL DB snapshot engine version</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The option group to identify with the upgraded DB snapshot.</p> <p>You can specify this parameter when you upgrade an Oracle DB snapshot. The same option group considerations apply when upgrading a DB snapshot as when upgrading a DB instance. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.html#USER_UpgradeDBInstance.Oracle.OGPG.OG">Option group considerations</a> in the <i>Amazon RDS User Guide.</i> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_snapshot_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBSnapshotIdentifier", str(value["db_snapshot_identifier"]))
        )
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "option_group_name" in value:
        pairs.append((f"{key_prefix}OptionGroupName", str(value["option_group_name"])))


def deserialize_query(el: Element) -> ModifyDBSnapshotMessage:
    out: ModifyDBSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_db_snapshot_identifier = el.find("DBSnapshotIdentifier")
    if child_db_snapshot_identifier is not None:
        out["db_snapshot_identifier"] = str(child_db_snapshot_identifier.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    return out
