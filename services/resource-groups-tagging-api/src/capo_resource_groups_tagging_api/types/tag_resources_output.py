"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#TagResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.failed_resources_map


class TagResourcesOutput(TypedDict, closed=True):
    failed_resources_map: NotRequired[
        "capo_resource_groups_tagging_api.types.failed_resources_map.FailedResourcesMap"
    ]
    """<p>A map containing a key-value pair for each failed item that couldn't be tagged. The key is the ARN of the failed resource. The value is a <code>FailureInfo</code> object that contains an error code, a status code, and an error message. If there are no errors, the <code>FailedResourcesMap</code> is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourcesOutput) -> dict:
    out: dict = {}
    if "failed_resources_map" in value:
        import capo_resource_groups_tagging_api.types.failed_resources_map

        out["FailedResourcesMap"] = (
            capo_resource_groups_tagging_api.types.failed_resources_map.serialize_aws_json_1_1(
                value["failed_resources_map"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourcesOutput:
    out: TagResourcesOutput = {}  # type: ignore[typeddict-item]
    if data.get("FailedResourcesMap") is not None:
        import capo_resource_groups_tagging_api.types.failed_resources_map

        out["failed_resources_map"] = (
            capo_resource_groups_tagging_api.types.failed_resources_map.deserialize_aws_json_1_1(
                data["FailedResourcesMap"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagResourcesOutput) -> dict:
    out: dict = {}
    if "failed_resources_map" in value:
        import capo_resource_groups_tagging_api.types.failed_resources_map

        out["FailedResourcesMap"] = (
            capo_resource_groups_tagging_api.types.failed_resources_map.serialize_cbor(
                value["failed_resources_map"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> TagResourcesOutput:
    out: TagResourcesOutput = {}  # type: ignore[typeddict-item]
    if data.get("FailedResourcesMap") is not None:
        import capo_resource_groups_tagging_api.types.failed_resources_map

        out["failed_resources_map"] = (
            capo_resource_groups_tagging_api.types.failed_resources_map.deserialize_cbor(
                data["FailedResourcesMap"]
            )
        )
    return out
