"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.customization_feature
    import capo_rekognition.types.project_auto_update
    import capo_rekognition.types.project_name
    import capo_rekognition.types.tag_map


class CreateProjectRequest(TypedDict, closed=True):
    project_name: "capo_rekognition.types.project_name.ProjectName"
    """<p>The name of the project to create.</p>"""
    feature: NotRequired[
        "capo_rekognition.types.customization_feature.CustomizationFeature"
    ]
    """<p>Specifies feature that is being customized. If no value is provided CUSTOM_LABELS is used as a default.</p>"""
    auto_update: NotRequired[
        "capo_rekognition.types.project_auto_update.ProjectAutoUpdate"
    ]
    """<p>Specifies whether automatic retraining should be attempted for the versions of the project. Automatic retraining is done as a best effort. Required argument for Content Moderation. Applicable only to adapters.</p>"""
    tags: NotRequired["capo_rekognition.types.tag_map.TagMap"]
    """<p>A set of tags (key-value pairs) that you want to attach to the project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProjectRequest) -> dict:
    out: dict = {}
    out["ProjectName"] = value["project_name"]
    if "feature" in value:
        import capo_rekognition.types.customization_feature

        out["Feature"] = (
            capo_rekognition.types.customization_feature.serialize_aws_json_1_1(
                value["feature"]
            )
        )
    if "auto_update" in value:
        import capo_rekognition.types.project_auto_update

        out["AutoUpdate"] = (
            capo_rekognition.types.project_auto_update.serialize_aws_json_1_1(
                value["auto_update"]
            )
        )
    if "tags" in value:
        import capo_rekognition.types.tag_map

        out["Tags"] = capo_rekognition.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProjectRequest:
    out: CreateProjectRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProjectName") is not None:
        out["project_name"] = data["ProjectName"]
    else:
        out["project_name"] = ""
    if data.get("Feature") is not None:
        import capo_rekognition.types.customization_feature

        out["feature"] = (
            capo_rekognition.types.customization_feature.deserialize_aws_json_1_1(
                data["Feature"]
            )
        )
    if data.get("AutoUpdate") is not None:
        import capo_rekognition.types.project_auto_update

        out["auto_update"] = (
            capo_rekognition.types.project_auto_update.deserialize_aws_json_1_1(
                data["AutoUpdate"]
            )
        )
    if data.get("Tags") is not None:
        import capo_rekognition.types.tag_map

        out["tags"] = capo_rekognition.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
