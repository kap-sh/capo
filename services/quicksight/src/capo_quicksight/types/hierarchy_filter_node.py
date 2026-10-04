"""Generated from Smithy shape ``com.amazonaws.quicksight#HierarchyFilterNode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.hierarchy_filter_node_list
    import capo_quicksight.types.hierarchy_filter_value
    import capo_quicksight.types.hierarchy_values_list


class HierarchyFilterNode(TypedDict, closed=True):
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that this node selects values from. This column must match the column of the corresponding level in <code>HierarchyFilter$HierarchyLevels</code>. The node at depth 1 must match the first level, the node at depth 2 must match the second level, and so on.</p>"""
    parent_value: NotRequired[
        "capo_quicksight.types.hierarchy_filter_value.HierarchyFilterValue"
    ]
    """<p>The value in the parent node's <code>HierarchyValues</code> that this node belongs to. When a parent selects several values, each of its children repeats one of them here to identify which branch of the hierarchy that child describes.</p> <p>Omit this attribute on the root node of <code>HierarchyTree</code>, which has no parent.</p>"""
    hierarchy_values: NotRequired[
        "capo_quicksight.types.hierarchy_values_list.HierarchyValuesList"
    ]
    """<p>The values that are selected at this level of the hierarchy. You can specify a maximum of 2,000 values per node.</p>"""
    children: NotRequired[
        "capo_quicksight.types.hierarchy_filter_node_list.HierarchyFilterNodeList"
    ]
    """<p>The nodes that record the selections at the next level of the hierarchy. You can specify a maximum of 1,000 children per node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyFilterNode) -> dict:
    out: dict = {}
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "parent_value" in value:
        out["ParentValue"] = value["parent_value"]
    if "hierarchy_values" in value:
        import capo_quicksight.types.hierarchy_values_list

        out["HierarchyValues"] = (
            capo_quicksight.types.hierarchy_values_list.serialize_json(
                value["hierarchy_values"]
            )
        )
    if "children" in value:
        import capo_quicksight.types.hierarchy_filter_node_list

        out["Children"] = (
            capo_quicksight.types.hierarchy_filter_node_list.serialize_json(
                value["children"]
            )
        )
    return out


def deserialize_json(data: dict) -> HierarchyFilterNode:
    out: HierarchyFilterNode = {}  # type: ignore[typeddict-item]
    if data.get("Column") is not None:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("HierarchyFilterNode.column required")
    if data.get("ParentValue") is not None:
        out["parent_value"] = data["ParentValue"]
    if data.get("HierarchyValues") is not None:
        import capo_quicksight.types.hierarchy_values_list

        out["hierarchy_values"] = (
            capo_quicksight.types.hierarchy_values_list.deserialize_json(
                data["HierarchyValues"]
            )
        )
    if data.get("Children") is not None:
        import capo_quicksight.types.hierarchy_filter_node_list

        out["children"] = (
            capo_quicksight.types.hierarchy_filter_node_list.deserialize_json(
                data["Children"]
            )
        )
    return out
