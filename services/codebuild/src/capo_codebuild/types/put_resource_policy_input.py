"""Generated from Smithy shape ``com.amazonaws.codebuild#PutResourcePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string


class PutResourcePolicyInput(TypedDict, closed=True):
    policy: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p> A JSON-formatted resource policy. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/project-sharing.html#project-sharing-share">Sharing a Project</a> and <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/report-groups-sharing.html#report-groups-sharing-share">Sharing a Report Group</a> in the <i>CodeBuild User Guide</i>. </p>"""
    resource_arn: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p> The ARN of the <code>Project</code> or <code>ReportGroup</code> resource you want to associate with a resource policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyInput) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyInput:
    out: PutResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("PutResourcePolicyInput.policy required")
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("PutResourcePolicyInput.resource_arn required")
    return out
