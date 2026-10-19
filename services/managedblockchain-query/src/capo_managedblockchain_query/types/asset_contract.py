"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#AssetContract``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.chain_address
    import capo_managedblockchain_query.types.contract_identifier
    import capo_managedblockchain_query.types.query_token_standard


class AssetContract(TypedDict, closed=True):
    contract_identifier: (
        "capo_managedblockchain_query.types.contract_identifier.ContractIdentifier"
    )
    """<p>The container for the contract identifier containing its blockchain network and address.</p>"""
    token_standard: (
        "capo_managedblockchain_query.types.query_token_standard.QueryTokenStandard"
    )
    """<p>The token standard of the contract.</p>"""
    deployer_address: "capo_managedblockchain_query.types.chain_address.ChainAddress"
    """<p>The address of the contract deployer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetContract) -> dict:
    out: dict = {}
    import capo_managedblockchain_query.types.contract_identifier

    out["contractIdentifier"] = (
        capo_managedblockchain_query.types.contract_identifier.serialize_json(
            value["contract_identifier"]
        )
    )
    out["tokenStandard"] = value["token_standard"]
    out["deployerAddress"] = value["deployer_address"]
    return out


def deserialize_json(data: dict) -> AssetContract:
    out: AssetContract = {}  # type: ignore[typeddict-item]
    if data.get("contractIdentifier") is not None:
        import capo_managedblockchain_query.types.contract_identifier

        out["contract_identifier"] = (
            capo_managedblockchain_query.types.contract_identifier.deserialize_json(
                data["contractIdentifier"]
            )
        )
    else:
        raise DeserializationError("AssetContract.contract_identifier required")
    if data.get("tokenStandard") is not None:
        out["token_standard"] = data["tokenStandard"]
    else:
        out["token_standard"] = ""
    if data.get("deployerAddress") is not None:
        out["deployer_address"] = data["deployerAddress"]
    else:
        out["deployer_address"] = ""
    return out
