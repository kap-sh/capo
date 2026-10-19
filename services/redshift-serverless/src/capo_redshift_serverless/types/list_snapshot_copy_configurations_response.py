"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListSnapshotCopyConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.pagination_token
    import capo_redshift_serverless.types.snapshot_copy_configurations


class ListSnapshotCopyConfigurationsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""
    snapshot_copy_configurations: "capo_redshift_serverless.types.snapshot_copy_configurations.SnapshotCopyConfigurations"
    """<p>All of the returned snapshot copy configurations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSnapshotCopyConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_redshift_serverless.types.snapshot_copy_configurations

    out["snapshotCopyConfigurations"] = (
        capo_redshift_serverless.types.snapshot_copy_configurations.serialize_aws_json_1_1(
            value["snapshot_copy_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSnapshotCopyConfigurationsResponse:
    out: ListSnapshotCopyConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("snapshotCopyConfigurations") is not None:
        import capo_redshift_serverless.types.snapshot_copy_configurations

        out["snapshot_copy_configurations"] = (
            capo_redshift_serverless.types.snapshot_copy_configurations.deserialize_aws_json_1_1(
                data["snapshotCopyConfigurations"]
            )
        )
    else:
        out["snapshot_copy_configurations"] = []
    return out
