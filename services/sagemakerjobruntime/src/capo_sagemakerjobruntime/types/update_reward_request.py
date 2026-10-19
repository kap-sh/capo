"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#UpdateRewardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakerjobruntime.types.double_list
    import capo_sagemakerjobruntime.types.job_arn
    import capo_sagemakerjobruntime.types.trajectory_id


class UpdateRewardRequest(TypedDict, closed=True):
    job_arn: "capo_sagemakerjobruntime.types.job_arn.JobArn"
    """The job ARN."""
    trajectory_id: "capo_sagemakerjobruntime.types.trajectory_id.TrajectoryId"
    """The trajectory ID to update with reward values."""
    rewards: "capo_sagemakerjobruntime.types.double_list.DoubleList"
    """The list of reward values to assign to this trajectory. Provide one reward value per turn in the trajectory."""
    client_token: NotRequired["str"]
    """A unique, case-sensitive identifier that you provide to ensure the idempotency of the request."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRewardRequest) -> dict:
    out: dict = {}
    out["TrajectoryId"] = value["trajectory_id"]
    import capo_sagemakerjobruntime.types.double_list

    out["Rewards"] = capo_sagemakerjobruntime.types.double_list.serialize_json(
        value["rewards"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateRewardRequest:
    out: UpdateRewardRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrajectoryId") is not None:
        out["trajectory_id"] = data["TrajectoryId"]
    else:
        out["trajectory_id"] = ""
    if data.get("Rewards") is not None:
        import capo_sagemakerjobruntime.types.double_list

        out["rewards"] = capo_sagemakerjobruntime.types.double_list.deserialize_json(
            data["Rewards"]
        )
    else:
        out["rewards"] = []
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
