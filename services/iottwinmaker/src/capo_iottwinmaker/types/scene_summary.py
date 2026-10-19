"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SceneSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.description
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.s3_url
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class SceneSummary(TypedDict, closed=True):
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
    """<p>The scene description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SceneSummary) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> SceneSummary:
    out: SceneSummary = {}  # type: ignore[typeddict-item]
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
    return out
