"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListEventTypesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codestar_notifications.types.list_event_types_filter_name
    import capo_codestar_notifications.types.list_event_types_filter_value


class ListEventTypesFilter(TypedDict, closed=True):
    name: "capo_codestar_notifications.types.list_event_types_filter_name.ListEventTypesFilterName"
    """<p>The system-generated name of the filter type you want to filter by.</p>"""
    value: "capo_codestar_notifications.types.list_event_types_filter_value.ListEventTypesFilterValue"
    """<p>The name of the resource type (for example, pipeline) or service name (for example, CodePipeline) that you want to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventTypesFilter) -> dict:
    out: dict = {}
    import capo_codestar_notifications.types.list_event_types_filter_name

    out["Name"] = (
        capo_codestar_notifications.types.list_event_types_filter_name.serialize_json(
            value["name"]
        )
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ListEventTypesFilter:
    out: ListEventTypesFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_codestar_notifications.types.list_event_types_filter_name

        out["name"] = (
            capo_codestar_notifications.types.list_event_types_filter_name.deserialize_json(
                data["Name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_codestar_notifications.types.list_event_types_filter_name.ListEventTypesFilterName",
            "",
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
