"""Generated from Smithy shape ``com.amazonaws.elasticache#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.filter_name
    import capo_elasticache.types.filter_value_list


class Filter(TypedDict, closed=True):
    name: NotRequired["capo_elasticache.types.filter_name.FilterName"]
    """<p>The property being filtered. For example, UserId.</p>"""
    values: NotRequired["capo_elasticache.types.filter_value_list.FilterValueList"]
    """<p>The property values to filter on. For example, "user-123".</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Filter, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "values" in value:
        import capo_elasticache.types.filter_value_list

        capo_elasticache.types.filter_value_list.serialize_query(
            value["values"], pairs, f"{key_prefix}Values"
        )


def deserialize_query(el: Element) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_values = el.find("Values")
    if child_values is not None:
        import capo_elasticache.types.filter_value_list

        out["values"] = capo_elasticache.types.filter_value_list.deserialize_query(
            child_values
        )
    return out
