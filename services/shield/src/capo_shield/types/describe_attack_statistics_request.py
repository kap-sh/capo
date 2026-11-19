"""Generated from Smithy shape ``com.amazonaws.shield#DescribeAttackStatisticsRequest``."""

from typing_extensions import TypedDict


class DescribeAttackStatisticsRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAttackStatisticsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAttackStatisticsRequest:
    out: DescribeAttackStatisticsRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAttackStatisticsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DescribeAttackStatisticsRequest:
    out: DescribeAttackStatisticsRequest = {}  # type: ignore[typeddict-item]
    return out
