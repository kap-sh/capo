"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ImportKeyCryptogram``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.import_token_id
    import capo_payment_cryptography.types.key_attributes
    import capo_payment_cryptography.types.wrapped_key_cryptogram
    import capo_payment_cryptography.types.wrapping_key_spec


class ImportKeyCryptogram(TypedDict, closed=True):
    key_attributes: "capo_payment_cryptography.types.key_attributes.KeyAttributes"
    exportable: "bool"
    """<p>Specifies whether the key is exportable from the service.</p>"""
    wrapped_key_cryptogram: (
        "capo_payment_cryptography.types.wrapped_key_cryptogram.WrappedKeyCryptogram"
    )
    """<p>The RSA wrapped key cryptogram under import.</p>"""
    import_token: "capo_payment_cryptography.types.import_token_id.ImportTokenId"
    """<p>The import token that initiates key import using the asymmetric RSA wrap and unwrap key exchange method into AWS Payment Cryptography. It expires after 30 days. You can use the same import token to import multiple keys to the same service account.</p>"""
    wrapping_spec: NotRequired[
        "capo_payment_cryptography.types.wrapping_key_spec.WrappingKeySpec"
    ]
    """<p>The wrapping spec for the wrapped key cryptogram.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportKeyCryptogram) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.key_attributes

    out["KeyAttributes"] = (
        capo_payment_cryptography.types.key_attributes.serialize_aws_json_1_0(
            value["key_attributes"]
        )
    )
    out["Exportable"] = value["exportable"]
    out["WrappedKeyCryptogram"] = value["wrapped_key_cryptogram"]
    out["ImportToken"] = value["import_token"]
    if "wrapping_spec" in value:
        out["WrappingSpec"] = value["wrapping_spec"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportKeyCryptogram:
    out: ImportKeyCryptogram = {}  # type: ignore[typeddict-item]
    if data.get("KeyAttributes") is not None:
        import capo_payment_cryptography.types.key_attributes

        out["key_attributes"] = (
            capo_payment_cryptography.types.key_attributes.deserialize_aws_json_1_0(
                data["KeyAttributes"]
            )
        )
    else:
        raise DeserializationError("ImportKeyCryptogram.key_attributes required")
    if data.get("Exportable") is not None:
        out["exportable"] = data["Exportable"]
    else:
        out["exportable"] = False
    if data.get("WrappedKeyCryptogram") is not None:
        out["wrapped_key_cryptogram"] = data["WrappedKeyCryptogram"]
    else:
        out["wrapped_key_cryptogram"] = ""
    if data.get("ImportToken") is not None:
        out["import_token"] = data["ImportToken"]
    else:
        out["import_token"] = ""
    if data.get("WrappingSpec") is not None:
        out["wrapping_spec"] = data["WrappingSpec"]
    return out


def redact_sensitive(value: ImportKeyCryptogram) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "wrapped_key_cryptogram" in value:
        out["wrapped_key_cryptogram"] = "*** Sensitive Data Redacted ***"
    return out
