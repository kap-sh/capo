"""Generated from Smithy shape ``com.amazonaws.mgn#StartRemoteSourceActionJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.client_idempotency_token
    import capo_mgn.types.connector_arn
    import capo_mgn.types.remote_source_action_arns
    import capo_mgn.types.source_server_arns
    import capo_mgn.types.tags_map


class StartRemoteSourceActionJobRequest(TypedDict, closed=True):
    remote_source_action_arns: (
        "capo_mgn.types.remote_source_action_arns.RemoteSourceActionArns"
    )
    """<p>The ARNs of the source actions to run.</p>"""
    connector_arn: "capo_mgn.types.connector_arn.ConnectorArn"
    """<p>The ARN of the connector that runs the source actions.</p>"""
    source_server_arns: "capo_mgn.types.source_server_arns.SourceServerArns"
    """<p>The ARNs of the source servers to run the source actions on.</p>"""
    client_token: NotRequired[
        "capo_mgn.types.client_idempotency_token.ClientIdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Tags to assign to the job.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRemoteSourceActionJobRequest) -> dict:
    out: dict = {}
    import capo_mgn.types.remote_source_action_arns

    out["remoteSourceActionArns"] = (
        capo_mgn.types.remote_source_action_arns.serialize_json(
            value["remote_source_action_arns"]
        )
    )
    out["connectorArn"] = value["connector_arn"]
    import capo_mgn.types.source_server_arns

    out["sourceServerArns"] = capo_mgn.types.source_server_arns.serialize_json(
        value["source_server_arns"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> StartRemoteSourceActionJobRequest:
    out: StartRemoteSourceActionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("remoteSourceActionArns") is not None:
        import capo_mgn.types.remote_source_action_arns

        out["remote_source_action_arns"] = (
            capo_mgn.types.remote_source_action_arns.deserialize_json(
                data["remoteSourceActionArns"]
            )
        )
    else:
        out["remote_source_action_arns"] = []
    if data.get("connectorArn") is not None:
        out["connector_arn"] = data["connectorArn"]
    else:
        out["connector_arn"] = ""
    if data.get("sourceServerArns") is not None:
        import capo_mgn.types.source_server_arns

        out["source_server_arns"] = capo_mgn.types.source_server_arns.deserialize_json(
            data["sourceServerArns"]
        )
    else:
        out["source_server_arns"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out


def redact_sensitive(value: StartRemoteSourceActionJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
