"""Generated from Smithy shape ``com.amazonaws.datazone#OutputLocation``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.s3_destination


class _OutputLocation_s3(TypedDict, closed=True):
    s3: "capo_datazone.types.s3_destination.S3Destination"


OutputLocation: TypeAlias = _OutputLocation_s3 | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: OutputLocation) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OutputLocation: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_datazone.types.s3_destination

        return {"s3": capo_datazone.types.s3_destination.serialize_json(value["s3"])}
    else:
        raise SerializationError("OutputLocation: no variant present")


def deserialize_json(data: dict) -> OutputLocation:
    if data.get("s3") is not None:
        import capo_datazone.types.s3_destination

        return {"s3": capo_datazone.types.s3_destination.deserialize_json(data["s3"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OutputLocation: no recognized variant key")


def redact_sensitive(value: OutputLocation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "s3" in value:
        import capo_datazone.types.s3_destination

        out["s3"] = capo_datazone.types.s3_destination.redact_sensitive(value["s3"])
    return out
