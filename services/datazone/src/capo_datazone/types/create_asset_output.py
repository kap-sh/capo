"""Generated from Smithy shape ``com.amazonaws.datazone#CreateAssetOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.asset_id
    import capo_datazone.types.asset_listing_details
    import capo_datazone.types.asset_name
    import capo_datazone.types.asset_type_identifier
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.external_identifier
    import capo_datazone.types.form_output_list
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.governed_glossary_terms
    import capo_datazone.types.prediction_configuration
    import capo_datazone.types.project_id
    import capo_datazone.types.revision
    import capo_datazone.types.time_series_data_point_summary_form_output_list


class CreateAssetOutput(TypedDict, closed=True):
    id: "capo_datazone.types.asset_id.AssetId"
    """<p>The unique identifier of the created asset.</p>"""
    name: "capo_datazone.types.asset_name.AssetName"
    """<p>The name of the created asset.</p>"""
    type_identifier: "capo_datazone.types.asset_type_identifier.AssetTypeIdentifier"
    """<p>The identifier of the created asset type.</p>"""
    type_revision: "capo_datazone.types.revision.Revision"
    """<p>The revision type of the asset.</p>"""
    external_identifier: NotRequired[
        "capo_datazone.types.external_identifier.ExternalIdentifier"
    ]
    """<p>The external identifier of the asset.</p>"""
    revision: "capo_datazone.types.revision.Revision"
    """<p>The revision of the asset.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the created asset.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the asset was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user that created this asset in the catalog.</p>"""
    first_revision_created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the first revision of the asset took place.</p>"""
    first_revision_created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user that made the first revision of the asset.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms that are attached to the created asset.</p>"""
    governed_glossary_terms: NotRequired[
        "capo_datazone.types.governed_glossary_terms.GovernedGlossaryTerms"
    ]
    """<p>The glossary terms in a restricted glossary.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the Amazon DataZone project that owns the created asset. </p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the asset was created.</p>"""
    listing: NotRequired[
        "capo_datazone.types.asset_listing_details.AssetListingDetails"
    ]
    """<p>The details of an asset published in an Amazon DataZone catalog.</p>"""
    forms_output: "capo_datazone.types.form_output_list.FormOutputList"
    """<p>The metadata forms that are attached to the created asset.</p>"""
    read_only_forms_output: NotRequired[
        "capo_datazone.types.form_output_list.FormOutputList"
    ]
    """<p>The read-only metadata forms that are attached to the created asset.</p>"""
    latest_time_series_data_point_forms_output: NotRequired[
        "capo_datazone.types.time_series_data_point_summary_form_output_list.TimeSeriesDataPointSummaryFormOutputList"
    ]
    """<p>The latest data point that was imported into the time series form for the asset. </p>"""
    prediction_configuration: NotRequired[
        "capo_datazone.types.prediction_configuration.PredictionConfiguration"
    ]
    """<p>The configuration of the automatically generated business-friendly metadata for the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["typeIdentifier"] = value["type_identifier"]
    out["typeRevision"] = value["type_revision"]
    if "external_identifier" in value:
        out["externalIdentifier"] = value["external_identifier"]
    out["revision"] = value["revision"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "first_revision_created_at" in value:
        import capo_datazone.types.created_at

        out["firstRevisionCreatedAt"] = capo_datazone.types.created_at.serialize_json(
            value["first_revision_created_at"]
        )
    if "first_revision_created_by" in value:
        out["firstRevisionCreatedBy"] = value["first_revision_created_by"]
    if "glossary_terms" in value:
        import capo_datazone.types.glossary_terms

        out["glossaryTerms"] = capo_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "governed_glossary_terms" in value:
        import capo_datazone.types.governed_glossary_terms

        out["governedGlossaryTerms"] = (
            capo_datazone.types.governed_glossary_terms.serialize_json(
                value["governed_glossary_terms"]
            )
        )
    out["owningProjectId"] = value["owning_project_id"]
    out["domainId"] = value["domain_id"]
    if "listing" in value:
        import capo_datazone.types.asset_listing_details

        out["listing"] = capo_datazone.types.asset_listing_details.serialize_json(
            value["listing"]
        )
    import capo_datazone.types.form_output_list

    out["formsOutput"] = capo_datazone.types.form_output_list.serialize_json(
        value["forms_output"]
    )
    if "read_only_forms_output" in value:
        import capo_datazone.types.form_output_list

        out["readOnlyFormsOutput"] = (
            capo_datazone.types.form_output_list.serialize_json(
                value["read_only_forms_output"]
            )
        )
    if "latest_time_series_data_point_forms_output" in value:
        import capo_datazone.types.time_series_data_point_summary_form_output_list

        out["latestTimeSeriesDataPointFormsOutput"] = (
            capo_datazone.types.time_series_data_point_summary_form_output_list.serialize_json(
                value["latest_time_series_data_point_forms_output"]
            )
        )
    if "prediction_configuration" in value:
        import capo_datazone.types.prediction_configuration

        out["predictionConfiguration"] = (
            capo_datazone.types.prediction_configuration.serialize_json(
                value["prediction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAssetOutput:
    out: CreateAssetOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateAssetOutput.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssetOutput.name required")
    if data.get("typeIdentifier") is not None:
        out["type_identifier"] = data["typeIdentifier"]
    else:
        raise DeserializationError("CreateAssetOutput.type_identifier required")
    if data.get("typeRevision") is not None:
        out["type_revision"] = data["typeRevision"]
    else:
        raise DeserializationError("CreateAssetOutput.type_revision required")
    if data.get("externalIdentifier") is not None:
        out["external_identifier"] = data["externalIdentifier"]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("CreateAssetOutput.revision required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("firstRevisionCreatedAt") is not None:
        import capo_datazone.types.created_at

        out["first_revision_created_at"] = (
            capo_datazone.types.created_at.deserialize_json(
                data["firstRevisionCreatedAt"]
            )
        )
    if data.get("firstRevisionCreatedBy") is not None:
        out["first_revision_created_by"] = data["firstRevisionCreatedBy"]
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.glossary_terms

        out["glossary_terms"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if data.get("governedGlossaryTerms") is not None:
        import capo_datazone.types.governed_glossary_terms

        out["governed_glossary_terms"] = (
            capo_datazone.types.governed_glossary_terms.deserialize_json(
                data["governedGlossaryTerms"]
            )
        )
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("CreateAssetOutput.owning_project_id required")
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateAssetOutput.domain_id required")
    if data.get("listing") is not None:
        import capo_datazone.types.asset_listing_details

        out["listing"] = capo_datazone.types.asset_listing_details.deserialize_json(
            data["listing"]
        )
    if data.get("formsOutput") is not None:
        import capo_datazone.types.form_output_list

        out["forms_output"] = capo_datazone.types.form_output_list.deserialize_json(
            data["formsOutput"]
        )
    else:
        raise DeserializationError("CreateAssetOutput.forms_output required")
    if data.get("readOnlyFormsOutput") is not None:
        import capo_datazone.types.form_output_list

        out["read_only_forms_output"] = (
            capo_datazone.types.form_output_list.deserialize_json(
                data["readOnlyFormsOutput"]
            )
        )
    if data.get("latestTimeSeriesDataPointFormsOutput") is not None:
        import capo_datazone.types.time_series_data_point_summary_form_output_list

        out["latest_time_series_data_point_forms_output"] = (
            capo_datazone.types.time_series_data_point_summary_form_output_list.deserialize_json(
                data["latestTimeSeriesDataPointFormsOutput"]
            )
        )
    if data.get("predictionConfiguration") is not None:
        import capo_datazone.types.prediction_configuration

        out["prediction_configuration"] = (
            capo_datazone.types.prediction_configuration.deserialize_json(
                data["predictionConfiguration"]
            )
        )
    return out


def redact_sensitive(value: CreateAssetOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "forms_output" in value:
        import capo_datazone.types.form_output_list

        out["forms_output"] = capo_datazone.types.form_output_list.redact_sensitive(
            value["forms_output"]
        )
    if "read_only_forms_output" in value:
        import capo_datazone.types.form_output_list

        out["read_only_forms_output"] = (
            capo_datazone.types.form_output_list.redact_sensitive(
                value["read_only_forms_output"]
            )
        )
    return out
