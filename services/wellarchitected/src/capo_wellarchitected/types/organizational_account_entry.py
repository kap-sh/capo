"""Generated from Smithy shape ``com.amazonaws.wellarchitected#OrganizationalAccountEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.account_id
    import capo_wellarchitected.types.regions


class OrganizationalAccountEntry(TypedDict, closed=True):
    account_id: "capo_wellarchitected.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID to include in the monitoring boundary.</p>"""
    regions: "capo_wellarchitected.types.regions.Regions"
    """<p>The list of regions to monitor for this account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalAccountEntry) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import capo_wellarchitected.types.regions

    out["regions"] = capo_wellarchitected.types.regions.serialize_json(value["regions"])
    return out


def deserialize_json(data: dict) -> OrganizationalAccountEntry:
    out: OrganizationalAccountEntry = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("regions") is not None:
        import capo_wellarchitected.types.regions

        out["regions"] = capo_wellarchitected.types.regions.deserialize_json(
            data["regions"]
        )
    else:
        out["regions"] = []
    return out
