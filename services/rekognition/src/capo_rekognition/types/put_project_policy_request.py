"""Generated from Smithy shape ``com.amazonaws.rekognition#PutProjectPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.project_arn
    import capo_rekognition.types.project_policy_document
    import capo_rekognition.types.project_policy_name
    import capo_rekognition.types.project_policy_revision_id


class PutProjectPolicyRequest(TypedDict, closed=True):
    project_arn: "capo_rekognition.types.project_arn.ProjectArn"
    """<p>The Amazon Resource Name (ARN) of the project that the project policy is attached to.</p>"""
    policy_name: "capo_rekognition.types.project_policy_name.ProjectPolicyName"
    """<p>A name for the policy.</p>"""
    policy_revision_id: NotRequired[
        "capo_rekognition.types.project_policy_revision_id.ProjectPolicyRevisionId"
    ]
    """<p>The revision ID for the Project Policy. Each time you modify a policy, Amazon Rekognition Custom Labels generates and assigns a new <code>PolicyRevisionId</code> and then deletes the previous version of the policy.</p>"""
    policy_document: (
        "capo_rekognition.types.project_policy_document.ProjectPolicyDocument"
    )
    """<p>A resource policy to add to the model. The policy is a JSON structure that contains one or more statements that define the policy. The policy must follow the IAM syntax. For more information about the contents of a JSON policy document, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html">IAM JSON policy reference</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutProjectPolicyRequest) -> dict:
    out: dict = {}
    out["ProjectArn"] = value["project_arn"]
    out["PolicyName"] = value["policy_name"]
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    out["PolicyDocument"] = value["policy_document"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutProjectPolicyRequest:
    out: PutProjectPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProjectArn") is not None:
        out["project_arn"] = data["ProjectArn"]
    else:
        raise DeserializationError("PutProjectPolicyRequest.project_arn required")
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    else:
        raise DeserializationError("PutProjectPolicyRequest.policy_name required")
    if data.get("PolicyRevisionId") is not None:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    if data.get("PolicyDocument") is not None:
        out["policy_document"] = data["PolicyDocument"]
    else:
        raise DeserializationError("PutProjectPolicyRequest.policy_document required")
    return out
