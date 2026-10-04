"""Generated from Smithy shape ``com.amazonaws.rds#TargetResourceConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.target_resource_configuration

TargetResourceConfigurationList: TypeAlias = list[
    "capo_rds.types.target_resource_configuration.TargetResourceConfiguration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetResourceConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.target_resource_configuration

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.target_resource_configuration.serialize_query(
            item, pairs, f"{prefix}.TargetResourceConfiguration.{n}"
        )


def deserialize_query(el: Element) -> TargetResourceConfigurationList:
    import capo_rds.types.target_resource_configuration

    out: TargetResourceConfigurationList = []
    for child in el.findall("TargetResourceConfiguration"):
        out.append(
            capo_rds.types.target_resource_configuration.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: TargetResourceConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.target_resource_configuration

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.target_resource_configuration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> TargetResourceConfigurationList:
    import capo_rds.types.target_resource_configuration

    out: TargetResourceConfigurationList = []
    for child in parent.findall(tag):
        out.append(
            capo_rds.types.target_resource_configuration.deserialize_query(child)
        )
    return out
