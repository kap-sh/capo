"""Generated from Smithy shape ``com.amazonaws.groundstation#TelemetrySinkData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError
from capo_groundstation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_groundstation.types.kinesis_data_stream_data


class TelemetrySinkDataKinesisDataStreamDataMember(TypedDict, closed=True):
    kinesisDataStreamData: (
        "capo_groundstation.types.kinesis_data_stream_data.KinesisDataStreamData"
    )


TelemetrySinkData: TypeAlias = (
    TelemetrySinkDataKinesisDataStreamDataMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TelemetrySinkData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TelemetrySinkData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "kinesisDataStreamData" in value:
        import capo_groundstation.types.kinesis_data_stream_data

        return {
            "kinesisDataStreamData": capo_groundstation.types.kinesis_data_stream_data.serialize_json(
                value["kinesisDataStreamData"]
            )
        }
    else:
        raise SerializationError("TelemetrySinkData: no variant present")


def deserialize_json(data: dict) -> TelemetrySinkData:
    if data.get("kinesisDataStreamData") is not None:
        import capo_groundstation.types.kinesis_data_stream_data

        return {
            "kinesisDataStreamData": capo_groundstation.types.kinesis_data_stream_data.deserialize_json(
                data["kinesisDataStreamData"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TelemetrySinkData: no recognized variant key")
