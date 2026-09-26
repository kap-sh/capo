"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AdminScopeSelectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_id_list
    import capo_network_security_manager.types.organizational_unit_id_list


class AdminScopeSelectionInput(TypedDict, closed=True):
    accounts: NotRequired[
        "capo_network_security_manager.types.account_id_list.AccountIdList"
    ]
    """<p>The AWS accounts in the selection.</p>"""
    organizational_units: NotRequired[
        "capo_network_security_manager.types.organizational_unit_id_list.OrganizationalUnitIdList"
    ]
    """<p>The AWS Organizations organizational units (OUs) in the selection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdminScopeSelectionInput) -> dict:
    out: dict = {}
    if "accounts" in value:
        import capo_network_security_manager.types.account_id_list

        out["accounts"] = (
            capo_network_security_manager.types.account_id_list.serialize_json(
                value["accounts"]
            )
        )
    if "organizational_units" in value:
        import capo_network_security_manager.types.organizational_unit_id_list

        out["organizationalUnits"] = (
            capo_network_security_manager.types.organizational_unit_id_list.serialize_json(
                value["organizational_units"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdminScopeSelectionInput:
    out: AdminScopeSelectionInput = {}  # type: ignore[typeddict-item]
    if data.get("accounts") is not None:
        import capo_network_security_manager.types.account_id_list

        out["accounts"] = (
            capo_network_security_manager.types.account_id_list.deserialize_json(
                data["accounts"]
            )
        )
    if data.get("organizationalUnits") is not None:
        import capo_network_security_manager.types.organizational_unit_id_list

        out["organizational_units"] = (
            capo_network_security_manager.types.organizational_unit_id_list.deserialize_json(
                data["organizationalUnits"]
            )
        )
    return out
