"""Generated from Smithy shape ``com.amazonaws.opensearch#TLSSecurityPolicy``."""

from typing import Literal, TypeAlias, cast

TLSSecurityPolicy: TypeAlias = Literal[
    "Policy-Min-TLS-1-0-2019-07",
    "Policy-Min-TLS-1-2-2019-07",
    "Policy-Min-TLS-1-2-PFS-2023-10",
    "Policy-Min-TLS-1-2-RFC9151-FIPS-2024-08",
    "Policy-Min-TLS-1-2-FIPS-PQ-2026-10",
]


# --- restJson1 ser/de ---
def serialize_json(value: TLSSecurityPolicy) -> str:
    return value


def deserialize_json(data: str) -> TLSSecurityPolicy:
    return cast(TLSSecurityPolicy, data)
