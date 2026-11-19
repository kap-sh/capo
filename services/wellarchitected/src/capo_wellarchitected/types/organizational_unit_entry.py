"""Generated from Smithy shape ``com.amazonaws.wellarchitected#OrganizationalUnitEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.organizational_node_id
    import capo_wellarchitected.types.regions


class OrganizationalUnitEntry(TypedDict, closed=True):
    organizational_unit_id: (
        "capo_wellarchitected.types.organizational_node_id.OrganizationalNodeId"
    )
    """<p>The AWS Organizations organizational unit ID or root ID. Must match the pattern <code>r-[a-z0-9]{4,32}</code> for roots or <code>ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}</code> for OUs.</p>"""
    regions: "capo_wellarchitected.types.regions.Regions"
    """<p>The list of regions to monitor for this organizational unit or root.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalUnitEntry) -> dict:
    out: dict = {}
    out["organizationalUnitId"] = value["organizational_unit_id"]
    import capo_wellarchitected.types.regions

    out["regions"] = capo_wellarchitected.types.regions.serialize_json(value["regions"])
    return out


def deserialize_json(data: dict) -> OrganizationalUnitEntry:
    out: OrganizationalUnitEntry = {}  # type: ignore[typeddict-item]
    if data.get("organizationalUnitId") is not None:
        out["organizational_unit_id"] = data["organizationalUnitId"]
    else:
        out["organizational_unit_id"] = ""
    if data.get("regions") is not None:
        import capo_wellarchitected.types.regions

        out["regions"] = capo_wellarchitected.types.regions.deserialize_json(
            data["regions"]
        )
    else:
        out["regions"] = []
    return out
