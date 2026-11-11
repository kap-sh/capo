"""Generated from Smithy shape ``com.amazonaws.gamelift#LogDeliveryDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.log_delivery_destination

LogDeliveryDestinationList: TypeAlias = list[
    "capo_gamelift.types.log_delivery_destination.LogDeliveryDestination"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogDeliveryDestinationList) -> list:
    import capo_gamelift.types.log_delivery_destination

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.log_delivery_destination.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LogDeliveryDestinationList:
    import capo_gamelift.types.log_delivery_destination

    out: LogDeliveryDestinationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.log_delivery_destination.deserialize_aws_json_1_1(item)
        )
    return out
