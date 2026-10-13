"""Generated from Smithy shape ``com.amazonaws.finspace#SuperuserParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import capo_finspace.types.email_id
    import capo_finspace.types.name_string


class SuperuserParameters(TypedDict, closed=True):
    email_address: "capo_finspace.types.email_id.EmailId"
    """<p>The email address of the superuser.</p>"""
    first_name: "capo_finspace.types.name_string.NameString"
    """<p>The first name of the superuser.</p>"""
    last_name: "capo_finspace.types.name_string.NameString"
    """<p>The last name of the superuser.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuperuserParameters) -> dict:
    out: dict = {}
    out["emailAddress"] = value["email_address"]
    out["firstName"] = value["first_name"]
    out["lastName"] = value["last_name"]
    return out


def deserialize_json(data: dict) -> SuperuserParameters:
    out: SuperuserParameters = {}  # type: ignore[typeddict-item]
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    else:
        raise DeserializationError("SuperuserParameters.email_address required")
    if data.get("firstName") is not None:
        out["first_name"] = data["firstName"]
    else:
        raise DeserializationError("SuperuserParameters.first_name required")
    if data.get("lastName") is not None:
        out["last_name"] = data["lastName"]
    else:
        raise DeserializationError("SuperuserParameters.last_name required")
    return out


def redact_sensitive(value: SuperuserParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    return out
