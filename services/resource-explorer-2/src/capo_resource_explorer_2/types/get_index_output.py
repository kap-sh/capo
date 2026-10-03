"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetIndexOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resource_explorer_2.types.index_state
    import capo_resource_explorer_2.types.index_type
    import capo_resource_explorer_2.types.region_list
    import capo_resource_explorer_2.types.tag_map


class GetIndexOutput(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the index.</p>"""
    type: NotRequired["capo_resource_explorer_2.types.index_type.IndexType"]
    """<p>The type of the index in this Region. For information about the aggregator index and how it differs from a local index, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html">Turning on cross-Region search by creating an aggregator index</a>.</p>"""
    state: NotRequired["capo_resource_explorer_2.types.index_state.IndexState"]
    """<p>The current state of the index in this Amazon Web Services Region.</p>"""
    replicating_from: NotRequired[
        "capo_resource_explorer_2.types.region_list.RegionList"
    ]
    """<p>This response value is present only if this index is <code>Type=AGGREGATOR</code>.</p> <p>A list of the Amazon Web Services Regions that replicate their content to the index in this Region.</p>"""
    replicating_to: NotRequired["capo_resource_explorer_2.types.region_list.RegionList"]
    """<p>This response value is present only if this index is <code>Type=LOCAL</code>.</p> <p>The Amazon Web Services Region that contains the aggregator index, if one exists. If an aggregator index does exist then the Region in which you called this operation replicates its index information to the Region specified in this response value. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the index was originally created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the index was last updated.</p>"""
    tags: NotRequired["capo_resource_explorer_2.types.tag_map.TagMap"]
    """<p>Tag key and value pairs that are attached to the index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "state" in value:
        out["State"] = value["state"]
    if "replicating_from" in value:
        import capo_resource_explorer_2.types.region_list

        out["ReplicatingFrom"] = (
            capo_resource_explorer_2.types.region_list.serialize_json(
                value["replicating_from"]
            )
        )
    if "replicating_to" in value:
        import capo_resource_explorer_2.types.region_list

        out["ReplicatingTo"] = (
            capo_resource_explorer_2.types.region_list.serialize_json(
                value["replicating_to"]
            )
        )
    if "created_at" in value:
        import capo_resource_explorer_2._protocol.serialize

        out["CreatedAt"] = capo_resource_explorer_2._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_resource_explorer_2._protocol.serialize

        out["LastUpdatedAt"] = (
            capo_resource_explorer_2._protocol.serialize.fmt_date_time(
                value["last_updated_at"]
            )
        )
    if "tags" in value:
        import capo_resource_explorer_2.types.tag_map

        out["Tags"] = capo_resource_explorer_2.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetIndexOutput:
    out: GetIndexOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("ReplicatingFrom") is not None:
        import capo_resource_explorer_2.types.region_list

        out["replicating_from"] = (
            capo_resource_explorer_2.types.region_list.deserialize_json(
                data["ReplicatingFrom"]
            )
        )
    if data.get("ReplicatingTo") is not None:
        import capo_resource_explorer_2.types.region_list

        out["replicating_to"] = (
            capo_resource_explorer_2.types.region_list.deserialize_json(
                data["ReplicatingTo"]
            )
        )
    if data.get("CreatedAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["CreatedAt"].replace("Z", "+00:00")
        )
    if data.get("LastUpdatedAt") is not None:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromisoformat(
            data["LastUpdatedAt"].replace("Z", "+00:00")
        )
    if data.get("Tags") is not None:
        import capo_resource_explorer_2.types.tag_map

        out["tags"] = capo_resource_explorer_2.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
