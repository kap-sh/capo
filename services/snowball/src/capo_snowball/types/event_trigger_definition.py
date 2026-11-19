"""Generated from Smithy shape ``com.amazonaws.snowball#EventTriggerDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.resource_arn


class EventTriggerDefinition(TypedDict, closed=True):
    event_resource_arn: NotRequired["capo_snowball.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an Lambda function's event trigger associated with this job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTriggerDefinition) -> dict:
    out: dict = {}
    if "event_resource_arn" in value:
        out["EventResourceARN"] = value["event_resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventTriggerDefinition:
    out: EventTriggerDefinition = {}  # type: ignore[typeddict-item]
    if data.get("EventResourceARN") is not None:
        out["event_resource_arn"] = data["EventResourceARN"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EventTriggerDefinition) -> dict:
    out: dict = {}
    if "event_resource_arn" in value:
        out["EventResourceARN"] = value["event_resource_arn"]
    return out


def deserialize_cbor(data: dict) -> EventTriggerDefinition:
    out: EventTriggerDefinition = {}  # type: ignore[typeddict-item]
    if data.get("EventResourceARN") is not None:
        out["event_resource_arn"] = data["EventResourceARN"]
    return out
