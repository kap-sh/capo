"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetApplicationAssignmentConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn


class GetApplicationAssignmentConfigurationRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationAssignmentConfigurationRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetApplicationAssignmentConfigurationRequest:
    out: GetApplicationAssignmentConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "GetApplicationAssignmentConfigurationRequest.application_arn required"
        )
    return out
