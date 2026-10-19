"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunSourceSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError, SerializationError
from capo_resiliencehubv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_run_observability_alarm_summary
    import capo_resiliencehubv2.types.test_run_success_criteria_alarm_summary


class _TestRunSourceSummary_successCriteriaAlarm(TypedDict, closed=True):
    successCriteriaAlarm: "capo_resiliencehubv2.types.test_run_success_criteria_alarm_summary.TestRunSuccessCriteriaAlarmSummary"


class _TestRunSourceSummary_observabilityAlarm(TypedDict, closed=True):
    observabilityAlarm: "capo_resiliencehubv2.types.test_run_observability_alarm_summary.TestRunObservabilityAlarmSummary"


TestRunSourceSummary: TypeAlias = (
    _TestRunSourceSummary_successCriteriaAlarm
    | _TestRunSourceSummary_observabilityAlarm
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TestRunSourceSummary) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"TestRunSourceSummary: cannot serialize unknown variant {value.name!r}"
        )
    elif "successCriteriaAlarm" in value:
        import capo_resiliencehubv2.types.test_run_success_criteria_alarm_summary

        return {
            "successCriteriaAlarm": capo_resiliencehubv2.types.test_run_success_criteria_alarm_summary.serialize_json(
                value["successCriteriaAlarm"]
            )
        }
    elif "observabilityAlarm" in value:
        import capo_resiliencehubv2.types.test_run_observability_alarm_summary

        return {
            "observabilityAlarm": capo_resiliencehubv2.types.test_run_observability_alarm_summary.serialize_json(
                value["observabilityAlarm"]
            )
        }
    else:
        raise SerializationError("TestRunSourceSummary: no variant present")


def deserialize_json(data: dict) -> TestRunSourceSummary:
    if data.get("successCriteriaAlarm") is not None:
        import capo_resiliencehubv2.types.test_run_success_criteria_alarm_summary

        return {
            "successCriteriaAlarm": capo_resiliencehubv2.types.test_run_success_criteria_alarm_summary.deserialize_json(
                data["successCriteriaAlarm"]
            )
        }
    elif data.get("observabilityAlarm") is not None:
        import capo_resiliencehubv2.types.test_run_observability_alarm_summary

        return {
            "observabilityAlarm": capo_resiliencehubv2.types.test_run_observability_alarm_summary.deserialize_json(
                data["observabilityAlarm"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("TestRunSourceSummary: no recognized variant key")
