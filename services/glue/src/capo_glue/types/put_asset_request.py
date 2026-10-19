"""Generated from Smithy shape ``com.amazonaws.glue#PutAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_description
    import capo_glue.types.asset_form_map
    import capo_glue.types.asset_id
    import capo_glue.types.asset_name
    import capo_glue.types.asset_type_id
    import capo_glue.types.hash_string


class PutAssetRequest(TypedDict, closed=True):
    asset_type_id: "capo_glue.types.asset_type_id.AssetTypeId"
    """<p>The identifier of the asset type for the asset.</p>"""
    identifier: "capo_glue.types.asset_id.AssetId"
    """<p>The unique identifier of the asset. If an asset with this identifier already exists, it is updated.</p>"""
    name: "capo_glue.types.asset_name.AssetName"
    """<p>The name of the asset.</p>"""
    description: NotRequired["capo_glue.types.asset_description.AssetDescription"]
    """<p>The description of the asset.</p>"""
    forms: "capo_glue.types.asset_form_map.AssetFormMap"
    """<p>The forms to set on the asset, keyed by form name. Each entry specifies the form type and its JSON content.</p>"""
    client_token: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAssetRequest) -> dict:
    out: dict = {}
    out["AssetTypeId"] = value["asset_type_id"]
    out["Identifier"] = value["identifier"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_glue.types.asset_form_map

    out["Forms"] = capo_glue.types.asset_form_map.serialize_aws_json_1_1(value["forms"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAssetRequest:
    out: PutAssetRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssetTypeId") is not None:
        out["asset_type_id"] = data["AssetTypeId"]
    else:
        out["asset_type_id"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Forms") is not None:
        import capo_glue.types.asset_form_map

        out["forms"] = capo_glue.types.asset_form_map.deserialize_aws_json_1_1(
            data["Forms"]
        )
    else:
        out["forms"] = {}
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
