"""Generated from Smithy shape ``com.amazonaws.billing#AttestationValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError, SerializationError
from capo_billing.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_billing.types.amount
    import capo_billing.types.attestation_quantities


class AttestationValueAttestationAmountMember(TypedDict, closed=True):
    attestationAmount: "capo_billing.types.amount.Amount"


class AttestationValueAttestationQuantitiesMember(TypedDict, closed=True):
    attestationQuantities: (
        "capo_billing.types.attestation_quantities.AttestationQuantities"
    )


AttestationValue: TypeAlias = (
    AttestationValueAttestationAmountMember
    | AttestationValueAttestationQuantitiesMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttestationValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AttestationValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "attestationAmount" in value:
        import capo_billing.types.amount

        return {
            "attestationAmount": capo_billing.types.amount.serialize_aws_json_1_0(
                value["attestationAmount"]
            )
        }
    elif "attestationQuantities" in value:
        import capo_billing.types.attestation_quantities

        return {
            "attestationQuantities": capo_billing.types.attestation_quantities.serialize_aws_json_1_0(
                value["attestationQuantities"]
            )
        }
    else:
        raise SerializationError("AttestationValue: no variant present")


def deserialize_aws_json_1_0(data: dict) -> AttestationValue:
    if data.get("attestationAmount") is not None:
        import capo_billing.types.amount

        return {
            "attestationAmount": capo_billing.types.amount.deserialize_aws_json_1_0(
                data["attestationAmount"]
            )
        }
    elif data.get("attestationQuantities") is not None:
        import capo_billing.types.attestation_quantities

        return {
            "attestationQuantities": capo_billing.types.attestation_quantities.deserialize_aws_json_1_0(
                data["attestationQuantities"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AttestationValue: no recognized variant key")
