"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBProxyTargetGroupRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.connection_pool_configuration
    import capo_rds.types.db_proxy_name
    import capo_rds.types.db_proxy_target_group_name
    import capo_rds.types.string


class ModifyDBProxyTargetGroupRequest(TypedDict, closed=True):
    target_group_name: NotRequired[
        "capo_rds.types.db_proxy_target_group_name.DBProxyTargetGroupName"
    ]
    """<p>The name of the target group to modify.</p>"""
    db_proxy_name: NotRequired["capo_rds.types.db_proxy_name.DBProxyName"]
    """<p>The name of the proxy.</p>"""
    connection_pool_config: NotRequired[
        "capo_rds.types.connection_pool_configuration.ConnectionPoolConfiguration"
    ]
    """<p>The settings that determine the size and behavior of the connection pool for the target group.</p>"""
    new_name: NotRequired["capo_rds.types.string.String"]
    """<p>The new name for the modified <code>DBProxyTarget</code>. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.</p> <p>You can't rename the <code>default</code> target group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBProxyTargetGroupRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "target_group_name" in value:
        pairs.append((f"{key_prefix}TargetGroupName", str(value["target_group_name"])))
    if "db_proxy_name" in value:
        pairs.append((f"{key_prefix}DBProxyName", str(value["db_proxy_name"])))
    if "connection_pool_config" in value:
        import capo_rds.types.connection_pool_configuration

        capo_rds.types.connection_pool_configuration.serialize_query(
            value["connection_pool_config"], pairs, f"{key_prefix}ConnectionPoolConfig"
        )
    if "new_name" in value:
        pairs.append((f"{key_prefix}NewName", str(value["new_name"])))


def deserialize_query(el: Element) -> ModifyDBProxyTargetGroupRequest:
    out: ModifyDBProxyTargetGroupRequest = {}  # type: ignore[typeddict-item]
    child_target_group_name = el.find("TargetGroupName")
    if child_target_group_name is not None:
        out["target_group_name"] = str(child_target_group_name.text or "")
    child_db_proxy_name = el.find("DBProxyName")
    if child_db_proxy_name is not None:
        out["db_proxy_name"] = str(child_db_proxy_name.text or "")
    child_connection_pool_config = el.find("ConnectionPoolConfig")
    if child_connection_pool_config is not None:
        import capo_rds.types.connection_pool_configuration

        out["connection_pool_config"] = (
            capo_rds.types.connection_pool_configuration.deserialize_query(
                child_connection_pool_config
            )
        )
    child_new_name = el.find("NewName")
    if child_new_name is not None:
        out["new_name"] = str(child_new_name.text or "")
    return out


def redact_sensitive(value: ModifyDBProxyTargetGroupRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connection_pool_config" in value:
        import capo_rds.types.connection_pool_configuration

        out["connection_pool_config"] = (
            capo_rds.types.connection_pool_configuration.redact_sensitive(
                value["connection_pool_config"]
            )
        )
    return out
