"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateRemoteSourceActionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.arn
    import capo_mgn.types.operating_system_string
    import capo_mgn.types.remote_source_action_description
    import capo_mgn.types.remote_source_action_id
    import capo_mgn.types.remote_source_action_name
    import capo_mgn.types.remote_source_action_timeout_seconds
    import capo_mgn.types.ssm_parameter_store_parameter_name
    import capo_mgn.types.tags_map


class UpdateRemoteSourceActionResponse(TypedDict, closed=True):
    remote_source_action_id: NotRequired[
        "capo_mgn.types.remote_source_action_id.RemoteSourceActionID"
    ]
    """<p>The unique identifier of the source action.</p>"""
    arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the source action.</p>"""
    name: NotRequired["capo_mgn.types.remote_source_action_name.RemoteSourceActionName"]
    """<p>The name of the source action.</p>"""
    description: NotRequired[
        "capo_mgn.types.remote_source_action_description.RemoteSourceActionDescription"
    ]
    """<p>A description of the source action.</p>"""
    ssm_parameter_name: NotRequired[
        "capo_mgn.types.ssm_parameter_store_parameter_name.SsmParameterStoreParameterName"
    ]
    """<p>AWS Systems Manager Parameter Store parameter name.</p>"""
    timeout_seconds: NotRequired[
        "capo_mgn.types.remote_source_action_timeout_seconds.RemoteSourceActionTimeoutSeconds"
    ]
    """<p>The maximum time, in seconds, that the script can run on each source server.</p>"""
    operating_system: NotRequired[
        "capo_mgn.types.operating_system_string.OperatingSystemString"
    ]
    """<p>The operating system of the source servers that the script runs on. Absent when the script runs on both Linux and Windows.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Tags assigned to the source action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRemoteSourceActionResponse) -> dict:
    out: dict = {}
    if "remote_source_action_id" in value:
        out["remoteSourceActionID"] = value["remote_source_action_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "ssm_parameter_name" in value:
        out["ssmParameterName"] = value["ssm_parameter_name"]
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    if "operating_system" in value:
        out["operatingSystem"] = value["operating_system"]
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> UpdateRemoteSourceActionResponse:
    out: UpdateRemoteSourceActionResponse = {}  # type: ignore[typeddict-item]
    if data.get("remoteSourceActionID") is not None:
        out["remote_source_action_id"] = data["remoteSourceActionID"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("ssmParameterName") is not None:
        out["ssm_parameter_name"] = data["ssmParameterName"]
    if data.get("timeoutSeconds") is not None:
        out["timeout_seconds"] = data["timeoutSeconds"]
    if data.get("operatingSystem") is not None:
        out["operating_system"] = data["operatingSystem"]
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: UpdateRemoteSourceActionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
