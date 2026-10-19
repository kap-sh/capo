"""Generated from Smithy shape ``com.amazonaws.connect#MediaConcurrency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.channel
    import capo_connect.types.concurrency
    import capo_connect.types.cross_channel_behavior
    import capo_connect.types.workload_type_concurrencies


class MediaConcurrency(TypedDict, closed=True):
    channel: "capo_connect.types.channel.Channel"
    """<p>The channels that agents can handle in the Contact Control Panel (CCP).</p>"""
    concurrency: "capo_connect.types.concurrency.Concurrency"
    """<p>The number of contacts an agent can have on a channel simultaneously.</p> <p>Valid Range for <code>VOICE</code>: Minimum value of 1. Maximum value of 1.</p> <p>Valid Range for <code>CHAT</code>: Minimum value of 1. Maximum value of 10.</p> <p>Valid Range for <code>TASK</code>: Minimum value of 1. Maximum value of 10.</p>"""
    cross_channel_behavior: NotRequired[
        "capo_connect.types.cross_channel_behavior.CrossChannelBehavior"
    ]
    """<p>Defines the cross-channel routing behavior for each channel that is enabled for this Routing Profile. For example, this allows you to offer an agent a different contact from another channel when they are currently working with a contact from a Voice channel.</p>"""
    workload_type_concurrencies: NotRequired[
        "capo_connect.types.workload_type_concurrencies.WorkloadTypeConcurrencies"
    ]
    """<p>Defines the list of workload type concurrency configurations for a channel. When provided, enables granular concurrency control based on workload type values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaConcurrency) -> dict:
    out: dict = {}
    import capo_connect.types.channel

    out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    out["Concurrency"] = value.get("concurrency", 0)
    if "cross_channel_behavior" in value:
        import capo_connect.types.cross_channel_behavior

        out["CrossChannelBehavior"] = (
            capo_connect.types.cross_channel_behavior.serialize_json(
                value["cross_channel_behavior"]
            )
        )
    if "workload_type_concurrencies" in value:
        import capo_connect.types.workload_type_concurrencies

        out["WorkloadTypeConcurrencies"] = (
            capo_connect.types.workload_type_concurrencies.serialize_json(
                value["workload_type_concurrencies"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaConcurrency:
    out: MediaConcurrency = {}  # type: ignore[typeddict-item]
    if data.get("Channel") is not None:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    else:
        import typing

        out["channel"] = typing.cast("capo_connect.types.channel.Channel", "")
    if data.get("Concurrency") is not None:
        out["concurrency"] = data["Concurrency"]
    else:
        out["concurrency"] = 0
    if data.get("CrossChannelBehavior") is not None:
        import capo_connect.types.cross_channel_behavior

        out["cross_channel_behavior"] = (
            capo_connect.types.cross_channel_behavior.deserialize_json(
                data["CrossChannelBehavior"]
            )
        )
    if data.get("WorkloadTypeConcurrencies") is not None:
        import capo_connect.types.workload_type_concurrencies

        out["workload_type_concurrencies"] = (
            capo_connect.types.workload_type_concurrencies.deserialize_json(
                data["WorkloadTypeConcurrencies"]
            )
        )
    return out
