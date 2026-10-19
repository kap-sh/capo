"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MetricSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.attributes


class MetricSource(TypedDict, closed=True):
    metric_source_key_attributes: "capo_application_signals.types.attributes.Attributes"
    """<p>Key attributes that identify the metric source.</p>"""
    metric_source_attributes: NotRequired[
        "capo_application_signals.types.attributes.Attributes"
    ]
    """<p>Additional attributes for the metric source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricSource) -> dict:
    out: dict = {}
    import capo_application_signals.types.attributes

    out["MetricSourceKeyAttributes"] = (
        capo_application_signals.types.attributes.serialize_json(
            value["metric_source_key_attributes"]
        )
    )
    if "metric_source_attributes" in value:
        import capo_application_signals.types.attributes

        out["MetricSourceAttributes"] = (
            capo_application_signals.types.attributes.serialize_json(
                value["metric_source_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetricSource:
    out: MetricSource = {}  # type: ignore[typeddict-item]
    if data.get("MetricSourceKeyAttributes") is not None:
        import capo_application_signals.types.attributes

        out["metric_source_key_attributes"] = (
            capo_application_signals.types.attributes.deserialize_json(
                data["MetricSourceKeyAttributes"]
            )
        )
    else:
        out["metric_source_key_attributes"] = {}
    if data.get("MetricSourceAttributes") is not None:
        import capo_application_signals.types.attributes

        out["metric_source_attributes"] = (
            capo_application_signals.types.attributes.deserialize_json(
                data["MetricSourceAttributes"]
            )
        )
    return out
