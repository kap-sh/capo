"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateSceneRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.description
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.s3_url
    import capo_iottwinmaker.types.scene_capabilities
    import capo_iottwinmaker.types.scene_metadata_map
    import capo_iottwinmaker.types.tag_map


class CreateSceneRequest(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the scene.</p>"""
    scene_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the scene.</p>"""
    content_location: "capo_iottwinmaker.types.s3_url.S3Url"
    """<p>The relative path that specifies the location of the content definition file.</p>"""
    description: NotRequired["capo_iottwinmaker.types.description.Description"]
    """<p>The description for this scene.</p>"""
    capabilities: NotRequired[
        "capo_iottwinmaker.types.scene_capabilities.SceneCapabilities"
    ]
    """<p>A list of capabilities that the scene uses to render itself.</p>"""
    tags: NotRequired["capo_iottwinmaker.types.tag_map.TagMap"]
    """<p>Metadata that you can use to manage the scene.</p>"""
    scene_metadata: NotRequired[
        "capo_iottwinmaker.types.scene_metadata_map.SceneMetadataMap"
    ]
    """<p>The request metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSceneRequest) -> dict:
    out: dict = {}
    out["sceneId"] = value["scene_id"]
    out["contentLocation"] = value["content_location"]
    if "description" in value:
        out["description"] = value["description"]
    if "capabilities" in value:
        import capo_iottwinmaker.types.scene_capabilities

        out["capabilities"] = capo_iottwinmaker.types.scene_capabilities.serialize_json(
            value["capabilities"]
        )
    if "tags" in value:
        import capo_iottwinmaker.types.tag_map

        out["tags"] = capo_iottwinmaker.types.tag_map.serialize_json(value["tags"])
    if "scene_metadata" in value:
        import capo_iottwinmaker.types.scene_metadata_map

        out["sceneMetadata"] = (
            capo_iottwinmaker.types.scene_metadata_map.serialize_json(
                value["scene_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSceneRequest:
    out: CreateSceneRequest = {}  # type: ignore[typeddict-item]
    if data.get("sceneId") is not None:
        out["scene_id"] = data["sceneId"]
    else:
        out["scene_id"] = ""
    if data.get("contentLocation") is not None:
        out["content_location"] = data["contentLocation"]
    else:
        out["content_location"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("capabilities") is not None:
        import capo_iottwinmaker.types.scene_capabilities

        out["capabilities"] = (
            capo_iottwinmaker.types.scene_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    if data.get("tags") is not None:
        import capo_iottwinmaker.types.tag_map

        out["tags"] = capo_iottwinmaker.types.tag_map.deserialize_json(data["tags"])
    if data.get("sceneMetadata") is not None:
        import capo_iottwinmaker.types.scene_metadata_map

        out["scene_metadata"] = (
            capo_iottwinmaker.types.scene_metadata_map.deserialize_json(
                data["sceneMetadata"]
            )
        )
    return out
