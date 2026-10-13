"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.boolean_object
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.identity_provider_user_id_for_update
    import capo_workmail.types.organization_id
    import capo_workmail.types.user_attribute
    import capo_workmail.types.user_role


class UpdateUserRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization under which the user exists.</p>"""
    user_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier for the user to be updated.</p> <p>The identifier can be the <i>UserId</i>, <i>Username</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>User ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: user@domain.tld</p> </li> <li> <p>User name: user</p> </li> </ul>"""
    role: NotRequired["capo_workmail.types.user_role.UserRole"]
    """<p>Updates the user role.</p> <p>You cannot pass <i>SYSTEM_USER</i> or <i>RESOURCE</i>.</p>"""
    display_name: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Updates the display name of the user.</p>"""
    first_name: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Updates the user's first name.</p>"""
    last_name: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Updates the user's last name.</p>"""
    hidden_from_global_address_list: NotRequired[
        "capo_workmail.types.boolean_object.BooleanObject"
    ]
    """<p>If enabled, the user is hidden from the global address list.</p>"""
    initials: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Updates the user's initials.</p>"""
    telephone: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Updates the user's contact details.</p>"""
    street: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Updates the user's street address.</p>"""
    job_title: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Updates the user's job title.</p>"""
    city: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Updates the user's city.</p>"""
    company: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Updates the user's company.</p>"""
    zip_code: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Updates the user's zip code.</p>"""
    department: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Updates the user's department.</p>"""
    country: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Updates the user's country.</p>"""
    office: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Updates the user's office.</p>"""
    identity_provider_user_id: NotRequired[
        "capo_workmail.types.identity_provider_user_id_for_update.IdentityProviderUserIdForUpdate"
    ]
    """<p>User ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["UserId"] = value["user_id"]
    if "role" in value:
        import capo_workmail.types.user_role

        out["Role"] = capo_workmail.types.user_role.serialize_aws_json_1_1(
            value["role"]
        )
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "hidden_from_global_address_list" in value:
        out["HiddenFromGlobalAddressList"] = value["hidden_from_global_address_list"]
    if "initials" in value:
        out["Initials"] = value["initials"]
    if "telephone" in value:
        out["Telephone"] = value["telephone"]
    if "street" in value:
        out["Street"] = value["street"]
    if "job_title" in value:
        out["JobTitle"] = value["job_title"]
    if "city" in value:
        out["City"] = value["city"]
    if "company" in value:
        out["Company"] = value["company"]
    if "zip_code" in value:
        out["ZipCode"] = value["zip_code"]
    if "department" in value:
        out["Department"] = value["department"]
    if "country" in value:
        out["Country"] = value["country"]
    if "office" in value:
        out["Office"] = value["office"]
    if "identity_provider_user_id" in value:
        out["IdentityProviderUserId"] = value["identity_provider_user_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("UpdateUserRequest.organization_id required")
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("UpdateUserRequest.user_id required")
    if data.get("Role") is not None:
        import capo_workmail.types.user_role

        out["role"] = capo_workmail.types.user_role.deserialize_aws_json_1_1(
            data["Role"]
        )
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    if data.get("HiddenFromGlobalAddressList") is not None:
        out["hidden_from_global_address_list"] = data["HiddenFromGlobalAddressList"]
    if data.get("Initials") is not None:
        out["initials"] = data["Initials"]
    if data.get("Telephone") is not None:
        out["telephone"] = data["Telephone"]
    if data.get("Street") is not None:
        out["street"] = data["Street"]
    if data.get("JobTitle") is not None:
        out["job_title"] = data["JobTitle"]
    if data.get("City") is not None:
        out["city"] = data["City"]
    if data.get("Company") is not None:
        out["company"] = data["Company"]
    if data.get("ZipCode") is not None:
        out["zip_code"] = data["ZipCode"]
    if data.get("Department") is not None:
        out["department"] = data["Department"]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("Office") is not None:
        out["office"] = data["Office"]
    if data.get("IdentityProviderUserId") is not None:
        out["identity_provider_user_id"] = data["IdentityProviderUserId"]
    return out


def redact_sensitive(value: UpdateUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    if "initials" in value:
        out["initials"] = "*** Sensitive Data Redacted ***"
    if "telephone" in value:
        out["telephone"] = "*** Sensitive Data Redacted ***"
    if "street" in value:
        out["street"] = "*** Sensitive Data Redacted ***"
    if "job_title" in value:
        out["job_title"] = "*** Sensitive Data Redacted ***"
    if "city" in value:
        out["city"] = "*** Sensitive Data Redacted ***"
    if "company" in value:
        out["company"] = "*** Sensitive Data Redacted ***"
    if "zip_code" in value:
        out["zip_code"] = "*** Sensitive Data Redacted ***"
    if "department" in value:
        out["department"] = "*** Sensitive Data Redacted ***"
    if "country" in value:
        out["country"] = "*** Sensitive Data Redacted ***"
    if "office" in value:
        out["office"] = "*** Sensitive Data Redacted ***"
    return out
