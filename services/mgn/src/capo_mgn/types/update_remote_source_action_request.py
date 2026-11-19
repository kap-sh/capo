"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateRemoteSourceActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.remote_source_action_description
    import capo_mgn.types.remote_source_action_id
    import capo_mgn.types.remote_source_action_name
    import capo_mgn.types.remote_source_action_operating_system
    import capo_mgn.types.remote_source_action_timeout_seconds
    import capo_mgn.types.ssm_parameter_store_parameter_name


class UpdateRemoteSourceActionRequest(TypedDict, closed=True):
    remote_source_action_id: (
        "capo_mgn.types.remote_source_action_id.RemoteSourceActionID"
    )
    """<p>The unique identifier of the source action to update.</p>"""
    name: NotRequired["capo_mgn.types.remote_source_action_name.RemoteSourceActionName"]
    """<p>The updated name of the source action.</p>"""
    description: NotRequired[
        "capo_mgn.types.remote_source_action_description.RemoteSourceActionDescription"
    ]
    """<p>The updated description of the source action.</p>"""
    ssm_parameter_name: NotRequired[
        "capo_mgn.types.ssm_parameter_store_parameter_name.SsmParameterStoreParameterName"
    ]
    """<p>AWS Systems Manager Parameter Store parameter name.</p>"""
    timeout_seconds: NotRequired[
        "capo_mgn.types.remote_source_action_timeout_seconds.RemoteSourceActionTimeoutSeconds"
    ]
    """<p>The updated maximum time, in seconds, that the script can run on each source server.</p>"""
    operating_system: NotRequired[
        "capo_mgn.types.remote_source_action_operating_system.RemoteSourceActionOperatingSystem"
    ]
    """<p>The updated operating system of the source servers that the script runs on. Set to <code>linux</code> or <code>windows</code> to run the script only on source servers with that operating system, or <code>all</code> to run it on both.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRemoteSourceActionRequest) -> dict:
    out: dict = {}
    out["remoteSourceActionID"] = value["remote_source_action_id"]
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
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> UpdateRemoteSourceActionRequest:
    out: UpdateRemoteSourceActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("remoteSourceActionID") is not None:
        out["remote_source_action_id"] = data["remoteSourceActionID"]
    else:
        out["remote_source_action_id"] = ""
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
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out
