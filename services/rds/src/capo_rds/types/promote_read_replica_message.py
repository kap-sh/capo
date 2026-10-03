"""Generated from Smithy shape ``com.amazonaws.rds#PromoteReadReplicaMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.integer_optional
    import capo_rds.types.string
    import capo_rds.types.tag_specification_list


class PromoteReadReplicaMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB instance identifier. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing read replica DB instance.</p> </li> </ul> <p>Example: <code>mydbinstance</code> </p>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.</p> <p>Default: 1</p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 0 to 35.</p> </li> <li> <p>Can't be set to 0 if the DB instance is a source to read replicas.</p> </li> </ul>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, using the <code>BackupRetentionPeriod</code> parameter.</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. To see the time blocks available, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AdjustingTheMaintenanceWindow.html"> Adjusting the Preferred Maintenance Window</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    tag_specifications: NotRequired[
        "capo_rds.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tags to assign to resources associated with the DB instance.</p> <p>Valid Values: </p> <ul> <li> <p> <code>auto-backup</code> - The DB instance's automated backup.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PromoteReadReplicaMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "backup_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}BackupRetentionPeriod",
                str(value["backup_retention_period"]),
            )
        )
    if "preferred_backup_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredBackupWindow",
                str(value["preferred_backup_window"]),
            )
        )
    if "tag_specifications" in value:
        import capo_rds.types.tag_specification_list

        capo_rds.types.tag_specification_list.serialize_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecifications"
        )


def deserialize_query(el: Element) -> PromoteReadReplicaMessage:
    out: PromoteReadReplicaMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_tag_specifications = el.find("TagSpecifications")
    if child_tag_specifications is not None:
        import capo_rds.types.tag_specification_list

        out["tag_specifications"] = (
            capo_rds.types.tag_specification_list.deserialize_query(
                child_tag_specifications
            )
        )
    return out
