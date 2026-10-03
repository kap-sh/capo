"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetApplicationAssignmentConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.assignment_required


class GetApplicationAssignmentConfigurationResponse(TypedDict, closed=True):
    assignment_required: "capo_sso_admin.types.assignment_required.AssignmentRequired"
    """<p>If <code>AssignmentsRequired</code> is <code>true</code> (default value), users don’t have access to the application unless an assignment is created using the <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplicationAssignment.html">CreateApplicationAssignment API</a>. If <code>false</code>, all users have access to the application. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetApplicationAssignmentConfigurationResponse,
) -> dict:
    out: dict = {}
    out["AssignmentRequired"] = value.get("assignment_required", True)
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetApplicationAssignmentConfigurationResponse:
    out: GetApplicationAssignmentConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("AssignmentRequired") is not None:
        out["assignment_required"] = data["AssignmentRequired"]
    else:
        out["assignment_required"] = True
    return out
