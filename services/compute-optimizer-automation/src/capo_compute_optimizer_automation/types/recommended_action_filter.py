"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RecommendedActionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.filter_values
    import capo_compute_optimizer_automation.types.recommended_action_filter_name


class RecommendedActionFilter(TypedDict, closed=True):
    name: "capo_compute_optimizer_automation.types.recommended_action_filter_name.RecommendedActionFilterName"
    """<p>The name of the filter field to apply.</p>"""
    values: "capo_compute_optimizer_automation.types.filter_values.FilterValues"
    """<p>List of filter values to match against the specified filter name. Used to narrow down recommended actions based on specific criteria.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedActionFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_compute_optimizer_automation.types.filter_values

    out["values"] = (
        capo_compute_optimizer_automation.types.filter_values.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendedActionFilter:
    out: RecommendedActionFilter = {}  # type: ignore[typeddict-item]
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
