"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExternalMetricStatusCode``."""

from typing import Literal, TypeAlias, cast

ExternalMetricStatusCode: TypeAlias = Literal[
    "NO_EXTERNAL_METRIC_SET",
    "INTEGRATION_SUCCESS",
    "DATADOG_INTEGRATION_ERROR",
    "DYNATRACE_INTEGRATION_ERROR",
    "NEWRELIC_INTEGRATION_ERROR",
    "INSTANA_INTEGRATION_ERROR",
    "INSUFFICIENT_DATADOG_METRICS",
    "INSUFFICIENT_DYNATRACE_METRICS",
    "INSUFFICIENT_NEWRELIC_METRICS",
    "INSUFFICIENT_INSTANA_METRICS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExternalMetricStatusCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExternalMetricStatusCode:
    return cast(ExternalMetricStatusCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExternalMetricStatusCode) -> str:
    return value


def deserialize_cbor(data: str) -> ExternalMetricStatusCode:
    return cast(ExternalMetricStatusCode, data)
