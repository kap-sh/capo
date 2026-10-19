"""Generated from Smithy shape ``com.amazonaws.managedblockchain#MemberFabricConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.password_string
    import capo_managedblockchain.types.username_string


class MemberFabricConfiguration(TypedDict, closed=True):
    admin_username: "capo_managedblockchain.types.username_string.UsernameString"
    """<p>The user name for the member's initial administrative user.</p>"""
    admin_password: "capo_managedblockchain.types.password_string.PasswordString"
    r"""<p>The password for the member's initial administrative user. The <code>AdminPassword</code> must be at least 8 characters long and no more than 32 characters. It must contain at least one uppercase letter, one lowercase letter, and one digit. It cannot have a single quotation mark (‘), a double quotation marks (“), a forward slash(/), a backward slash(\), @, or a space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberFabricConfiguration) -> dict:
    out: dict = {}
    out["AdminUsername"] = value["admin_username"]
    out["AdminPassword"] = value["admin_password"]
    return out


def deserialize_json(data: dict) -> MemberFabricConfiguration:
    out: MemberFabricConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AdminUsername") is not None:
        out["admin_username"] = data["AdminUsername"]
    else:
        out["admin_username"] = ""
    if data.get("AdminPassword") is not None:
        out["admin_password"] = data["AdminPassword"]
    else:
        out["admin_password"] = ""
    return out


def redact_sensitive(value: MemberFabricConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "admin_password" in value:
        out["admin_password"] = "*** Sensitive Data Redacted ***"
    return out
