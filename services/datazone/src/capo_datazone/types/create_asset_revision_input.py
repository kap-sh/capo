"""Generated from Smithy shape ``com.amazonaws.datazone#CreateAssetRevisionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.asset_identifier
    import capo_datazone.types.asset_name
    import capo_datazone.types.client_token
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.form_input_list
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.prediction_configuration
    import capo_datazone.types.revision


class CreateAssetRevisionInput(TypedDict, closed=True):
    name: "capo_datazone.types.asset_name.AssetName"
    """<p>Te revised name of the asset.</p>"""
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The unique identifier of the domain where the asset is being revised.</p>"""
    identifier: "capo_datazone.types.asset_identifier.AssetIdentifier"
    """<p>The identifier of the asset.</p>"""
    type_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision type of the asset.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The revised description of the asset.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms to be attached to the asset as part of asset revision.</p>"""
    forms_input: NotRequired["capo_datazone.types.form_input_list.FormInputList"]
    """<p>The metadata forms to be attached to the asset as part of asset revision.</p>"""
    prediction_configuration: NotRequired[
        "capo_datazone.types.prediction_configuration.PredictionConfiguration"
    ]
    """<p>The configuration of the automatically generated business-friendly metadata for the asset.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetRevisionInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
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


def deserialize_json(data: dict) -> CreateAssetRevisionInput:
    out: CreateAssetRevisionInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssetRevisionInput.name required")
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


def redact_sensitive(value: CreateAssetRevisionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "forms_input" in value:
        out["forms_input"] = "*** Sensitive Data Redacted ***"
    return out
