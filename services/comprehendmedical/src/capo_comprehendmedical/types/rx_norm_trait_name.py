"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormTraitName``."""

from typing import Literal, TypeAlias, cast

RxNormTraitName: TypeAlias = Literal[
    "NEGATION",
    "PAST_HISTORY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormTraitName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RxNormTraitName:
    return cast(RxNormTraitName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RxNormTraitName) -> str:
    return value


def deserialize_cbor(data: str) -> RxNormTraitName:
    return cast(RxNormTraitName, data)
