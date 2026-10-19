"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ImportSignalCatalogRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.formatted_vss
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.tag_list


class ImportSignalCatalogRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p>The name of the signal catalog to import.</p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p> A brief description of the signal catalog. </p>"""
    vss: NotRequired["capo_iotfleetwise.types.formatted_vss.FormattedVss"]
    """<p>The contents of the Vehicle Signal Specification (VSS) configuration. VSS is a precise language used to describe and model signals in vehicle networks.</p>"""
    tags: NotRequired["capo_iotfleetwise.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the signal catalog.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportSignalCatalogRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "vss" in value:
        import capo_iotfleetwise.types.formatted_vss

        out["vss"] = capo_iotfleetwise.types.formatted_vss.serialize_aws_json_1_0(
            value["vss"]
        )
    if "tags" in value:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportSignalCatalogRequest:
    out: ImportSignalCatalogRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("vss") is not None:
        import capo_iotfleetwise.types.formatted_vss

        out["vss"] = capo_iotfleetwise.types.formatted_vss.deserialize_aws_json_1_0(
            data["vss"]
        )
    if data.get("tags") is not None:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
