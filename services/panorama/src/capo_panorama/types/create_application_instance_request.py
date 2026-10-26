"""Generated from Smithy shape ``com.amazonaws.panorama#CreateApplicationInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.application_instance_id
    import capo_panorama.types.application_instance_name
    import capo_panorama.types.default_runtime_context_device
    import capo_panorama.types.description
    import capo_panorama.types.manifest_overrides_payload
    import capo_panorama.types.manifest_payload
    import capo_panorama.types.runtime_role_arn
    import capo_panorama.types.tag_map


class CreateApplicationInstanceRequest(TypedDict, closed=True):
    name: NotRequired[
        "capo_panorama.types.application_instance_name.ApplicationInstanceName"
    ]
    """<p>A name for the application instance.</p>"""
    description: NotRequired["capo_panorama.types.description.Description"]
    """<p>A description for the application instance.</p>"""
    manifest_payload: "capo_panorama.types.manifest_payload.ManifestPayload"
    """<p>The application's manifest document.</p>"""
    manifest_overrides_payload: NotRequired[
        "capo_panorama.types.manifest_overrides_payload.ManifestOverridesPayload"
    ]
    """<p>Setting overrides for the application manifest.</p>"""
    application_instance_id_to_replace: NotRequired[
        "capo_panorama.types.application_instance_id.ApplicationInstanceId"
    ]
    """<p>The ID of an application instance to replace with the new instance.</p>"""
    runtime_role_arn: NotRequired["capo_panorama.types.runtime_role_arn.RuntimeRoleArn"]
    """<p>The ARN of a runtime role for the application instance.</p>"""
    default_runtime_context_device: (
        "capo_panorama.types.default_runtime_context_device.DefaultRuntimeContextDevice"
    )
    """<p>A device's ID.</p>"""
    tags: NotRequired["capo_panorama.types.tag_map.TagMap"]
    """<p>Tags for the application instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationInstanceRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_panorama.types.manifest_payload

    out["ManifestPayload"] = capo_panorama.types.manifest_payload.serialize_json(
        value["manifest_payload"]
    )
    if "manifest_overrides_payload" in value:
        import capo_panorama.types.manifest_overrides_payload

        out["ManifestOverridesPayload"] = (
            capo_panorama.types.manifest_overrides_payload.serialize_json(
                value["manifest_overrides_payload"]
            )
        )
    if "application_instance_id_to_replace" in value:
        out["ApplicationInstanceIdToReplace"] = value[
            "application_instance_id_to_replace"
        ]
    if "runtime_role_arn" in value:
        out["RuntimeRoleArn"] = value["runtime_role_arn"]
    out["DefaultRuntimeContextDevice"] = value["default_runtime_context_device"]
    if "tags" in value:
        import capo_panorama.types.tag_map

        out["Tags"] = capo_panorama.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateApplicationInstanceRequest:
    out: CreateApplicationInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ManifestPayload") is not None:
        import capo_panorama.types.manifest_payload

        out["manifest_payload"] = capo_panorama.types.manifest_payload.deserialize_json(
            data["ManifestPayload"]
        )
    else:
        out["manifest_payload"] = {"$unknown": {"name": ""}}
    if data.get("ManifestOverridesPayload") is not None:
        import capo_panorama.types.manifest_overrides_payload

        out["manifest_overrides_payload"] = (
            capo_panorama.types.manifest_overrides_payload.deserialize_json(
                data["ManifestOverridesPayload"]
            )
        )
    if data.get("ApplicationInstanceIdToReplace") is not None:
        out["application_instance_id_to_replace"] = data[
            "ApplicationInstanceIdToReplace"
        ]
    if data.get("RuntimeRoleArn") is not None:
        out["runtime_role_arn"] = data["RuntimeRoleArn"]
    if data.get("DefaultRuntimeContextDevice") is not None:
        out["default_runtime_context_device"] = data["DefaultRuntimeContextDevice"]
    else:
        out["default_runtime_context_device"] = ""
    if data.get("Tags") is not None:
        import capo_panorama.types.tag_map

        out["tags"] = capo_panorama.types.tag_map.deserialize_json(data["Tags"])
    return out
