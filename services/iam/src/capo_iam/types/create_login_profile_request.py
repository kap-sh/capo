"""Generated from Smithy shape ``com.amazonaws.iam#CreateLoginProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_type
    import capo_iam.types.max_signin_session_duration_type
    import capo_iam.types.password_type
    import capo_iam.types.user_name_type


class CreateLoginProfileRequest(TypedDict, closed=True):
    user_name: NotRequired["capo_iam.types.user_name_type.userNameType"]
    """<p>The name of the IAM user to create a password for. The user must already exist.</p> <p>This parameter is optional. If no user name is included, it defaults to the principal making the request. When you make this request with root user credentials, you must use an <a href="https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoot.html">AssumeRoot</a> session to omit the user name.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    password: NotRequired["capo_iam.types.password_type.passwordType"]
    r"""<p>The new password for the user.</p> <p>This parameter must be omitted when you make the request with an <a href="https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoot.html">AssumeRoot</a> session. It is required in all other cases.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> that is used to validate this parameter is a string of characters. That string can include almost any printable ASCII character from the space (<code>\u0020</code>) through the end of the ASCII character range (<code>\u00FF</code>). You can also include the tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>) characters. Any of these characters are valid in a password. However, many tools, such as the Amazon Web Services Management Console, might restrict the ability to type certain characters because they have special meaning within that tool.</p>"""
    password_reset_required: NotRequired["capo_iam.types.boolean_type.booleanType"]
    """<p>Specifies whether the user is required to set a new password on next sign-in.</p>"""
    max_signin_session_duration: NotRequired[
        "capo_iam.types.max_signin_session_duration_type.maxSigninSessionDurationType"
    ]
    """<p>The maximum duration (in seconds) of an Amazon Web Services Sign-In session for this IAM user. This setting can have a value from 1 hour (3600 seconds) to 90 days (7776000 seconds), inclusive. If you do not specify a value, the setting remains unset and the existing sign-in session behavior applies.</p> <note> <p>This setting is not supported for the root user.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateLoginProfileRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_name" in value:
        pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    if "password" in value:
        pairs.append((f"{key_prefix}Password", str(value["password"])))
    if "password_reset_required" in value:
        pairs.append(
            (
                f"{key_prefix}PasswordResetRequired",
                "true" if value["password_reset_required"] else "false",
            )
        )
    if "max_signin_session_duration" in value:
        pairs.append(
            (
                f"{key_prefix}MaxSigninSessionDuration",
                str(value["max_signin_session_duration"]),
            )
        )


def deserialize_query(el: Element) -> CreateLoginProfileRequest:
    out: CreateLoginProfileRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_password = el.find("Password")
    if child_password is not None:
        out["password"] = str(child_password.text or "")
    child_password_reset_required = el.find("PasswordResetRequired")
    if child_password_reset_required is not None:
        out["password_reset_required"] = (
            child_password_reset_required.text or ""
        ).lower() == "true"
    child_max_signin_session_duration = el.find("MaxSigninSessionDuration")
    if child_max_signin_session_duration is not None:
        out["max_signin_session_duration"] = int(
            child_max_signin_session_duration.text or ""
        )
    return out


def redact_sensitive(value: CreateLoginProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
