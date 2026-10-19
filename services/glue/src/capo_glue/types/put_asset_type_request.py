"""Generated from Smithy shape ``com.amazonaws.glue#PutAssetTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_type_forms_map
    import capo_glue.types.asset_type_name
    import capo_glue.types.hash_string


class PutAssetTypeRequest(TypedDict, closed=True):
    name: "capo_glue.types.asset_type_name.AssetTypeName"
    """<p>The name of the asset type.</p>"""
    forms: "capo_glue.types.asset_type_forms_map.AssetTypeFormsMap"
    """<p>The forms that make up the asset type, keyed by form name. Each entry references the form type that defines the form's schema.</p>"""
    client_token: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAssetTypeRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.asset_type_forms_map

    out["Forms"] = capo_glue.types.asset_type_forms_map.serialize_aws_json_1_1(
        value["forms"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAssetTypeRequest:
    out: PutAssetTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Forms") is not None:
        import capo_glue.types.asset_type_forms_map

        out["forms"] = capo_glue.types.asset_type_forms_map.deserialize_aws_json_1_1(
            data["Forms"]
        )
    else:
        out["forms"] = {}
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
