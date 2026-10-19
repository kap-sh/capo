"""Generated from Smithy shape ``com.amazonaws.opensearch#AttachDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.arn
    import capo_opensearch.types.client_token
    import capo_opensearch.types.id
    import capo_opensearch.types.string
    import capo_opensearch.types.workspace_configuration_input


class AttachDataSourceRequest(TypedDict, closed=True):
    id: "capo_opensearch.types.id.Id"
    """<p>The unique identifier or name of the OpenSearch application to attach the data source to. This is the same identifier used with <code>UpdateApplication</code>, <code>GetApplication</code>, and <code>DeleteApplication</code>.</p>"""
    data_source_arn: "capo_opensearch.types.arn.ARN"
    workspace_id: NotRequired["capo_opensearch.types.string.String"]
    """<p>The identifier of an existing workspace to update with the new data source. Mutually exclusive with <code>workspaceConfiguration</code>.</p>"""
    workspace_configuration: NotRequired[
        "capo_opensearch.types.workspace_configuration_input.WorkspaceConfigurationInput"
    ]
    """<p>Configuration for creating a new workspace during the attachment. If specified, a workspace is created and linked to the data source after the attachment completes. Mutually exclusive with <code>workspaceId</code>.</p>"""
    client_token: NotRequired["capo_opensearch.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. If you retry a request with the same client token and the same parameters, the retry succeeds without performing any further actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachDataSourceRequest) -> dict:
    out: dict = {}
    out["dataSourceArn"] = value["data_source_arn"]
    if "workspace_id" in value:
        out["workspaceId"] = value["workspace_id"]
    if "workspace_configuration" in value:
        import capo_opensearch.types.workspace_configuration_input

        out["workspaceConfiguration"] = (
            capo_opensearch.types.workspace_configuration_input.serialize_json(
                value["workspace_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AttachDataSourceRequest:
    out: AttachDataSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("dataSourceArn") is not None:
        out["data_source_arn"] = data["dataSourceArn"]
    else:
        out["data_source_arn"] = ""
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    if data.get("workspaceConfiguration") is not None:
        import capo_opensearch.types.workspace_configuration_input

        out["workspace_configuration"] = (
            capo_opensearch.types.workspace_configuration_input.deserialize_json(
                data["workspaceConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
