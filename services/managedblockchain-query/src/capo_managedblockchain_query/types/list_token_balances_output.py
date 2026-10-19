"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ListTokenBalancesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.next_token
    import capo_managedblockchain_query.types.token_balance_list


class ListTokenBalancesOutput(TypedDict, closed=True):
    token_balances: (
        "capo_managedblockchain_query.types.token_balance_list.TokenBalanceList"
    )
    """<p>An array of <code>TokenBalance</code> objects. Each object contains details about the token balance.</p>"""
    next_token: NotRequired["capo_managedblockchain_query.types.next_token.NextToken"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTokenBalancesOutput) -> dict:
    out: dict = {}
    import capo_managedblockchain_query.types.token_balance_list

    out["tokenBalances"] = (
        capo_managedblockchain_query.types.token_balance_list.serialize_json(
            value["token_balances"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTokenBalancesOutput:
    out: ListTokenBalancesOutput = {}  # type: ignore[typeddict-item]
    if data.get("tokenBalances") is not None:
        import capo_managedblockchain_query.types.token_balance_list

        out["token_balances"] = (
            capo_managedblockchain_query.types.token_balance_list.deserialize_json(
                data["tokenBalances"]
            )
        )
    else:
        out["token_balances"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
