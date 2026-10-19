"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportDukptInitialKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.hex_length20_or24


class ExportDukptInitialKey(TypedDict, closed=True):
    key_serial_number: (
        "capo_payment_cryptography.types.hex_length20_or24.HexLength20Or24"
    )
    """<p>The KSN for IPEK generation using DUKPT. </p> <p>KSN must be padded before sending to Amazon Web Services Payment Cryptography. KSN hex length should be 20 for a TDES_2KEY key or 24 for an AES key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportDukptInitialKey) -> dict:
    out: dict = {}
    out["KeySerialNumber"] = value["key_serial_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportDukptInitialKey:
    out: ExportDukptInitialKey = {}  # type: ignore[typeddict-item]
    if data.get("KeySerialNumber") is not None:
        out["key_serial_number"] = data["KeySerialNumber"]
    else:
        out["key_serial_number"] = ""
    return out
