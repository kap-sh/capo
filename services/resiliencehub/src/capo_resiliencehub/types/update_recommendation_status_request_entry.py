"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UpdateRecommendationStatusRequestEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.boolean_optional
    import capo_resiliencehub.types.entity_name255
    import capo_resiliencehub.types.exclude_recommendation_reason
    import capo_resiliencehub.types.spec_reference_id
    import capo_resiliencehub.types.string255
    import capo_resiliencehub.types.update_recommendation_status_item


class UpdateRecommendationStatusRequestEntry(TypedDict, closed=True):
    entry_id: "capo_resiliencehub.types.string255.String255"
    """<p>An identifier for an entry in this batch that is used to communicate the result.</p> <note> <p>The <code>entryId</code>s of a batch request need to be unique within a request.</p> </note>"""
    reference_id: "capo_resiliencehub.types.spec_reference_id.SpecReferenceId"
    """<p>Reference identifier of the operational recommendation item.</p>"""
    item: NotRequired[
        "capo_resiliencehub.types.update_recommendation_status_item.UpdateRecommendationStatusItem"
    ]
    """<p>The operational recommendation item.</p>"""
    excluded: "capo_resiliencehub.types.boolean_optional.BooleanOptional"
    """<p>Indicates if the operational recommendation needs to be excluded. If set to True, the operational recommendation will be excluded.</p>"""
    app_component_id: NotRequired[
        "capo_resiliencehub.types.entity_name255.EntityName255"
    ]
    """<p>Indicates the identifier of the AppComponent.</p>"""
    exclude_reason: NotRequired[
        "capo_resiliencehub.types.exclude_recommendation_reason.ExcludeRecommendationReason"
    ]
    """<p>Indicates the reason for excluding an operational recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommendationStatusRequestEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    out["referenceId"] = value["reference_id"]
    if "item" in value:
        import capo_resiliencehub.types.update_recommendation_status_item

        out["item"] = (
            capo_resiliencehub.types.update_recommendation_status_item.serialize_json(
                value["item"]
            )
        )
    out["excluded"] = value["excluded"]
    if "app_component_id" in value:
        out["appComponentId"] = value["app_component_id"]
    if "exclude_reason" in value:
        import capo_resiliencehub.types.exclude_recommendation_reason

        out["excludeReason"] = (
            capo_resiliencehub.types.exclude_recommendation_reason.serialize_json(
                value["exclude_reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRecommendationStatusRequestEntry:
    out: UpdateRecommendationStatusRequestEntry = {}  # type: ignore[typeddict-item]
    if data.get("entryId") is not None:
        out["entry_id"] = data["entryId"]
    else:
        out["entry_id"] = ""
    if data.get("referenceId") is not None:
        out["reference_id"] = data["referenceId"]
    else:
        out["reference_id"] = ""
    if data.get("item") is not None:
        import capo_resiliencehub.types.update_recommendation_status_item

        out["item"] = (
            capo_resiliencehub.types.update_recommendation_status_item.deserialize_json(
                data["item"]
            )
        )
    if data.get("excluded") is not None:
        out["excluded"] = data["excluded"]
    else:
        out["excluded"] = False
    if data.get("appComponentId") is not None:
        out["app_component_id"] = data["appComponentId"]
    if data.get("excludeReason") is not None:
        import capo_resiliencehub.types.exclude_recommendation_reason

        out["exclude_reason"] = (
            capo_resiliencehub.types.exclude_recommendation_reason.deserialize_json(
                data["excludeReason"]
            )
        )
    return out
