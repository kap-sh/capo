"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentContent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.s3


class _DocumentContent_blob(TypedDict, closed=True):
    blob: "bytes"


class _DocumentContent_s3(TypedDict, closed=True):
    s3: "capo_qbusiness.types.s3.S3"


DocumentContent: TypeAlias = (
    _DocumentContent_blob | _DocumentContent_s3 | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DocumentContent) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DocumentContent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "blob" in value:
        import capo_qbusiness.types._prelude.blob

        return {
            "blob": capo_qbusiness.types._prelude.blob.serialize_json(value["blob"])
        }
    elif "s3" in value:
        import capo_qbusiness.types.s3

        return {"s3": capo_qbusiness.types.s3.serialize_json(value["s3"])}
    else:
        raise SerializationError("DocumentContent: no variant present")


def deserialize_json(data: dict) -> DocumentContent:
    if data.get("blob") is not None:
        import capo_qbusiness.types._prelude.blob

        return {
            "blob": capo_qbusiness.types._prelude.blob.deserialize_json(data["blob"])
        }
    elif data.get("s3") is not None:
        import capo_qbusiness.types.s3

        return {"s3": capo_qbusiness.types.s3.deserialize_json(data["s3"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DocumentContent: no recognized variant key")
