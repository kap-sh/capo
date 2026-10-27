"""Generated from Smithy shape ``com.amazonaws.billing#InvestmentAttestationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The current state of a submitted investment attestation in its lifecycle. Valid values are <code>PENDING_REVIEW</code>, <code>PENDING_C_LEVEL_APPROVAL</code>, <code>PENDING_CANCELLATION</code>, <code>REJECTED</code>, <code>CANCELLED</code>, and <code>DISBURSED</code>. The values <code>DISBURSED</code>, <code>REJECTED</code>, and <code>CANCELLED</code> are terminal. The values <code>PENDING_REVIEW</code>, <code>PENDING_C_LEVEL_APPROVAL</code>, and <code>PENDING_CANCELLATION</code> indicate the attestation is still in progress.</p>"""
InvestmentAttestationStatus: TypeAlias = Literal[
    "PENDING_REVIEW",
    "PENDING_C_LEVEL_APPROVAL",
    "PENDING_CANCELLATION",
    "REJECTED",
    "CANCELLED",
    "DISBURSED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvestmentAttestationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InvestmentAttestationStatus:
    return cast(InvestmentAttestationStatus, data)
