"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestSourceInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError, SerializationError
from capo_resiliencehubv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.observability_alarm_input
    import capo_resiliencehubv2.types.success_criteria_alarm_input


class _TestSourceInput_successCriteriaAlarm(TypedDict, closed=True):
    successCriteriaAlarm: "capo_resiliencehubv2.types.success_criteria_alarm_input.SuccessCriteriaAlarmInput"


class _TestSourceInput_observabilityAlarm(TypedDict, closed=True):
    observabilityAlarm: (
        "capo_resiliencehubv2.types.observability_alarm_input.ObservabilityAlarmInput"
    )


TestSourceInput: TypeAlias = (
    _TestSourceInput_successCriteriaAlarm
    | _TestSourceInput_observabilityAlarm
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TestSourceInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TestSourceInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "successCriteriaAlarm" in value:
        import capo_resiliencehubv2.types.success_criteria_alarm_input

        return {
            "successCriteriaAlarm": capo_resiliencehubv2.types.success_criteria_alarm_input.serialize_json(
                value["successCriteriaAlarm"]
            )
        }
    elif "observabilityAlarm" in value:
        import capo_resiliencehubv2.types.observability_alarm_input

        return {
            "observabilityAlarm": capo_resiliencehubv2.types.observability_alarm_input.serialize_json(
                value["observabilityAlarm"]
            )
        }
    else:
        raise SerializationError("TestSourceInput: no variant present")


def deserialize_json(data: dict) -> TestSourceInput:
    if data.get("successCriteriaAlarm") is not None:
        import capo_resiliencehubv2.types.success_criteria_alarm_input

        return {
            "successCriteriaAlarm": capo_resiliencehubv2.types.success_criteria_alarm_input.deserialize_json(
                data["successCriteriaAlarm"]
            )
        }
    elif data.get("observabilityAlarm") is not None:
        import capo_resiliencehubv2.types.observability_alarm_input

        return {
            "observabilityAlarm": capo_resiliencehubv2.types.observability_alarm_input.deserialize_json(
                data["observabilityAlarm"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TestSourceInput: no recognized variant key")
