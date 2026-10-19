"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AlarmRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.alarm_type
    import capo_resiliencehub.types.app_component_name_list
    import capo_resiliencehub.types.entity_description
    import capo_resiliencehub.types.entity_id
    import capo_resiliencehub.types.recommendation_item_list
    import capo_resiliencehub.types.recommendation_status
    import capo_resiliencehub.types.spec_reference_id
    import capo_resiliencehub.types.string500
    import capo_resiliencehub.types.uuid


class AlarmRecommendation(TypedDict, closed=True):
    recommendation_id: "capo_resiliencehub.types.uuid.Uuid"
    """<p>Identifier of the alarm recommendation.</p>"""
    reference_id: "capo_resiliencehub.types.spec_reference_id.SpecReferenceId"
    """<p>Reference identifier of the alarm recommendation.</p>"""
    name: "capo_resiliencehub.types.string500.String500"
    """<p>Name of the alarm recommendation.</p>"""
    description: NotRequired[
        "capo_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>Description of the alarm recommendation.</p>"""
    type: "capo_resiliencehub.types.alarm_type.AlarmType"
    """<p>Type of alarm recommendation.</p>"""
    app_component_name: NotRequired["capo_resiliencehub.types.entity_id.EntityId"]
    """<p>Application Component name for the CloudWatch alarm recommendation. This name is saved as the first item in the <code>appComponentNames</code> list.</p>"""
    items: NotRequired[
        "capo_resiliencehub.types.recommendation_item_list.RecommendationItemList"
    ]
    """<p>List of CloudWatch alarm recommendations.</p>"""
    prerequisite: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>The prerequisite for the alarm recommendation.</p>"""
    app_component_names: NotRequired[
        "capo_resiliencehub.types.app_component_name_list.AppComponentNameList"
    ]
    """<p>List of Application Component names for the CloudWatch alarm recommendation.</p>"""
    recommendation_status: NotRequired[
        "capo_resiliencehub.types.recommendation_status.RecommendationStatus"
    ]
    """<p>Status of the recommended Amazon CloudWatch alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlarmRecommendation) -> dict:
    out: dict = {}
    out["recommendationId"] = value["recommendation_id"]
    out["referenceId"] = value["reference_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_resiliencehub.types.alarm_type

    out["type"] = capo_resiliencehub.types.alarm_type.serialize_json(value["type"])
    if "app_component_name" in value:
        out["appComponentName"] = value["app_component_name"]
    if "items" in value:
        import capo_resiliencehub.types.recommendation_item_list

        out["items"] = capo_resiliencehub.types.recommendation_item_list.serialize_json(
            value["items"]
        )
    if "prerequisite" in value:
        out["prerequisite"] = value["prerequisite"]
    if "app_component_names" in value:
        import capo_resiliencehub.types.app_component_name_list

        out["appComponentNames"] = (
            capo_resiliencehub.types.app_component_name_list.serialize_json(
                value["app_component_names"]
            )
        )
    if "recommendation_status" in value:
        import capo_resiliencehub.types.recommendation_status

        out["recommendationStatus"] = (
            capo_resiliencehub.types.recommendation_status.serialize_json(
                value["recommendation_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AlarmRecommendation:
    out: AlarmRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("recommendationId") is not None:
        out["recommendation_id"] = data["recommendationId"]
    else:
        out["recommendation_id"] = ""
    if data.get("referenceId") is not None:
        out["reference_id"] = data["referenceId"]
    else:
        out["reference_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_resiliencehub.types.alarm_type

        out["type"] = capo_resiliencehub.types.alarm_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_resiliencehub.types.alarm_type.AlarmType", "")
    if data.get("appComponentName") is not None:
        out["app_component_name"] = data["appComponentName"]
    if data.get("items") is not None:
        import capo_resiliencehub.types.recommendation_item_list

        out["items"] = (
            capo_resiliencehub.types.recommendation_item_list.deserialize_json(
                data["items"]
            )
        )
    if data.get("prerequisite") is not None:
        out["prerequisite"] = data["prerequisite"]
    if data.get("appComponentNames") is not None:
        import capo_resiliencehub.types.app_component_name_list

        out["app_component_names"] = (
            capo_resiliencehub.types.app_component_name_list.deserialize_json(
                data["appComponentNames"]
            )
        )
    if data.get("recommendationStatus") is not None:
        import capo_resiliencehub.types.recommendation_status

        out["recommendation_status"] = (
            capo_resiliencehub.types.recommendation_status.deserialize_json(
                data["recommendationStatus"]
            )
        )
    return out
