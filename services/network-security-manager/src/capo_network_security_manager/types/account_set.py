"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AccountSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_list
    import capo_network_security_manager.types.organizational_unit_list


class AccountSet(TypedDict, closed=True):
    account_ids: NotRequired[
        "capo_network_security_manager.types.account_list.AccountList"
    ]
    """<p>The list of AWS account IDs.</p>"""
    organizational_units: NotRequired[
        "capo_network_security_manager.types.organizational_unit_list.OrganizationalUnitList"
    ]
    """<p>The AWS Organizations organizational units (OUs) in the selection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountSet) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_network_security_manager.types.account_list

        out["accountIds"] = (
            capo_network_security_manager.types.account_list.serialize_json(
                value["account_ids"]
            )
        )
    if "organizational_units" in value:
        import capo_network_security_manager.types.organizational_unit_list

        out["organizationalUnits"] = (
            capo_network_security_manager.types.organizational_unit_list.serialize_json(
                value["organizational_units"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccountSet:
    out: AccountSet = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_network_security_manager.types.account_list

        out["account_ids"] = (
            capo_network_security_manager.types.account_list.deserialize_json(
                data["accountIds"]
            )
        )
    if data.get("organizationalUnits") is not None:
        import capo_network_security_manager.types.organizational_unit_list

        out["organizational_units"] = (
            capo_network_security_manager.types.organizational_unit_list.deserialize_json(
                data["organizationalUnits"]
            )
        )
    return out
