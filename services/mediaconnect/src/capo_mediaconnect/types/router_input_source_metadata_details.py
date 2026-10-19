"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputSourceMetadataDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.router_input_messages
    import capo_mediaconnect.types.router_input_metadata


class RouterInputSourceMetadataDetails(TypedDict, closed=True):
    source_metadata_messages: (
        "capo_mediaconnect.types.router_input_messages.RouterInputMessages"
    )
    """<p>Collection of metadata messages associated with the router input source.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp when the metadata was last updated.</p>"""
    router_input_metadata: NotRequired[
        "capo_mediaconnect.types.router_input_metadata.RouterInputMetadata"
    ]
    """<p>Metadata information specific to the router input configuration and state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputSourceMetadataDetails) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.router_input_messages

    out["sourceMetadataMessages"] = (
        capo_mediaconnect.types.router_input_messages.serialize_json(
            value["source_metadata_messages"]
        )
    )
    import capo_mediaconnect._protocol.serialize

    out["timestamp"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
        value["timestamp"]
    )
    if "router_input_metadata" in value:
        import capo_mediaconnect.types.router_input_metadata

        out["routerInputMetadata"] = (
            capo_mediaconnect.types.router_input_metadata.serialize_json(
                value["router_input_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouterInputSourceMetadataDetails:
    out: RouterInputSourceMetadataDetails = {}  # type: ignore[typeddict-item]
    if data.get("sourceMetadataMessages") is not None:
        import capo_mediaconnect.types.router_input_messages

        out["source_metadata_messages"] = (
            capo_mediaconnect.types.router_input_messages.deserialize_json(
                data["sourceMetadataMessages"]
            )
        )
    else:
        out["source_metadata_messages"] = []
    if data.get("timestamp") is not None:
        import datetime

        out["timestamp"] = datetime.datetime.fromisoformat(
            data["timestamp"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("routerInputMetadata") is not None:
        import capo_mediaconnect.types.router_input_metadata

        out["router_input_metadata"] = (
            capo_mediaconnect.types.router_input_metadata.deserialize_json(
                data["routerInputMetadata"]
            )
        )
    return out
