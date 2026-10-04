"""Generated from Smithy shape ``com.amazonaws.quicksight#HierarchyFilterListControlDisplayOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.hierarchy_filter_list_control_search_options
    import capo_quicksight.types.label_options
    import capo_quicksight.types.sheet_control_info_icon_label_options


class HierarchyFilterListControlDisplayOptions(TypedDict, closed=True):
    title_options: NotRequired["capo_quicksight.types.label_options.LabelOptions"]
    """<p>The options to configure the title visibility, name, and font size.</p>"""
    info_icon_label_options: NotRequired[
        "capo_quicksight.types.sheet_control_info_icon_label_options.SheetControlInfoIconLabelOptions"
    ]
    """<p>The configuration of info icon label options.</p>"""
    search_options: NotRequired[
        "capo_quicksight.types.hierarchy_filter_list_control_search_options.HierarchyFilterListControlSearchOptions"
    ]
    """<p>The configuration of the search options in a hierarchy list control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyFilterListControlDisplayOptions) -> dict:
    out: dict = {}
    if "title_options" in value:
        import capo_quicksight.types.label_options

        out["TitleOptions"] = capo_quicksight.types.label_options.serialize_json(
            value["title_options"]
        )
    if "info_icon_label_options" in value:
        import capo_quicksight.types.sheet_control_info_icon_label_options

        out["InfoIconLabelOptions"] = (
            capo_quicksight.types.sheet_control_info_icon_label_options.serialize_json(
                value["info_icon_label_options"]
            )
        )
    if "search_options" in value:
        import capo_quicksight.types.hierarchy_filter_list_control_search_options

        out["SearchOptions"] = (
            capo_quicksight.types.hierarchy_filter_list_control_search_options.serialize_json(
                value["search_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> HierarchyFilterListControlDisplayOptions:
    out: HierarchyFilterListControlDisplayOptions = {}  # type: ignore[typeddict-item]
    if data.get("TitleOptions") is not None:
        import capo_quicksight.types.label_options

        out["title_options"] = capo_quicksight.types.label_options.deserialize_json(
            data["TitleOptions"]
        )
    if data.get("InfoIconLabelOptions") is not None:
        import capo_quicksight.types.sheet_control_info_icon_label_options

        out["info_icon_label_options"] = (
            capo_quicksight.types.sheet_control_info_icon_label_options.deserialize_json(
                data["InfoIconLabelOptions"]
            )
        )
    if data.get("SearchOptions") is not None:
        import capo_quicksight.types.hierarchy_filter_list_control_search_options

        out["search_options"] = (
            capo_quicksight.types.hierarchy_filter_list_control_search_options.deserialize_json(
                data["SearchOptions"]
            )
        )
    return out
