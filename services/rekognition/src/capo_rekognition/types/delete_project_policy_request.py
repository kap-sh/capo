"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteProjectPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.project_arn
    import capo_rekognition.types.project_policy_name
    import capo_rekognition.types.project_policy_revision_id


class DeleteProjectPolicyRequest(TypedDict, closed=True):
    project_arn: "capo_rekognition.types.project_arn.ProjectArn"
    """<p>The Amazon Resource Name (ARN) of the project that the project policy you want to delete is attached to.</p>"""
    policy_name: "capo_rekognition.types.project_policy_name.ProjectPolicyName"
    """<p>The name of the policy that you want to delete.</p>"""
    policy_revision_id: NotRequired[
        "capo_rekognition.types.project_policy_revision_id.ProjectPolicyRevisionId"
    ]
    """<p>The ID of the project policy revision that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProjectPolicyRequest) -> dict:
    out: dict = {}
    out["ProjectArn"] = value["project_arn"]
    out["PolicyName"] = value["policy_name"]
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProjectPolicyRequest:
    out: DeleteProjectPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProjectArn") is not None:
        out["project_arn"] = data["ProjectArn"]
    else:
        out["project_arn"] = ""
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    else:
        out["policy_name"] = ""
    if data.get("PolicyRevisionId") is not None:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    return out
