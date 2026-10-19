"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ImportTr31KeyBlock``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.key_arn_or_key_alias_type
    import capo_payment_cryptography.types.tr31_wrapped_key_block


class ImportTr31KeyBlock(TypedDict, closed=True):
    wrapping_key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    """<p>The <code>KeyARN</code> of the key that will decrypt or unwrap a TR-31 key block during import.</p>"""
    wrapped_key_block: (
        "capo_payment_cryptography.types.tr31_wrapped_key_block.Tr31WrappedKeyBlock"
    )
    """<p>The TR-31 wrapped key block to import.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportTr31KeyBlock) -> dict:
    out: dict = {}
    out["WrappingKeyIdentifier"] = value["wrapping_key_identifier"]
    out["WrappedKeyBlock"] = value["wrapped_key_block"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportTr31KeyBlock:
    out: ImportTr31KeyBlock = {}  # type: ignore[typeddict-item]
    if data.get("WrappingKeyIdentifier") is not None:
        out["wrapping_key_identifier"] = data["WrappingKeyIdentifier"]
    else:
        out["wrapping_key_identifier"] = ""
    if data.get("WrappedKeyBlock") is not None:
        out["wrapped_key_block"] = data["WrappedKeyBlock"]
    else:
        out["wrapped_key_block"] = ""
    return out


def redact_sensitive(value: ImportTr31KeyBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "wrapped_key_block" in value:
        out["wrapped_key_block"] = "*** Sensitive Data Redacted ***"
    return out
