"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisterUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.identity_type
    import capo_quicksight.types.namespace
    import capo_quicksight.types.role_name
    import capo_quicksight.types.role_session_name
    import capo_quicksight.types.string
    import capo_quicksight.types.tag_list
    import capo_quicksight.types.user_name
    import capo_quicksight.types.user_role


class RegisterUserRequest(TypedDict, closed=True):
    identity_type: "capo_quicksight.types.identity_type.IdentityType"
    """<p>The identity type that your Quick Sight account uses to manage the identity of users.</p>"""
    email: "capo_quicksight.types.string.String"
    """<p>The email address of the user that you want to register.</p>"""
    user_role: "capo_quicksight.types.user_role.UserRole"
    """<p>The Amazon Quick Sight role for the user. The user role can be one of the following:</p> <ul> <li> <p> <code>READER</code>: A user who has read-only access to dashboards.</p> </li> <li> <p> <code>AUTHOR</code>: A user who can create data sources, datasets, analyses, and dashboards.</p> </li> <li> <p> <code>ADMIN</code>: A user who is an author, who can also manage Amazon Quick Sight settings.</p> </li> <li> <p> <code>READER_PRO</code>: Reader Pro adds Generative BI capabilities to the Reader role. Reader Pros have access to Amazon Q in Quick Sight, can build stories with Amazon Q, and can generate executive summaries from dashboards.</p> </li> <li> <p> <code>AUTHOR_PRO</code>: Author Pro adds Generative BI capabilities to the Author role. Author Pros can author dashboards with natural language with Amazon Q, build stories with Amazon Q, create Topics for Q&A, and generate executive summaries from dashboards.</p> </li> <li> <p> <code>ADMIN_PRO</code>: Admin Pros are Author Pros who can also manage Amazon Quick Sight administrative settings. Admin Pro users are billed at Author Pro pricing.</p> </li> <li> <p> <code>RESTRICTED_READER</code>: This role isn't currently available for use.</p> </li> <li> <p> <code>RESTRICTED_AUTHOR</code>: This role isn't currently available for use.</p> </li> </ul>"""
    iam_arn: NotRequired["capo_quicksight.types.string.String"]
    """<p>The ARN of the IAM user or role that you are registering with Amazon Quick Sight. </p>"""
    session_name: NotRequired["capo_quicksight.types.role_session_name.RoleSessionName"]
    """<p>You need to use this parameter only when you register one or more users using an assumed IAM role. You don't need to provide the session name for other scenarios, for example when you are registering an IAM user or an Amazon Quick Sight user. You can register multiple users using the same IAM role if each user has a different session name. For more information on assuming IAM roles, see <a href="https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html"> <code>assume-role</code> </a> in the <i>CLI Reference.</i> </p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the user is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace. Currently, you should set this to <code>default</code>.</p>"""
    user_name: NotRequired["capo_quicksight.types.user_name.UserName"]
    """<p>The Amazon Quick Sight user name that you want to create for the user you are registering.</p>"""
    custom_permissions_name: NotRequired["capo_quicksight.types.role_name.RoleName"]
    """<p>(Enterprise edition only) The name of the custom permissions profile that you want to assign to this user. Customized permissions allows you to control a user's access by restricting access the following operations:</p> <ul> <li> <p>Create and update data sources</p> </li> <li> <p>Create and update datasets</p> </li> <li> <p>Create and update email reports</p> </li> <li> <p>Subscribe to email reports</p> </li> </ul> <p>To add custom permissions to an existing user, use <code> <a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateUser.html">UpdateUser</a> </code> instead.</p> <p>A set of custom permissions includes any combination of these restrictions. Currently, you need to create the profile names for custom permission sets by using the Quick Sight console. Then, you use the <code>RegisterUser</code> API operation to assign the named set of permissions to a Quick Sight user. </p> <p>Quick Sight custom permissions are applied through IAM policies. Therefore, they override the permissions typically granted by assigning Quick Sight users to one of the default security cohorts in Quick Sight (admin, author, reader, admin pro, author pro, reader pro).</p> <p>This feature is available only to Quick Sight Enterprise edition subscriptions.</p>"""
    external_login_federation_provider_type: NotRequired[
        "capo_quicksight.types.string.String"
    ]
    """<p>The type of supported external login provider that provides identity to let a user federate into Amazon Quick Sight with an associated Identity and Access Management(IAM) role. The type of supported external login provider can be one of the following.</p> <ul> <li> <p> <code>COGNITO</code>: Amazon Cognito. The provider URL is cognito-identity.amazonaws.com. When choosing the <code>COGNITO</code> provider type, don’t use the "CustomFederationProviderUrl" parameter which is only needed when the external provider is custom.</p> </li> <li> <p> <code>CUSTOM_OIDC</code>: Custom OpenID Connect (OIDC) provider. When choosing <code>CUSTOM_OIDC</code> type, use the <code>CustomFederationProviderUrl</code> parameter to provide the custom OIDC provider URL.</p> </li> </ul>"""
    custom_federation_provider_url: NotRequired["capo_quicksight.types.string.String"]
    """<p>The URL of the custom OpenID Connect (OIDC) provider that provides identity to let a user federate into Quick Sight with an associated Identity and Access Management(IAM) role. This parameter should only be used when <code>ExternalLoginFederationProviderType</code> parameter is set to <code>CUSTOM_OIDC</code>.</p>"""
    external_login_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The identity ID for a user in the external login provider.</p>"""
    tags: NotRequired["capo_quicksight.types.tag_list.TagList"]
    """<p>The tags to associate with the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterUserRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.identity_type

    out["IdentityType"] = capo_quicksight.types.identity_type.serialize_json(
        value["identity_type"]
    )
    out["Email"] = value["email"]
    import capo_quicksight.types.user_role

    out["UserRole"] = capo_quicksight.types.user_role.serialize_json(value["user_role"])
    if "iam_arn" in value:
        out["IamArn"] = value["iam_arn"]
    if "session_name" in value:
        out["SessionName"] = value["session_name"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "custom_permissions_name" in value:
        out["CustomPermissionsName"] = value["custom_permissions_name"]
    if "external_login_federation_provider_type" in value:
        out["ExternalLoginFederationProviderType"] = value[
            "external_login_federation_provider_type"
        ]
    if "custom_federation_provider_url" in value:
        out["CustomFederationProviderUrl"] = value["custom_federation_provider_url"]
    if "external_login_id" in value:
        out["ExternalLoginId"] = value["external_login_id"]
    if "tags" in value:
        import capo_quicksight.types.tag_list

        out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RegisterUserRequest:
    out: RegisterUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdentityType") is not None:
        import capo_quicksight.types.identity_type

        out["identity_type"] = capo_quicksight.types.identity_type.deserialize_json(
            data["IdentityType"]
        )
    else:
        raise DeserializationError("RegisterUserRequest.identity_type required")
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("RegisterUserRequest.email required")
    if data.get("UserRole") is not None:
        import capo_quicksight.types.user_role

        out["user_role"] = capo_quicksight.types.user_role.deserialize_json(
            data["UserRole"]
        )
    else:
        raise DeserializationError("RegisterUserRequest.user_role required")
    if data.get("IamArn") is not None:
        out["iam_arn"] = data["IamArn"]
    if data.get("SessionName") is not None:
        out["session_name"] = data["SessionName"]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("CustomPermissionsName") is not None:
        out["custom_permissions_name"] = data["CustomPermissionsName"]
    if data.get("ExternalLoginFederationProviderType") is not None:
        out["external_login_federation_provider_type"] = data[
            "ExternalLoginFederationProviderType"
        ]
    if data.get("CustomFederationProviderUrl") is not None:
        out["custom_federation_provider_url"] = data["CustomFederationProviderUrl"]
    if data.get("ExternalLoginId") is not None:
        out["external_login_id"] = data["ExternalLoginId"]
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    return out
