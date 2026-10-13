"""Generated from Smithy shape ``com.amazonaws.rds#OptionGroupsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.option_group

OptionGroupsList: TypeAlias = list["capo_rds.types.option_group.OptionGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroupsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.option_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.option_group.serialize_query(
            item, pairs, f"{prefix}.OptionGroup.{n}"
        )


def deserialize_query(el: Element) -> OptionGroupsList:
    import capo_rds.types.option_group

    out: OptionGroupsList = []
    for child in el.findall("OptionGroup"):
        out.append(capo_rds.types.option_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OptionGroupsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.option_group

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.option_group.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> OptionGroupsList:
    import capo_rds.types.option_group

    out: OptionGroupsList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.option_group.deserialize_query(child))
    return out


def redact_sensitive(value: OptionGroupsList) -> list[Any]:
    import capo_rds.types.option_group

    return [capo_rds.types.option_group.redact_sensitive(item) for item in value]
