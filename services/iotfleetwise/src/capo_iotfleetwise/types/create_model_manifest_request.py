"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateModelManifestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.list_of_strings
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.tag_list


class CreateModelManifestRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the vehicle model to create.</p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p> A brief description of the vehicle model. </p>"""
    nodes: "capo_iotfleetwise.types.list_of_strings.listOfStrings"
    """<p> A list of nodes, which are a general abstraction of signals. </p>"""
    signal_catalog_arn: "capo_iotfleetwise.types.arn.arn"
    """<p> The Amazon Resource Name (ARN) of a signal catalog. </p>"""
    tags: NotRequired["capo_iotfleetwise.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the vehicle model.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateModelManifestRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_iotfleetwise.types.list_of_strings

    out["nodes"] = capo_iotfleetwise.types.list_of_strings.serialize_aws_json_1_0(
        value["nodes"]
    )
    out["signalCatalogArn"] = value["signal_catalog_arn"]
    if "tags" in value:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateModelManifestRequest:
    out: CreateModelManifestRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("nodes") is not None:
        import capo_iotfleetwise.types.list_of_strings

        out["nodes"] = capo_iotfleetwise.types.list_of_strings.deserialize_aws_json_1_0(
            data["nodes"]
        )
    else:
        out["nodes"] = []
    if data.get("signalCatalogArn") is not None:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    else:
        out["signal_catalog_arn"] = ""
    if data.get("tags") is not None:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
