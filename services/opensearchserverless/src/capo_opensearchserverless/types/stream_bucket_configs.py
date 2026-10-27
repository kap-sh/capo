"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#StreamBucketConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.stream_bucket_config

StreamBucketConfigs: TypeAlias = list[
    "capo_opensearchserverless.types.stream_bucket_config.StreamBucketConfig"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StreamBucketConfigs) -> list:
    import capo_opensearchserverless.types.stream_bucket_config

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.stream_bucket_config.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StreamBucketConfigs:
    import capo_opensearchserverless.types.stream_bucket_config

    out: StreamBucketConfigs = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_opensearchserverless.types.stream_bucket_config.deserialize_aws_json_1_0(
                item
            )
        )
    return out
