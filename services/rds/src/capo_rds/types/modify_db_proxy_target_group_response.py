"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBProxyTargetGroupResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_proxy_target_group


class ModifyDBProxyTargetGroupResponse(TypedDict, closed=True):
    db_proxy_target_group: NotRequired[
        "capo_rds.types.db_proxy_target_group.DBProxyTargetGroup"
    ]
    """<p>The settings of the modified <code>DBProxyTarget</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBProxyTargetGroupResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_proxy_target_group" in value:
        import capo_rds.types.db_proxy_target_group

        capo_rds.types.db_proxy_target_group.serialize_query(
            value["db_proxy_target_group"], pairs, f"{key_prefix}DBProxyTargetGroup"
        )


def deserialize_query(el: Element) -> ModifyDBProxyTargetGroupResponse:
    out: ModifyDBProxyTargetGroupResponse = {}  # type: ignore[typeddict-item]
    child_db_proxy_target_group = el.find("DBProxyTargetGroup")
    if child_db_proxy_target_group is not None:
        import capo_rds.types.db_proxy_target_group

        out["db_proxy_target_group"] = (
            capo_rds.types.db_proxy_target_group.deserialize_query(
                child_db_proxy_target_group
            )
        )
    return out


def redact_sensitive(value: ModifyDBProxyTargetGroupResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "db_proxy_target_group" in value:
        import capo_rds.types.db_proxy_target_group

        out["db_proxy_target_group"] = (
            capo_rds.types.db_proxy_target_group.redact_sensitive(
                value["db_proxy_target_group"]
            )
        )
    return out
