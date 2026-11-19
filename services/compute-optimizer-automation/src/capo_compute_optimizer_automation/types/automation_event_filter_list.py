"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AutomationEventFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.automation_event_filter

AutomationEventFilterList: TypeAlias = list[
    "capo_compute_optimizer_automation.types.automation_event_filter.AutomationEventFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomationEventFilterList) -> list:
    import capo_compute_optimizer_automation.types.automation_event_filter

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.automation_event_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutomationEventFilterList:
    import capo_compute_optimizer_automation.types.automation_event_filter

    out: AutomationEventFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.automation_event_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutomationEventFilterList) -> list:
    import capo_compute_optimizer_automation.types.automation_event_filter

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.automation_event_filter.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> AutomationEventFilterList:
    import capo_compute_optimizer_automation.types.automation_event_filter

    out: AutomationEventFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.automation_event_filter.deserialize_cbor(
                item
            )
        )
    return out
