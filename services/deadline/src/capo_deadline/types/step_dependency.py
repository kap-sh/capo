"""Generated from Smithy shape ``com.amazonaws.deadline#StepDependency``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.dependency_consumer_resolution_status
    import capo_deadline.types.step_id


class StepDependency(TypedDict, closed=True):
    step_id: "capo_deadline.types.step_id.StepId"
    """The step ID."""
    status: "capo_deadline.types.dependency_consumer_resolution_status.DependencyConsumerResolutionStatus"
    """The step dependency status."""


# --- restJson1 ser/de ---
def serialize_json(value: StepDependency) -> dict:
    out: dict = {}
    out["stepId"] = value["step_id"]
    import capo_deadline.types.dependency_consumer_resolution_status

    out["status"] = (
        capo_deadline.types.dependency_consumer_resolution_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> StepDependency:
    out: StepDependency = {}  # type: ignore[typeddict-item]
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    else:
        out["step_id"] = ""
    if data.get("status") is not None:
        import capo_deadline.types.dependency_consumer_resolution_status

        out["status"] = (
            capo_deadline.types.dependency_consumer_resolution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_deadline.types.dependency_consumer_resolution_status.DependencyConsumerResolutionStatus",
            "",
        )
    return out
