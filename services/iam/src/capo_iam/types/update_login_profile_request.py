"""Generated from Smithy shape ``com.amazonaws.iam#UpdateLoginProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_object_type
    import capo_iam.types.max_signin_session_duration_type
    import capo_iam.types.password_type
    import capo_iam.types.user_name_type


class UpdateLoginProfileRequest(TypedDict, closed=True):
    user_name: "capo_iam.types.user_name_type.userNameType"
    """<p>The name of the user whose password you want to update.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    password: NotRequired["capo_iam.types.password_type.passwordType"]
    r"""<p>The new password for the specified IAM user.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</p> </li> </ul> <p>However, the format can be further restricted by the account administrator by setting a password policy on the Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAccountPasswordPolicy.html">UpdateAccountPasswordPolicy</a>.</p>"""
    password_reset_required: NotRequired[
        "capo_iam.types.boolean_object_type.booleanObjectType"
    ]
    """<p>Allows this new password to be used only once by requiring the specified IAM user to set a new password on next sign-in.</p>"""
    max_signin_session_duration: NotRequired[
        "capo_iam.types.max_signin_session_duration_type.maxSigninSessionDurationType"
    ]
    """<p>The maximum duration (in seconds) of an Amazon Web Services Sign-In session for the specified IAM user. This setting can have a value from 1 hour (3600 seconds) to 90 days (7776000 seconds), inclusive, and replaces any value currently configured for the user.</p> <p>If you omit both this parameter and <code>ResetMaxSigninSessionDuration</code>, the current setting is unchanged. You cannot specify this parameter and set <code>ResetMaxSigninSessionDuration</code> to <code>true</code> in the same request. If you update only the sign-in session duration, the user's password and <code>PasswordResetRequired</code> setting do not change.</p> <p>Changes to this setting apply to new sign-in sessions. Sessions that are already established are not affected.</p> <note> <p>This setting is not supported for the root user.</p> </note>"""
    reset_max_signin_session_duration: NotRequired[
        "capo_iam.types.boolean_object_type.booleanObjectType"
    ]
    """<p>Specifies whether to clear the maximum sign-in session duration for the specified IAM user. Set this value to <code>true</code> to return the setting to its unset state, so that the existing sign-in session behavior applies. When the setting is unset, the user's <code>MaxSigninSessionDuration</code> is omitted from responses.</p> <p>If you set this value to <code>false</code> or omit it, the current setting is not cleared. You cannot set this value to <code>true</code> and specify <code>MaxSigninSessionDuration</code> in the same request. Clearing a setting that is already unset has no effect.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateLoginProfileRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
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
    if "reset_max_signin_session_duration" in value:
        pairs.append(
            (
                f"{key_prefix}ResetMaxSigninSessionDuration",
                "true" if value["reset_max_signin_session_duration"] else "false",
            )
        )


def deserialize_query(el: Element) -> UpdateLoginProfileRequest:
    out: UpdateLoginProfileRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        out["user_name"] = ""
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
    child_reset_max_signin_session_duration = el.find("ResetMaxSigninSessionDuration")
    if child_reset_max_signin_session_duration is not None:
        out["reset_max_signin_session_duration"] = (
            child_reset_max_signin_session_duration.text or ""
        ).lower() == "true"
    return out


def redact_sensitive(value: UpdateLoginProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
