"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AutomationEventFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.automation_event_filter_name
    import capo_compute_optimizer_automation.types.filter_values


class AutomationEventFilter(TypedDict, closed=True):
    name: "capo_compute_optimizer_automation.types.automation_event_filter_name.AutomationEventFilterName"
    """<p> The name of the filter to apply. </p>"""
    values: "capo_compute_optimizer_automation.types.filter_values.FilterValues"
    """<p> The values to use for the specified filter. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomationEventFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_compute_optimizer_automation.types.filter_values

    out["values"] = (
        capo_compute_optimizer_automation.types.filter_values.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutomationEventFilter:
    out: AutomationEventFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("values") is not None:
        import capo_compute_optimizer_automation.types.filter_values

        out["values"] = (
            capo_compute_optimizer_automation.types.filter_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    else:
        out["values"] = []
    return out
