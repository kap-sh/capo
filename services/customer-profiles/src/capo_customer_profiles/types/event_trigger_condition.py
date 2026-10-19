"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventTriggerCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.event_trigger_dimensions
    import capo_customer_profiles.types.event_trigger_logical_operator


class EventTriggerCondition(TypedDict, closed=True):
    event_trigger_dimensions: (
        "capo_customer_profiles.types.event_trigger_dimensions.EventTriggerDimensions"
    )
    """<p>A list of dimensions to be evaluated for the event.</p>"""
    logical_operator: "capo_customer_profiles.types.event_trigger_logical_operator.EventTriggerLogicalOperator"
    """<p>The operator used to combine multiple dimensions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventTriggerCondition) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.event_trigger_dimensions

    out["EventTriggerDimensions"] = (
        capo_customer_profiles.types.event_trigger_dimensions.serialize_json(
            value["event_trigger_dimensions"]
        )
    )
    import capo_customer_profiles.types.event_trigger_logical_operator

    out["LogicalOperator"] = (
        capo_customer_profiles.types.event_trigger_logical_operator.serialize_json(
            value["logical_operator"]
        )
    )
    return out


def deserialize_json(data: dict) -> EventTriggerCondition:
    out: EventTriggerCondition = {}  # type: ignore[typeddict-item]
    if data.get("EventTriggerDimensions") is not None:
        import capo_customer_profiles.types.event_trigger_dimensions

        out["event_trigger_dimensions"] = (
            capo_customer_profiles.types.event_trigger_dimensions.deserialize_json(
                data["EventTriggerDimensions"]
            )
        )
    else:
        out["event_trigger_dimensions"] = []
    if data.get("LogicalOperator") is not None:
        import capo_customer_profiles.types.event_trigger_logical_operator

        out["logical_operator"] = (
            capo_customer_profiles.types.event_trigger_logical_operator.deserialize_json(
                data["LogicalOperator"]
            )
        )
    else:
        import typing

        out["logical_operator"] = typing.cast(
            "capo_customer_profiles.types.event_trigger_logical_operator.EventTriggerLogicalOperator",
            "",
        )
    return out
