"""Generated from Smithy shape ``com.amazonaws.eventbridge#ReplayDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.arn
    import capo_eventbridge.types.replay_destination_filters


class ReplayDestination(TypedDict, closed=True):
    arn: "capo_eventbridge.types.arn.Arn"
    """<p>The ARN of the event bus to replay event to. You can replay events only to the event bus specified to create the archive.</p>"""
    filter_arns: NotRequired[
        "capo_eventbridge.types.replay_destination_filters.ReplayDestinationFilters"
    ]
    """<p>A list of ARNs for rules to replay events to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplayDestination) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "filter_arns" in value:
        import capo_eventbridge.types.replay_destination_filters

        out["FilterArns"] = (
            capo_eventbridge.types.replay_destination_filters.serialize_aws_json_1_1(
                value["filter_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplayDestination:
    out: ReplayDestination = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("FilterArns") is not None:
        import capo_eventbridge.types.replay_destination_filters

        out["filter_arns"] = (
            capo_eventbridge.types.replay_destination_filters.deserialize_aws_json_1_1(
                data["FilterArns"]
            )
        )
    return out
