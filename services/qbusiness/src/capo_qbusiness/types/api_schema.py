"""Generated from Smithy shape ``com.amazonaws.qbusiness#APISchema``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.payload
    import capo_qbusiness.types.s3


class _APISchema_payload(TypedDict, closed=True):
    payload: "capo_qbusiness.types.payload.Payload"


class _APISchema_s3(TypedDict, closed=True):
    s3: "capo_qbusiness.types.s3.S3"


APISchema: TypeAlias = _APISchema_payload | _APISchema_s3 | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: APISchema) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"APISchema: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "payload" in value:
        return {"payload": value["payload"]}
    elif "s3" in value:
        import capo_qbusiness.types.s3

        return {"s3": capo_qbusiness.types.s3.serialize_json(value["s3"])}
    else:
        raise SerializationError("APISchema: no variant present")


def deserialize_json(data: dict) -> APISchema:
    if data.get("payload") is not None:
        return {"payload": data["payload"]}
    elif data.get("s3") is not None:
        import capo_qbusiness.types.s3

        return {"s3": capo_qbusiness.types.s3.deserialize_json(data["s3"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("APISchema: no recognized variant key")


def redact_sensitive(value: APISchema) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        out["payload"] = "*** Sensitive Data Redacted ***"
    return out
