"""Generated from Smithy shape ``com.amazonaws.rds#DBProxyTargetGroup``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.connection_pool_configuration_info
    import capo_rds.types.string
    import capo_rds.types.t_stamp


class DBProxyTargetGroup(TypedDict, closed=True):
    db_proxy_name: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the RDS proxy associated with this target group.</p>"""
    target_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the target group. This name must be unique for all target groups owned by your Amazon Web Services account in the specified Amazon Web Services Region.</p>"""
    target_group_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) representing the target group.</p>"""
    is_default: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether this target group is the first one used for connection requests by the associated proxy. Because each proxy is currently associated with a single target group, currently this setting is always <code>true</code>.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The current status of this target group. A status of <code>available</code> means the target group is correctly associated with a database. Other values indicate that you must wait for the target group to be ready, or take some action to resolve an issue.</p>"""
    connection_pool_config: NotRequired[
        "capo_rds.types.connection_pool_configuration_info.ConnectionPoolConfigurationInfo"
    ]
    """<p>The settings that determine the size and behavior of the connection pool for the target group.</p>"""
    created_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date and time when the target group was first created.</p>"""
    updated_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date and time when the target group was last updated.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBProxyTargetGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_proxy_name" in value:
        pairs.append((f"{key_prefix}DBProxyName", str(value["db_proxy_name"])))
    if "target_group_name" in value:
        pairs.append((f"{key_prefix}TargetGroupName", str(value["target_group_name"])))
    if "target_group_arn" in value:
        pairs.append((f"{key_prefix}TargetGroupArn", str(value["target_group_arn"])))
    if "is_default" in value:
        pairs.append(
            (f"{key_prefix}IsDefault", "true" if value["is_default"] else "false")
        )
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "connection_pool_config" in value:
        import capo_rds.types.connection_pool_configuration_info

        capo_rds.types.connection_pool_configuration_info.serialize_query(
            value["connection_pool_config"], pairs, f"{key_prefix}ConnectionPoolConfig"
        )
    if "created_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["created_date"], pairs, f"{key_prefix}CreatedDate"
        )
    if "updated_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["updated_date"], pairs, f"{key_prefix}UpdatedDate"
        )


def deserialize_query(el: Element) -> DBProxyTargetGroup:
    out: DBProxyTargetGroup = {}  # type: ignore[typeddict-item]
    child_db_proxy_name = el.find("DBProxyName")
    if child_db_proxy_name is not None:
        out["db_proxy_name"] = str(child_db_proxy_name.text or "")
    child_target_group_name = el.find("TargetGroupName")
    if child_target_group_name is not None:
        out["target_group_name"] = str(child_target_group_name.text or "")
    child_target_group_arn = el.find("TargetGroupArn")
    if child_target_group_arn is not None:
        out["target_group_arn"] = str(child_target_group_arn.text or "")
    child_is_default = el.find("IsDefault")
    if child_is_default is not None:
        out["is_default"] = (child_is_default.text or "").lower() == "true"
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_connection_pool_config = el.find("ConnectionPoolConfig")
    if child_connection_pool_config is not None:
        import capo_rds.types.connection_pool_configuration_info

        out["connection_pool_config"] = (
            capo_rds.types.connection_pool_configuration_info.deserialize_query(
                child_connection_pool_config
            )
        )
    child_created_date = el.find("CreatedDate")
    if child_created_date is not None:
        import capo_rds.types.t_stamp

        out["created_date"] = capo_rds.types.t_stamp.deserialize_query(
            child_created_date
        )
    child_updated_date = el.find("UpdatedDate")
    if child_updated_date is not None:
        import capo_rds.types.t_stamp

        out["updated_date"] = capo_rds.types.t_stamp.deserialize_query(
            child_updated_date
        )
    return out


def redact_sensitive(value: DBProxyTargetGroup) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connection_pool_config" in value:
        import capo_rds.types.connection_pool_configuration_info

        out["connection_pool_config"] = (
            capo_rds.types.connection_pool_configuration_info.redact_sensitive(
                value["connection_pool_config"]
            )
        )
    return out
