"""Generated from Smithy shape ``com.amazonaws.iam#UpdateLoginProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.boolean_object_type
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


def deserialize_query(el: Element) -> UpdateLoginProfileRequest:
    out: UpdateLoginProfileRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("UpdateLoginProfileRequest.user_name required")
    child_password = el.find("Password")
    if child_password is not None:
        out["password"] = str(child_password.text or "")
    child_password_reset_required = el.find("PasswordResetRequired")
    if child_password_reset_required is not None:
        out["password_reset_required"] = (
            child_password_reset_required.text or ""
        ).lower() == "true"
    return out
