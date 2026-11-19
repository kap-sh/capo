"""Generated from Smithy shape ``com.amazonaws.emrserverless#FlexExecution``."""

from typing_extensions import NotRequired, TypedDict


class FlexExecution(TypedDict, closed=True):
    enabled: NotRequired["bool"]
    """<p>Enables Amazon EMR Serverless Flex capacity for the job run and defaults to false. If set to true, the job run uses Flex capacity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlexExecution) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> FlexExecution:
    out: FlexExecution = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    return out
