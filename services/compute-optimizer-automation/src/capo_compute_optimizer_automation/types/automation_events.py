"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AutomationEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.automation_event

AutomationEvents: TypeAlias = list[
    "capo_compute_optimizer_automation.types.automation_event.AutomationEvent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomationEvents) -> list:
    import capo_compute_optimizer_automation.types.automation_event

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.automation_event.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutomationEvents:
    import capo_compute_optimizer_automation.types.automation_event

    out: AutomationEvents = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.automation_event.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutomationEvents) -> list:
    import capo_compute_optimizer_automation.types.automation_event

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.automation_event.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> AutomationEvents:
    import capo_compute_optimizer_automation.types.automation_event

    out: AutomationEvents = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.automation_event.deserialize_cbor(
                item
            )
        )
    return out
