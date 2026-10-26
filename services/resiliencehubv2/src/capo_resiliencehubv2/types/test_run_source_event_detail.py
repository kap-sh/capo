"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunSourceEventDetail``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError, SerializationError
from capo_resiliencehubv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.alarm_state_change_detail
    import capo_resiliencehubv2.types.test_run_source_event_error


class _TestRunSourceEventDetail_alarmStateChange(TypedDict, closed=True):
    alarmStateChange: (
        "capo_resiliencehubv2.types.alarm_state_change_detail.AlarmStateChangeDetail"
    )


class _TestRunSourceEventDetail_error(TypedDict, closed=True):
    error: (
        "capo_resiliencehubv2.types.test_run_source_event_error.TestRunSourceEventError"
    )


TestRunSourceEventDetail: TypeAlias = (
    _TestRunSourceEventDetail_alarmStateChange
    | _TestRunSourceEventDetail_error
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TestRunSourceEventDetail) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TestRunSourceEventDetail: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "alarmStateChange" in value:
        import capo_resiliencehubv2.types.alarm_state_change_detail

        return {
            "alarmStateChange": capo_resiliencehubv2.types.alarm_state_change_detail.serialize_json(
                value["alarmStateChange"]
            )
        }
    elif "error" in value:
        import capo_resiliencehubv2.types.test_run_source_event_error

        return {
            "error": capo_resiliencehubv2.types.test_run_source_event_error.serialize_json(
                value["error"]
            )
        }
    else:
        raise SerializationError("TestRunSourceEventDetail: no variant present")


def deserialize_json(data: dict) -> TestRunSourceEventDetail:
    if data.get("alarmStateChange") is not None:
        import capo_resiliencehubv2.types.alarm_state_change_detail

        return {
            "alarmStateChange": capo_resiliencehubv2.types.alarm_state_change_detail.deserialize_json(
                data["alarmStateChange"]
            )
        }
    elif data.get("error") is not None:
        import capo_resiliencehubv2.types.test_run_source_event_error

        return {
            "error": capo_resiliencehubv2.types.test_run_source_event_error.deserialize_json(
                data["error"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "TestRunSourceEventDetail: no recognized variant key"
        )
