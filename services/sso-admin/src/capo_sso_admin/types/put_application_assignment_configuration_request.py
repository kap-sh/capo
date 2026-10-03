"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PutApplicationAssignmentConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.assignment_required


class PutApplicationAssignmentConfigurationRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    assignment_required: "capo_sso_admin.types.assignment_required.AssignmentRequired"
    """<p>If <code>AssignmentsRequired</code> is <code>true</code> (default value), users don’t have access to the application unless an assignment is created using the <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplicationAssignment.html">CreateApplicationAssignment API</a>. If <code>false</code>, all users have access to the application. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutApplicationAssignmentConfigurationRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    out["AssignmentRequired"] = value.get("assignment_required", True)
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> PutApplicationAssignmentConfigurationRequest:
    out: PutApplicationAssignmentConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "PutApplicationAssignmentConfigurationRequest.application_arn required"
        )
    if data.get("AssignmentRequired") is not None:
        out["assignment_required"] = data["AssignmentRequired"]
    else:
        out["assignment_required"] = True
    return out
