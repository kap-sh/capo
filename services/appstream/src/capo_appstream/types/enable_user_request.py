"""Generated from Smithy shape ``com.amazonaws.appstream#EnableUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.authentication_type
    import capo_appstream.types.username


class EnableUserRequest(TypedDict, closed=True):
    user_name: NotRequired["capo_appstream.types.username.Username"]
    """<p>The email address of the user.</p> <note> <p>Users' email addresses are case-sensitive. During login, if they specify an email address that doesn't use the same capitalization as the email address specified when their user pool account was created, a "user does not exist" error message displays. </p> </note>"""
    authentication_type: NotRequired[
        "capo_appstream.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type for the user. You must specify USERPOOL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableUserRequest) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "authentication_type" in value:
        import capo_appstream.types.authentication_type

        out["AuthenticationType"] = (
            capo_appstream.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableUserRequest:
    out: EnableUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("AuthenticationType") is not None:
        import capo_appstream.types.authentication_type

        out["authentication_type"] = (
            capo_appstream.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    return out
