"""Generated from Smithy shape ``com.amazonaws.pipes#PipeSourceRabbitMQBrokerParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.limit_max10000
    import capo_pipes.types.maximum_batching_window_in_seconds
    import capo_pipes.types.mq_broker_access_credentials
    import capo_pipes.types.mq_broker_queue_name
    import capo_pipes.types.uri


class PipeSourceRabbitMQBrokerParameters(TypedDict, closed=True):
    credentials: (
        "capo_pipes.types.mq_broker_access_credentials.MQBrokerAccessCredentials"
    )
    """<p>The credentials needed to access the resource.</p>"""
    queue_name: "capo_pipes.types.mq_broker_queue_name.MQBrokerQueueName"
    """<p>The name of the destination queue to consume.</p>"""
    virtual_host: NotRequired["capo_pipes.types.uri.URI"]
    """<p>The name of the virtual host associated with the source broker.</p>"""
    batch_size: NotRequired["capo_pipes.types.limit_max10000.LimitMax10000"]
    """<p>The maximum number of records to include in each batch.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "capo_pipes.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum length of a time to wait for events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeSourceRabbitMQBrokerParameters) -> dict:
    out: dict = {}
    import capo_pipes.types.mq_broker_access_credentials

    out["Credentials"] = capo_pipes.types.mq_broker_access_credentials.serialize_json(
        value["credentials"]
    )
    out["QueueName"] = value["queue_name"]
    if "virtual_host" in value:
        out["VirtualHost"] = value["virtual_host"]
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    return out


def deserialize_json(data: dict) -> PipeSourceRabbitMQBrokerParameters:
    out: PipeSourceRabbitMQBrokerParameters = {}  # type: ignore[typeddict-item]
    if data.get("Credentials") is not None:
        import capo_pipes.types.mq_broker_access_credentials

        out["credentials"] = (
            capo_pipes.types.mq_broker_access_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    else:
        out["credentials"] = {"$unknown": {"name": ""}}
    if data.get("QueueName") is not None:
        out["queue_name"] = data["QueueName"]
    else:
        out["queue_name"] = ""
    if data.get("VirtualHost") is not None:
        out["virtual_host"] = data["VirtualHost"]
    if data.get("BatchSize") is not None:
        out["batch_size"] = data["BatchSize"]
    if data.get("MaximumBatchingWindowInSeconds") is not None:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    return out


def redact_sensitive(value: PipeSourceRabbitMQBrokerParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "queue_name" in value:
        out["queue_name"] = "*** Sensitive Data Redacted ***"
    if "virtual_host" in value:
        out["virtual_host"] = "*** Sensitive Data Redacted ***"
    return out
