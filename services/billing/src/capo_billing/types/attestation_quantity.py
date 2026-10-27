"""Generated from Smithy shape ``com.amazonaws.billing#AttestationQuantity``."""

from typing_extensions import TypedDict


class AttestationQuantity(TypedDict, closed=True):
    attestation_volume: "str"
    """<p>The number of units being attested, expressed as a decimal string to preserve precision. The value is digits with an optional decimal point and is 1–1000 characters.</p>"""
    attestation_unit: "str"
    """<p>The unit of the attestation, such as <code>workloads migrated</code>. This value is 1–1000 characters.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttestationQuantity) -> dict:
    out: dict = {}
    out["attestationVolume"] = value["attestation_volume"]
    out["attestationUnit"] = value["attestation_unit"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AttestationQuantity:
    out: AttestationQuantity = {}  # type: ignore[typeddict-item]
    if data.get("attestationVolume") is not None:
        out["attestation_volume"] = data["attestationVolume"]
    else:
        out["attestation_volume"] = ""
    if data.get("attestationUnit") is not None:
        out["attestation_unit"] = data["attestationUnit"]
    else:
        out["attestation_unit"] = ""
    return out
