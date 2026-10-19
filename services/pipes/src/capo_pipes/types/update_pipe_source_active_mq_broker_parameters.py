"""Generated from Smithy shape ``com.amazonaws.pipes#UpdatePipeSourceActiveMQBrokerParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.limit_max10000
    import capo_pipes.types.maximum_batching_window_in_seconds
    import capo_pipes.types.mq_broker_access_credentials


class UpdatePipeSourceActiveMQBrokerParameters(TypedDict, closed=True):
    credentials: (
        "capo_pipes.types.mq_broker_access_credentials.MQBrokerAccessCredentials"
    )
    """<p>The credentials needed to access the resource.</p>"""
    batch_size: NotRequired["capo_pipes.types.limit_max10000.LimitMax10000"]
    """<p>The maximum number of records to include in each batch.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "capo_pipes.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum length of a time to wait for events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePipeSourceActiveMQBrokerParameters) -> dict:
    out: dict = {}
    import capo_pipes.types.mq_broker_access_credentials

    out["Credentials"] = capo_pipes.types.mq_broker_access_credentials.serialize_json(
        value["credentials"]
    )
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    return out


def deserialize_json(data: dict) -> UpdatePipeSourceActiveMQBrokerParameters:
    out: UpdatePipeSourceActiveMQBrokerParameters = {}  # type: ignore[typeddict-item]
    if data.get("Credentials") is not None:
        import capo_pipes.types.mq_broker_access_credentials

        out["credentials"] = (
            capo_pipes.types.mq_broker_access_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    else:
        import capo_pipes.types._unknown

        out["credentials"] = capo_pipes.types._unknown.UnknownUnionMember("")
    if data.get("BatchSize") is not None:
        out["batch_size"] = data["BatchSize"]
    if data.get("MaximumBatchingWindowInSeconds") is not None:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    return out
