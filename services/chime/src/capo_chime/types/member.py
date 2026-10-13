"""Generated from Smithy shape ``com.amazonaws.chime#Member``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.member_type
    import capo_chime.types.non_empty_string
    import capo_chime.types.sensitive_string


class Member(TypedDict, closed=True):
    member_id: NotRequired["capo_chime.types.non_empty_string.NonEmptyString"]
    """<p>The member ID (user ID or bot ID).</p>"""
    member_type: NotRequired["capo_chime.types.member_type.MemberType"]
    """<p>The member type.</p>"""
    email: NotRequired["capo_chime.types.sensitive_string.SensitiveString"]
    """<p>The member email address.</p>"""
    full_name: NotRequired["capo_chime.types.sensitive_string.SensitiveString"]
    """<p>The member name.</p>"""
    account_id: NotRequired["capo_chime.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Chime account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Member) -> dict:
    out: dict = {}
    if "member_id" in value:
        out["MemberId"] = value["member_id"]
    if "member_type" in value:
        import capo_chime.types.member_type

        out["MemberType"] = capo_chime.types.member_type.serialize_json(
            value["member_type"]
        )
    if "email" in value:
        out["Email"] = value["email"]
    if "full_name" in value:
        out["FullName"] = value["full_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> Member:
    out: Member = {}  # type: ignore[typeddict-item]
    if data.get("MemberId") is not None:
        out["member_id"] = data["MemberId"]
    if data.get("MemberType") is not None:
        import capo_chime.types.member_type

        out["member_type"] = capo_chime.types.member_type.deserialize_json(
            data["MemberType"]
        )
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    if data.get("FullName") is not None:
        out["full_name"] = data["FullName"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out


def redact_sensitive(value: Member) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    if "full_name" in value:
        out["full_name"] = "*** Sensitive Data Redacted ***"
    return out
