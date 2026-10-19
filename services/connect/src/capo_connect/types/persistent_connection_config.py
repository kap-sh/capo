"""Generated from Smithy shape ``com.amazonaws.connect#PersistentConnectionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.channel
    import capo_connect.types.persistent_connection


class PersistentConnectionConfig(TypedDict, closed=True):
    channel: "capo_connect.types.channel.Channel"
    """<p>Configuration settings for persistent connection. <b>Only <code>VOICE</code> is supported for this data type.</b> </p>"""
    persistent_connection: (
        "capo_connect.types.persistent_connection.PersistentConnection"
    )
    """<p>Indicates whether persistent connection is enabled. When enabled, the agent's connection is maintained after a call ends, enabling subsequent calls to connect faster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PersistentConnectionConfig) -> dict:
    out: dict = {}
    import capo_connect.types.channel

    out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    out["PersistentConnection"] = value["persistent_connection"]
    return out


def deserialize_json(data: dict) -> PersistentConnectionConfig:
    out: PersistentConnectionConfig = {}  # type: ignore[typeddict-item]
    if data.get("Channel") is not None:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    else:
        import typing

        out["channel"] = typing.cast("capo_connect.types.channel.Channel", "")
    if data.get("PersistentConnection") is not None:
        out["persistent_connection"] = data["PersistentConnection"]
    else:
        out["persistent_connection"] = False
    return out
