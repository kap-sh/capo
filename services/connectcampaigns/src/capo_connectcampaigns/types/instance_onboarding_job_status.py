"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#InstanceOnboardingJobStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.instance_id
    import capo_connectcampaigns.types.instance_onboarding_job_failure_code
    import capo_connectcampaigns.types.instance_onboarding_job_status_code


class InstanceOnboardingJobStatus(TypedDict, closed=True):
    connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId"
    status: "capo_connectcampaigns.types.instance_onboarding_job_status_code.InstanceOnboardingJobStatusCode"
    failure_code: NotRequired[
        "capo_connectcampaigns.types.instance_onboarding_job_failure_code.InstanceOnboardingJobFailureCode"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceOnboardingJobStatus) -> dict:
    out: dict = {}
    out["connectInstanceId"] = value["connect_instance_id"]
    out["status"] = value["status"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    return out


def deserialize_json(data: dict) -> InstanceOnboardingJobStatus:
    out: InstanceOnboardingJobStatus = {}  # type: ignore[typeddict-item]
    if data.get("connectInstanceId") is not None:
        out["connect_instance_id"] = data["connectInstanceId"]
    else:
        out["connect_instance_id"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("failureCode") is not None:
        out["failure_code"] = data["failureCode"]
    return out
