"""Generated from Smithy shape ``com.amazonaws.opensearch#PrometheusDirectQueryDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.amp_workspace_arn
    import capo_opensearch.types.direct_query_data_source_role_arn


class PrometheusDirectQueryDataSource(TypedDict, closed=True):
    role_arn: "capo_opensearch.types.direct_query_data_source_role_arn.DirectQueryDataSourceRoleArn"
    """<p> The unique identifier of the IAM role that grants OpenSearch Service permission to access the specified data source. </p>"""
    workspace_arn: "capo_opensearch.types.amp_workspace_arn.AMPWorkspaceArn"
    """<p> The unique identifier of the Amazon Managed Prometheus Workspace that is associated with the specified data source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrometheusDirectQueryDataSource) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    out["WorkspaceArn"] = value["workspace_arn"]
    return out


def deserialize_json(data: dict) -> PrometheusDirectQueryDataSource:
    out: PrometheusDirectQueryDataSource = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("WorkspaceArn") is not None:
        out["workspace_arn"] = data["WorkspaceArn"]
    else:
        out["workspace_arn"] = ""
    return out
