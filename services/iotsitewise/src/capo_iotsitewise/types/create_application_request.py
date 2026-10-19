"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.application_name
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.tag_map
    import capo_iotsitewise.types.workspace_name


class CreateApplicationRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>Unique client token for idempotent request handling</p>"""
    idc_instance_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>Identity Center Instance ARN to create the application in</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>Name of the workspace to associate with the underlying Application</p>"""
    name: "capo_iotsitewise.types.application_name.ApplicationName"
    """<p>Name of the application</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>Description of the application</p>"""
    tags: NotRequired["capo_iotsitewise.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["idcInstanceArn"] = value["idc_instance_arn"]
    out["workspaceName"] = value["workspace_name"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("idcInstanceArn") is not None:
        out["idc_instance_arn"] = data["idcInstanceArn"]
    else:
        out["idc_instance_arn"] = ""
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.deserialize_json(data["tags"])
    return out
