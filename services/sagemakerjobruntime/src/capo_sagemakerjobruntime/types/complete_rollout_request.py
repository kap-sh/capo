"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#CompleteRolloutRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakerjobruntime.types.completion_status
    import capo_sagemakerjobruntime.types.job_arn
    import capo_sagemakerjobruntime.types.trajectory_id


class CompleteRolloutRequest(TypedDict, closed=True):
    job_arn: "capo_sagemakerjobruntime.types.job_arn.JobArn"
    """The job ARN."""
    trajectory_id: "capo_sagemakerjobruntime.types.trajectory_id.TrajectoryId"
    """The trajectory ID to mark as complete."""
    status: NotRequired[
        "capo_sagemakerjobruntime.types.completion_status.CompletionStatus"
    ]
    """The target status for the trajectory. Defaults to READY if not specified. Set to FAILED if the rollout encountered an error and the trajectory should not be used for processing."""
    client_token: NotRequired["str"]
    """A unique, case-sensitive identifier that you provide to ensure the idempotency of the request."""


# --- restJson1 ser/de ---
def serialize_json(value: CompleteRolloutRequest) -> dict:
    out: dict = {}
    out["TrajectoryId"] = value["trajectory_id"]
    if "status" in value:
        import capo_sagemakerjobruntime.types.completion_status

        out["Status"] = capo_sagemakerjobruntime.types.completion_status.serialize_json(
            value["status"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CompleteRolloutRequest:
    out: CompleteRolloutRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrajectoryId") is not None:
        out["trajectory_id"] = data["TrajectoryId"]
    else:
        out["trajectory_id"] = ""
    if data.get("Status") is not None:
        import capo_sagemakerjobruntime.types.completion_status

        out["status"] = (
            capo_sagemakerjobruntime.types.completion_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
