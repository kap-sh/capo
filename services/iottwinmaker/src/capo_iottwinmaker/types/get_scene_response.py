"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetSceneResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.description
    import capo_iottwinmaker.types.generated_scene_metadata_map
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.s3_url
    import capo_iottwinmaker.types.scene_capabilities
    import capo_iottwinmaker.types.scene_error
    import capo_iottwinmaker.types.scene_metadata_map
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class GetSceneResponse(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the scene.</p>"""
    scene_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the scene.</p>"""
    content_location: "capo_iottwinmaker.types.s3_url.S3Url"
    """<p>The relative path that specifies the location of the content definition file.</p>"""
    arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the scene.</p>"""
    creation_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the scene was created.</p>"""
    update_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the scene was last updated.</p>"""
    description: NotRequired["capo_iottwinmaker.types.description.Description"]
    """<p>The description of the scene.</p>"""
    capabilities: NotRequired[
        "capo_iottwinmaker.types.scene_capabilities.SceneCapabilities"
    ]
    """<p>A list of capabilities that the scene uses to render.</p>"""
    scene_metadata: NotRequired[
        "capo_iottwinmaker.types.scene_metadata_map.SceneMetadataMap"
    ]
    """<p>The response metadata.</p>"""
    generated_scene_metadata: NotRequired[
        "capo_iottwinmaker.types.generated_scene_metadata_map.GeneratedSceneMetadataMap"
    ]
    """<p>The generated scene metadata.</p>"""
    error: NotRequired["capo_iottwinmaker.types.scene_error.SceneError"]
    """<p>The SceneResponse error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSceneResponse) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    out["sceneId"] = value["scene_id"]
    out["contentLocation"] = value["content_location"]
    out["arn"] = value["arn"]
    import capo_iottwinmaker.types.timestamp

    out["creationDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import capo_iottwinmaker.types.timestamp

    out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "capabilities" in value:
        import capo_iottwinmaker.types.scene_capabilities

        out["capabilities"] = capo_iottwinmaker.types.scene_capabilities.serialize_json(
            value["capabilities"]
        )
    if "scene_metadata" in value:
        import capo_iottwinmaker.types.scene_metadata_map

        out["sceneMetadata"] = (
            capo_iottwinmaker.types.scene_metadata_map.serialize_json(
                value["scene_metadata"]
            )
        )
    if "generated_scene_metadata" in value:
        import capo_iottwinmaker.types.generated_scene_metadata_map

        out["generatedSceneMetadata"] = (
            capo_iottwinmaker.types.generated_scene_metadata_map.serialize_json(
                value["generated_scene_metadata"]
            )
        )
    if "error" in value:
        import capo_iottwinmaker.types.scene_error

        out["error"] = capo_iottwinmaker.types.scene_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> GetSceneResponse:
    out: GetSceneResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("sceneId") is not None:
        out["scene_id"] = data["sceneId"]
    else:
        out["scene_id"] = ""
    if data.get("contentLocation") is not None:
        out["content_location"] = data["contentLocation"]
    else:
        out["content_location"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("creationDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["creation_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    else:
        import datetime

        out["creation_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["update_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        import datetime

        out["update_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("capabilities") is not None:
        import capo_iottwinmaker.types.scene_capabilities

        out["capabilities"] = (
            capo_iottwinmaker.types.scene_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    if data.get("sceneMetadata") is not None:
        import capo_iottwinmaker.types.scene_metadata_map

        out["scene_metadata"] = (
            capo_iottwinmaker.types.scene_metadata_map.deserialize_json(
                data["sceneMetadata"]
            )
        )
    if data.get("generatedSceneMetadata") is not None:
        import capo_iottwinmaker.types.generated_scene_metadata_map

        out["generated_scene_metadata"] = (
            capo_iottwinmaker.types.generated_scene_metadata_map.deserialize_json(
                data["generatedSceneMetadata"]
            )
        )
    if data.get("error") is not None:
        import capo_iottwinmaker.types.scene_error

        out["error"] = capo_iottwinmaker.types.scene_error.deserialize_json(
            data["error"]
        )
    return out
