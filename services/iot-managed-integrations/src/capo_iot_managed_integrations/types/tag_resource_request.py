"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#TagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.io_t_managed_integrations_resource_arn
    import capo_iot_managed_integrations.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_iot_managed_integrations.types.io_t_managed_integrations_resource_arn.IoTManagedIntegrationsResourceARN"
    """<p>The Amazon Resource Name (ARN) of the resource to which to add tags.</p>"""
    tags: "capo_iot_managed_integrations.types.tags_map.TagsMap"
    """<p>A set of key/value pairs that are used to manage the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_iot_managed_integrations.types.tags_map

    out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    else:
        out["tags"] = {}
    return out


def redact_sensitive(value: TagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
