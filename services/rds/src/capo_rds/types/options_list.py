"""Generated from Smithy shape ``com.amazonaws.rds#OptionsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.option

OptionsList: TypeAlias = list["capo_rds.types.option.Option"]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.option

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.option.serialize_query(item, pairs, f"{prefix}.Option.{n}")


def deserialize_query(el: Element) -> OptionsList:
    import capo_rds.types.option

    out: OptionsList = []
    for child in el.findall("Option"):
        out.append(capo_rds.types.option.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.option

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.option.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> OptionsList:
    import capo_rds.types.option

    out: OptionsList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.option.deserialize_query(child))
    return out


def redact_sensitive(value: OptionsList) -> list[Any]:
    import capo_rds.types.option

    return [capo_rds.types.option.redact_sensitive(item) for item in value]
