"""Generated from Smithy shape ``com.amazonaws.customerprofiles#TriggerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.trigger_properties
    import capo_customer_profiles.types.trigger_type


class TriggerConfig(TypedDict, closed=True):
    trigger_type: "capo_customer_profiles.types.trigger_type.TriggerType"
    """<p>Specifies the type of flow trigger. It can be OnDemand, Scheduled, or Event.</p>"""
    trigger_properties: NotRequired[
        "capo_customer_profiles.types.trigger_properties.TriggerProperties"
    ]
    """<p>Specifies the configuration details of a schedule-triggered flow that you define. Currently, these settings only apply to the Scheduled trigger type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TriggerConfig) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.trigger_type

    out["TriggerType"] = capo_customer_profiles.types.trigger_type.serialize_json(
        value["trigger_type"]
    )
    if "trigger_properties" in value:
        import capo_customer_profiles.types.trigger_properties

        out["TriggerProperties"] = (
            capo_customer_profiles.types.trigger_properties.serialize_json(
                value["trigger_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> TriggerConfig:
    out: TriggerConfig = {}  # type: ignore[typeddict-item]
    if data.get("TriggerType") is not None:
        import capo_customer_profiles.types.trigger_type

        out["trigger_type"] = (
            capo_customer_profiles.types.trigger_type.deserialize_json(
                data["TriggerType"]
            )
        )
    else:
        import typing

        out["trigger_type"] = typing.cast(
            "capo_customer_profiles.types.trigger_type.TriggerType", ""
        )
    if data.get("TriggerProperties") is not None:
        import capo_customer_profiles.types.trigger_properties

        out["trigger_properties"] = (
            capo_customer_profiles.types.trigger_properties.deserialize_json(
                data["TriggerProperties"]
            )
        )
    return out
