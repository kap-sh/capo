"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionQueueLogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.log_delivery_destination_list


class GameSessionQueueLogConfiguration(TypedDict, closed=True):
    delivery_destinations: NotRequired[
        "capo_gamelift.types.log_delivery_destination_list.LogDeliveryDestinationList"
    ]
    """<p>The destinations that receive game session placement insight logs for the queue. You can specify up to 3 destinations. Each destination must have a unique ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionQueueLogConfiguration) -> dict:
    out: dict = {}
    if "delivery_destinations" in value:
        import capo_gamelift.types.log_delivery_destination_list

        out["DeliveryDestinations"] = (
            capo_gamelift.types.log_delivery_destination_list.serialize_aws_json_1_1(
                value["delivery_destinations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GameSessionQueueLogConfiguration:
    out: GameSessionQueueLogConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryDestinations") is not None:
        import capo_gamelift.types.log_delivery_destination_list

        out["delivery_destinations"] = (
            capo_gamelift.types.log_delivery_destination_list.deserialize_aws_json_1_1(
                data["DeliveryDestinations"]
            )
        )
    return out
