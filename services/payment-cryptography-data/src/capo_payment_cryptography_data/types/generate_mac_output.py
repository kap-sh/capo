"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GenerateMacOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.key_arn
    import capo_payment_cryptography_data.types.key_check_value
    import capo_payment_cryptography_data.types.mac_output_type


class GenerateMacOutput(TypedDict, closed=True):
    key_arn: "capo_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>The <code>keyARN</code> of the encryption key that Amazon Web Services Payment Cryptography uses for MAC generation.</p>"""
    key_check_value: (
        "capo_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p> <p>Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.</p>"""
    mac: "capo_payment_cryptography_data.types.mac_output_type.MacOutputType"
    """<p>The MAC cryptogram generated within Amazon Web Services Payment Cryptography.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateMacOutput) -> dict:
    out: dict = {}
    out["KeyArn"] = value["key_arn"]
    out["KeyCheckValue"] = value["key_check_value"]
    out["Mac"] = value["mac"]
    return out


def deserialize_json(data: dict) -> GenerateMacOutput:
    out: GenerateMacOutput = {}  # type: ignore[typeddict-item]
    if data.get("KeyArn") is not None:
        out["key_arn"] = data["KeyArn"]
    else:
        out["key_arn"] = ""
    if data.get("KeyCheckValue") is not None:
        out["key_check_value"] = data["KeyCheckValue"]
    else:
        out["key_check_value"] = ""
    if data.get("Mac") is not None:
        out["mac"] = data["Mac"]
    else:
        out["mac"] = ""
    return out


def redact_sensitive(value: GenerateMacOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "mac" in value:
        out["mac"] = "*** Sensitive Data Redacted ***"
    return out
