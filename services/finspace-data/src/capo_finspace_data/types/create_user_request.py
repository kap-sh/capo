"""Generated from Smithy shape ``com.amazonaws.finspacedata#CreateUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_finspace_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_finspace_data.types.api_access
    import capo_finspace_data.types.client_token
    import capo_finspace_data.types.email
    import capo_finspace_data.types.first_name
    import capo_finspace_data.types.last_name
    import capo_finspace_data.types.role_arn
    import capo_finspace_data.types.user_type


class CreateUserRequest(TypedDict, closed=True):
    email_address: "capo_finspace_data.types.email.Email"
    """<p>The email address of the user that you want to register. The email address serves as a uniquer identifier for each user and cannot be changed after it's created.</p>"""
    type: "capo_finspace_data.types.user_type.UserType"
    """<p>The option to indicate the type of user. Use one of the following options to specify this parameter:</p> <ul> <li> <p> <code>SUPER_USER</code> – A user with permission to all the functionality and data in FinSpace.</p> </li> <li> <p> <code>APP_USER</code> – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.</p> </li> </ul>"""
    first_name: NotRequired["capo_finspace_data.types.first_name.FirstName"]
    """<p>The first name of the user that you want to register.</p>"""
    last_name: NotRequired["capo_finspace_data.types.last_name.LastName"]
    """<p>The last name of the user that you want to register.</p>"""
    api_access: NotRequired["capo_finspace_data.types.api_access.ApiAccess"]
    """<p>The option to indicate whether the user can use the <code>GetProgrammaticAccessCredentials</code> API to obtain credentials that can then be used to access other FinSpace Data API operations.</p> <ul> <li> <p> <code>ENABLED</code> – The user has permissions to use the APIs.</p> </li> <li> <p> <code>DISABLED</code> – The user does not have permissions to use any APIs.</p> </li> </ul>"""
    api_access_principal_arn: NotRequired["capo_finspace_data.types.role_arn.RoleArn"]
    """<p>The ARN identifier of an AWS user or role that is allowed to call the <code>GetProgrammaticAccessCredentials</code> API to obtain a credentials token for a specific FinSpace user. This must be an IAM role within your FinSpace account.</p>"""
    client_token: NotRequired["capo_finspace_data.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserRequest) -> dict:
    out: dict = {}
    out["emailAddress"] = value["email_address"]
    import capo_finspace_data.types.user_type

    out["type"] = capo_finspace_data.types.user_type.serialize_json(value["type"])
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    if "api_access" in value:
        import capo_finspace_data.types.api_access

        out["apiAccess"] = capo_finspace_data.types.api_access.serialize_json(
            value["api_access"]
        )
    if "api_access_principal_arn" in value:
        out["apiAccessPrincipalArn"] = value["api_access_principal_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    else:
        raise DeserializationError("CreateUserRequest.email_address required")
    if data.get("type") is not None:
        import capo_finspace_data.types.user_type

        out["type"] = capo_finspace_data.types.user_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("CreateUserRequest.type required")
    if data.get("firstName") is not None:
        out["first_name"] = data["firstName"]
    if data.get("lastName") is not None:
        out["last_name"] = data["lastName"]
    if data.get("apiAccess") is not None:
        import capo_finspace_data.types.api_access

        out["api_access"] = capo_finspace_data.types.api_access.deserialize_json(
            data["apiAccess"]
        )
    if data.get("apiAccessPrincipalArn") is not None:
        out["api_access_principal_arn"] = data["apiAccessPrincipalArn"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    return out
