"""Generated from Smithy shape ``com.amazonaws.securityhub#CspmConnectorProviderName``."""

from typing import Literal, TypeAlias, cast

"""<p>The name of the cloud provider for a CSPM connector.</p>"""
CspmConnectorProviderName: TypeAlias = Literal[
    "AZURE",
    "GCP",
]


# --- restJson1 ser/de ---
def serialize_json(value: CspmConnectorProviderName) -> str:
    return value


def deserialize_json(data: str) -> CspmConnectorProviderName:
    return cast(CspmConnectorProviderName, data)
