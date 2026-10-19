"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ListAssetContractsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.asset_contract_list
    import capo_managedblockchain_query.types.next_token


class ListAssetContractsOutput(TypedDict, closed=True):
    contracts: (
        "capo_managedblockchain_query.types.asset_contract_list.AssetContractList"
    )
    """<p>An array of contract objects that contain the properties for each contract.</p>"""
    next_token: NotRequired["capo_managedblockchain_query.types.next_token.NextToken"]
    """<p>The pagination token that indicates the next set of results to retrieve. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetContractsOutput) -> dict:
    out: dict = {}
    import capo_managedblockchain_query.types.asset_contract_list

    out["contracts"] = (
        capo_managedblockchain_query.types.asset_contract_list.serialize_json(
            value["contracts"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetContractsOutput:
    out: ListAssetContractsOutput = {}  # type: ignore[typeddict-item]
    if data.get("contracts") is not None:
        import capo_managedblockchain_query.types.asset_contract_list

        out["contracts"] = (
            capo_managedblockchain_query.types.asset_contract_list.deserialize_json(
                data["contracts"]
            )
        )
    else:
        out["contracts"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
