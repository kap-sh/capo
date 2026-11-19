"""Generated from Smithy shape ``com.amazonaws.workspaces#TimeoutSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.disconnect_timeout_in_seconds
    import capo_workspaces.types.idle_disconnect_timeout_in_seconds
    import capo_workspaces.types.max_user_duration_in_seconds


class TimeoutSettings(TypedDict, closed=True):
    disconnect_timeout_in_seconds: NotRequired[
        "capo_workspaces.types.disconnect_timeout_in_seconds.DisconnectTimeoutInSeconds"
    ]
    """<p>Specifies the amount of time, in seconds, that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within the time set, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.</p>"""
    idle_disconnect_timeout_in_seconds: NotRequired[
        "capo_workspaces.types.idle_disconnect_timeout_in_seconds.IdleDisconnectTimeoutInSeconds"
    ]
    """<p>The amount of time in seconds a connection will stay active while idle.</p>"""
    max_user_duration_in_seconds: NotRequired[
        "capo_workspaces.types.max_user_duration_in_seconds.MaxUserDurationInSeconds"
    ]
    """<p>Specifies the maximum amount of time, in seconds, that a streaming session can remain active. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeoutSettings) -> dict:
    out: dict = {}
    if "disconnect_timeout_in_seconds" in value:
        out["DisconnectTimeoutInSeconds"] = value["disconnect_timeout_in_seconds"]
    if "idle_disconnect_timeout_in_seconds" in value:
        out["IdleDisconnectTimeoutInSeconds"] = value[
            "idle_disconnect_timeout_in_seconds"
        ]
    if "max_user_duration_in_seconds" in value:
        out["MaxUserDurationInSeconds"] = value["max_user_duration_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeoutSettings:
    out: TimeoutSettings = {}  # type: ignore[typeddict-item]
    if data.get("DisconnectTimeoutInSeconds") is not None:
        out["disconnect_timeout_in_seconds"] = data["DisconnectTimeoutInSeconds"]
    if data.get("IdleDisconnectTimeoutInSeconds") is not None:
        out["idle_disconnect_timeout_in_seconds"] = data[
            "IdleDisconnectTimeoutInSeconds"
        ]
    if data.get("MaxUserDurationInSeconds") is not None:
        out["max_user_duration_in_seconds"] = data["MaxUserDurationInSeconds"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TimeoutSettings) -> dict:
    out: dict = {}
    if "disconnect_timeout_in_seconds" in value:
        out["DisconnectTimeoutInSeconds"] = value["disconnect_timeout_in_seconds"]
    if "idle_disconnect_timeout_in_seconds" in value:
        out["IdleDisconnectTimeoutInSeconds"] = value[
            "idle_disconnect_timeout_in_seconds"
        ]
    if "max_user_duration_in_seconds" in value:
        out["MaxUserDurationInSeconds"] = value["max_user_duration_in_seconds"]
    return out


def deserialize_cbor(data: dict) -> TimeoutSettings:
    out: TimeoutSettings = {}  # type: ignore[typeddict-item]
    if data.get("DisconnectTimeoutInSeconds") is not None:
        out["disconnect_timeout_in_seconds"] = data["DisconnectTimeoutInSeconds"]
    if data.get("IdleDisconnectTimeoutInSeconds") is not None:
        out["idle_disconnect_timeout_in_seconds"] = data[
            "IdleDisconnectTimeoutInSeconds"
        ]
    if data.get("MaxUserDurationInSeconds") is not None:
        out["max_user_duration_in_seconds"] = data["MaxUserDurationInSeconds"]
    return out
