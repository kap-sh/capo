"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.boolean
    import capo_quicksight.types.namespace
    import capo_quicksight.types.role_name
    import capo_quicksight.types.string
    import capo_quicksight.types.user_name
    import capo_quicksight.types.user_role


class UpdateUserRequest(TypedDict, closed=True):
    user_name: "capo_quicksight.types.user_name.UserName"
    """<p>The Amazon Quick Sight user name that you want to update.</p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the user is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace. Currently, you should set this to <code>default</code>.</p>"""
    email: "capo_quicksight.types.string.String"
    """<p>The email address of the user that you want to update.</p>"""
    role: "capo_quicksight.types.user_role.UserRole"
    """<p>The Amazon Quick Sight role of the user. The role can be one of the following default security cohorts:</p> <ul> <li> <p> <code>READER</code>: A user who has read-only access to dashboards.</p> </li> <li> <p> <code>AUTHOR</code>: A user who can create data sources, datasets, analyses, and dashboards.</p> </li> <li> <p> <code>ADMIN</code>: A user who is an author, who can also manage Amazon Quick Sight settings.</p> </li> <li> <p> <code>READER_PRO</code>: Reader Pro adds Generative BI capabilities to the Reader role. Reader Pros have access to Amazon Q in Quick Sight, can build stories with Amazon Q, and can generate executive summaries from dashboards.</p> </li> <li> <p> <code>AUTHOR_PRO</code>: Author Pro adds Generative BI capabilities to the Author role. Author Pros can author dashboards with natural language with Amazon Q, build stories with Amazon Q, create Topics for Q&A, and generate executive summaries from dashboards.</p> </li> <li> <p> <code>ADMIN_PRO</code>: Admin Pros are Author Pros who can also manage Amazon Quick Sight administrative settings. Admin Pro users are billed at Author Pro pricing.</p> </li> </ul> <p>The name of the Quick Sight role is invisible to the user except for the console screens dealing with permissions.</p>"""
    custom_permissions_name: NotRequired["capo_quicksight.types.role_name.RoleName"]
    """<p>(Enterprise edition only) The name of the custom permissions profile that you want to assign to this user. Customized permissions allows you to control a user's access by restricting access the following operations:</p> <ul> <li> <p>Create and update data sources</p> </li> <li> <p>Create and update datasets</p> </li> <li> <p>Create and update email reports</p> </li> <li> <p>Subscribe to email reports</p> </li> </ul> <p>A set of custom permissions includes any combination of these restrictions. Currently, you need to create the profile names for custom permission sets by using the Quick Sight console. Then, you use the <code>RegisterUser</code> API operation to assign the named set of permissions to a Quick Sight user. </p> <p>Quick Sight custom permissions are applied through IAM policies. Therefore, they override the permissions typically granted by assigning Quick Sight users to one of the default security cohorts in Quick Sight (admin, author, reader).</p> <p>This feature is available only to Quick Sight Enterprise edition subscriptions.</p>"""
    unapply_custom_permissions: "capo_quicksight.types.boolean.Boolean"
    """<p>A flag that you use to indicate that you want to remove all custom permissions from this user. Using this parameter resets the user to the state it was in before a custom permissions profile was applied. This parameter defaults to NULL and it doesn't accept any other value.</p>"""
    external_login_federation_provider_type: NotRequired[
        "capo_quicksight.types.string.String"
    ]
    """<p>The type of supported external login provider that provides identity to let a user federate into Quick Sight with an associated Identity and Access Management(IAM) role. The type of supported external login provider can be one of the following.</p> <ul> <li> <p> <code>COGNITO</code>: Amazon Cognito. The provider URL is cognito-identity.amazonaws.com. When choosing the <code>COGNITO</code> provider type, don’t use the "CustomFederationProviderUrl" parameter which is only needed when the external provider is custom.</p> </li> <li> <p> <code>CUSTOM_OIDC</code>: Custom OpenID Connect (OIDC) provider. When choosing <code>CUSTOM_OIDC</code> type, use the <code>CustomFederationProviderUrl</code> parameter to provide the custom OIDC provider URL.</p> </li> <li> <p> <code>NONE</code>: This clears all the previously saved external login information for a user. Use the <code> <a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeUser.html">DescribeUser</a> </code> API operation to check the external login information.</p> </li> </ul>"""
    custom_federation_provider_url: NotRequired["capo_quicksight.types.string.String"]
    """<p>The URL of the custom OpenID Connect (OIDC) provider that provides identity to let a user federate into Quick Sight with an associated Identity and Access Management(IAM) role. This parameter should only be used when <code>ExternalLoginFederationProviderType</code> parameter is set to <code>CUSTOM_OIDC</code>.</p>"""
    external_login_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The identity ID for a user in the external login provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRequest) -> dict:
    out: dict = {}
    out["Email"] = value["email"]
    import capo_quicksight.types.user_role

    out["Role"] = capo_quicksight.types.user_role.serialize_json(value["role"])
    if "custom_permissions_name" in value:
        out["CustomPermissionsName"] = value["custom_permissions_name"]
    out["UnapplyCustomPermissions"] = value.get("unapply_custom_permissions", False)
    if "external_login_federation_provider_type" in value:
        out["ExternalLoginFederationProviderType"] = value[
            "external_login_federation_provider_type"
        ]
    if "custom_federation_provider_url" in value:
        out["CustomFederationProviderUrl"] = value["custom_federation_provider_url"]
    if "external_login_id" in value:
        out["ExternalLoginId"] = value["external_login_id"]
    return out


def deserialize_json(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("UpdateUserRequest.email required")
    if data.get("Role") is not None:
        import capo_quicksight.types.user_role

        out["role"] = capo_quicksight.types.user_role.deserialize_json(data["Role"])
    else:
        raise DeserializationError("UpdateUserRequest.role required")
    if data.get("CustomPermissionsName") is not None:
        out["custom_permissions_name"] = data["CustomPermissionsName"]
    if data.get("UnapplyCustomPermissions") is not None:
        out["unapply_custom_permissions"] = data["UnapplyCustomPermissions"]
    else:
        out["unapply_custom_permissions"] = False
    if data.get("ExternalLoginFederationProviderType") is not None:
        out["external_login_federation_provider_type"] = data[
            "ExternalLoginFederationProviderType"
        ]
    if data.get("CustomFederationProviderUrl") is not None:
        out["custom_federation_provider_url"] = data["CustomFederationProviderUrl"]
    if data.get("ExternalLoginId") is not None:
        out["external_login_id"] = data["ExternalLoginId"]
    return out
