"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#BatchGetTokenBalanceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.batch_get_token_balance_errors
    import capo_managedblockchain_query.types.batch_get_token_balance_output_list


class BatchGetTokenBalanceOutput(TypedDict, closed=True):
    token_balances: "capo_managedblockchain_query.types.batch_get_token_balance_output_list.BatchGetTokenBalanceOutputList"
    """<p>An array of <code>BatchGetTokenBalanceOutputItem</code> objects returned by the response.</p>"""
    errors: "capo_managedblockchain_query.types.batch_get_token_balance_errors.BatchGetTokenBalanceErrors"
    """<p>An array of <code>BatchGetTokenBalanceErrorItem</code> objects returned from the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTokenBalanceOutput) -> dict:
    out: dict = {}
    import capo_managedblockchain_query.types.batch_get_token_balance_output_list

    out["tokenBalances"] = (
        capo_managedblockchain_query.types.batch_get_token_balance_output_list.serialize_json(
            value["token_balances"]
        )
    )
    import capo_managedblockchain_query.types.batch_get_token_balance_errors

    out["errors"] = (
        capo_managedblockchain_query.types.batch_get_token_balance_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetTokenBalanceOutput:
    out: BatchGetTokenBalanceOutput = {}  # type: ignore[typeddict-item]
    if data.get("tokenBalances") is not None:
        import capo_managedblockchain_query.types.batch_get_token_balance_output_list

        out["token_balances"] = (
            capo_managedblockchain_query.types.batch_get_token_balance_output_list.deserialize_json(
                data["tokenBalances"]
            )
        )
    else:
        out["token_balances"] = []
    if data.get("errors") is not None:
        import capo_managedblockchain_query.types.batch_get_token_balance_errors

        out["errors"] = (
            capo_managedblockchain_query.types.batch_get_token_balance_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
