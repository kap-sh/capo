"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeUserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.boolean
    import capo_workmail.types.email_address
    import capo_workmail.types.entity_state
    import capo_workmail.types.identity_provider_identity_store_id
    import capo_workmail.types.identity_provider_user_id
    import capo_workmail.types.timestamp
    import capo_workmail.types.user_attribute
    import capo_workmail.types.user_name
    import capo_workmail.types.user_role
    import capo_workmail.types.work_mail_identifier


class DescribeUserResponse(TypedDict, closed=True):
    user_id: NotRequired["capo_workmail.types.work_mail_identifier.WorkMailIdentifier"]
    """<p>The identifier for the described user.</p>"""
    name: NotRequired["capo_workmail.types.user_name.UserName"]
    """<p>The name for the user.</p>"""
    email: NotRequired["capo_workmail.types.email_address.EmailAddress"]
    """<p>The email of the user.</p>"""
    display_name: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>The display name of the user.</p>"""
    state: NotRequired["capo_workmail.types.entity_state.EntityState"]
    """<p>The state of a user: enabled (registered to WorkMail) or disabled (deregistered or never registered to WorkMail).</p>"""
    user_role: NotRequired["capo_workmail.types.user_role.UserRole"]
    """<p>In certain cases, other entities are modeled as users. If interoperability is enabled, resources are imported into WorkMail as users. Because different WorkMail organizations rely on different directory types, administrators can distinguish between an unregistered user (account is disabled and has a user role) and the directory administrators. The values are USER, RESOURCE, SYSTEM_USER, and REMOTE_USER.</p>"""
    enabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date and time at which the user was enabled for WorkMailusage, in UNIX epoch time format.</p>"""
    disabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date and time at which the user was disabled for WorkMail usage, in UNIX epoch time format.</p>"""
    mailbox_provisioned_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date when the mailbox was created for the user.</p>"""
    mailbox_deprovisioned_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date when the mailbox was removed for the user.</p>"""
    first_name: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>First name of the user.</p>"""
    last_name: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Last name of the user.</p>"""
    hidden_from_global_address_list: "capo_workmail.types.boolean.Boolean"
    """<p>If enabled, the user is hidden from the global address list.</p>"""
    initials: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Initials of the user.</p>"""
    telephone: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>User's contact number.</p>"""
    street: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Street where the user is located.</p>"""
    job_title: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Job title of the user.</p>"""
    city: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>City where the user is located.</p>"""
    company: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Company of the user.</p>"""
    zip_code: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Zip code of the user.</p>"""
    department: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Department of the user.</p>"""
    country: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Country where the user is located.</p>"""
    office: NotRequired["capo_workmail.types.user_attribute.UserAttribute"]
    """<p>Office where the user is located.</p>"""
    identity_provider_user_id: NotRequired[
        "capo_workmail.types.identity_provider_user_id.IdentityProviderUserId"
    ]
    """<p>User ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.</p>"""
    identity_provider_identity_store_id: NotRequired[
        "capo_workmail.types.identity_provider_identity_store_id.IdentityProviderIdentityStoreId"
    ]
    """<p> Identity Store ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserResponse) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "email" in value:
        out["Email"] = value["email"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "state" in value:
        import capo_workmail.types.entity_state

        out["State"] = capo_workmail.types.entity_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "user_role" in value:
        import capo_workmail.types.user_role

        out["UserRole"] = capo_workmail.types.user_role.serialize_aws_json_1_1(
            value["user_role"]
        )
    if "enabled_date" in value:
        import capo_workmail.types.timestamp

        out["EnabledDate"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["enabled_date"]
        )
    if "disabled_date" in value:
        import capo_workmail.types.timestamp

        out["DisabledDate"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["disabled_date"]
        )
    if "mailbox_provisioned_date" in value:
        import capo_workmail.types.timestamp

        out["MailboxProvisionedDate"] = (
            capo_workmail.types.timestamp.serialize_aws_json_1_1(
                value["mailbox_provisioned_date"]
            )
        )
    if "mailbox_deprovisioned_date" in value:
        import capo_workmail.types.timestamp

        out["MailboxDeprovisionedDate"] = (
            capo_workmail.types.timestamp.serialize_aws_json_1_1(
                value["mailbox_deprovisioned_date"]
            )
        )
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    out["HiddenFromGlobalAddressList"] = value.get(
        "hidden_from_global_address_list", False
    )
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
    if "identity_provider_identity_store_id" in value:
        out["IdentityProviderIdentityStoreId"] = value[
            "identity_provider_identity_store_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserResponse:
    out: DescribeUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("State") is not None:
        import capo_workmail.types.entity_state

        out["state"] = capo_workmail.types.entity_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("UserRole") is not None:
        import capo_workmail.types.user_role

        out["user_role"] = capo_workmail.types.user_role.deserialize_aws_json_1_1(
            data["UserRole"]
        )
    if data.get("EnabledDate") is not None:
        import capo_workmail.types.timestamp

        out["enabled_date"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["EnabledDate"]
        )
    if data.get("DisabledDate") is not None:
        import capo_workmail.types.timestamp

        out["disabled_date"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DisabledDate"]
        )
    if data.get("MailboxProvisionedDate") is not None:
        import capo_workmail.types.timestamp

        out["mailbox_provisioned_date"] = (
            capo_workmail.types.timestamp.deserialize_aws_json_1_1(
                data["MailboxProvisionedDate"]
            )
        )
    if data.get("MailboxDeprovisionedDate") is not None:
        import capo_workmail.types.timestamp

        out["mailbox_deprovisioned_date"] = (
            capo_workmail.types.timestamp.deserialize_aws_json_1_1(
                data["MailboxDeprovisionedDate"]
            )
        )
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    if data.get("HiddenFromGlobalAddressList") is not None:
        out["hidden_from_global_address_list"] = data["HiddenFromGlobalAddressList"]
    else:
        out["hidden_from_global_address_list"] = False
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
    if data.get("IdentityProviderIdentityStoreId") is not None:
        out["identity_provider_identity_store_id"] = data[
            "IdentityProviderIdentityStoreId"
        ]
    return out


def redact_sensitive(value: DescribeUserResponse) -> dict[str, Any]:
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
