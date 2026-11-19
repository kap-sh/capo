"""Generated from Smithy shape ``com.amazonaws.mgn#CreateRemoteSourceActionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.remote_source_action_description
    import capo_mgn.types.remote_source_action_name
    import capo_mgn.types.remote_source_action_operating_system
    import capo_mgn.types.remote_source_action_timeout_seconds
    import capo_mgn.types.ssm_parameter_store_parameter_name
    import capo_mgn.types.tags_map


class CreateRemoteSourceActionRequest(TypedDict, closed=True):
    name: "capo_mgn.types.remote_source_action_name.RemoteSourceActionName"
    """<p>The name of the source action.</p>"""
    description: NotRequired[
        "capo_mgn.types.remote_source_action_description.RemoteSourceActionDescription"
    ]
    """<p>A description of the source action.</p>"""
    ssm_parameter_name: "capo_mgn.types.ssm_parameter_store_parameter_name.SsmParameterStoreParameterName"
    """<p>AWS Systems Manager Parameter Store parameter name.</p>"""
    timeout_seconds: NotRequired[
        "capo_mgn.types.remote_source_action_timeout_seconds.RemoteSourceActionTimeoutSeconds"
    ]
    """<p>The maximum time, in seconds, that the script can run on each source server.</p>"""
    operating_system: NotRequired[
        "capo_mgn.types.remote_source_action_operating_system.RemoteSourceActionOperatingSystem"
    ]
    """<p>The operating system of the source servers that the script runs on. Set to <code>linux</code> or <code>windows</code> to run the script only on source servers with that operating system, or <code>all</code> to run it on both.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Tags to assign to the source action.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRemoteSourceActionRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["ssmParameterName"] = value["ssm_parameter_name"]
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    if "operating_system" in value:
        out["operatingSystem"] = value["operating_system"]
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> CreateRemoteSourceActionRequest:
    out: CreateRemoteSourceActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("ssmParameterName") is not None:
        out["ssm_parameter_name"] = data["ssmParameterName"]
    else:
        out["ssm_parameter_name"] = ""
    if data.get("timeoutSeconds") is not None:
        out["timeout_seconds"] = data["timeoutSeconds"]
    if data.get("operatingSystem") is not None:
        out["operating_system"] = data["operatingSystem"]
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out


def redact_sensitive(value: CreateRemoteSourceActionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
