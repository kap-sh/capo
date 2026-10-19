"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AlarmStateChangeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.alarm_state


class AlarmStateChangeDetail(TypedDict, closed=True):
    state: "capo_resiliencehubv2.types.alarm_state.AlarmState"
    """<p>The state the alarm transitioned to.</p>"""
    previous_state: NotRequired["capo_resiliencehubv2.types.alarm_state.AlarmState"]
    """<p>The state the alarm transitioned from. Absent on the initial event, which records the alarm's state when collection began.</p>"""
    reason: NotRequired["str"]
    """<p>A human-readable explanation of the state change, as reported by CloudWatch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlarmStateChangeDetail) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.alarm_state

    out["state"] = capo_resiliencehubv2.types.alarm_state.serialize_json(value["state"])
    if "previous_state" in value:
        import capo_resiliencehubv2.types.alarm_state

        out["previousState"] = capo_resiliencehubv2.types.alarm_state.serialize_json(
            value["previous_state"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> AlarmStateChangeDetail:
    out: AlarmStateChangeDetail = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_resiliencehubv2.types.alarm_state

        out["state"] = capo_resiliencehubv2.types.alarm_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_resiliencehubv2.types.alarm_state.AlarmState", ""
        )
    if data.get("previousState") is not None:
        import capo_resiliencehubv2.types.alarm_state

        out["previous_state"] = capo_resiliencehubv2.types.alarm_state.deserialize_json(
            data["previousState"]
        )
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
