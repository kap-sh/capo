"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#GetAssetContractOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.chain_address
    import capo_managedblockchain_query.types.contract_identifier
    import capo_managedblockchain_query.types.contract_metadata
    import capo_managedblockchain_query.types.query_token_standard


class GetAssetContractOutput(TypedDict, closed=True):
    contract_identifier: (
        "capo_managedblockchain_query.types.contract_identifier.ContractIdentifier"
    )
    """<p>Contains the blockchain address and network information about the contract.</p>"""
    token_standard: (
        "capo_managedblockchain_query.types.query_token_standard.QueryTokenStandard"
    )
    """<p>The token standard of the contract requested.</p>"""
    deployer_address: "capo_managedblockchain_query.types.chain_address.ChainAddress"
    """<p>The address of the deployer of contract.</p>"""
    metadata: NotRequired[
        "capo_managedblockchain_query.types.contract_metadata.ContractMetadata"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetContractOutput) -> dict:
    out: dict = {}
    import capo_managedblockchain_query.types.contract_identifier

    out["contractIdentifier"] = (
        capo_managedblockchain_query.types.contract_identifier.serialize_json(
            value["contract_identifier"]
        )
    )
    out["tokenStandard"] = value["token_standard"]
    out["deployerAddress"] = value["deployer_address"]
    if "metadata" in value:
        import capo_managedblockchain_query.types.contract_metadata

        out["metadata"] = (
            capo_managedblockchain_query.types.contract_metadata.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAssetContractOutput:
    out: GetAssetContractOutput = {}  # type: ignore[typeddict-item]
    if data.get("contractIdentifier") is not None:
        import capo_managedblockchain_query.types.contract_identifier

        out["contract_identifier"] = (
            capo_managedblockchain_query.types.contract_identifier.deserialize_json(
                data["contractIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "GetAssetContractOutput.contract_identifier required"
        )
    if data.get("tokenStandard") is not None:
        out["token_standard"] = data["tokenStandard"]
    else:
        out["token_standard"] = ""
    if data.get("deployerAddress") is not None:
        out["deployer_address"] = data["deployerAddress"]
    else:
        out["deployer_address"] = ""
    if data.get("metadata") is not None:
        import capo_managedblockchain_query.types.contract_metadata

        out["metadata"] = (
            capo_managedblockchain_query.types.contract_metadata.deserialize_json(
                data["metadata"]
            )
        )
    return out
