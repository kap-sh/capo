"""Generated from Smithy shape ``com.amazonaws.iotsitewise#EnrichmentJobConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError, SerializationError
from capo_iotsitewise.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iotsitewise.types.event_detection


class EnrichmentJobConfigurationEventDetectionMember(TypedDict, closed=True):
    eventDetection: "capo_iotsitewise.types.event_detection.EventDetection"


EnrichmentJobConfiguration: TypeAlias = (
    EnrichmentJobConfigurationEventDetectionMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EnrichmentJobConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EnrichmentJobConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "eventDetection" in value:
        import capo_iotsitewise.types.event_detection

        return {
            "eventDetection": capo_iotsitewise.types.event_detection.serialize_json(
                value["eventDetection"]
            )
        }
    else:
        raise SerializationError("EnrichmentJobConfiguration: no variant present")


def deserialize_json(data: dict) -> EnrichmentJobConfiguration:
    if data.get("eventDetection") is not None:
        import capo_iotsitewise.types.event_detection

        return {
            "eventDetection": capo_iotsitewise.types.event_detection.deserialize_json(
                data["eventDetection"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "EnrichmentJobConfiguration: no recognized variant key"
        )
