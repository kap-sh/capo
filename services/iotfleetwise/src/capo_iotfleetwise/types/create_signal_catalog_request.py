"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateSignalCatalogRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.nodes
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.tag_list


class CreateSignalCatalogRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the signal catalog to create. </p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p>A brief description of the signal catalog.</p>"""
    nodes: NotRequired["capo_iotfleetwise.types.nodes.Nodes"]
    """<p> A list of information about nodes, which are a general abstraction of signals. For more information, see the API data type.</p>"""
    tags: NotRequired["capo_iotfleetwise.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the signal catalog.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateSignalCatalogRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "nodes" in value:
        import capo_iotfleetwise.types.nodes

        out["nodes"] = capo_iotfleetwise.types.nodes.serialize_aws_json_1_0(
            value["nodes"]
        )
    if "tags" in value:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateSignalCatalogRequest:
    out: CreateSignalCatalogRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("nodes") is not None:
        import capo_iotfleetwise.types.nodes

        out["nodes"] = capo_iotfleetwise.types.nodes.deserialize_aws_json_1_0(
            data["nodes"]
        )
    if data.get("tags") is not None:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
