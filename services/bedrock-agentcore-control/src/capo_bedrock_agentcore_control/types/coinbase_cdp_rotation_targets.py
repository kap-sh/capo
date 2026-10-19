"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CoinbaseCdpRotationTargets``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.coinbase_cdp_secrets


class CoinbaseCdpRotationTargets(TypedDict, closed=True):
    secrets: (
        "capo_bedrock_agentcore_control.types.coinbase_cdp_secrets.CoinbaseCdpSecrets"
    )
    """<p>The secrets to rotate. Specify at least one value. Each secret that you specify is rotated independently.</p> <ul> <li> <p> <code>API_KEY</code> - The API key that the payment connector uses to call Coinbase CDP. Rotate it as routine maintenance, or if you suspect that it is compromised.</p> </li> <li> <p> <code>WALLET_SECRET</code> - The wallet secret that signs transactions. Rotate it only if it is lost or compromised. Coinbase CDP allows one wallet secret per project, so it is replaced in place and signing can be briefly interrupted.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoinbaseCdpRotationTargets) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.coinbase_cdp_secrets

    out["secrets"] = (
        capo_bedrock_agentcore_control.types.coinbase_cdp_secrets.serialize_json(
            value["secrets"]
        )
    )
    return out


def deserialize_json(data: dict) -> CoinbaseCdpRotationTargets:
    out: CoinbaseCdpRotationTargets = {}  # type: ignore[typeddict-item]
    if data.get("secrets") is not None:
        import capo_bedrock_agentcore_control.types.coinbase_cdp_secrets

        out["secrets"] = (
            capo_bedrock_agentcore_control.types.coinbase_cdp_secrets.deserialize_json(
                data["secrets"]
            )
        )
    else:
        out["secrets"] = []
    return out
