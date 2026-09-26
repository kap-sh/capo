"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AdminScopeSelection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_reference_list
    import capo_network_security_manager.types.organizational_unit_reference_list


class AdminScopeSelection(TypedDict, closed=True):
    accounts: NotRequired[
        "capo_network_security_manager.types.account_reference_list.AccountReferenceList"
    ]
    """<p>The AWS accounts in the selection.</p>"""
    organizational_units: NotRequired[
        "capo_network_security_manager.types.organizational_unit_reference_list.OrganizationalUnitReferenceList"
    ]
    """<p>The AWS Organizations organizational units (OUs) in the selection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdminScopeSelection) -> dict:
    out: dict = {}
    if "accounts" in value:
        import capo_network_security_manager.types.account_reference_list

        out["accounts"] = (
            capo_network_security_manager.types.account_reference_list.serialize_json(
                value["accounts"]
            )
        )
    if "organizational_units" in value:
        import capo_network_security_manager.types.organizational_unit_reference_list

        out["organizationalUnits"] = (
            capo_network_security_manager.types.organizational_unit_reference_list.serialize_json(
                value["organizational_units"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdminScopeSelection:
    out: AdminScopeSelection = {}  # type: ignore[typeddict-item]
    if data.get("accounts") is not None:
        import capo_network_security_manager.types.account_reference_list

        out["accounts"] = (
            capo_network_security_manager.types.account_reference_list.deserialize_json(
                data["accounts"]
            )
        )
    if data.get("organizationalUnits") is not None:
        import capo_network_security_manager.types.organizational_unit_reference_list

        out["organizational_units"] = (
            capo_network_security_manager.types.organizational_unit_reference_list.deserialize_json(
                data["organizationalUnits"]
            )
        )
    return out
