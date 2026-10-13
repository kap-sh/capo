"""Generated from Smithy shape ``com.amazonaws.rds#TargetGroupList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_proxy_target_group

TargetGroupList: TypeAlias = list[
    "capo_rds.types.db_proxy_target_group.DBProxyTargetGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_proxy_target_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_proxy_target_group.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TargetGroupList:
    import capo_rds.types.db_proxy_target_group

    out: TargetGroupList = []
    for child in el.findall("member"):
        out.append(capo_rds.types.db_proxy_target_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TargetGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_proxy_target_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_proxy_target_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TargetGroupList:
    import capo_rds.types.db_proxy_target_group

    out: TargetGroupList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_proxy_target_group.deserialize_query(child))
    return out


def redact_sensitive(value: TargetGroupList) -> list[Any]:
    import capo_rds.types.db_proxy_target_group

    return [
        capo_rds.types.db_proxy_target_group.redact_sensitive(item) for item in value
    ]
