"""Generated from Smithy shape ``com.amazonaws.rds#ConnectionPoolConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.integer_optional
    import capo_rds.types.operator_sensitive_string
    import capo_rds.types.string_list


class ConnectionPoolConfiguration(TypedDict, closed=True):
    max_connections_percent: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum size of the connection pool for each target in a target group. The value is expressed as a percentage of the <code>max_connections</code> setting for the RDS DB instance or Aurora DB cluster used by the target group.</p> <p>If you specify <code>MaxIdleConnectionsPercent</code>, then you must also include a value for this parameter.</p> <p>Default: <code>10</code> for RDS for Microsoft SQL Server, and <code>100</code> for all other engines</p> <p>Constraints:</p> <ul> <li> <p>Must be between 1 and 100.</p> </li> </ul>"""
    max_idle_connections_percent: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>A value that controls how actively the proxy closes idle database connections in the connection pool. The value is expressed as a percentage of the <code>max_connections</code> setting for the RDS DB instance or Aurora DB cluster used by the target group. With a high value, the proxy leaves a high percentage of idle database connections open. A low value causes the proxy to close more idle connections and return them to the database.</p> <p>If you specify this parameter, then you must also include a value for <code>MaxConnectionsPercent</code>.</p> <p>Default: The default value is half of the value of <code>MaxConnectionsPercent</code>. For example, if <code>MaxConnectionsPercent</code> is 80, then the default value of <code>MaxIdleConnectionsPercent</code> is 40. If the value of <code>MaxConnectionsPercent</code> isn't specified, then for SQL Server, <code>MaxIdleConnectionsPercent</code> is <code>5</code>, and for all other engines, the default is <code>50</code>.</p> <p>Constraints:</p> <ul> <li> <p>Must be between 0 and the value of <code>MaxConnectionsPercent</code>.</p> </li> </ul>"""
    connection_borrow_timeout: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of seconds for a proxy to wait for a connection to become available in the connection pool. This setting only applies when the proxy has opened its maximum number of connections and all connections are busy with client sessions.</p> <p>Default: <code>120</code> </p> <p>Constraints:</p> <ul> <li> <p>Must be between 0 and 300.</p> </li> </ul>"""
    session_pinning_filters: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>Each item in the list represents a class of SQL operations that normally cause all later statements in a session using a proxy to be pinned to the same underlying database connection. Including an item in the list exempts that class of SQL operations from the pinning behavior.</p> <p>Default: no session pinning filters</p>"""
    init_query: NotRequired[
        "capo_rds.types.operator_sensitive_string.OperatorSensitiveString"
    ]
    """<p>Add an initialization query, or modify the current one. You can specify one or more SQL statements for the proxy to run when opening each new database connection. The setting is typically used with <code>SET</code> statements to make sure that each connection has identical settings. Make sure the query added here is valid. This is an optional field, so you can choose to leave it empty. For including multiple variables in a single SET statement, use a comma separator.</p> <p>For example: <code>SET variable1=value1, variable2=value2</code> </p> <p>Default: no initialization query</p> <important> <p>Since you can access initialization query as part of target group configuration, it is not protected by authentication or cryptographic methods. Anyone with access to view or manage your proxy target group configuration can view the initialization query. You should not add sensitive data, such as passwords or long-lived encryption keys, to this option.</p> </important>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConnectionPoolConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "max_connections_percent" in value:
        pairs.append(
            (
                f"{key_prefix}MaxConnectionsPercent",
                str(value["max_connections_percent"]),
            )
        )
    if "max_idle_connections_percent" in value:
        pairs.append(
            (
                f"{key_prefix}MaxIdleConnectionsPercent",
                str(value["max_idle_connections_percent"]),
            )
        )
    if "connection_borrow_timeout" in value:
        pairs.append(
            (
                f"{key_prefix}ConnectionBorrowTimeout",
                str(value["connection_borrow_timeout"]),
            )
        )
    if "session_pinning_filters" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["session_pinning_filters"],
            pairs,
            f"{key_prefix}SessionPinningFilters",
        )
    if "init_query" in value:
        pairs.append((f"{key_prefix}InitQuery", str(value["init_query"])))


def deserialize_query(el: Element) -> ConnectionPoolConfiguration:
    out: ConnectionPoolConfiguration = {}  # type: ignore[typeddict-item]
    child_max_connections_percent = el.find("MaxConnectionsPercent")
    if child_max_connections_percent is not None:
        out["max_connections_percent"] = int(child_max_connections_percent.text or "")
    child_max_idle_connections_percent = el.find("MaxIdleConnectionsPercent")
    if child_max_idle_connections_percent is not None:
        out["max_idle_connections_percent"] = int(
            child_max_idle_connections_percent.text or ""
        )
    child_connection_borrow_timeout = el.find("ConnectionBorrowTimeout")
    if child_connection_borrow_timeout is not None:
        out["connection_borrow_timeout"] = int(
            child_connection_borrow_timeout.text or ""
        )
    child_session_pinning_filters = el.find("SessionPinningFilters")
    if child_session_pinning_filters is not None:
        import capo_rds.types.string_list

        out["session_pinning_filters"] = capo_rds.types.string_list.deserialize_query(
            child_session_pinning_filters
        )
    child_init_query = el.find("InitQuery")
    if child_init_query is not None:
        out["init_query"] = str(child_init_query.text or "")
    return out


def redact_sensitive(value: ConnectionPoolConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "init_query" in value:
        out["init_query"] = "*** Sensitive Data Redacted ***"
    return out
