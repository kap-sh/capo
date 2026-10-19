"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunStateChange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.assessment_run_state
    import capo_inspector.types.timestamp


class AssessmentRunStateChange(TypedDict, closed=True):
    state_changed_at: "capo_inspector.types.timestamp.Timestamp"
    """<p>The last time the assessment run state changed.</p>"""
    state: "capo_inspector.types.assessment_run_state.AssessmentRunState"
    """<p>The assessment run state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunStateChange) -> dict:
    out: dict = {}
    import capo_inspector.types.timestamp

    out["stateChangedAt"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
        value["state_changed_at"]
    )
    import capo_inspector.types.assessment_run_state

    out["state"] = capo_inspector.types.assessment_run_state.serialize_aws_json_1_1(
        value["state"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentRunStateChange:
    out: AssessmentRunStateChange = {}  # type: ignore[typeddict-item]
    if data.get("stateChangedAt") is not None:
        import capo_inspector.types.timestamp

        out["state_changed_at"] = (
            capo_inspector.types.timestamp.deserialize_aws_json_1_1(
                data["stateChangedAt"]
            )
        )
    else:
        import datetime

        out["state_changed_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("state") is not None:
        import capo_inspector.types.assessment_run_state

        out["state"] = (
            capo_inspector.types.assessment_run_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_inspector.types.assessment_run_state.AssessmentRunState", ""
        )
    return out
