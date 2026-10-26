"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#MacAttributes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)
from capo_payment_cryptography_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.mac_algorithm
    import capo_payment_cryptography_data.types.mac_algorithm_dukpt
    import capo_payment_cryptography_data.types.mac_algorithm_emv


class _MacAttributes_Algorithm(TypedDict, closed=True):
    Algorithm: "capo_payment_cryptography_data.types.mac_algorithm.MacAlgorithm"


class _MacAttributes_EmvMac(TypedDict, closed=True):
    EmvMac: "capo_payment_cryptography_data.types.mac_algorithm_emv.MacAlgorithmEmv"


class _MacAttributes_DukptIso9797Algorithm1(TypedDict, closed=True):
    DukptIso9797Algorithm1: (
        "capo_payment_cryptography_data.types.mac_algorithm_dukpt.MacAlgorithmDukpt"
    )


class _MacAttributes_DukptIso9797Algorithm3(TypedDict, closed=True):
    DukptIso9797Algorithm3: (
        "capo_payment_cryptography_data.types.mac_algorithm_dukpt.MacAlgorithmDukpt"
    )


class _MacAttributes_DukptCmac(TypedDict, closed=True):
    DukptCmac: (
        "capo_payment_cryptography_data.types.mac_algorithm_dukpt.MacAlgorithmDukpt"
    )


MacAttributes: TypeAlias = (
    _MacAttributes_Algorithm
    | _MacAttributes_EmvMac
    | _MacAttributes_DukptIso9797Algorithm1
    | _MacAttributes_DukptIso9797Algorithm3
    | _MacAttributes_DukptCmac
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MacAttributes) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MacAttributes: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Algorithm" in value:
        import capo_payment_cryptography_data.types.mac_algorithm

        return {
            "Algorithm": capo_payment_cryptography_data.types.mac_algorithm.serialize_json(
                value["Algorithm"]
            )
        }
    elif "EmvMac" in value:
        import capo_payment_cryptography_data.types.mac_algorithm_emv

        return {
            "EmvMac": capo_payment_cryptography_data.types.mac_algorithm_emv.serialize_json(
                value["EmvMac"]
            )
        }
    elif "DukptIso9797Algorithm1" in value:
        import capo_payment_cryptography_data.types.mac_algorithm_dukpt

        return {
            "DukptIso9797Algorithm1": capo_payment_cryptography_data.types.mac_algorithm_dukpt.serialize_json(
                value["DukptIso9797Algorithm1"]
            )
        }
    elif "DukptIso9797Algorithm3" in value:
        import capo_payment_cryptography_data.types.mac_algorithm_dukpt

        return {
            "DukptIso9797Algorithm3": capo_payment_cryptography_data.types.mac_algorithm_dukpt.serialize_json(
                value["DukptIso9797Algorithm3"]
            )
        }
    elif "DukptCmac" in value:
        import capo_payment_cryptography_data.types.mac_algorithm_dukpt

        return {
            "DukptCmac": capo_payment_cryptography_data.types.mac_algorithm_dukpt.serialize_json(
                value["DukptCmac"]
            )
        }
    else:
        raise SerializationError("MacAttributes: no variant present")


def deserialize_json(data: dict) -> MacAttributes:
    if data.get("Algorithm") is not None:
        import capo_payment_cryptography_data.types.mac_algorithm

        return {
            "Algorithm": capo_payment_cryptography_data.types.mac_algorithm.deserialize_json(
                data["Algorithm"]
            )
        }
    elif data.get("EmvMac") is not None:
        import capo_payment_cryptography_data.types.mac_algorithm_emv

        return {
            "EmvMac": capo_payment_cryptography_data.types.mac_algorithm_emv.deserialize_json(
                data["EmvMac"]
            )
        }
    elif data.get("DukptIso9797Algorithm1") is not None:
        import capo_payment_cryptography_data.types.mac_algorithm_dukpt

        return {
            "DukptIso9797Algorithm1": capo_payment_cryptography_data.types.mac_algorithm_dukpt.deserialize_json(
                data["DukptIso9797Algorithm1"]
            )
        }
    elif data.get("DukptIso9797Algorithm3") is not None:
        import capo_payment_cryptography_data.types.mac_algorithm_dukpt

        return {
            "DukptIso9797Algorithm3": capo_payment_cryptography_data.types.mac_algorithm_dukpt.deserialize_json(
                data["DukptIso9797Algorithm3"]
            )
        }
    elif data.get("DukptCmac") is not None:
        import capo_payment_cryptography_data.types.mac_algorithm_dukpt

        return {
            "DukptCmac": capo_payment_cryptography_data.types.mac_algorithm_dukpt.deserialize_json(
                data["DukptCmac"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("MacAttributes: no recognized variant key")


def redact_sensitive(value: MacAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "EmvMac" in value:
        import capo_payment_cryptography_data.types.mac_algorithm_emv

        out["EmvMac"] = (
            capo_payment_cryptography_data.types.mac_algorithm_emv.redact_sensitive(
                value["EmvMac"]
            )
        )
    return out
