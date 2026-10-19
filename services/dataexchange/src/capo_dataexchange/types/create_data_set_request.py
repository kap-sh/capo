"""Generated from Smithy shape ``com.amazonaws.dataexchange#CreateDataSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.asset_type
    import capo_dataexchange.types.description
    import capo_dataexchange.types.map_of__string
    import capo_dataexchange.types.name


class CreateDataSetRequest(TypedDict, closed=True):
    asset_type: "capo_dataexchange.types.asset_type.AssetType"
    """<p>The type of asset that is added to a data set.</p>"""
    description: "capo_dataexchange.types.description.Description"
    """<p>A description for the data set. This value can be up to 16,348 characters long.</p>"""
    name: "capo_dataexchange.types.name.Name"
    """<p>The name of the data set.</p>"""
    tags: NotRequired["capo_dataexchange.types.map_of__string.MapOf__string"]
    """<p>A data set tag is an optional label that you can assign to a data set when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to these data sets and revisions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSetRequest) -> dict:
    out: dict = {}
    out["AssetType"] = value["asset_type"]
    out["Description"] = value["description"]
    out["Name"] = value["name"]
    if "tags" in value:
        import capo_dataexchange.types.map_of__string

        out["Tags"] = capo_dataexchange.types.map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDataSetRequest:
    out: CreateDataSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssetType") is not None:
        out["asset_type"] = data["AssetType"]
    else:
        out["asset_type"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Tags") is not None:
        import capo_dataexchange.types.map_of__string

        out["tags"] = capo_dataexchange.types.map_of__string.deserialize_json(
            data["Tags"]
        )
    return out
