"""Generated from Smithy shape ``com.amazonaws.quicksight#GroupSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.group_filter_attribute
    import capo_quicksight.types.group_filter_operator
    import capo_quicksight.types.string


class GroupSearchFilter(TypedDict, closed=True):
    operator: "capo_quicksight.types.group_filter_operator.GroupFilterOperator"
    """<p>The comparison operator that you want to use as a filter, for example <code>"Operator": "StartsWith"</code>. Currently, the only supported operator is <code>StartsWith</code>.</p>"""
    name: "capo_quicksight.types.group_filter_attribute.GroupFilterAttribute"
    """<p>The name of the value that you want to use as a filter, for example <code>"Name": "GROUP_NAME"</code>. Currently, the only supported name is <code>GROUP_NAME</code>.</p>"""
    value: "capo_quicksight.types.string.String"
    """<p>The value of the named item, in this case <code>GROUP_NAME</code>, that you want to use as a filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupSearchFilter) -> dict:
    out: dict = {}
    import capo_quicksight.types.group_filter_operator

    out["Operator"] = capo_quicksight.types.group_filter_operator.serialize_json(
        value["operator"]
    )
    import capo_quicksight.types.group_filter_attribute

    out["Name"] = capo_quicksight.types.group_filter_attribute.serialize_json(
        value["name"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> GroupSearchFilter:
    out: GroupSearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("Operator") is not None:
        import capo_quicksight.types.group_filter_operator

        out["operator"] = capo_quicksight.types.group_filter_operator.deserialize_json(
            data["Operator"]
        )
    else:
        raise DeserializationError("GroupSearchFilter.operator required")
    if data.get("Name") is not None:
        import capo_quicksight.types.group_filter_attribute

        out["name"] = capo_quicksight.types.group_filter_attribute.deserialize_json(
            data["Name"]
        )
    else:
        raise DeserializationError("GroupSearchFilter.name required")
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("GroupSearchFilter.value required")
    return out
