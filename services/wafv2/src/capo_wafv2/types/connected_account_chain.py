"""Generated from Smithy shape ``com.amazonaws.wafv2#ConnectedAccountChain``."""

from typing import Literal, TypeAlias, cast

"""<p>The blockchain network for a connected account. Production networks only. Test networks are not supported because connected accounts settle production payments only.</p> <p>Valid values:</p> <ul> <li> <p> <code>BASE</code> - Base mainnet.</p> </li> <li> <p> <code>SOLANA</code> - Solana mainnet.</p> </li> </ul>"""
ConnectedAccountChain: TypeAlias = Literal[
    "BASE",
    "SOLANA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectedAccountChain) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectedAccountChain:
    return cast(ConnectedAccountChain, data)
