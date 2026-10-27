"""Generated from Smithy shape ``com.amazonaws.billing#AttestationQuantities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.attestation_quantity

AttestationQuantities: TypeAlias = list[
    "capo_billing.types.attestation_quantity.AttestationQuantity"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttestationQuantities) -> list:
    import capo_billing.types.attestation_quantity

    out: list = []
    for item in value:
        out.append(capo_billing.types.attestation_quantity.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AttestationQuantities:
    import capo_billing.types.attestation_quantity

    out: AttestationQuantities = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.attestation_quantity.deserialize_aws_json_1_0(item)
        )
    return out
