"""Generated from Smithy shape ``com.amazonaws.appfabric#Destination``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_appfabric.errors import DeserializationError, SerializationError
from capo_appfabric.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_appfabric.types.firehose_stream
    import capo_appfabric.types.s3_bucket


class _Destination_s3Bucket(TypedDict, closed=True):
    s3Bucket: "capo_appfabric.types.s3_bucket.S3Bucket"


class _Destination_firehoseStream(TypedDict, closed=True):
    firehoseStream: "capo_appfabric.types.firehose_stream.FirehoseStream"


Destination: TypeAlias = (
    _Destination_s3Bucket | _Destination_firehoseStream | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Destination: cannot serialize unknown variant {value.name!r}"
        )
    elif "s3Bucket" in value:
        import capo_appfabric.types.s3_bucket

        return {
            "s3Bucket": capo_appfabric.types.s3_bucket.serialize_json(value["s3Bucket"])
        }
    elif "firehoseStream" in value:
        import capo_appfabric.types.firehose_stream

        return {
            "firehoseStream": capo_appfabric.types.firehose_stream.serialize_json(
                value["firehoseStream"]
            )
        }
    else:
        raise SerializationError("Destination: no variant present")


def deserialize_json(data: dict) -> Destination:
    if data.get("s3Bucket") is not None:
        import capo_appfabric.types.s3_bucket

        return {
            "s3Bucket": capo_appfabric.types.s3_bucket.deserialize_json(
                data["s3Bucket"]
            )
        }
    elif data.get("firehoseStream") is not None:
        import capo_appfabric.types.firehose_stream

        return {
            "firehoseStream": capo_appfabric.types.firehose_stream.deserialize_json(
                data["firehoseStream"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Destination: no recognized variant key")
