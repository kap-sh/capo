"""Generated from Smithy shape ``com.amazonaws.abusesignal#ReportData``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_abuse_signal.errors import DeserializationError, SerializationError
from capo_abuse_signal.types._unknown import UnknownUnionMember


class ReportDataXarfMember(TypedDict, closed=True):
    xarf: "object"


ReportData: TypeAlias = ReportDataXarfMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ReportData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ReportData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "xarf" in value:
        return {"xarf": value["xarf"]}
    else:
        raise SerializationError("ReportData: no variant present")


def deserialize_json(data: dict) -> ReportData:
    if data.get("xarf") is not None:
        return {"xarf": data["xarf"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ReportData: no recognized variant key")
