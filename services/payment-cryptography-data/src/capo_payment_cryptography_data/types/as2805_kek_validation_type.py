"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#As2805KekValidationType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)
from capo_payment_cryptography_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.kek_validation_request
    import capo_payment_cryptography_data.types.kek_validation_response


class _As2805KekValidationType_KekValidationRequest(TypedDict, closed=True):
    KekValidationRequest: "capo_payment_cryptography_data.types.kek_validation_request.KekValidationRequest"


class _As2805KekValidationType_KekValidationResponse(TypedDict, closed=True):
    KekValidationResponse: "capo_payment_cryptography_data.types.kek_validation_response.KekValidationResponse"


As2805KekValidationType: TypeAlias = (
    _As2805KekValidationType_KekValidationRequest
    | _As2805KekValidationType_KekValidationResponse
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: As2805KekValidationType) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"As2805KekValidationType: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "KekValidationRequest" in value:
        import capo_payment_cryptography_data.types.kek_validation_request

        return {
            "KekValidationRequest": capo_payment_cryptography_data.types.kek_validation_request.serialize_json(
                value["KekValidationRequest"]
            )
        }
    elif "KekValidationResponse" in value:
        import capo_payment_cryptography_data.types.kek_validation_response

        return {
            "KekValidationResponse": capo_payment_cryptography_data.types.kek_validation_response.serialize_json(
                value["KekValidationResponse"]
            )
        }
    else:
        raise SerializationError("As2805KekValidationType: no variant present")


def deserialize_json(data: dict) -> As2805KekValidationType:
    if data.get("KekValidationRequest") is not None:
        import capo_payment_cryptography_data.types.kek_validation_request

        return {
            "KekValidationRequest": capo_payment_cryptography_data.types.kek_validation_request.deserialize_json(
                data["KekValidationRequest"]
            )
        }
    elif data.get("KekValidationResponse") is not None:
        import capo_payment_cryptography_data.types.kek_validation_response

        return {
            "KekValidationResponse": capo_payment_cryptography_data.types.kek_validation_response.deserialize_json(
                data["KekValidationResponse"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("As2805KekValidationType: no recognized variant key")


def redact_sensitive(value: As2805KekValidationType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "KekValidationResponse" in value:
        import capo_payment_cryptography_data.types.kek_validation_response

        out["KekValidationResponse"] = (
            capo_payment_cryptography_data.types.kek_validation_response.redact_sensitive(
                value["KekValidationResponse"]
            )
        )
    return out
