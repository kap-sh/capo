"""Generated from Smithy shape ``com.amazonaws.glue#GetAssetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_description
    import capo_glue.types.asset_form_map
    import capo_glue.types.asset_id
    import capo_glue.types.asset_name
    import capo_glue.types.asset_type_id
    import capo_glue.types.created_at
    import capo_glue.types.glossary_term_id_list
    import capo_glue.types.iterable_form_map
    import capo_glue.types.updated_at


class GetAssetOutput(TypedDict, closed=True):
    id: "capo_glue.types.asset_id.AssetId"
    """<p>The unique identifier of the asset.</p>"""
    name: NotRequired["capo_glue.types.asset_name.AssetName"]
    """<p>The name of the asset.</p>"""
    description: NotRequired["capo_glue.types.asset_description.AssetDescription"]
    """<p>The description of the asset.</p>"""
    created_at: NotRequired["capo_glue.types.created_at.CreatedAt"]
    """<p>The timestamp at which the asset was created.</p>"""
    updated_at: NotRequired["capo_glue.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the asset was last updated.</p>"""
    asset_type_id: "capo_glue.types.asset_type_id.AssetTypeId"
    """<p>The identifier of the asset type for this asset.</p>"""
    glossary_terms: NotRequired[
        "capo_glue.types.glossary_term_id_list.GlossaryTermIdList"
    ]
    """<p>The identifiers of the glossary terms associated with the asset.</p>"""
    forms: NotRequired["capo_glue.types.asset_form_map.AssetFormMap"]
    """<p>The forms on the asset, keyed by form name.</p>"""
    attachments: NotRequired["capo_glue.types.asset_form_map.AssetFormMap"]
    """<p>Additional attachments on the asset for more context, keyed by attachment name.</p>"""
    iterable_forms: NotRequired["capo_glue.types.iterable_form_map.IterableFormMap"]
    """<p>The iterable forms available on the asset, keyed by form name (for example, <code>columns</code>). Use the form name with <code>ListIterableForms</code> or <code>BatchGetIterableForms</code> to retrieve the form's items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAssetOutput) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import capo_glue.types.created_at

        out["CreatedAt"] = capo_glue.types.created_at.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_glue.types.updated_at

        out["UpdatedAt"] = capo_glue.types.updated_at.serialize_aws_json_1_1(
            value["updated_at"]
        )
    out["AssetTypeId"] = value["asset_type_id"]
    if "glossary_terms" in value:
        import capo_glue.types.glossary_term_id_list

        out["GlossaryTerms"] = (
            capo_glue.types.glossary_term_id_list.serialize_aws_json_1_1(
                value["glossary_terms"]
            )
        )
    if "forms" in value:
        import capo_glue.types.asset_form_map

        out["Forms"] = capo_glue.types.asset_form_map.serialize_aws_json_1_1(
            value["forms"]
        )
    if "attachments" in value:
        import capo_glue.types.asset_form_map

        out["Attachments"] = capo_glue.types.asset_form_map.serialize_aws_json_1_1(
            value["attachments"]
        )
    if "iterable_forms" in value:
        import capo_glue.types.iterable_form_map

        out["IterableForms"] = capo_glue.types.iterable_form_map.serialize_aws_json_1_1(
            value["iterable_forms"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAssetOutput:
    out: GetAssetOutput = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedAt") is not None:
        import capo_glue.types.created_at

        out["created_at"] = capo_glue.types.created_at.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_glue.types.updated_at

        out["updated_at"] = capo_glue.types.updated_at.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if data.get("AssetTypeId") is not None:
        out["asset_type_id"] = data["AssetTypeId"]
    else:
        out["asset_type_id"] = ""
    if data.get("GlossaryTerms") is not None:
        import capo_glue.types.glossary_term_id_list

        out["glossary_terms"] = (
            capo_glue.types.glossary_term_id_list.deserialize_aws_json_1_1(
                data["GlossaryTerms"]
            )
        )
    if data.get("Forms") is not None:
        import capo_glue.types.asset_form_map

        out["forms"] = capo_glue.types.asset_form_map.deserialize_aws_json_1_1(
            data["Forms"]
        )
    if data.get("Attachments") is not None:
        import capo_glue.types.asset_form_map

        out["attachments"] = capo_glue.types.asset_form_map.deserialize_aws_json_1_1(
            data["Attachments"]
        )
    if data.get("IterableForms") is not None:
        import capo_glue.types.iterable_form_map

        out["iterable_forms"] = (
            capo_glue.types.iterable_form_map.deserialize_aws_json_1_1(
                data["IterableForms"]
            )
        )
    return out
