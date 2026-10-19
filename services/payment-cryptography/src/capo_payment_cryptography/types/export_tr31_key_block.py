"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportTr31KeyBlock``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.key_arn_or_key_alias_type
    import capo_payment_cryptography.types.key_block_headers


class ExportTr31KeyBlock(TypedDict, closed=True):
    wrapping_key_identifier: (
        "capo_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    )
    """<p>The <code>KeyARN</code> of the the wrapping key. This key encrypts or wraps the key under export for TR-31 key block generation.</p>"""
    key_block_headers: NotRequired[
        "capo_payment_cryptography.types.key_block_headers.KeyBlockHeaders"
    ]
    """<p>Optional metadata for export associated with the key material. This data is signed but transmitted in clear text.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportTr31KeyBlock) -> dict:
    out: dict = {}
    out["WrappingKeyIdentifier"] = value["wrapping_key_identifier"]
    if "key_block_headers" in value:
        import capo_payment_cryptography.types.key_block_headers

        out["KeyBlockHeaders"] = (
            capo_payment_cryptography.types.key_block_headers.serialize_aws_json_1_0(
                value["key_block_headers"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportTr31KeyBlock:
    out: ExportTr31KeyBlock = {}  # type: ignore[typeddict-item]
    if data.get("WrappingKeyIdentifier") is not None:
        out["wrapping_key_identifier"] = data["WrappingKeyIdentifier"]
    else:
        out["wrapping_key_identifier"] = ""
    if data.get("KeyBlockHeaders") is not None:
        import capo_payment_cryptography.types.key_block_headers

        out["key_block_headers"] = (
            capo_payment_cryptography.types.key_block_headers.deserialize_aws_json_1_0(
                data["KeyBlockHeaders"]
            )
        )
    return out


def redact_sensitive(value: ExportTr31KeyBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key_block_headers" in value:
        import capo_payment_cryptography.types.key_block_headers

        out["key_block_headers"] = (
            capo_payment_cryptography.types.key_block_headers.redact_sensitive(
                value["key_block_headers"]
            )
        )
    return out
