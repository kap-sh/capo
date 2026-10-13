"""Generated from Smithy shape ``com.amazonaws.wickr#BatchCreateUserRequestItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.security_group_id_list
    import capo_wickr.types.sensitive_string


class BatchCreateUserRequestItem(TypedDict, closed=True):
    first_name: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>The first name of the user.</p>"""
    last_name: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>The last name of the user.</p>"""
    security_group_ids: "capo_wickr.types.security_group_id_list.SecurityGroupIdList"
    """<p>A list of security group IDs to which the user should be assigned.</p>"""
    username: "capo_wickr.types.generic_string.GenericString"
    """<p>The email address or username for the user. Must be unique within the network.</p>"""
    invite_code: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A custom invite code for the user. If not provided, one will be generated automatically.</p>"""
    invite_code_ttl: NotRequired["int"]
    """<p>The time-to-live for the invite code in days. After this period, the invite code will expire.</p>"""
    code_validation: NotRequired["bool"]
    """<p>Indicates whether the user can be verified through a custom invite code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateUserRequestItem) -> dict:
    out: dict = {}
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    import capo_wickr.types.security_group_id_list

    out["securityGroupIds"] = capo_wickr.types.security_group_id_list.serialize_json(
        value["security_group_ids"]
    )
    out["username"] = value["username"]
    if "invite_code" in value:
        out["inviteCode"] = value["invite_code"]
    if "invite_code_ttl" in value:
        out["inviteCodeTtl"] = value["invite_code_ttl"]
    if "code_validation" in value:
        out["codeValidation"] = value["code_validation"]
    return out


def deserialize_json(data: dict) -> BatchCreateUserRequestItem:
    out: BatchCreateUserRequestItem = {}  # type: ignore[typeddict-item]
    if data.get("firstName") is not None:
        out["first_name"] = data["firstName"]
    if data.get("lastName") is not None:
        out["last_name"] = data["lastName"]
    if data.get("securityGroupIds") is not None:
        import capo_wickr.types.security_group_id_list

        out["security_group_ids"] = (
            capo_wickr.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateUserRequestItem.security_group_ids required"
        )
    if data.get("username") is not None:
        out["username"] = data["username"]
    else:
        raise DeserializationError("BatchCreateUserRequestItem.username required")
    if data.get("inviteCode") is not None:
        out["invite_code"] = data["inviteCode"]
    if data.get("inviteCodeTtl") is not None:
        out["invite_code_ttl"] = data["inviteCodeTtl"]
    if data.get("codeValidation") is not None:
        out["code_validation"] = data["codeValidation"]
    return out


def redact_sensitive(value: BatchCreateUserRequestItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    return out
