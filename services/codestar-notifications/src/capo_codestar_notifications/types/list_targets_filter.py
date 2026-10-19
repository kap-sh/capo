"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListTargetsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codestar_notifications.types.list_targets_filter_name
    import capo_codestar_notifications.types.list_targets_filter_value


class ListTargetsFilter(TypedDict, closed=True):
    name: "capo_codestar_notifications.types.list_targets_filter_name.ListTargetsFilterName"
    """<p>The name of the attribute you want to use to filter the returned targets.</p>"""
    value: "capo_codestar_notifications.types.list_targets_filter_value.ListTargetsFilterValue"
    """<p>The value of the attribute you want to use to filter the returned targets. For example, if you specify <code>SNS</code> for the Target type, you could specify an Amazon Resource Name (ARN) for a topic as the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsFilter) -> dict:
    out: dict = {}
    import capo_codestar_notifications.types.list_targets_filter_name

    out["Name"] = (
        capo_codestar_notifications.types.list_targets_filter_name.serialize_json(
            value["name"]
        )
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ListTargetsFilter:
    out: ListTargetsFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_codestar_notifications.types.list_targets_filter_name

        out["name"] = (
            capo_codestar_notifications.types.list_targets_filter_name.deserialize_json(
                data["Name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_codestar_notifications.types.list_targets_filter_name.ListTargetsFilterName",
            "",
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
