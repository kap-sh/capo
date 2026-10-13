"""Generated from Smithy shape ``com.amazonaws.rds#OptionGroups``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.option_groups_list
    import capo_rds.types.string


class OptionGroups(TypedDict, closed=True):
    option_groups_list: NotRequired[
        "capo_rds.types.option_groups_list.OptionGroupsList"
    ]
    """<p>List of option groups.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "option_groups_list" in value:
        import capo_rds.types.option_groups_list

        capo_rds.types.option_groups_list.serialize_query(
            value["option_groups_list"], pairs, f"{key_prefix}OptionGroupsList"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> OptionGroups:
    out: OptionGroups = {}  # type: ignore[typeddict-item]
    child_option_groups_list = el.find("OptionGroupsList")
    if child_option_groups_list is not None:
        import capo_rds.types.option_groups_list

        out["option_groups_list"] = capo_rds.types.option_groups_list.deserialize_query(
            child_option_groups_list
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out


def redact_sensitive(value: OptionGroups) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "option_groups_list" in value:
        import capo_rds.types.option_groups_list

        out["option_groups_list"] = capo_rds.types.option_groups_list.redact_sensitive(
            value["option_groups_list"]
        )
    return out
