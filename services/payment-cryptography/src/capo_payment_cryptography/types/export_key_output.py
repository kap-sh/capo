"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportKeyOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.wrapped_key


class ExportKeyOutput(TypedDict, closed=True):
    wrapped_key: NotRequired["capo_payment_cryptography.types.wrapped_key.WrappedKey"]
    """<p>The key material under export as a TR-34 WrappedKeyBlock or a TR-31 WrappedKeyBlock. or a RSA WrappedKeyCryptogram.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportKeyOutput) -> dict:
    out: dict = {}
    if "wrapped_key" in value:
        import capo_payment_cryptography.types.wrapped_key

        out["WrappedKey"] = (
            capo_payment_cryptography.types.wrapped_key.serialize_aws_json_1_0(
                value["wrapped_key"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportKeyOutput:
    out: ExportKeyOutput = {}  # type: ignore[typeddict-item]
    if data.get("WrappedKey") is not None:
        import capo_payment_cryptography.types.wrapped_key

        out["wrapped_key"] = (
            capo_payment_cryptography.types.wrapped_key.deserialize_aws_json_1_0(
                data["WrappedKey"]
            )
        )
    return out


def redact_sensitive(value: ExportKeyOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "wrapped_key" in value:
        import capo_payment_cryptography.types.wrapped_key

        out["wrapped_key"] = (
            capo_payment_cryptography.types.wrapped_key.redact_sensitive(
                value["wrapped_key"]
            )
        )
    return out
