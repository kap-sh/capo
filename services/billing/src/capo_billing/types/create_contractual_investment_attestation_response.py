"""Generated from Smithy shape ``com.amazonaws.billing#CreateContractualInvestmentAttestationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.identifier_string


class CreateContractualInvestmentAttestationResponse(TypedDict, closed=True):
    attestation_id: "capo_billing.types.identifier_string.IdentifierString"
    """<p>The identifier of the submitted attestation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: CreateContractualInvestmentAttestationResponse,
) -> dict:
    out: dict = {}
    out["attestationId"] = value["attestation_id"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> CreateContractualInvestmentAttestationResponse:
    out: CreateContractualInvestmentAttestationResponse = {}  # type: ignore[typeddict-item]
    if data.get("attestationId") is not None:
        out["attestation_id"] = data["attestationId"]
    else:
        out["attestation_id"] = ""
    return out
