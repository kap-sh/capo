"""Generated from Smithy shape ``com.amazonaws.lightsail#DistributionMetricName``."""

from typing import Literal, TypeAlias, cast

DistributionMetricName: TypeAlias = Literal[
    "Requests",
    "BytesDownloaded",
    "BytesUploaded",
    "TotalErrorRate",
    "Http4xxErrorRate",
    "Http5xxErrorRate",
    "WafAllowedRequests",
    "WafBlockedRequests",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistributionMetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DistributionMetricName:
    return cast(DistributionMetricName, data)
