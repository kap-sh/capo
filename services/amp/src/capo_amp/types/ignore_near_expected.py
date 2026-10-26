"""Generated from Smithy shape ``com.amazonaws.amp#IgnoreNearExpected``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError, SerializationError
from capo_amp.types._unknown import UnknownUnionMember


class _IgnoreNearExpected_amount(TypedDict, closed=True):
    amount: "float"


class _IgnoreNearExpected_ratio(TypedDict, closed=True):
    ratio: "float"


IgnoreNearExpected: TypeAlias = (
    _IgnoreNearExpected_amount | _IgnoreNearExpected_ratio | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IgnoreNearExpected) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IgnoreNearExpected: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "amount" in value:
        return {
            "amount": (
                "NaN"
                if value["amount"] != value["amount"]
                else "Infinity"
                if value["amount"] == float("inf")
                else "-Infinity"
                if value["amount"] == float("-inf")
                else value["amount"]
            )
        }
    elif "ratio" in value:
        return {
            "ratio": (
                "NaN"
                if value["ratio"] != value["ratio"]
                else "Infinity"
                if value["ratio"] == float("inf")
                else "-Infinity"
                if value["ratio"] == float("-inf")
                else value["ratio"]
            )
        }
    else:
        raise SerializationError("IgnoreNearExpected: no variant present")


def deserialize_json(data: dict) -> IgnoreNearExpected:
    if data.get("amount") is not None:
        return {"amount": float(data["amount"])}
    elif data.get("ratio") is not None:
        return {"ratio": float(data["ratio"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("IgnoreNearExpected: no recognized variant key")
