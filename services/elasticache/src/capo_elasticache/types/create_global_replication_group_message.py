"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateGlobalReplicationGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string
    import capo_elasticache.types.tag_list


class CreateGlobalReplicationGroupMessage(TypedDict, closed=True):
    global_replication_group_id_suffix: NotRequired[
        "capo_elasticache.types.string.String"
    ]
    """<p>The suffix name of a Global datastore. Amazon ElastiCache automatically applies a prefix to the Global datastore ID when it is created. Each Amazon Region has its own prefix. For instance, a Global datastore ID created in the US-West-1 region will begin with "dsdfu" along with the suffix name you provide. The suffix, combined with the auto-generated prefix, guarantees uniqueness of the Global datastore name across multiple regions. </p> <p>For a full list of Amazon Regions and their respective Global datastore iD prefixes, see <a href="http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Redis-Global-Datastores-CLI.html">Using the Amazon CLI with Global datastores </a>.</p>"""
    global_replication_group_description: NotRequired[
        "capo_elasticache.types.string.String"
    ]
    """<p>Provides details of the Global datastore</p>"""
    primary_replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the primary cluster that accepts writes and will replicate updates to the secondary cluster. This value is stored as a lowercase string.</p>"""
    tags: NotRequired["capo_elasticache.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateGlobalReplicationGroupMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "global_replication_group_id_suffix" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalReplicationGroupIdSuffix",
                str(value["global_replication_group_id_suffix"]),
            )
        )
    if "global_replication_group_description" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalReplicationGroupDescription",
                str(value["global_replication_group_description"]),
            )
        )
    if "primary_replication_group_id" in value:
        pairs.append(
            (
                f"{key_prefix}PrimaryReplicationGroupId",
                str(value["primary_replication_group_id"]),
            )
        )
    if "tags" in value:
        import capo_elasticache.types.tag_list

        capo_elasticache.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateGlobalReplicationGroupMessage:
    out: CreateGlobalReplicationGroupMessage = {}  # type: ignore[typeddict-item]
    child_global_replication_group_id_suffix = el.find("GlobalReplicationGroupIdSuffix")
    if child_global_replication_group_id_suffix is not None:
        out["global_replication_group_id_suffix"] = str(
            child_global_replication_group_id_suffix.text or ""
        )
    child_global_replication_group_description = el.find(
        "GlobalReplicationGroupDescription"
    )
    if child_global_replication_group_description is not None:
        out["global_replication_group_description"] = str(
            child_global_replication_group_description.text or ""
        )
    child_primary_replication_group_id = el.find("PrimaryReplicationGroupId")
    if child_primary_replication_group_id is not None:
        out["primary_replication_group_id"] = str(
            child_primary_replication_group_id.text or ""
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elasticache.types.tag_list

        out["tags"] = capo_elasticache.types.tag_list.deserialize_query(child_tags)
    return out
