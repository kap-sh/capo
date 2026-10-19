"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetPaymentInstrumentBalanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.blockchain_chain_id
    import capo_bedrock_agentcore.types.instrument_balance_token
    import capo_bedrock_agentcore.types.payment_agent_name
    import capo_bedrock_agentcore.types.payment_connector_id
    import capo_bedrock_agentcore.types.payment_instrument_id
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.user_id


class GetPaymentInstrumentBalanceRequest(TypedDict, closed=True):
    user_id: NotRequired["capo_bedrock_agentcore.types.user_id.UserId"]
    """<p>The user ID associated with this payment instrument.</p>"""
    agent_name: NotRequired[
        "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
    ]
    """<p>The agent name associated with this request, used for observability.</p>"""
    payment_manager_arn: (
        "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager that owns this payment instrument.</p>"""
    payment_connector_id: (
        "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The ID of the payment connector associated with this instrument.</p>"""
    payment_instrument_id: (
        "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId"
    )
    """<p>The ID of the payment instrument to query balance for.</p>"""
    chain: "capo_bedrock_agentcore.types.blockchain_chain_id.BlockchainChainId"
    """<p>The specific blockchain chain to query balance on. Required because balances are chain-specific.</p>"""
    token: (
        "capo_bedrock_agentcore.types.instrument_balance_token.InstrumentBalanceToken"
    )
    """<p>The token to query balance for. Only tokens supported for X402 payments are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentInstrumentBalanceRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentConnectorId"] = value["payment_connector_id"]
    out["paymentInstrumentId"] = value["payment_instrument_id"]
    import capo_bedrock_agentcore.types.blockchain_chain_id

    out["chain"] = capo_bedrock_agentcore.types.blockchain_chain_id.serialize_json(
        value["chain"]
    )
    import capo_bedrock_agentcore.types.instrument_balance_token

    out["token"] = capo_bedrock_agentcore.types.instrument_balance_token.serialize_json(
        value["token"]
    )
    return out


def deserialize_json(data: dict) -> GetPaymentInstrumentBalanceRequest:
    out: GetPaymentInstrumentBalanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("paymentManagerArn") is not None:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        out["payment_manager_arn"] = ""
    if data.get("paymentConnectorId") is not None:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        out["payment_connector_id"] = ""
    if data.get("paymentInstrumentId") is not None:
        out["payment_instrument_id"] = data["paymentInstrumentId"]
    else:
        out["payment_instrument_id"] = ""
    if data.get("chain") is not None:
        import capo_bedrock_agentcore.types.blockchain_chain_id

        out["chain"] = (
            capo_bedrock_agentcore.types.blockchain_chain_id.deserialize_json(
                data["chain"]
            )
        )
    else:
        import typing

        out["chain"] = typing.cast(
            "capo_bedrock_agentcore.types.blockchain_chain_id.BlockchainChainId", ""
        )
    if data.get("token") is not None:
        import capo_bedrock_agentcore.types.instrument_balance_token

        out["token"] = (
            capo_bedrock_agentcore.types.instrument_balance_token.deserialize_json(
                data["token"]
            )
        )
    else:
        import typing

        out["token"] = typing.cast(
            "capo_bedrock_agentcore.types.instrument_balance_token.InstrumentBalanceToken",
            "",
        )
    return out
