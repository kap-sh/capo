"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#FailedResourcesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.failure_info
    import capo_resource_groups_tagging_api.types.resource_arn

FailedResourcesMap: TypeAlias = dict[
    "capo_resource_groups_tagging_api.types.resource_arn.ResourceARN",
    "capo_resource_groups_tagging_api.types.failure_info.FailureInfo",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FailedResourcesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_resource_groups_tagging_api.types.failure_info

        out[key] = (
            capo_resource_groups_tagging_api.types.failure_info.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedResourcesMap:
    out: FailedResourcesMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_resource_groups_tagging_api.types.failure_info

        out[key] = (
            capo_resource_groups_tagging_api.types.failure_info.deserialize_aws_json_1_1(
                value
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: FailedResourcesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_resource_groups_tagging_api.types.failure_info

        out[key] = capo_resource_groups_tagging_api.types.failure_info.serialize_cbor(
            value
        )
    return out


def deserialize_cbor(data: dict) -> FailedResourcesMap:
    out: FailedResourcesMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_resource_groups_tagging_api.types.failure_info

        out[key] = capo_resource_groups_tagging_api.types.failure_info.deserialize_cbor(
            value
        )
    return out
