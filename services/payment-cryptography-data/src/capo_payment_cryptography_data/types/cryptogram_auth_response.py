"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#CryptogramAuthResponse``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.cryptogram_verification_arpc_method1
    import capo_payment_cryptography_data.types.cryptogram_verification_arpc_method2


class _CryptogramAuthResponse_ArpcMethod1(TypedDict, closed=True):
    ArpcMethod1: "capo_payment_cryptography_data.types.cryptogram_verification_arpc_method1.CryptogramVerificationArpcMethod1"


class _CryptogramAuthResponse_ArpcMethod2(TypedDict, closed=True):
    ArpcMethod2: "capo_payment_cryptography_data.types.cryptogram_verification_arpc_method2.CryptogramVerificationArpcMethod2"


CryptogramAuthResponse: TypeAlias = (
    _CryptogramAuthResponse_ArpcMethod1 | _CryptogramAuthResponse_ArpcMethod2
)


# --- restJson1 ser/de ---
def serialize_json(value: CryptogramAuthResponse) -> dict:
    if "ArpcMethod1" in value:
        import capo_payment_cryptography_data.types.cryptogram_verification_arpc_method1

        return {
            "ArpcMethod1": capo_payment_cryptography_data.types.cryptogram_verification_arpc_method1.serialize_json(
                value["ArpcMethod1"]
            )
        }
    elif "ArpcMethod2" in value:
        import capo_payment_cryptography_data.types.cryptogram_verification_arpc_method2

        return {
            "ArpcMethod2": capo_payment_cryptography_data.types.cryptogram_verification_arpc_method2.serialize_json(
                value["ArpcMethod2"]
            )
        }
    else:
        raise SerializationError("CryptogramAuthResponse: no variant present")


def deserialize_json(data: dict) -> CryptogramAuthResponse:
    if data.get("ArpcMethod1") is not None:
        import capo_payment_cryptography_data.types.cryptogram_verification_arpc_method1

        return {
            "ArpcMethod1": capo_payment_cryptography_data.types.cryptogram_verification_arpc_method1.deserialize_json(
                data["ArpcMethod1"]
            )
        }
    elif data.get("ArpcMethod2") is not None:
        import capo_payment_cryptography_data.types.cryptogram_verification_arpc_method2

        return {
            "ArpcMethod2": capo_payment_cryptography_data.types.cryptogram_verification_arpc_method2.deserialize_json(
                data["ArpcMethod2"]
            )
        }
    else:
        raise DeserializationError("CryptogramAuthResponse: no recognized variant key")


def redact_sensitive(value: CryptogramAuthResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ArpcMethod2" in value:
        import capo_payment_cryptography_data.types.cryptogram_verification_arpc_method2

        out["ArpcMethod2"] = (
            capo_payment_cryptography_data.types.cryptogram_verification_arpc_method2.redact_sensitive(
                value["ArpcMethod2"]
            )
        )
    return out
