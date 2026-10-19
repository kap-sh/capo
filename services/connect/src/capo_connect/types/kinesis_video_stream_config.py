"""Generated from Smithy shape ``com.amazonaws.connect#KinesisVideoStreamConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.encryption_config
    import capo_connect.types.hours
    import capo_connect.types.prefix


class KinesisVideoStreamConfig(TypedDict, closed=True):
    prefix: "capo_connect.types.prefix.Prefix"
    """<p>The prefix of the video stream.</p>"""
    retention_period_hours: "capo_connect.types.hours.Hours"
    """<p>The number of hours data is retained in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream.</p> <p>The default value is 0, indicating that the stream does not persist data.</p>"""
    encryption_config: "capo_connect.types.encryption_config.EncryptionConfig"
    """<p>The encryption configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisVideoStreamConfig) -> dict:
    out: dict = {}
    out["Prefix"] = value["prefix"]
    out["RetentionPeriodHours"] = value.get("retention_period_hours", 0)
    import capo_connect.types.encryption_config

    out["EncryptionConfig"] = capo_connect.types.encryption_config.serialize_json(
        value["encryption_config"]
    )
    return out


def deserialize_json(data: dict) -> KinesisVideoStreamConfig:
    out: KinesisVideoStreamConfig = {}  # type: ignore[typeddict-item]
    if data.get("Prefix") is not None:
        out["prefix"] = data["Prefix"]
    else:
        out["prefix"] = ""
    if data.get("RetentionPeriodHours") is not None:
        out["retention_period_hours"] = data["RetentionPeriodHours"]
    else:
        out["retention_period_hours"] = 0
    if data.get("EncryptionConfig") is not None:
        import capo_connect.types.encryption_config

        out["encryption_config"] = (
            capo_connect.types.encryption_config.deserialize_json(
                data["EncryptionConfig"]
            )
        )
    else:
        raise DeserializationError(
            "KinesisVideoStreamConfig.encryption_config required"
        )
    return out
