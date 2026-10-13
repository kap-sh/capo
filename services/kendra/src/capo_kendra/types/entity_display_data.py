"""Generated from Smithy shape ``com.amazonaws.kendra#EntityDisplayData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.name_type


class EntityDisplayData(TypedDict, closed=True):
    user_name: NotRequired["capo_kendra.types.name_type.NameType"]
    """<p>The name of the user.</p>"""
    group_name: NotRequired["capo_kendra.types.name_type.NameType"]
    """<p>The name of the group.</p>"""
    identified_user_name: NotRequired["capo_kendra.types.name_type.NameType"]
    """<p>The user name of the user.</p>"""
    first_name: NotRequired["capo_kendra.types.name_type.NameType"]
    """<p>The first name of the user.</p>"""
    last_name: NotRequired["capo_kendra.types.name_type.NameType"]
    """<p>The last name of the user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityDisplayData) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "identified_user_name" in value:
        out["IdentifiedUserName"] = value["identified_user_name"]
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityDisplayData:
    out: EntityDisplayData = {}  # type: ignore[typeddict-item]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    if data.get("IdentifiedUserName") is not None:
        out["identified_user_name"] = data["IdentifiedUserName"]
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    return out


def redact_sensitive(value: EntityDisplayData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_name" in value:
        out["user_name"] = "*** Sensitive Data Redacted ***"
    if "group_name" in value:
        out["group_name"] = "*** Sensitive Data Redacted ***"
    if "identified_user_name" in value:
        out["identified_user_name"] = "*** Sensitive Data Redacted ***"
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    return out
