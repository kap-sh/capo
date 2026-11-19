"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AutomationEventSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.automation_event_step

AutomationEventSteps: TypeAlias = list[
    "capo_compute_optimizer_automation.types.automation_event_step.AutomationEventStep"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomationEventSteps) -> list:
    import capo_compute_optimizer_automation.types.automation_event_step

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.automation_event_step.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutomationEventSteps:
    import capo_compute_optimizer_automation.types.automation_event_step

    out: AutomationEventSteps = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.automation_event_step.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutomationEventSteps) -> list:
    import capo_compute_optimizer_automation.types.automation_event_step

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.automation_event_step.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> AutomationEventSteps:
    import capo_compute_optimizer_automation.types.automation_event_step

    out: AutomationEventSteps = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.automation_event_step.deserialize_cbor(
                item
            )
        )
    return out
