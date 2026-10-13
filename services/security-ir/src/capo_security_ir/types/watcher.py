"""Generated from Smithy shape ``com.amazonaws.securityir#Watcher``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import capo_security_ir.types.email_address
    import capo_security_ir.types.job_title
    import capo_security_ir.types.person_name


class Watcher(TypedDict, closed=True):
    email: "capo_security_ir.types.email_address.EmailAddress"
    """<p/>"""
    name: NotRequired["capo_security_ir.types.person_name.PersonName"]
    """<p/>"""
    job_title: NotRequired["capo_security_ir.types.job_title.JobTitle"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: Watcher) -> dict:
    out: dict = {}
    out["email"] = value["email"]
    if "name" in value:
        out["name"] = value["name"]
    if "job_title" in value:
        out["jobTitle"] = value["job_title"]
    return out


def deserialize_json(data: dict) -> Watcher:
    out: Watcher = {}  # type: ignore[typeddict-item]
    if data.get("email") is not None:
        out["email"] = data["email"]
    else:
        raise DeserializationError("Watcher.email required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("jobTitle") is not None:
        out["job_title"] = data["jobTitle"]
    return out


def redact_sensitive(value: Watcher) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "job_title" in value:
        out["job_title"] = "*** Sensitive Data Redacted ***"
    return out
