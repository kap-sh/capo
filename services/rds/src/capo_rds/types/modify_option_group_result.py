"""Generated from Smithy shape ``com.amazonaws.rds#ModifyOptionGroupResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.option_group


class ModifyOptionGroupResult(TypedDict, closed=True):
    option_group: NotRequired["capo_rds.types.option_group.OptionGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyOptionGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "option_group" in value:
        import capo_rds.types.option_group

        capo_rds.types.option_group.serialize_query(
            value["option_group"], pairs, f"{key_prefix}OptionGroup"
        )


def deserialize_query(el: Element) -> ModifyOptionGroupResult:
    out: ModifyOptionGroupResult = {}  # type: ignore[typeddict-item]
    child_option_group = el.find("OptionGroup")
    if child_option_group is not None:
        import capo_rds.types.option_group

        out["option_group"] = capo_rds.types.option_group.deserialize_query(
            child_option_group
        )
    return out


def redact_sensitive(value: ModifyOptionGroupResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "option_group" in value:
        import capo_rds.types.option_group

        out["option_group"] = capo_rds.types.option_group.redact_sensitive(
            value["option_group"]
        )
    return out
