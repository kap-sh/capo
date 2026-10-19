"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListNotificationRulesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codestar_notifications.types.list_notification_rules_filter_name
    import capo_codestar_notifications.types.list_notification_rules_filter_value


class ListNotificationRulesFilter(TypedDict, closed=True):
    name: "capo_codestar_notifications.types.list_notification_rules_filter_name.ListNotificationRulesFilterName"
    """<p>The name of the attribute you want to use to filter the returned notification rules.</p>"""
    value: "capo_codestar_notifications.types.list_notification_rules_filter_value.ListNotificationRulesFilterValue"
    """<p>The value of the attribute you want to use to filter the returned notification rules. For example, if you specify filtering by <i>RESOURCE</i> in Name, you might specify the ARN of a pipeline in CodePipeline for the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationRulesFilter) -> dict:
    out: dict = {}
    import capo_codestar_notifications.types.list_notification_rules_filter_name

    out["Name"] = (
        capo_codestar_notifications.types.list_notification_rules_filter_name.serialize_json(
            value["name"]
        )
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ListNotificationRulesFilter:
    out: ListNotificationRulesFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_codestar_notifications.types.list_notification_rules_filter_name

        out["name"] = (
            capo_codestar_notifications.types.list_notification_rules_filter_name.deserialize_json(
                data["Name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_codestar_notifications.types.list_notification_rules_filter_name.ListNotificationRulesFilterName",
            "",
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
