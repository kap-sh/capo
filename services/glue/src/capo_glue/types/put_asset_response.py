"""Generated from Smithy shape ``com.amazonaws.glue#PutAssetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_description
    import capo_glue.types.asset_form_map
    import capo_glue.types.asset_id
    import capo_glue.types.asset_name
    import capo_glue.types.created_at


class PutAssetResponse(TypedDict, closed=True):
    id: "capo_glue.types.asset_id.AssetId"
    """<p>The unique identifier of the asset.</p>"""
    name: "capo_glue.types.asset_name.AssetName"
    """<p>The name of the asset.</p>"""
    description: NotRequired["capo_glue.types.asset_description.AssetDescription"]
    """<p>The description of the asset.</p>"""
    created_at: NotRequired["capo_glue.types.created_at.CreatedAt"]
    """<p>The timestamp at which the asset was created.</p>"""
    forms: NotRequired["capo_glue.types.asset_form_map.AssetFormMap"]
    """<p>The forms attached to the asset, keyed by form name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAssetResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import capo_glue.types.created_at

        out["CreatedAt"] = capo_glue.types.created_at.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "forms" in value:
        import capo_glue.types.asset_form_map

        out["Forms"] = capo_glue.types.asset_form_map.serialize_aws_json_1_1(
            value["forms"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAssetResponse:
    out: PutAssetResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedAt") is not None:
        import capo_glue.types.created_at

        out["created_at"] = capo_glue.types.created_at.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("Forms") is not None:
        import capo_glue.types.asset_form_map

        out["forms"] = capo_glue.types.asset_form_map.deserialize_aws_json_1_1(
            data["Forms"]
        )
    return out
