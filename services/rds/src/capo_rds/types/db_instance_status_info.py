"""Generated from Smithy shape ``com.amazonaws.rds#DBInstanceStatusInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.string


class DBInstanceStatusInfo(TypedDict, closed=True):
    status_type: NotRequired["capo_rds.types.string.String"]
    """<p>This value is currently "read replication."</p>"""
    normal: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the instance is operating normally (TRUE) or is in an error state (FALSE).</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of the DB instance. For a StatusType of read replica, the values can be replicating, replication stop point set, replication stop point reached, error, stopped, or terminated.</p>"""
    message: NotRequired["capo_rds.types.string.String"]
    """<p>Details of the error if there is an error for the instance. If the instance isn't in an error state, this value is blank.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceStatusInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status_type" in value:
        pairs.append((f"{key_prefix}StatusType", str(value["status_type"])))
    if "normal" in value:
        pairs.append((f"{key_prefix}Normal", "true" if value["normal"] else "false"))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> DBInstanceStatusInfo:
    out: DBInstanceStatusInfo = {}  # type: ignore[typeddict-item]
    child_status_type = el.find("StatusType")
    if child_status_type is not None:
        out["status_type"] = str(child_status_type.text or "")
    child_normal = el.find("Normal")
    if child_normal is not None:
        out["normal"] = (child_normal.text or "").lower() == "true"
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
