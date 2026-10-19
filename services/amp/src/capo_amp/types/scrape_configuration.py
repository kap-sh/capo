"""Generated from Smithy shape ``com.amazonaws.amp#ScrapeConfiguration``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError, SerializationError
from capo_amp.types._unknown import UnknownUnionMember


class _ScrapeConfiguration_configurationBlob(TypedDict, closed=True):
    configurationBlob: "bytes"


ScrapeConfiguration: TypeAlias = (
    _ScrapeConfiguration_configurationBlob | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ScrapeConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ScrapeConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "configurationBlob" in value:
        import capo_amp.types._prelude.blob

        return {
            "configurationBlob": capo_amp.types._prelude.blob.serialize_json(
                value["configurationBlob"]
            )
        }
    else:
        raise SerializationError("ScrapeConfiguration: no variant present")


def deserialize_json(data: dict) -> ScrapeConfiguration:
    if data.get("configurationBlob") is not None:
        import capo_amp.types._prelude.blob

        return {
            "configurationBlob": capo_amp.types._prelude.blob.deserialize_json(
                data["configurationBlob"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ScrapeConfiguration: no recognized variant key")
