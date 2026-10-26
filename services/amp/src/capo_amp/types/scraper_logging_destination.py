"""Generated from Smithy shape ``com.amazonaws.amp#ScraperLoggingDestination``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError, SerializationError
from capo_amp.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_amp.types.cloud_watch_log_destination


class _ScraperLoggingDestination_cloudWatchLogs(TypedDict, closed=True):
    cloudWatchLogs: (
        "capo_amp.types.cloud_watch_log_destination.CloudWatchLogDestination"
    )


ScraperLoggingDestination: TypeAlias = (
    _ScraperLoggingDestination_cloudWatchLogs | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ScraperLoggingDestination) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ScraperLoggingDestination: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "cloudWatchLogs" in value:
        import capo_amp.types.cloud_watch_log_destination

        return {
            "cloudWatchLogs": capo_amp.types.cloud_watch_log_destination.serialize_json(
                value["cloudWatchLogs"]
            )
        }
    else:
        raise SerializationError("ScraperLoggingDestination: no variant present")


def deserialize_json(data: dict) -> ScraperLoggingDestination:
    if data.get("cloudWatchLogs") is not None:
        import capo_amp.types.cloud_watch_log_destination

        return {
            "cloudWatchLogs": capo_amp.types.cloud_watch_log_destination.deserialize_json(
                data["cloudWatchLogs"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ScraperLoggingDestination: no recognized variant key"
        )
