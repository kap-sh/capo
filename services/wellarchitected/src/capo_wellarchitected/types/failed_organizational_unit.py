"""Generated from Smithy shape ``com.amazonaws.wellarchitected#FailedOrganizationalUnit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.organizational_unit_id


class FailedOrganizationalUnit(TypedDict, closed=True):
    organizational_unit_id: (
        "capo_wellarchitected.types.organizational_unit_id.OrganizationalUnitId"
    )
    """<p>The AWS Organizations OU ID that could not be expanded.</p>"""
    reason: "str"
    """<p>A human-readable explanation of why the organizational unit could not be expanded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedOrganizationalUnit) -> dict:
    out: dict = {}
    out["organizationalUnitId"] = value["organizational_unit_id"]
    out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> FailedOrganizationalUnit:
    out: FailedOrganizationalUnit = {}  # type: ignore[typeddict-item]
    if data.get("organizationalUnitId") is not None:
        out["organizational_unit_id"] = data["organizationalUnitId"]
    else:
        out["organizational_unit_id"] = ""
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        out["reason"] = ""
    return out
