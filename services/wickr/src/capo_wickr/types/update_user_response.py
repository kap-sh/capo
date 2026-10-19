"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateUserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id
    import capo_wickr.types.security_group_id_list
    import capo_wickr.types.sensitive_string
    import capo_wickr.types.user_id


class UpdateUserResponse(TypedDict, closed=True):
    user_id: "capo_wickr.types.user_id.UserId"
    """<p>The unique identifier of the updated user.</p>"""
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the network where the user was updated.</p>"""
    security_group_ids: NotRequired[
        "capo_wickr.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The list of security group IDs to which the user now belongs after the update.</p>"""
    first_name: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>The updated first name of the user.</p>"""
    last_name: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>The updated last name of the user.</p>"""
    middle_name: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The middle name of the user (currently not used).</p>"""
    suspended: "bool"
    """<p>Indicates whether the user is suspended after the update.</p>"""
    modified: NotRequired["int"]
    """<p>The timestamp when the user was last modified, specified in epoch seconds.</p>"""
    status: NotRequired["int"]
    """<p>The user's status after the update.</p>"""
    invite_code: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The updated invite code for the user, if applicable.</p>"""
    invite_expiration: NotRequired["int"]
    """<p>The expiration time of the user's invite code, specified in epoch seconds.</p>"""
    code_validation: NotRequired["bool"]
    """<p>Indicates whether the user can be verified through a custom invite code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserResponse) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    out["networkId"] = value["network_id"]
    if "security_group_ids" in value:
        import capo_wickr.types.security_group_id_list

        out["securityGroupIds"] = (
            capo_wickr.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    if "middle_name" in value:
        out["middleName"] = value["middle_name"]
    out["suspended"] = value["suspended"]
    if "modified" in value:
        out["modified"] = value["modified"]
    if "status" in value:
        out["status"] = value["status"]
    if "invite_code" in value:
        out["inviteCode"] = value["invite_code"]
    if "invite_expiration" in value:
        out["inviteExpiration"] = value["invite_expiration"]
    if "code_validation" in value:
        out["codeValidation"] = value["code_validation"]
    return out


def deserialize_json(data: dict) -> UpdateUserResponse:
    out: UpdateUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    if data.get("networkId") is not None:
        out["network_id"] = data["networkId"]
    else:
        out["network_id"] = ""
    if data.get("securityGroupIds") is not None:
        import capo_wickr.types.security_group_id_list

        out["security_group_ids"] = (
            capo_wickr.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if data.get("firstName") is not None:
        out["first_name"] = data["firstName"]
    if data.get("lastName") is not None:
        out["last_name"] = data["lastName"]
    if data.get("middleName") is not None:
        out["middle_name"] = data["middleName"]
    if data.get("suspended") is not None:
        out["suspended"] = data["suspended"]
    else:
        out["suspended"] = False
    if data.get("modified") is not None:
        out["modified"] = data["modified"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("inviteCode") is not None:
        out["invite_code"] = data["inviteCode"]
    if data.get("inviteExpiration") is not None:
        out["invite_expiration"] = data["inviteExpiration"]
    if data.get("codeValidation") is not None:
        out["code_validation"] = data["codeValidation"]
    return out


def redact_sensitive(value: UpdateUserResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    return out
