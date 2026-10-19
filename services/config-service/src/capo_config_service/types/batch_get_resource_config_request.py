"""Generated from Smithy shape ``com.amazonaws.configservice#BatchGetResourceConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.resource_keys


class BatchGetResourceConfigRequest(TypedDict, closed=True):
    resource_keys: "capo_config_service.types.resource_keys.ResourceKeys"
    """<p>A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetResourceConfigRequest) -> dict:
    out: dict = {}
    import capo_config_service.types.resource_keys

    out["resourceKeys"] = (
        capo_config_service.types.resource_keys.serialize_aws_json_1_1(
            value["resource_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetResourceConfigRequest:
    out: BatchGetResourceConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceKeys") is not None:
        import capo_config_service.types.resource_keys

        out["resource_keys"] = (
            capo_config_service.types.resource_keys.deserialize_aws_json_1_1(
                data["resourceKeys"]
            )
        )
    else:
        out["resource_keys"] = []
    return out
