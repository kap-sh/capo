"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ResumeConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string


class ResumeConnectorRequest(TypedDict, closed=True):
    connector_arn: "capo_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the connector that you want to resume.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResumeConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ResumeConnectorRequest:
    out: ResumeConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
