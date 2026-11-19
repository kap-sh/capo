"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.delete_replication
    import capo_ecr.types.replication_destination_list
    import capo_ecr.types.repository_filter_list


class ReplicationRule(TypedDict, closed=True):
    destinations: (
        "capo_ecr.types.replication_destination_list.ReplicationDestinationList"
    )
    """<p>An array of objects representing the destination for a replication rule.</p>"""
    repository_filters: NotRequired[
        "capo_ecr.types.repository_filter_list.RepositoryFilterList"
    ]
    """<p>An array of objects representing the filters for a replication rule. Specifying a repository filter for a replication rule provides a method for controlling which repositories in a private registry are replicated.</p>"""
    delete_replication: NotRequired[
        "capo_ecr.types.delete_replication.DeleteReplication"
    ]
    """<p>The delete replication settings for the replication rule. When delete replication is enabled, the service replicates image deletions and image tag removals from the source registry to the replication destinations. If you do not specify this parameter, the service does not replicate image deletions or image tag removals for the replication rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationRule) -> dict:
    out: dict = {}
    import capo_ecr.types.replication_destination_list

    out["destinations"] = (
        capo_ecr.types.replication_destination_list.serialize_aws_json_1_1(
            value["destinations"]
        )
    )
    if "repository_filters" in value:
        import capo_ecr.types.repository_filter_list

        out["repositoryFilters"] = (
            capo_ecr.types.repository_filter_list.serialize_aws_json_1_1(
                value["repository_filters"]
            )
        )
    if "delete_replication" in value:
        import capo_ecr.types.delete_replication

        out["deleteReplication"] = (
            capo_ecr.types.delete_replication.serialize_aws_json_1_1(
                value["delete_replication"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationRule:
    out: ReplicationRule = {}  # type: ignore[typeddict-item]
    if data.get("destinations") is not None:
        import capo_ecr.types.replication_destination_list

        out["destinations"] = (
            capo_ecr.types.replication_destination_list.deserialize_aws_json_1_1(
                data["destinations"]
            )
        )
    else:
        out["destinations"] = []
    if data.get("repositoryFilters") is not None:
        import capo_ecr.types.repository_filter_list

        out["repository_filters"] = (
            capo_ecr.types.repository_filter_list.deserialize_aws_json_1_1(
                data["repositoryFilters"]
            )
        )
    if data.get("deleteReplication") is not None:
        import capo_ecr.types.delete_replication

        out["delete_replication"] = (
            capo_ecr.types.delete_replication.deserialize_aws_json_1_1(
                data["deleteReplication"]
            )
        )
    return out
