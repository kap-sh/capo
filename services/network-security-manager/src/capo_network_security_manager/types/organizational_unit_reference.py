"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#OrganizationalUnitReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.organizational_unit_id


class OrganizationalUnitReference(TypedDict, closed=True):
    ou_id: "capo_network_security_manager.types.organizational_unit_id.OrganizationalUnitId"
    """<p>The ID of the AWS Organizations organizational unit (OU).</p>"""
    name: NotRequired["str"]
    """<p>The display name of the organizational unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalUnitReference) -> dict:
    out: dict = {}
    out["ouId"] = value["ou_id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> OrganizationalUnitReference:
    out: OrganizationalUnitReference = {}  # type: ignore[typeddict-item]
    if data.get("ouId") is not None:
        out["ou_id"] = data["ouId"]
    else:
        raise DeserializationError("OrganizationalUnitReference.ou_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
