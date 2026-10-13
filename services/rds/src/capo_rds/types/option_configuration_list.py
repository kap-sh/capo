"""Generated from Smithy shape ``com.amazonaws.rds#OptionConfigurationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.option_configuration

OptionConfigurationList: TypeAlias = list[
    "capo_rds.types.option_configuration.OptionConfiguration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.option_configuration

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.option_configuration.serialize_query(
            item, pairs, f"{prefix}.OptionConfiguration.{n}"
        )


def deserialize_query(el: Element) -> OptionConfigurationList:
    import capo_rds.types.option_configuration

    out: OptionConfigurationList = []
    for child in el.findall("OptionConfiguration"):
        out.append(capo_rds.types.option_configuration.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OptionConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.option_configuration

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.option_configuration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> OptionConfigurationList:
    import capo_rds.types.option_configuration

    out: OptionConfigurationList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.option_configuration.deserialize_query(child))
    return out


def redact_sensitive(value: OptionConfigurationList) -> list[Any]:
    import capo_rds.types.option_configuration

    return [
        capo_rds.types.option_configuration.redact_sensitive(item) for item in value
    ]
