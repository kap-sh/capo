"""Generated from Smithy shape ``com.amazonaws.opensearch#CloudWatchDirectQueryDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.direct_query_data_source_role_arn


class CloudWatchDirectQueryDataSource(TypedDict, closed=True):
    role_arn: "capo_opensearch.types.direct_query_data_source_role_arn.DirectQueryDataSourceRoleArn"
    """<p> The unique identifier of the IAM role that grants OpenSearch Service permission to access the specified data source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchDirectQueryDataSource) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> CloudWatchDirectQueryDataSource:
    out: CloudWatchDirectQueryDataSource = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    return out
