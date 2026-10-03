"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.tag_map


class CreateProjectRequest(TypedDict, closed=True):
    portal_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the portal in which to create the project.</p>"""
    project_name: "capo_iotsitewise.types.name.Name"
    """<p>A friendly name for the project.</p>"""
    project_description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>A description for the project.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    tags: NotRequired["capo_iotsitewise.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the project. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectRequest) -> dict:
    out: dict = {}
    out["portalId"] = value["portal_id"]
    out["projectName"] = value["project_name"]
    if "project_description" in value:
        out["projectDescription"] = value["project_description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateProjectRequest:
    out: CreateProjectRequest = {}  # type: ignore[typeddict-item]
    if data.get("portalId") is not None:
        out["portal_id"] = data["portalId"]
    else:
        raise DeserializationError("CreateProjectRequest.portal_id required")
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("CreateProjectRequest.project_name required")
    if data.get("projectDescription") is not None:
        out["project_description"] = data["projectDescription"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.deserialize_json(data["tags"])
    return out
