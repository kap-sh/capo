"""Generated from Smithy shape ``com.amazonaws.ecr#DeregisterPullTimeUpdateExclusionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.principal_arn


class DeregisterPullTimeUpdateExclusionRequest(TypedDict, closed=True):
    principal_arn: "capo_ecr.types.principal_arn.PrincipalArn"
    """<p>The ARN of the IAM principal to remove from the pull time update exclusion list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterPullTimeUpdateExclusionRequest) -> dict:
    out: dict = {}
    out["principalArn"] = value["principal_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterPullTimeUpdateExclusionRequest:
    out: DeregisterPullTimeUpdateExclusionRequest = {}  # type: ignore[typeddict-item]
    if data.get("principalArn") is not None:
        out["principal_arn"] = data["principalArn"]
    else:
        out["principal_arn"] = ""
    return out
