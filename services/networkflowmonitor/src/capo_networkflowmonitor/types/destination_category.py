"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#DestinationCategory``."""

from typing import Literal, TypeAlias, cast

DestinationCategory: TypeAlias = Literal[
    "INTRA_AZ",
    "INTER_AZ",
    "INTER_VPC",
    "UNCLASSIFIED",
    "AMAZON_S3",
    "AMAZON_DYNAMODB",
    "INTER_REGION",
    "INTERNET",
    "AWS_SERVICE",
    "LOCAL_ZONE",
    "TRANSIT_GATEWAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationCategory) -> str:
    return value


def deserialize_json(data: str) -> DestinationCategory:
    return cast(DestinationCategory, data)
