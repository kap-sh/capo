"""Generated from Smithy shape ``com.amazonaws.datazone#CreateAssetInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.asset_name
    import capo_datazone.types.asset_type_identifier
    import capo_datazone.types.client_token
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.external_identifier
    import capo_datazone.types.form_input_list
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.prediction_configuration
    import capo_datazone.types.project_id
    import capo_datazone.types.revision


class CreateAssetInput(TypedDict, closed=True):
    name: "capo_datazone.types.asset_name.AssetName"
    """<p>Asset name.</p>"""
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>Amazon DataZone domain where the asset is created.</p>"""
    external_identifier: NotRequired[
        "capo_datazone.types.external_identifier.ExternalIdentifier"
    ]
    """<p>The external identifier of the asset.</p> <p>If the value for the <code>externalIdentifier</code> parameter is specified, it must be a unique value.</p>"""
    type_identifier: "capo_datazone.types.asset_type_identifier.AssetTypeIdentifier"
    """<p>The unique identifier of this asset's type.</p>"""
    type_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of this asset's type.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>Asset description.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>Glossary terms attached to the asset.</p>"""
    forms_input: NotRequired["capo_datazone.types.form_input_list.FormInputList"]
    """<p>Metadata forms attached to the asset.</p>"""
    owning_project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The unique identifier of the project that owns this asset.</p>"""
    prediction_configuration: NotRequired[
        "capo_datazone.types.prediction_configuration.PredictionConfiguration"
    ]
    """<p>The configuration of the automatically generated business-friendly metadata for the asset.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "external_identifier" in value:
        out["externalIdentifier"] = value["external_identifier"]
    out["typeIdentifier"] = value["type_identifier"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
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
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    if "prediction_configuration" in value:
        import capo_datazone.types.prediction_configuration

        out["predictionConfiguration"] = (
            capo_datazone.types.prediction_configuration.serialize_json(
                value["prediction_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAssetInput:
    out: CreateAssetInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssetInput.name required")
    if data.get("externalIdentifier") is not None:
        out["external_identifier"] = data["externalIdentifier"]
    if data.get("typeIdentifier") is not None:
        out["type_identifier"] = data["typeIdentifier"]
    else:
        raise DeserializationError("CreateAssetInput.type_identifier required")
    if data.get("typeRevision") is not None:
        out["type_revision"] = data["typeRevision"]
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
    if data.get("owningProjectIdentifier") is not None:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        raise DeserializationError(
            "CreateAssetInput.owning_project_identifier required"
        )
    if data.get("predictionConfiguration") is not None:
        import capo_datazone.types.prediction_configuration

        out["prediction_configuration"] = (
            capo_datazone.types.prediction_configuration.deserialize_json(
                data["predictionConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateAssetInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "forms_input" in value:
        out["forms_input"] = "*** Sensitive Data Redacted ***"
    return out
