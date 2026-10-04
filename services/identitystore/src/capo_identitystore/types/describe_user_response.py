"""Generated from Smithy shape ``com.amazonaws.identitystore#DescribeUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.addresses
    import capo_identitystore.types.date_type
    import capo_identitystore.types.emails
    import capo_identitystore.types.extensions
    import capo_identitystore.types.external_ids
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.name
    import capo_identitystore.types.phone_numbers
    import capo_identitystore.types.photos
    import capo_identitystore.types.resource_arn
    import capo_identitystore.types.resource_id
    import capo_identitystore.types.resource_revision
    import capo_identitystore.types.roles
    import capo_identitystore.types.sensitive_string_type
    import capo_identitystore.types.string_type
    import capo_identitystore.types.user_name
    import capo_identitystore.types.user_status


class DescribeUserResponse(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    user_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a user in the identity store.</p>"""
    user_arn: "capo_identitystore.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the user in the identity store. For example, <code>arn:aws:identitystore:::user/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>.</p>"""
    revision: "capo_identitystore.types.resource_revision.ResourceRevision"
    """<p>The current revision of the user in the identity store. This value changes each time the user is modified.</p>"""
    user_name: NotRequired["capo_identitystore.types.user_name.UserName"]
    """<p>A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at the time the user is created and stored as an attribute of the user object in the identity store.</p>"""
    external_ids: NotRequired["capo_identitystore.types.external_ids.ExternalIds"]
    """<p>A list of <code>ExternalId</code> objects that contains the identifiers issued to this resource by an external identity provider.</p>"""
    name: NotRequired["capo_identitystore.types.name.Name"]
    """<p>The name of the user.</p>"""
    display_name: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The display name of the user.</p>"""
    nick_name: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>An alternative descriptive name for the user.</p>"""
    profile_url: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A URL link for the user's profile.</p>"""
    emails: NotRequired["capo_identitystore.types.emails.Emails"]
    """<p>The email address of the user.</p>"""
    addresses: NotRequired["capo_identitystore.types.addresses.Addresses"]
    """<p>The physical address of the user.</p>"""
    phone_numbers: NotRequired["capo_identitystore.types.phone_numbers.PhoneNumbers"]
    """<p>A list of <code>PhoneNumber</code> objects associated with a user.</p>"""
    user_type: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string indicating the type of user.</p>"""
    title: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing the title of the user.</p>"""
    preferred_language: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The preferred language of the user.</p>"""
    locale: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing the geographical region or location of the user.</p>"""
    timezone: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The time zone for a user.</p>"""
    user_status: NotRequired["capo_identitystore.types.user_status.UserStatus"]
    """<p>The current status of the user account.</p>"""
    photos: NotRequired["capo_identitystore.types.photos.Photos"]
    """<p>A list of photos associated with the user. Returns up to 3 photos with their associated metadata including type, display name, and primary designation.</p>"""
    website: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The user's personal website or blog URL. Returns the stored website information for the user.</p>"""
    birthdate: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The user's birthdate in YYYY-MM-DD format. This field returns the stored birthdate information for the user.</p>"""
    roles: NotRequired["capo_identitystore.types.roles.Roles"]
    """<p>The roles of the user.</p>"""
    created_at: NotRequired["capo_identitystore.types.date_type.DateType"]
    """<p>The date and time the user was created.</p>"""
    created_by: NotRequired["capo_identitystore.types.string_type.StringType"]
    """<p>The identifier of the user or system that created the user.</p>"""
    updated_at: NotRequired["capo_identitystore.types.date_type.DateType"]
    """<p>The date and time the user was last updated.</p>"""
    updated_by: NotRequired["capo_identitystore.types.string_type.StringType"]
    """<p>The identifier of the user or system that last updated the user.</p>"""
    extensions: NotRequired["capo_identitystore.types.extensions.Extensions"]
    """<p>A map of explicitly requested attribute extensions associated with the user. Not populated if the user has no requested extensions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserResponse) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["UserId"] = value["user_id"]
    out["UserArn"] = value["user_arn"]
    out["Revision"] = value["revision"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "external_ids" in value:
        import capo_identitystore.types.external_ids

        out["ExternalIds"] = (
            capo_identitystore.types.external_ids.serialize_aws_json_1_1(
                value["external_ids"]
            )
        )
    if "name" in value:
        import capo_identitystore.types.name

        out["Name"] = capo_identitystore.types.name.serialize_aws_json_1_1(
            value["name"]
        )
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "nick_name" in value:
        out["NickName"] = value["nick_name"]
    if "profile_url" in value:
        out["ProfileUrl"] = value["profile_url"]
    if "emails" in value:
        import capo_identitystore.types.emails

        out["Emails"] = capo_identitystore.types.emails.serialize_aws_json_1_1(
            value["emails"]
        )
    if "addresses" in value:
        import capo_identitystore.types.addresses

        out["Addresses"] = capo_identitystore.types.addresses.serialize_aws_json_1_1(
            value["addresses"]
        )
    if "phone_numbers" in value:
        import capo_identitystore.types.phone_numbers

        out["PhoneNumbers"] = (
            capo_identitystore.types.phone_numbers.serialize_aws_json_1_1(
                value["phone_numbers"]
            )
        )
    if "user_type" in value:
        out["UserType"] = value["user_type"]
    if "title" in value:
        out["Title"] = value["title"]
    if "preferred_language" in value:
        out["PreferredLanguage"] = value["preferred_language"]
    if "locale" in value:
        out["Locale"] = value["locale"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    if "user_status" in value:
        import capo_identitystore.types.user_status

        out["UserStatus"] = capo_identitystore.types.user_status.serialize_aws_json_1_1(
            value["user_status"]
        )
    if "photos" in value:
        import capo_identitystore.types.photos

        out["Photos"] = capo_identitystore.types.photos.serialize_aws_json_1_1(
            value["photos"]
        )
    if "website" in value:
        out["Website"] = value["website"]
    if "birthdate" in value:
        out["Birthdate"] = value["birthdate"]
    if "roles" in value:
        import capo_identitystore.types.roles

        out["Roles"] = capo_identitystore.types.roles.serialize_aws_json_1_1(
            value["roles"]
        )
    if "created_at" in value:
        import capo_identitystore.types.date_type

        out["CreatedAt"] = capo_identitystore.types.date_type.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_identitystore.types.date_type

        out["UpdatedAt"] = capo_identitystore.types.date_type.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["UpdatedBy"] = value["updated_by"]
    if "extensions" in value:
        import capo_identitystore.types.extensions

        out["Extensions"] = capo_identitystore.types.extensions.serialize_aws_json_1_1(
            value["extensions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserResponse:
    out: DescribeUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("DescribeUserResponse.identity_store_id required")
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("DescribeUserResponse.user_id required")
    if data.get("UserArn") is not None:
        out["user_arn"] = data["UserArn"]
    else:
        raise DeserializationError("DescribeUserResponse.user_arn required")
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    else:
        raise DeserializationError("DescribeUserResponse.revision required")
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("ExternalIds") is not None:
        import capo_identitystore.types.external_ids

        out["external_ids"] = (
            capo_identitystore.types.external_ids.deserialize_aws_json_1_1(
                data["ExternalIds"]
            )
        )
    if data.get("Name") is not None:
        import capo_identitystore.types.name

        out["name"] = capo_identitystore.types.name.deserialize_aws_json_1_1(
            data["Name"]
        )
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("NickName") is not None:
        out["nick_name"] = data["NickName"]
    if data.get("ProfileUrl") is not None:
        out["profile_url"] = data["ProfileUrl"]
    if data.get("Emails") is not None:
        import capo_identitystore.types.emails

        out["emails"] = capo_identitystore.types.emails.deserialize_aws_json_1_1(
            data["Emails"]
        )
    if data.get("Addresses") is not None:
        import capo_identitystore.types.addresses

        out["addresses"] = capo_identitystore.types.addresses.deserialize_aws_json_1_1(
            data["Addresses"]
        )
    if data.get("PhoneNumbers") is not None:
        import capo_identitystore.types.phone_numbers

        out["phone_numbers"] = (
            capo_identitystore.types.phone_numbers.deserialize_aws_json_1_1(
                data["PhoneNumbers"]
            )
        )
    if data.get("UserType") is not None:
        out["user_type"] = data["UserType"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("PreferredLanguage") is not None:
        out["preferred_language"] = data["PreferredLanguage"]
    if data.get("Locale") is not None:
        out["locale"] = data["Locale"]
    if data.get("Timezone") is not None:
        out["timezone"] = data["Timezone"]
    if data.get("UserStatus") is not None:
        import capo_identitystore.types.user_status

        out["user_status"] = (
            capo_identitystore.types.user_status.deserialize_aws_json_1_1(
                data["UserStatus"]
            )
        )
    if data.get("Photos") is not None:
        import capo_identitystore.types.photos

        out["photos"] = capo_identitystore.types.photos.deserialize_aws_json_1_1(
            data["Photos"]
        )
    if data.get("Website") is not None:
        out["website"] = data["Website"]
    if data.get("Birthdate") is not None:
        out["birthdate"] = data["Birthdate"]
    if data.get("Roles") is not None:
        import capo_identitystore.types.roles

        out["roles"] = capo_identitystore.types.roles.deserialize_aws_json_1_1(
            data["Roles"]
        )
    if data.get("CreatedAt") is not None:
        import capo_identitystore.types.date_type

        out["created_at"] = capo_identitystore.types.date_type.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("UpdatedAt") is not None:
        import capo_identitystore.types.date_type

        out["updated_at"] = capo_identitystore.types.date_type.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if data.get("UpdatedBy") is not None:
        out["updated_by"] = data["UpdatedBy"]
    if data.get("Extensions") is not None:
        import capo_identitystore.types.extensions

        out["extensions"] = (
            capo_identitystore.types.extensions.deserialize_aws_json_1_1(
                data["Extensions"]
            )
        )
    return out
