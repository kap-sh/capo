"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ResourceRequestStatusSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cloudcontrol.types.progress_event

ResourceRequestStatusSummaries: TypeAlias = list[
    "capo_cloudcontrol.types.progress_event.ProgressEvent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceRequestStatusSummaries) -> list:
    import capo_cloudcontrol.types.progress_event

    out: list = []
    for item in value:
        out.append(capo_cloudcontrol.types.progress_event.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceRequestStatusSummaries:
    import capo_cloudcontrol.types.progress_event

    out: ResourceRequestStatusSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudcontrol.types.progress_event.deserialize_aws_json_1_0(item)
        )
    return out


def redact_sensitive(value: ResourceRequestStatusSummaries) -> list[Any]:
    import capo_cloudcontrol.types.progress_event

    return [
        capo_cloudcontrol.types.progress_event.redact_sensitive(item) for item in value
    ]
