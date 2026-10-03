"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CoinbaseCdpTokenRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.coinbase_cdp_payment_request_body_type
    import capo_bedrock_agentcore.types.payment_http_method_type
    import capo_bedrock_agentcore.types.payment_request_host_type
    import capo_bedrock_agentcore.types.payment_request_path_type


class CoinbaseCdpTokenRequestInput(TypedDict, closed=True):
    request_method: (
        "capo_bedrock_agentcore.types.payment_http_method_type.PaymentHttpMethodType"
    )
    """<p>The HTTP method for the payment API request.</p>"""
    request_host: NotRequired[
        "capo_bedrock_agentcore.types.payment_request_host_type.PaymentRequestHostType"
    ]
    """<p>The host for the payment API request. Defaults to "api.cdp.coinbase.com".</p>"""
    request_path: (
        "capo_bedrock_agentcore.types.payment_request_path_type.PaymentRequestPathType"
    )
    """<p>The path of the payment API request.</p>"""
    include_wallet_auth_token: "bool"
    """<p>Set to true for wallet write operations (requires walletSecret configured).</p>"""
    request_body: NotRequired[
        "capo_bedrock_agentcore.types.coinbase_cdp_payment_request_body_type.CoinbaseCdpPaymentRequestBodyType"
    ]
    """<p>Request body JSON — used to generate wallet auth JWT.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoinbaseCdpTokenRequestInput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.payment_http_method_type

    out["requestMethod"] = (
        capo_bedrock_agentcore.types.payment_http_method_type.serialize_json(
            value["request_method"]
        )
    )
    if "request_host" in value:
        out["requestHost"] = value["request_host"]
    out["requestPath"] = value["request_path"]
    out["includeWalletAuthToken"] = value.get("include_wallet_auth_token", False)
    if "request_body" in value:
        out["requestBody"] = value["request_body"]
    return out


def deserialize_json(data: dict) -> CoinbaseCdpTokenRequestInput:
    out: CoinbaseCdpTokenRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("requestMethod") is not None:
        import capo_bedrock_agentcore.types.payment_http_method_type

        out["request_method"] = (
            capo_bedrock_agentcore.types.payment_http_method_type.deserialize_json(
                data["requestMethod"]
            )
        )
    else:
        raise DeserializationError(
            "CoinbaseCdpTokenRequestInput.request_method required"
        )
    if data.get("requestHost") is not None:
        out["request_host"] = data["requestHost"]
    if data.get("requestPath") is not None:
        out["request_path"] = data["requestPath"]
    else:
        raise DeserializationError("CoinbaseCdpTokenRequestInput.request_path required")
    if data.get("includeWalletAuthToken") is not None:
        out["include_wallet_auth_token"] = data["includeWalletAuthToken"]
    else:
        out["include_wallet_auth_token"] = False
    if data.get("requestBody") is not None:
        out["request_body"] = data["requestBody"]
    return out
