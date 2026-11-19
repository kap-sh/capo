"""Generated from Smithy shape ``com.amazonaws.wellarchitected#OrganizationalAggregationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.organizational_account_entry_list
    import capo_wellarchitected.types.organizational_unit_entry_list


class OrganizationalAggregationConfiguration(TypedDict, closed=True):
    organizational_units: NotRequired[
        "capo_wellarchitected.types.organizational_unit_entry_list.OrganizationalUnitEntryList"
    ]
    """<p>A list of organizational unit or root entries that define the organizational scope. Each entry specifies an OU or root ID and the regions to monitor within it.</p>"""
    accounts: NotRequired[
        "capo_wellarchitected.types.organizational_account_entry_list.OrganizationalAccountEntryList"
    ]
    """<p>A list of individual account entries that define additional accounts to include. Each entry specifies an account ID and the regions to monitor within it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalAggregationConfiguration) -> dict:
    out: dict = {}
    if "organizational_units" in value:
        import capo_wellarchitected.types.organizational_unit_entry_list

        out["organizationalUnits"] = (
            capo_wellarchitected.types.organizational_unit_entry_list.serialize_json(
                value["organizational_units"]
            )
        )
    if "accounts" in value:
        import capo_wellarchitected.types.organizational_account_entry_list

        out["accounts"] = (
            capo_wellarchitected.types.organizational_account_entry_list.serialize_json(
                value["accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrganizationalAggregationConfiguration:
    out: OrganizationalAggregationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("organizationalUnits") is not None:
        import capo_wellarchitected.types.organizational_unit_entry_list

        out["organizational_units"] = (
            capo_wellarchitected.types.organizational_unit_entry_list.deserialize_json(
                data["organizationalUnits"]
            )
        )
    if data.get("accounts") is not None:
        import capo_wellarchitected.types.organizational_account_entry_list

        out["accounts"] = (
            capo_wellarchitected.types.organizational_account_entry_list.deserialize_json(
                data["accounts"]
            )
        )
    return out
