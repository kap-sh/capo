"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateUserDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.security_group_id_list
    import capo_wickr.types.sensitive_string


class UpdateUserDetails(TypedDict, closed=True):
    first_name: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>The new first name for the user.</p>"""
    last_name: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>The new last name for the user.</p>"""
    username: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The new username or email address for the user.</p>"""
    security_group_ids: NotRequired[
        "capo_wickr.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The updated list of security group IDs to which the user should belong.</p>"""
    invite_code: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A new custom invite code for the user.</p>"""
    invite_code_ttl: NotRequired["int"]
    """<p>The new time-to-live for the invite code in days.</p>"""
    code_validation: NotRequired["bool"]
    """<p>Indicates whether the user can be verified through a custom invite code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserDetails) -> dict:
    out: dict = {}
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    if "username" in value:
        out["username"] = value["username"]
    if "security_group_ids" in value:
        import capo_wickr.types.security_group_id_list

        out["securityGroupIds"] = (
            capo_wickr.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "invite_code" in value:
        out["inviteCode"] = value["invite_code"]
    if "invite_code_ttl" in value:
        out["inviteCodeTtl"] = value["invite_code_ttl"]
    if "code_validation" in value:
        out["codeValidation"] = value["code_validation"]
    return out


def deserialize_json(data: dict) -> UpdateUserDetails:
    out: UpdateUserDetails = {}  # type: ignore[typeddict-item]
    if data.get("firstName") is not None:
        out["first_name"] = data["firstName"]
    if data.get("lastName") is not None:
        out["last_name"] = data["lastName"]
    if data.get("username") is not None:
        out["username"] = data["username"]
    if data.get("securityGroupIds") is not None:
        import capo_wickr.types.security_group_id_list

        out["security_group_ids"] = (
            capo_wickr.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if data.get("inviteCode") is not None:
        out["invite_code"] = data["inviteCode"]
    if data.get("inviteCodeTtl") is not None:
        out["invite_code_ttl"] = data["inviteCodeTtl"]
    if data.get("codeValidation") is not None:
        out["code_validation"] = data["codeValidation"]
    return out


def redact_sensitive(value: UpdateUserDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    return out
