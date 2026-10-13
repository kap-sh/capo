"""Generated from Smithy shape ``com.amazonaws.workdocs#User``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.email_address_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.locale_type
    import capo_workdocs.types.resource_id_type
    import capo_workdocs.types.time_zone_id_type
    import capo_workdocs.types.timestamp_type
    import capo_workdocs.types.user_attribute_value_type
    import capo_workdocs.types.user_status_type
    import capo_workdocs.types.user_storage_metadata
    import capo_workdocs.types.user_type
    import capo_workdocs.types.username_type


class User(TypedDict, closed=True):
    id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the user.</p>"""
    username: NotRequired["capo_workdocs.types.username_type.UsernameType"]
    """<p>The login name of the user.</p>"""
    email_address: NotRequired[
        "capo_workdocs.types.email_address_type.EmailAddressType"
    ]
    """<p>The email address of the user.</p>"""
    given_name: NotRequired[
        "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    ]
    """<p>The given name of the user.</p>"""
    surname: NotRequired[
        "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    ]
    """<p>The surname of the user.</p>"""
    organization_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the organization.</p>"""
    root_folder_id: NotRequired["capo_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The ID of the root folder.</p>"""
    recycle_bin_folder_id: NotRequired[
        "capo_workdocs.types.resource_id_type.ResourceIdType"
    ]
    """<p>The ID of the recycle bin folder.</p>"""
    status: NotRequired["capo_workdocs.types.user_status_type.UserStatusType"]
    """<p>The status of the user.</p>"""
    type: NotRequired["capo_workdocs.types.user_type.UserType"]
    """<p>The type of user.</p>"""
    created_timestamp: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The time when the user was created.</p>"""
    modified_timestamp: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The time when the user was modified.</p>"""
    time_zone_id: NotRequired["capo_workdocs.types.time_zone_id_type.TimeZoneIdType"]
    """<p>The time zone ID of the user.</p>"""
    locale: NotRequired["capo_workdocs.types.locale_type.LocaleType"]
    """<p>The locale of the user.</p>"""
    storage: NotRequired[
        "capo_workdocs.types.user_storage_metadata.UserStorageMetadata"
    ]
    """<p>The storage for the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: User) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "username" in value:
        out["Username"] = value["username"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "surname" in value:
        out["Surname"] = value["surname"]
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    if "root_folder_id" in value:
        out["RootFolderId"] = value["root_folder_id"]
    if "recycle_bin_folder_id" in value:
        out["RecycleBinFolderId"] = value["recycle_bin_folder_id"]
    if "status" in value:
        import capo_workdocs.types.user_status_type

        out["Status"] = capo_workdocs.types.user_status_type.serialize_json(
            value["status"]
        )
    if "type" in value:
        import capo_workdocs.types.user_type

        out["Type"] = capo_workdocs.types.user_type.serialize_json(value["type"])
    if "created_timestamp" in value:
        import capo_workdocs.types.timestamp_type

        out["CreatedTimestamp"] = capo_workdocs.types.timestamp_type.serialize_json(
            value["created_timestamp"]
        )
    if "modified_timestamp" in value:
        import capo_workdocs.types.timestamp_type

        out["ModifiedTimestamp"] = capo_workdocs.types.timestamp_type.serialize_json(
            value["modified_timestamp"]
        )
    if "time_zone_id" in value:
        out["TimeZoneId"] = value["time_zone_id"]
    if "locale" in value:
        import capo_workdocs.types.locale_type

        out["Locale"] = capo_workdocs.types.locale_type.serialize_json(value["locale"])
    if "storage" in value:
        import capo_workdocs.types.user_storage_metadata

        out["Storage"] = capo_workdocs.types.user_storage_metadata.serialize_json(
            value["storage"]
        )
    return out


def deserialize_json(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    if data.get("GivenName") is not None:
        out["given_name"] = data["GivenName"]
    if data.get("Surname") is not None:
        out["surname"] = data["Surname"]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    if data.get("RootFolderId") is not None:
        out["root_folder_id"] = data["RootFolderId"]
    if data.get("RecycleBinFolderId") is not None:
        out["recycle_bin_folder_id"] = data["RecycleBinFolderId"]
    if data.get("Status") is not None:
        import capo_workdocs.types.user_status_type

        out["status"] = capo_workdocs.types.user_status_type.deserialize_json(
            data["Status"]
        )
    if data.get("Type") is not None:
        import capo_workdocs.types.user_type

        out["type"] = capo_workdocs.types.user_type.deserialize_json(data["Type"])
    if data.get("CreatedTimestamp") is not None:
        import capo_workdocs.types.timestamp_type

        out["created_timestamp"] = capo_workdocs.types.timestamp_type.deserialize_json(
            data["CreatedTimestamp"]
        )
    if data.get("ModifiedTimestamp") is not None:
        import capo_workdocs.types.timestamp_type

        out["modified_timestamp"] = capo_workdocs.types.timestamp_type.deserialize_json(
            data["ModifiedTimestamp"]
        )
    if data.get("TimeZoneId") is not None:
        out["time_zone_id"] = data["TimeZoneId"]
    if data.get("Locale") is not None:
        import capo_workdocs.types.locale_type

        out["locale"] = capo_workdocs.types.locale_type.deserialize_json(data["Locale"])
    if data.get("Storage") is not None:
        import capo_workdocs.types.user_storage_metadata

        out["storage"] = capo_workdocs.types.user_storage_metadata.deserialize_json(
            data["Storage"]
        )
    return out


def redact_sensitive(value: User) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    if "given_name" in value:
        out["given_name"] = "*** Sensitive Data Redacted ***"
    if "surname" in value:
        out["surname"] = "*** Sensitive Data Redacted ***"
    return out
