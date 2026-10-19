"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#RestartConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__boolean
    import capo_kafkaconnect.types.__string


class RestartConnectorRequest(TypedDict, closed=True):
    connector_arn: "capo_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the connector that you want to restart.</p>"""
    only_failed_tasks: NotRequired["capo_kafkaconnect.types.__boolean.__boolean"]
    """<p>Specifies whether to restart only the connector's failed tasks. If <code>true</code>, the operation restarts only the tasks that are currently in a failed state, and healthy tasks continue running. If <code>false</code> or not specified, the operation restarts the connector and all of its tasks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestartConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RestartConnectorRequest:
    out: RestartConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
