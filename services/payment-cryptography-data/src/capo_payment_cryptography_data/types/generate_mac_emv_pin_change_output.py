"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GenerateMacEmvPinChangeOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.encrypted_pin_block_type
    import capo_payment_cryptography_data.types.key_arn
    import capo_payment_cryptography_data.types.key_check_value
    import capo_payment_cryptography_data.types.pin_change_mac_output_type
    import capo_payment_cryptography_data.types.visa_amex_derivation_outputs


class GenerateMacEmvPinChangeOutput(TypedDict, closed=True):
    new_pin_pek_arn: "capo_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>Returns the <code>keyArn</code> of the PEK protecting the incoming new encrypted PIN block.</p>"""
    secure_messaging_integrity_key_arn: (
        "capo_payment_cryptography_data.types.key_arn.KeyArn"
    )
    """<p>Returns the <code>keyArn</code> of the IMK-SMI used by the operation.</p>"""
    secure_messaging_confidentiality_key_arn: (
        "capo_payment_cryptography_data.types.key_arn.KeyArn"
    )
    """<p>Returns the <code>keyArn</code> of the IMK-SMC used by the operation.</p>"""
    mac: "capo_payment_cryptography_data.types.pin_change_mac_output_type.PinChangeMacOutputType"
    """<p>Returns the mac of the issuer script containing message data and appended target encrypted pin block in ISO2 format.</p>"""
    encrypted_pin_block: "capo_payment_cryptography_data.types.encrypted_pin_block_type.EncryptedPinBlockType"
    """<p>Returns the incoming new encrpted PIN block.</p>"""
    new_pin_pek_key_check_value: (
        "capo_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the PEK uprotecting the incoming new encrypted PIN block.</p>"""
    secure_messaging_integrity_key_check_value: (
        "capo_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the SMI issuer master key used by the operation.</p>"""
    secure_messaging_confidentiality_key_check_value: (
        "capo_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the SMC issuer master key used by the operation.</p>"""
    visa_amex_derivation_outputs: NotRequired[
        "capo_payment_cryptography_data.types.visa_amex_derivation_outputs.VisaAmexDerivationOutputs"
    ]
    """<p>The attribute values used for Amex and Visa derivation methods.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateMacEmvPinChangeOutput) -> dict:
    out: dict = {}
    out["NewPinPekArn"] = value["new_pin_pek_arn"]
    out["SecureMessagingIntegrityKeyArn"] = value["secure_messaging_integrity_key_arn"]
    out["SecureMessagingConfidentialityKeyArn"] = value[
        "secure_messaging_confidentiality_key_arn"
    ]
    out["Mac"] = value["mac"]
    out["EncryptedPinBlock"] = value["encrypted_pin_block"]
    out["NewPinPekKeyCheckValue"] = value["new_pin_pek_key_check_value"]
    out["SecureMessagingIntegrityKeyCheckValue"] = value[
        "secure_messaging_integrity_key_check_value"
    ]
    out["SecureMessagingConfidentialityKeyCheckValue"] = value[
        "secure_messaging_confidentiality_key_check_value"
    ]
    if "visa_amex_derivation_outputs" in value:
        import capo_payment_cryptography_data.types.visa_amex_derivation_outputs

        out["VisaAmexDerivationOutputs"] = (
            capo_payment_cryptography_data.types.visa_amex_derivation_outputs.serialize_json(
                value["visa_amex_derivation_outputs"]
            )
        )
    return out


def deserialize_json(data: dict) -> GenerateMacEmvPinChangeOutput:
    out: GenerateMacEmvPinChangeOutput = {}  # type: ignore[typeddict-item]
    if data.get("NewPinPekArn") is not None:
        out["new_pin_pek_arn"] = data["NewPinPekArn"]
    else:
        out["new_pin_pek_arn"] = ""
    if data.get("SecureMessagingIntegrityKeyArn") is not None:
        out["secure_messaging_integrity_key_arn"] = data[
            "SecureMessagingIntegrityKeyArn"
        ]
    else:
        out["secure_messaging_integrity_key_arn"] = ""
    if data.get("SecureMessagingConfidentialityKeyArn") is not None:
        out["secure_messaging_confidentiality_key_arn"] = data[
            "SecureMessagingConfidentialityKeyArn"
        ]
    else:
        out["secure_messaging_confidentiality_key_arn"] = ""
    if data.get("Mac") is not None:
        out["mac"] = data["Mac"]
    else:
        out["mac"] = ""
    if data.get("EncryptedPinBlock") is not None:
        out["encrypted_pin_block"] = data["EncryptedPinBlock"]
    else:
        out["encrypted_pin_block"] = ""
    if data.get("NewPinPekKeyCheckValue") is not None:
        out["new_pin_pek_key_check_value"] = data["NewPinPekKeyCheckValue"]
    else:
        out["new_pin_pek_key_check_value"] = ""
    if data.get("SecureMessagingIntegrityKeyCheckValue") is not None:
        out["secure_messaging_integrity_key_check_value"] = data[
            "SecureMessagingIntegrityKeyCheckValue"
        ]
    else:
        out["secure_messaging_integrity_key_check_value"] = ""
    if data.get("SecureMessagingConfidentialityKeyCheckValue") is not None:
        out["secure_messaging_confidentiality_key_check_value"] = data[
            "SecureMessagingConfidentialityKeyCheckValue"
        ]
    else:
        out["secure_messaging_confidentiality_key_check_value"] = ""
    if data.get("VisaAmexDerivationOutputs") is not None:
        import capo_payment_cryptography_data.types.visa_amex_derivation_outputs

        out["visa_amex_derivation_outputs"] = (
            capo_payment_cryptography_data.types.visa_amex_derivation_outputs.deserialize_json(
                data["VisaAmexDerivationOutputs"]
            )
        )
    return out


def redact_sensitive(value: GenerateMacEmvPinChangeOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "mac" in value:
        out["mac"] = "*** Sensitive Data Redacted ***"
    if "encrypted_pin_block" in value:
        out["encrypted_pin_block"] = "*** Sensitive Data Redacted ***"
    return out
