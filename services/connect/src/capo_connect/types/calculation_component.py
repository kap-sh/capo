"""Generated from Smithy shape ``com.amazonaws.connect#CalculationComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.component_alias
    import capo_connect.types.metric_filter_list
    import capo_connect.types.metric_id
    import capo_connect.types.metric_name


class CalculationComponent(TypedDict, closed=True):
    alias: "capo_connect.types.component_alias.ComponentAlias"
    """<p>The alias used to reference this component in the calculation expression.</p>"""
    metric_name: NotRequired["capo_connect.types.metric_name.MetricName"]
    """<p>The name of an AWS-managed metric used in this calculation component (for example, <code>CONTACTS_HANDLED</code>). Mutually exclusive with <code>MetricId</code>.</p>"""
    metric_id: NotRequired["capo_connect.types.metric_id.MetricId"]
    """<p>The ARN of an AWS-managed metric used in this calculation component. Mutually exclusive with <code>MetricName</code>.</p>"""
    metric_filters: NotRequired[
        "capo_connect.types.metric_filter_list.MetricFilterList"
    ]
    """<p>The filters applied to the calculation component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculationComponent) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "metric_id" in value:
        out["MetricId"] = value["metric_id"]
    if "metric_filters" in value:
        import capo_connect.types.metric_filter_list

        out["MetricFilters"] = capo_connect.types.metric_filter_list.serialize_json(
            value["metric_filters"]
        )
    return out


def deserialize_json(data: dict) -> CalculationComponent:
    out: CalculationComponent = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        out["alias"] = ""
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("MetricId") is not None:
        out["metric_id"] = data["MetricId"]
    if data.get("MetricFilters") is not None:
        import capo_connect.types.metric_filter_list

        out["metric_filters"] = capo_connect.types.metric_filter_list.deserialize_json(
            data["MetricFilters"]
        )
    return out
