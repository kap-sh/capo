"""Generated from Smithy shape ``com.amazonaws.appstream#User``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn
    import capo_appstream.types.authentication_type
    import capo_appstream.types.boolean
    import capo_appstream.types.string
    import capo_appstream.types.timestamp
    import capo_appstream.types.user_attribute_value
    import capo_appstream.types.username


class User(TypedDict, closed=True):
    arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the user.</p>"""
    user_name: NotRequired["capo_appstream.types.username.Username"]
    """<p>The email address of the user.</p> <note> <p>Users' email addresses are case-sensitive.</p> </note>"""
    enabled: NotRequired["capo_appstream.types.boolean.Boolean"]
    """<p>Specifies whether the user in the user pool is enabled.</p>"""
    status: NotRequired["capo_appstream.types.string.String"]
    """<p>The status of the user in the user pool. The status can be one of the following:</p> <ul> <li> <p>UNCONFIRMED – The user is created but not confirmed.</p> </li> <li> <p>CONFIRMED – The user is confirmed.</p> </li> <li> <p>ARCHIVED – The user is no longer active.</p> </li> <li> <p>COMPROMISED – The user is disabled because of a potential security threat.</p> </li> <li> <p>UNKNOWN – The user status is not known.</p> </li> </ul>"""
    first_name: NotRequired[
        "capo_appstream.types.user_attribute_value.UserAttributeValue"
    ]
    """<p>The first name, or given name, of the user.</p>"""
    last_name: NotRequired[
        "capo_appstream.types.user_attribute_value.UserAttributeValue"
    ]
    """<p>The last name, or surname, of the user.</p>"""
    created_time: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The date and time the user was created in the user pool.</p>"""
    authentication_type: NotRequired[
        "capo_appstream.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type for the user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: User) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "status" in value:
        out["Status"] = value["status"]
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "created_time" in value:
        import capo_appstream.types.timestamp

        out["CreatedTime"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "authentication_type" in value:
        import capo_appstream.types.authentication_type

        out["AuthenticationType"] = (
            capo_appstream.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    if data.get("CreatedTime") is not None:
        import capo_appstream.types.timestamp

        out["created_time"] = capo_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    if data.get("AuthenticationType") is not None:
        import capo_appstream.types.authentication_type

        out["authentication_type"] = (
            capo_appstream.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    return out


def redact_sensitive(value: User) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_name" in value:
        out["user_name"] = "*** Sensitive Data Redacted ***"
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    return out
