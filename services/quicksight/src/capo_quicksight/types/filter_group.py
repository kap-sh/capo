"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterGroup``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.cross_dataset_types
    import capo_quicksight.types.filter_list
    import capo_quicksight.types.filter_scope_configuration
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.widget_status


class FilterGroup(TypedDict, closed=True):
    filter_group_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The value that uniquely identifies a <code>FilterGroup</code> within a dashboard, template, or analysis.</p>"""
    filters: "capo_quicksight.types.filter_list.FilterList"
    """<p>The list of filters that are present in a <code>FilterGroup</code>.</p>"""
    scope_configuration: (
        "capo_quicksight.types.filter_scope_configuration.FilterScopeConfiguration"
    )
    """<p>The configuration that specifies what scope to apply to a <code>FilterGroup</code>.</p> <p>This is a union type structure. For this structure to be valid, only one of the attributes can be defined.</p>"""
    status: NotRequired["capo_quicksight.types.widget_status.WidgetStatus"]
    """<p>The status of the <code>FilterGroup</code>.</p>"""
    cross_dataset: "capo_quicksight.types.cross_dataset_types.CrossDatasetTypes"
    """<p>The filter new feature which can apply filter group to all data sets. Choose one of the following options:</p> <ul> <li> <p> <code>ALL_DATASETS</code> </p> </li> <li> <p> <code>SINGLE_DATASET</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterGroup) -> dict:
    out: dict = {}
    out["FilterGroupId"] = value["filter_group_id"]
    import capo_quicksight.types.filter_list

    out["Filters"] = capo_quicksight.types.filter_list.serialize_json(value["filters"])
    import capo_quicksight.types.filter_scope_configuration

    out["ScopeConfiguration"] = (
        capo_quicksight.types.filter_scope_configuration.serialize_json(
            value["scope_configuration"]
        )
    )
    if "status" in value:
        import capo_quicksight.types.widget_status

        out["Status"] = capo_quicksight.types.widget_status.serialize_json(
            value["status"]
        )
    import capo_quicksight.types.cross_dataset_types

    out["CrossDataset"] = capo_quicksight.types.cross_dataset_types.serialize_json(
        value["cross_dataset"]
    )
    return out


def deserialize_json(data: dict) -> FilterGroup:
    out: FilterGroup = {}  # type: ignore[typeddict-item]
    if data.get("FilterGroupId") is not None:
        out["filter_group_id"] = data["FilterGroupId"]
    else:
        out["filter_group_id"] = ""
    if data.get("Filters") is not None:
        import capo_quicksight.types.filter_list

        out["filters"] = capo_quicksight.types.filter_list.deserialize_json(
            data["Filters"]
        )
    else:
        out["filters"] = []
    if data.get("ScopeConfiguration") is not None:
        import capo_quicksight.types.filter_scope_configuration

        out["scope_configuration"] = (
            capo_quicksight.types.filter_scope_configuration.deserialize_json(
                data["ScopeConfiguration"]
            )
        )
    else:
        raise DeserializationError("FilterGroup.scope_configuration required")
    if data.get("Status") is not None:
        import capo_quicksight.types.widget_status

        out["status"] = capo_quicksight.types.widget_status.deserialize_json(
            data["Status"]
        )
    if data.get("CrossDataset") is not None:
        import capo_quicksight.types.cross_dataset_types

        out["cross_dataset"] = (
            capo_quicksight.types.cross_dataset_types.deserialize_json(
                data["CrossDataset"]
            )
        )
    else:
        import typing

        out["cross_dataset"] = typing.cast(
            "capo_quicksight.types.cross_dataset_types.CrossDatasetTypes", ""
        )
    return out


def redact_sensitive(value: FilterGroup) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters" in value:
        import capo_quicksight.types.filter_list

        out["filters"] = capo_quicksight.types.filter_list.redact_sensitive(
            value["filters"]
        )
    return out
