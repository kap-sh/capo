"""Generated from Smithy shape ``com.amazonaws.appflow#TriggerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.trigger_properties
    import capo_appflow.types.trigger_type


class TriggerConfig(TypedDict, closed=True):
    trigger_type: "capo_appflow.types.trigger_type.TriggerType"
    """<p> Specifies the type of flow trigger. This can be <code>OnDemand</code>, <code>Scheduled</code>, or <code>Event</code>. </p>"""
    trigger_properties: NotRequired[
        "capo_appflow.types.trigger_properties.TriggerProperties"
    ]
    """<p> Specifies the configuration details of a schedule-triggered flow as defined by the user. Currently, these settings only apply to the <code>Scheduled</code> trigger type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TriggerConfig) -> dict:
    out: dict = {}
    import capo_appflow.types.trigger_type

    out["triggerType"] = capo_appflow.types.trigger_type.serialize_json(
        value["trigger_type"]
    )
    if "trigger_properties" in value:
        import capo_appflow.types.trigger_properties

        out["triggerProperties"] = capo_appflow.types.trigger_properties.serialize_json(
            value["trigger_properties"]
        )
    return out


def deserialize_json(data: dict) -> TriggerConfig:
    out: TriggerConfig = {}  # type: ignore[typeddict-item]
    if data.get("triggerType") is not None:
        import capo_appflow.types.trigger_type

        out["trigger_type"] = capo_appflow.types.trigger_type.deserialize_json(
            data["triggerType"]
        )
    else:
        import typing

        out["trigger_type"] = typing.cast(
            "capo_appflow.types.trigger_type.TriggerType", ""
        )
    if data.get("triggerProperties") is not None:
        import capo_appflow.types.trigger_properties

        out["trigger_properties"] = (
            capo_appflow.types.trigger_properties.deserialize_json(
                data["triggerProperties"]
            )
        )
    return out
