"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MppPaymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.version
    import capo_bedrock_agentcore.types.www_authenticate_header_list


class MppPaymentInput(TypedDict, closed=True):
    version: "capo_bedrock_agentcore.types.version.Version"
    """<p>The MPP protocol version, for example "1" or "2".</p>"""
    www_authenticate_headers: "capo_bedrock_agentcore.types.www_authenticate_header_list.WwwAuthenticateHeaderList"
    """<p>The raw <code>WWW-Authenticate: Payment</code> header value from the 402 response, passed verbatim. Provide exactly one entry. The service uses this value to generate the payment credential.</p>"""
    buyer_pays_gas_fees: NotRequired["bool"]
    """<p>Authorizes the service to sign a payment whose blockchain network (gas) fees are charged to your wallet, on top of the payment amount.</p> <p>The challenge indicates who sponsors the network fees. When the challenge does not sponsor them, the service signs the payment only if this field is <code>true</code>. Otherwise it returns a validation error, so you can decide whether to pay the fees or obtain a challenge that sponsors them.</p> <p>Optional. When omitted or <code>false</code>, you decline to pay network fees. This field has no effect on challenges that already sponsor the fees.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MppPaymentInput) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    import capo_bedrock_agentcore.types.www_authenticate_header_list

    out["wwwAuthenticateHeaders"] = (
        capo_bedrock_agentcore.types.www_authenticate_header_list.serialize_json(
            value["www_authenticate_headers"]
        )
    )
    if "buyer_pays_gas_fees" in value:
        out["buyerPaysGasFees"] = value["buyer_pays_gas_fees"]
    return out


def deserialize_json(data: dict) -> MppPaymentInput:
    out: MppPaymentInput = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("MppPaymentInput.version required")
    if data.get("wwwAuthenticateHeaders") is not None:
        import capo_bedrock_agentcore.types.www_authenticate_header_list

        out["www_authenticate_headers"] = (
            capo_bedrock_agentcore.types.www_authenticate_header_list.deserialize_json(
                data["wwwAuthenticateHeaders"]
            )
        )
    else:
        raise DeserializationError("MppPaymentInput.www_authenticate_headers required")
    if data.get("buyerPaysGasFees") is not None:
        out["buyer_pays_gas_fees"] = data["buyerPaysGasFees"]
    return out
