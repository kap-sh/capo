"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateWorkteamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.member_definitions
    import capo_sagemaker.types.notification_configuration
    import capo_sagemaker.types.string200
    import capo_sagemaker.types.worker_access_configuration
    import capo_sagemaker.types.workteam_name


class UpdateWorkteamRequest(TypedDict, closed=True):
    workteam_name: NotRequired["capo_sagemaker.types.workteam_name.WorkteamName"]
    """<p>The name of the work team to update.</p>"""
    member_definitions: NotRequired[
        "capo_sagemaker.types.member_definitions.MemberDefinitions"
    ]
    """<p>A list of <code>MemberDefinition</code> objects that contains objects that identify the workers that make up the work team. </p> <p>Workforces can be created using Amazon Cognito or your own OIDC Identity Provider (IdP). For private workforces created using Amazon Cognito use <code>CognitoMemberDefinition</code>. For workforces created using your own OIDC identity provider (IdP) use <code>OidcMemberDefinition</code>. You should not provide input for both of these parameters in a single request.</p> <p>For workforces created using Amazon Cognito, private work teams correspond to Amazon Cognito <i>user groups</i> within the user pool used to create a workforce. All of the <code>CognitoMemberDefinition</code> objects that make up the member definition must have the same <code>ClientId</code> and <code>UserPool</code> values. To add a Amazon Cognito user group to an existing worker pool, see <a href="">Adding groups to a User Pool</a>. For more information about user pools, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html">Amazon Cognito User Pools</a>.</p> <p>For workforces created using your own OIDC IdP, specify the user groups that you want to include in your private work team in <code>OidcMemberDefinition</code> by listing those groups in <code>Groups</code>. Be aware that user groups that are already in the work team must also be listed in <code>Groups</code> when you make this request to remain on the work team. If you do not include these user groups, they will no longer be associated with the work team you update. </p>"""
    description: NotRequired["capo_sagemaker.types.string200.String200"]
    """<p>An updated description for the work team.</p>"""
    notification_configuration: NotRequired[
        "capo_sagemaker.types.notification_configuration.NotificationConfiguration"
    ]
    """<p>Configures SNS topic notifications for available or expiring work items</p>"""
    worker_access_configuration: NotRequired[
        "capo_sagemaker.types.worker_access_configuration.WorkerAccessConfiguration"
    ]
    """<p>Use this optional parameter to constrain access to an Amazon S3 resource based on the IP address using supported IAM global condition keys. The Amazon S3 resource is accessed in the worker portal using a Amazon S3 presigned URL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkteamRequest) -> dict:
    out: dict = {}
    if "workteam_name" in value:
        out["WorkteamName"] = value["workteam_name"]
    if "member_definitions" in value:
        import capo_sagemaker.types.member_definitions

        out["MemberDefinitions"] = (
            capo_sagemaker.types.member_definitions.serialize_aws_json_1_1(
                value["member_definitions"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "notification_configuration" in value:
        import capo_sagemaker.types.notification_configuration

        out["NotificationConfiguration"] = (
            capo_sagemaker.types.notification_configuration.serialize_aws_json_1_1(
                value["notification_configuration"]
            )
        )
    if "worker_access_configuration" in value:
        import capo_sagemaker.types.worker_access_configuration

        out["WorkerAccessConfiguration"] = (
            capo_sagemaker.types.worker_access_configuration.serialize_aws_json_1_1(
                value["worker_access_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkteamRequest:
    out: UpdateWorkteamRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkteamName") is not None:
        out["workteam_name"] = data["WorkteamName"]
    if data.get("MemberDefinitions") is not None:
        import capo_sagemaker.types.member_definitions

        out["member_definitions"] = (
            capo_sagemaker.types.member_definitions.deserialize_aws_json_1_1(
                data["MemberDefinitions"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("NotificationConfiguration") is not None:
        import capo_sagemaker.types.notification_configuration

        out["notification_configuration"] = (
            capo_sagemaker.types.notification_configuration.deserialize_aws_json_1_1(
                data["NotificationConfiguration"]
            )
        )
    if data.get("WorkerAccessConfiguration") is not None:
        import capo_sagemaker.types.worker_access_configuration

        out["worker_access_configuration"] = (
            capo_sagemaker.types.worker_access_configuration.deserialize_aws_json_1_1(
                data["WorkerAccessConfiguration"]
            )
        )
    return out
