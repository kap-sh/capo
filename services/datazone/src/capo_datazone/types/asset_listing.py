"""Generated from Smithy shape ``com.amazonaws.datazone#AssetListing``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_id
    import capo_datazone.types.created_at
    import capo_datazone.types.detailed_glossary_terms
    import capo_datazone.types.forms
    import capo_datazone.types.project_id
    import capo_datazone.types.revision
    import capo_datazone.types.time_series_data_point_summary_form_output_list
    import capo_datazone.types.type_name


class AssetListing(TypedDict, closed=True):
    asset_id: NotRequired["capo_datazone.types.asset_id.AssetId"]
    """<p>The identifier of an asset published in an Amazon DataZone catalog. </p>"""
    asset_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of an asset published in an Amazon DataZone catalog. </p>"""
    asset_type: NotRequired["capo_datazone.types.type_name.TypeName"]
    """<p>The type of an asset published in an Amazon DataZone catalog. </p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when an asset published in an Amazon DataZone catalog was created. </p>"""
    forms: NotRequired["capo_datazone.types.forms.Forms"]
    """<p>The metadata forms attached to an asset published in an Amazon DataZone catalog. </p>"""
    latest_time_series_data_point_forms: NotRequired[
        "capo_datazone.types.time_series_data_point_summary_form_output_list.TimeSeriesDataPointSummaryFormOutputList"
    ]
    """<p>The latest time series data points forms included in the additional attributes of an asset.</p>"""
    glossary_terms: NotRequired[
        "capo_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>The glossary terms attached to an asset published in an Amazon DataZone catalog. </p>"""
    governed_glossary_terms: NotRequired[
        "capo_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>The restricted glossary terms associated with an asset.</p>"""
    owning_project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the project where an asset published in an Amazon DataZone catalog exists. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetListing) -> dict:
    out: dict = {}
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "asset_revision" in value:
        out["assetRevision"] = value["asset_revision"]
    if "asset_type" in value:
        out["assetType"] = value["asset_type"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "forms" in value:
        out["forms"] = value["forms"]
    if "latest_time_series_data_point_forms" in value:
        import capo_datazone.types.time_series_data_point_summary_form_output_list

        out["latestTimeSeriesDataPointForms"] = (
            capo_datazone.types.time_series_data_point_summary_form_output_list.serialize_json(
                value["latest_time_series_data_point_forms"]
            )
        )
    if "glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["glossaryTerms"] = (
            capo_datazone.types.detailed_glossary_terms.serialize_json(
                value["glossary_terms"]
            )
        )
    if "governed_glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["governedGlossaryTerms"] = (
            capo_datazone.types.detailed_glossary_terms.serialize_json(
                value["governed_glossary_terms"]
            )
        )
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    return out


def deserialize_json(data: dict) -> AssetListing:
    out: AssetListing = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    if data.get("assetRevision") is not None:
        out["asset_revision"] = data["assetRevision"]
    if data.get("assetType") is not None:
        out["asset_type"] = data["assetType"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("forms") is not None:
        out["forms"] = data["forms"]
    if data.get("latestTimeSeriesDataPointForms") is not None:
        import capo_datazone.types.time_series_data_point_summary_form_output_list

        out["latest_time_series_data_point_forms"] = (
            capo_datazone.types.time_series_data_point_summary_form_output_list.deserialize_json(
                data["latestTimeSeriesDataPointForms"]
            )
        )
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.deserialize_json(
                data["glossaryTerms"]
            )
        )
    if data.get("governedGlossaryTerms") is not None:
        import capo_datazone.types.detailed_glossary_terms

        out["governed_glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.deserialize_json(
                data["governedGlossaryTerms"]
            )
        )
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    return out


def redact_sensitive(value: AssetListing) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.redact_sensitive(
                value["glossary_terms"]
            )
        )
    if "governed_glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["governed_glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.redact_sensitive(
                value["governed_glossary_terms"]
            )
        )
    return out
