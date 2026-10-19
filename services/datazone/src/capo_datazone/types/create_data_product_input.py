"""Generated from Smithy shape ``com.amazonaws.datazone#CreateDataProductInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.data_product_description
    import capo_datazone.types.data_product_items
    import capo_datazone.types.data_product_name
    import capo_datazone.types.domain_id
    import capo_datazone.types.form_input_list
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.project_id


class CreateDataProductInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the data product is created.</p>"""
    name: "capo_datazone.types.data_product_name.DataProductName"
    """<p>The name of the data product.</p>"""
    owning_project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the owning project of the data product.</p>"""
    description: NotRequired[
        "capo_datazone.types.data_product_description.DataProductDescription"
    ]
    """<p>The description of the data product.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms of the data product.</p>"""
    forms_input: NotRequired["capo_datazone.types.form_input_list.FormInputList"]
    """<p>The metadata forms of the data product.</p>"""
    items: NotRequired["capo_datazone.types.data_product_items.DataProductItems"]
    """<p>The data assets of the data product.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataProductInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    if "description" in value:
        out["description"] = value["description"]
    if "glossary_terms" in value:
        import capo_datazone.types.glossary_terms

        out["glossaryTerms"] = capo_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "forms_input" in value:
        import capo_datazone.types.form_input_list

        out["formsInput"] = capo_datazone.types.form_input_list.serialize_json(
            value["forms_input"]
        )
    if "items" in value:
        import capo_datazone.types.data_product_items

        out["items"] = capo_datazone.types.data_product_items.serialize_json(
            value["items"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateDataProductInput:
    out: CreateDataProductInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("owningProjectIdentifier") is not None:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        out["owning_project_identifier"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.glossary_terms

        out["glossary_terms"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if data.get("formsInput") is not None:
        import capo_datazone.types.form_input_list

        out["forms_input"] = capo_datazone.types.form_input_list.deserialize_json(
            data["formsInput"]
        )
    if data.get("items") is not None:
        import capo_datazone.types.data_product_items

        out["items"] = capo_datazone.types.data_product_items.deserialize_json(
            data["items"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateDataProductInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "forms_input" in value:
        out["forms_input"] = "*** Sensitive Data Redacted ***"
    return out
