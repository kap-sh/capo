"""Generated from Smithy shape ``com.amazonaws.quicksight#HierarchyFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.default_filter_control_configuration
    import capo_quicksight.types.filter_null_option
    import capo_quicksight.types.hierarchy_filter_level_list
    import capo_quicksight.types.hierarchy_filter_match_operator
    import capo_quicksight.types.hierarchy_filter_node
    import capo_quicksight.types.short_restrictive_resource_id


class HierarchyFilter(TypedDict, closed=True):
    filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that anchors the filter. This column determines the dataset that the whole filter applies to, so every column in <code>HierarchyLevels</code> and in <code>HierarchyTree</code> must belong to the same dataset.</p>"""
    hierarchy_levels: (
        "capo_quicksight.types.hierarchy_filter_level_list.HierarchyFilterLevelList"
    )
    """<p>The ordered list of columns that defines the drill-down path of the filter. The first level is the top of the hierarchy. You can specify a maximum of 5 levels.</p>"""
    hierarchy_tree: NotRequired[
        "capo_quicksight.types.hierarchy_filter_node.HierarchyFilterNode"
    ]
    """<p>The tree of selected values for the filter. Each node records the values that are selected at one level of the hierarchy, and its children record the selections beneath those values. Omit this attribute to define the drill-down path without restricting any values.</p>"""
    null_option: "capo_quicksight.types.filter_null_option.FilterNullOption"
    """<p>This option determines how null values should be treated when filtering data.</p> <ul> <li> <p> <code>ALL_VALUES</code>: Include null values in filtered results.</p> </li> <li> <p> <code>NULLS_ONLY</code>: Only include null values in filtered results.</p> </li> <li> <p> <code>NON_NULLS_ONLY</code>: Exclude null values from filtered results.</p> </li> </ul>"""
    match_operator: "capo_quicksight.types.hierarchy_filter_match_operator.HierarchyFilterMatchOperator"
    """<p>Determines whether the values selected in <code>HierarchyTree</code> are kept or removed. Choose one of the following options:</p> <ul> <li> <p> <code>INCLUDE</code>: Keep only the selected values.</p> </li> <li> <p> <code>EXCLUDE</code>: Remove the selected values.</p> </li> </ul>"""
    default_filter_control_configuration: NotRequired[
        "capo_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    import capo_quicksight.types.hierarchy_filter_level_list

    out["HierarchyLevels"] = (
        capo_quicksight.types.hierarchy_filter_level_list.serialize_json(
            value["hierarchy_levels"]
        )
    )
    if "hierarchy_tree" in value:
        import capo_quicksight.types.hierarchy_filter_node

        out["HierarchyTree"] = (
            capo_quicksight.types.hierarchy_filter_node.serialize_json(
                value["hierarchy_tree"]
            )
        )
    import capo_quicksight.types.filter_null_option

    out["NullOption"] = capo_quicksight.types.filter_null_option.serialize_json(
        value["null_option"]
    )
    import capo_quicksight.types.hierarchy_filter_match_operator

    out["MatchOperator"] = (
        capo_quicksight.types.hierarchy_filter_match_operator.serialize_json(
            value["match_operator"]
        )
    )
    if "default_filter_control_configuration" in value:
        import capo_quicksight.types.default_filter_control_configuration

        out["DefaultFilterControlConfiguration"] = (
            capo_quicksight.types.default_filter_control_configuration.serialize_json(
                value["default_filter_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> HierarchyFilter:
    out: HierarchyFilter = {}  # type: ignore[typeddict-item]
    if data.get("FilterId") is not None:
        out["filter_id"] = data["FilterId"]
    else:
        raise DeserializationError("HierarchyFilter.filter_id required")
    if data.get("Column") is not None:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("HierarchyFilter.column required")
    if data.get("HierarchyLevels") is not None:
        import capo_quicksight.types.hierarchy_filter_level_list

        out["hierarchy_levels"] = (
            capo_quicksight.types.hierarchy_filter_level_list.deserialize_json(
                data["HierarchyLevels"]
            )
        )
    else:
        raise DeserializationError("HierarchyFilter.hierarchy_levels required")
    if data.get("HierarchyTree") is not None:
        import capo_quicksight.types.hierarchy_filter_node

        out["hierarchy_tree"] = (
            capo_quicksight.types.hierarchy_filter_node.deserialize_json(
                data["HierarchyTree"]
            )
        )
    if data.get("NullOption") is not None:
        import capo_quicksight.types.filter_null_option

        out["null_option"] = capo_quicksight.types.filter_null_option.deserialize_json(
            data["NullOption"]
        )
    else:
        raise DeserializationError("HierarchyFilter.null_option required")
    if data.get("MatchOperator") is not None:
        import capo_quicksight.types.hierarchy_filter_match_operator

        out["match_operator"] = (
            capo_quicksight.types.hierarchy_filter_match_operator.deserialize_json(
                data["MatchOperator"]
            )
        )
    else:
        raise DeserializationError("HierarchyFilter.match_operator required")
    if data.get("DefaultFilterControlConfiguration") is not None:
        import capo_quicksight.types.default_filter_control_configuration

        out["default_filter_control_configuration"] = (
            capo_quicksight.types.default_filter_control_configuration.deserialize_json(
                data["DefaultFilterControlConfiguration"]
            )
        )
    return out
