"""Generated from Smithy shape ``com.amazonaws.glue#UpdateAssetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_description
    import capo_glue.types.asset_id
    import capo_glue.types.asset_name
    import capo_glue.types.updated_at


class UpdateAssetResponse(TypedDict, closed=True):
    id: "capo_glue.types.asset_id.AssetId"
    """<p>The unique identifier of the asset.</p>"""
    name: NotRequired["capo_glue.types.asset_name.AssetName"]
    """<p>The name of the asset.</p>"""
    description: NotRequired["capo_glue.types.asset_description.AssetDescription"]
    """<p>The description of the asset.</p>"""
    updated_at: NotRequired["capo_glue.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the asset was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAssetResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "updated_at" in value:
        import capo_glue.types.updated_at

        out["UpdatedAt"] = capo_glue.types.updated_at.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAssetResponse:
    out: UpdateAssetResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("UpdatedAt") is not None:
        import capo_glue.types.updated_at

        out["updated_at"] = capo_glue.types.updated_at.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    return out
