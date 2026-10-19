"""Generated from Smithy shape ``com.amazonaws.omics#CreateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.configuration_description
    import capo_omics.types.configuration_name
    import capo_omics.types.configuration_request_id
    import capo_omics.types.run_configurations
    import capo_omics.types.tag_map


class CreateConfigurationRequest(TypedDict, closed=True):
    name: "capo_omics.types.configuration_name.ConfigurationName"
    """<p>User-friendly name for the configuration.</p>"""
    description: NotRequired[
        "capo_omics.types.configuration_description.ConfigurationDescription"
    ]
    """<p>Optional description for the configuration.</p>"""
    run_configurations: "capo_omics.types.run_configurations.RunConfigurations"
    """<p>Required run-specific configurations.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>Optional tags for the configuration.</p>"""
    request_id: "capo_omics.types.configuration_request_id.ConfigurationRequestId"
    """<p>Optional request idempotency token. If not specified, a universally unique identifier (UUID) will be automatically generated for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_omics.types.run_configurations

    out["runConfigurations"] = capo_omics.types.run_configurations.serialize_json(
        value["run_configurations"]
    )
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    out["requestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateConfigurationRequest:
    out: CreateConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("runConfigurations") is not None:
        import capo_omics.types.run_configurations

        out["run_configurations"] = (
            capo_omics.types.run_configurations.deserialize_json(
                data["runConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConfigurationRequest.run_configurations required"
        )
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    else:
        out["request_id"] = ""
    return out
