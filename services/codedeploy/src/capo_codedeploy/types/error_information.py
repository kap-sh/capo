"""Generated from Smithy shape ``com.amazonaws.codedeploy#ErrorInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.error_code
    import capo_codedeploy.types.error_message


class ErrorInformation(TypedDict, closed=True):
    code: NotRequired["capo_codedeploy.types.error_code.ErrorCode"]
    """<p>For more information, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html">Error Codes for CodeDeploy</a> in the <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide">CodeDeploy User Guide</a>.</p> <p>The error code:</p> <ul> <li> <p>APPLICATION_MISSING: The application was missing. This error code is most likely raised if the application is deleted after the deployment is created, but before it is started.</p> </li> <li> <p>DEPLOYMENT_GROUP_MISSING: The deployment group was missing. This error code is most likely raised if the deployment group is deleted after the deployment is created, but before it is started.</p> </li> <li> <p>HEALTH_CONSTRAINTS: The deployment failed on too many instances to be successfully deployed within the instance health constraints specified.</p> </li> <li> <p>HEALTH_CONSTRAINTS_INVALID: The revision cannot be successfully deployed within the instance health constraints specified.</p> </li> <li> <p>IAM_ROLE_MISSING: The service role cannot be accessed.</p> </li> <li> <p>IAM_ROLE_PERMISSIONS: The service role does not have the correct permissions.</p> </li> <li> <p>INTERNAL_ERROR: There was an internal error.</p> </li> <li> <p>NO_EC2_SUBSCRIPTION: The calling account is not subscribed to Amazon EC2.</p> </li> <li> <p>NO_INSTANCES: No instances were specified, or no instances can be found.</p> </li> <li> <p>OVER_MAX_INSTANCES: The maximum number of instances was exceeded.</p> </li> <li> <p>THROTTLED: The operation was throttled because the calling account exceeded the throttling limits of one or more Amazon Web Services services.</p> </li> <li> <p>TIMEOUT: The deployment has timed out.</p> </li> <li> <p>REVISION_MISSING: The revision ID was missing. This error code is most likely raised if the revision is deleted after the deployment is created, but before it is started.</p> </li> </ul>"""
    message: NotRequired["capo_codedeploy.types.error_message.ErrorMessage"]
    """<p>An accompanying error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorInformation) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_codedeploy.types.error_code

        out["code"] = capo_codedeploy.types.error_code.serialize_aws_json_1_1(
            value["code"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorInformation:
    out: ErrorInformation = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_codedeploy.types.error_code

        out["code"] = capo_codedeploy.types.error_code.deserialize_aws_json_1_1(
            data["code"]
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
