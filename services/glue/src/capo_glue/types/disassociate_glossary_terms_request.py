"""Generated from Smithy shape ``com.amazonaws.glue#DisassociateGlossaryTermsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.asset_id
    import capo_glue.types.glossary_term_id_list
    import capo_glue.types.hash_string
    import capo_glue.types.item_identifier
    import capo_glue.types.iterable_form_name


class DisassociateGlossaryTermsRequest(TypedDict, closed=True):
    asset_identifier: "capo_glue.types.asset_id.AssetId"
    """<p>The unique identifier of the asset to disassociate glossary terms from.</p>"""
    iterable_form_name: NotRequired[
        "capo_glue.types.iterable_form_name.IterableFormName"
    ]
    """<p>The name of the iterable form. When specified along with <code>itemIdentifier</code>, the glossary terms are disassociated from an item within the iterable form rather than the asset itself.</p>"""
    item_identifier: NotRequired["capo_glue.types.item_identifier.ItemIdentifier"]
    """<p>The identifier of the item within the iterable form. Required when <code>iterableFormName</code> is specified.</p>"""
    glossary_term_identifiers: (
        "capo_glue.types.glossary_term_id_list.GlossaryTermIdList"
    )
    """<p>The list of glossary term identifiers to disassociate from the asset.</p>"""
    client_token: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateGlossaryTermsRequest) -> dict:
    out: dict = {}
    out["AssetIdentifier"] = value["asset_identifier"]
    if "iterable_form_name" in value:
        out["IterableFormName"] = value["iterable_form_name"]
    if "item_identifier" in value:
        out["ItemIdentifier"] = value["item_identifier"]
    import capo_glue.types.glossary_term_id_list

    out["GlossaryTermIdentifiers"] = (
        capo_glue.types.glossary_term_id_list.serialize_aws_json_1_1(
            value["glossary_term_identifiers"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateGlossaryTermsRequest:
    out: DisassociateGlossaryTermsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssetIdentifier") is not None:
        out["asset_identifier"] = data["AssetIdentifier"]
    else:
        out["asset_identifier"] = ""
    if data.get("IterableFormName") is not None:
        out["iterable_form_name"] = data["IterableFormName"]
    if data.get("ItemIdentifier") is not None:
        out["item_identifier"] = data["ItemIdentifier"]
    if data.get("GlossaryTermIdentifiers") is not None:
        import capo_glue.types.glossary_term_id_list

        out["glossary_term_identifiers"] = (
            capo_glue.types.glossary_term_id_list.deserialize_aws_json_1_1(
                data["GlossaryTermIdentifiers"]
            )
        )
    else:
        out["glossary_term_identifiers"] = []
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
