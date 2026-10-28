"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestSourceSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError, SerializationError
from capo_resiliencehubv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.observability_alarm_summary
    import capo_resiliencehubv2.types.success_criteria_alarm_summary


class TestSourceSummarySuccessCriteriaAlarmMember(TypedDict, closed=True):
    successCriteriaAlarm: "capo_resiliencehubv2.types.success_criteria_alarm_summary.SuccessCriteriaAlarmSummary"


class TestSourceSummaryObservabilityAlarmMember(TypedDict, closed=True):
    observabilityAlarm: "capo_resiliencehubv2.types.observability_alarm_summary.ObservabilityAlarmSummary"


TestSourceSummary: TypeAlias = (
    TestSourceSummarySuccessCriteriaAlarmMember
    | TestSourceSummaryObservabilityAlarmMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TestSourceSummary) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TestSourceSummary: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "successCriteriaAlarm" in value:
        import capo_resiliencehubv2.types.success_criteria_alarm_summary

        return {
            "successCriteriaAlarm": capo_resiliencehubv2.types.success_criteria_alarm_summary.serialize_json(
                value["successCriteriaAlarm"]
            )
        }
    elif "observabilityAlarm" in value:
        import capo_resiliencehubv2.types.observability_alarm_summary

        return {
            "observabilityAlarm": capo_resiliencehubv2.types.observability_alarm_summary.serialize_json(
                value["observabilityAlarm"]
            )
        }
    else:
        raise SerializationError("TestSourceSummary: no variant present")


def deserialize_json(data: dict) -> TestSourceSummary:
    if data.get("successCriteriaAlarm") is not None:
        import capo_resiliencehubv2.types.success_criteria_alarm_summary

        return {
            "successCriteriaAlarm": capo_resiliencehubv2.types.success_criteria_alarm_summary.deserialize_json(
                data["successCriteriaAlarm"]
            )
        }
    elif data.get("observabilityAlarm") is not None:
        import capo_resiliencehubv2.types.observability_alarm_summary

        return {
            "observabilityAlarm": capo_resiliencehubv2.types.observability_alarm_summary.deserialize_json(
                data["observabilityAlarm"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TestSourceSummary: no recognized variant key")
