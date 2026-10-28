"""Generated from Smithy shape ``com.amazonaws.connect#ContactMetricValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.double


class ContactMetricValueNumberMember(TypedDict, closed=True):
    Number: "capo_connect.types.double.Double"


ContactMetricValue: TypeAlias = ContactMetricValueNumberMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ContactMetricValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ContactMetricValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Number" in value:
        return {
            "Number": (
                "NaN"
                if value["Number"] != value["Number"]
                else "Infinity"
                if value["Number"] == float("inf")
                else "-Infinity"
                if value["Number"] == float("-inf")
                else value["Number"]
            )
        }
    else:
        raise SerializationError("ContactMetricValue: no variant present")


def deserialize_json(data: dict) -> ContactMetricValue:
    if data.get("Number") is not None:
        return {"Number": float(data["Number"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ContactMetricValue: no recognized variant key")
