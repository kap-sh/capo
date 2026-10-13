"""Generated from Smithy shape ``com.amazonaws.securityir#IncidentResponder``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import capo_security_ir.types.communication_preferences
    import capo_security_ir.types.email_address
    import capo_security_ir.types.incident_responder_name
    import capo_security_ir.types.job_title


class IncidentResponder(TypedDict, closed=True):
    name: "capo_security_ir.types.incident_responder_name.IncidentResponderName"
    """<p/>"""
    job_title: "capo_security_ir.types.job_title.JobTitle"
    """<p/>"""
    email: "capo_security_ir.types.email_address.EmailAddress"
    """<p/>"""
    communication_preferences: NotRequired[
        "capo_security_ir.types.communication_preferences.CommunicationPreferences"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncidentResponder) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["jobTitle"] = value["job_title"]
    out["email"] = value["email"]
    if "communication_preferences" in value:
        import capo_security_ir.types.communication_preferences

        out["communicationPreferences"] = (
            capo_security_ir.types.communication_preferences.serialize_json(
                value["communication_preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> IncidentResponder:
    out: IncidentResponder = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("IncidentResponder.name required")
    if data.get("jobTitle") is not None:
        out["job_title"] = data["jobTitle"]
    else:
        raise DeserializationError("IncidentResponder.job_title required")
    if data.get("email") is not None:
        out["email"] = data["email"]
    else:
        raise DeserializationError("IncidentResponder.email required")
    if data.get("communicationPreferences") is not None:
        import capo_security_ir.types.communication_preferences

        out["communication_preferences"] = (
            capo_security_ir.types.communication_preferences.deserialize_json(
                data["communicationPreferences"]
            )
        )
    return out


def redact_sensitive(value: IncidentResponder) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "job_title" in value:
        out["job_title"] = "*** Sensitive Data Redacted ***"
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    return out
