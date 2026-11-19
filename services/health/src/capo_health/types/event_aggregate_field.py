"""Generated from Smithy shape ``com.amazonaws.health#eventAggregateField``."""

from typing import Literal, TypeAlias, cast

eventAggregateField: TypeAlias = Literal["eventTypeCategory",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: eventAggregateField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> eventAggregateField:
    return cast(eventAggregateField, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: eventAggregateField) -> str:
    return value


def deserialize_cbor(data: str) -> eventAggregateField:
    return cast(eventAggregateField, data)
