"""Generated from Smithy shape ``com.amazonaws.rds#DBInstanceMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_instance_list
    import capo_rds.types.string


class DBInstanceMessage(TypedDict, closed=True):
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code> .</p>"""
    db_instances: NotRequired["capo_rds.types.db_instance_list.DBInstanceList"]
    """<p>A list of <code>DBInstance</code> instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "db_instances" in value:
        import capo_rds.types.db_instance_list

        capo_rds.types.db_instance_list.serialize_query(
            value["db_instances"], pairs, f"{key_prefix}DBInstances"
        )


def deserialize_query(el: Element) -> DBInstanceMessage:
    out: DBInstanceMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_instances = el.find("DBInstances")
    if child_db_instances is not None:
        import capo_rds.types.db_instance_list

        out["db_instances"] = capo_rds.types.db_instance_list.deserialize_query(
            child_db_instances
        )
    return out


def redact_sensitive(value: DBInstanceMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "db_instances" in value:
        import capo_rds.types.db_instance_list

        out["db_instances"] = capo_rds.types.db_instance_list.redact_sensitive(
            value["db_instances"]
        )
    return out
