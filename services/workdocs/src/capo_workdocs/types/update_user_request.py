"""Generated from Smithy shape ``com.amazonaws.workdocs#UpdateUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.boolean_enum_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.locale_type
    import capo_workdocs.types.storage_rule_type
    import capo_workdocs.types.time_zone_id_type
    import capo_workdocs.types.user_attribute_value_type
    import capo_workdocs.types.user_type


class UpdateUserRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    user_id: "capo_workdocs.types.id_type.IdType"
    """<p>The ID of the user.</p>"""
    given_name: NotRequired[
        "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    ]
    """<p>The given name of the user.</p>"""
    surname: NotRequired[
        "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    ]
    """<p>The surname of the user.</p>"""
    type: NotRequired["capo_workdocs.types.user_type.UserType"]
    """<p>The type of the user.</p>"""
    storage_rule: NotRequired["capo_workdocs.types.storage_rule_type.StorageRuleType"]
    """<p>The amount of storage for the user.</p>"""
    time_zone_id: NotRequired["capo_workdocs.types.time_zone_id_type.TimeZoneIdType"]
    """<p>The time zone ID of the user.</p>"""
    locale: NotRequired["capo_workdocs.types.locale_type.LocaleType"]
    """<p>The locale of the user.</p>"""
    grant_poweruser_privileges: NotRequired[
        "capo_workdocs.types.boolean_enum_type.BooleanEnumType"
    ]
    """<p>Boolean value to determine whether the user is granted Power user privileges.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRequest) -> dict:
    out: dict = {}
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "surname" in value:
        out["Surname"] = value["surname"]
    if "type" in value:
        import capo_workdocs.types.user_type

        out["Type"] = capo_workdocs.types.user_type.serialize_json(value["type"])
    if "storage_rule" in value:
        import capo_workdocs.types.storage_rule_type

        out["StorageRule"] = capo_workdocs.types.storage_rule_type.serialize_json(
            value["storage_rule"]
        )
    if "time_zone_id" in value:
        out["TimeZoneId"] = value["time_zone_id"]
    if "locale" in value:
        import capo_workdocs.types.locale_type

        out["Locale"] = capo_workdocs.types.locale_type.serialize_json(value["locale"])
    if "grant_poweruser_privileges" in value:
        import capo_workdocs.types.boolean_enum_type

        out["GrantPoweruserPrivileges"] = (
            capo_workdocs.types.boolean_enum_type.serialize_json(
                value["grant_poweruser_privileges"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("GivenName") is not None:
        out["given_name"] = data["GivenName"]
    if data.get("Surname") is not None:
        out["surname"] = data["Surname"]
    if data.get("Type") is not None:
        import capo_workdocs.types.user_type

        out["type"] = capo_workdocs.types.user_type.deserialize_json(data["Type"])
    if data.get("StorageRule") is not None:
        import capo_workdocs.types.storage_rule_type

        out["storage_rule"] = capo_workdocs.types.storage_rule_type.deserialize_json(
            data["StorageRule"]
        )
    if data.get("TimeZoneId") is not None:
        out["time_zone_id"] = data["TimeZoneId"]
    if data.get("Locale") is not None:
        import capo_workdocs.types.locale_type

        out["locale"] = capo_workdocs.types.locale_type.deserialize_json(data["Locale"])
    if data.get("GrantPoweruserPrivileges") is not None:
        import capo_workdocs.types.boolean_enum_type

        out["grant_poweruser_privileges"] = (
            capo_workdocs.types.boolean_enum_type.deserialize_json(
                data["GrantPoweruserPrivileges"]
            )
        )
    return out


def redact_sensitive(value: UpdateUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    if "given_name" in value:
        out["given_name"] = "*** Sensitive Data Redacted ***"
    if "surname" in value:
        out["surname"] = "*** Sensitive Data Redacted ***"
    return out
