"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExternalMetricsSource``."""

from typing import Literal, TypeAlias, cast

ExternalMetricsSource: TypeAlias = Literal[
    "Datadog",
    "Dynatrace",
    "NewRelic",
    "Instana",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExternalMetricsSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExternalMetricsSource:
    return cast(ExternalMetricsSource, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExternalMetricsSource) -> str:
    return value


def deserialize_cbor(data: str) -> ExternalMetricsSource:
    return cast(ExternalMetricsSource, data)
