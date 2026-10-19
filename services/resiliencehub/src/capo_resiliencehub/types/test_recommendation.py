"""Generated from Smithy shape ``com.amazonaws.resiliencehub#TestRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.alarm_reference_id_list
    import capo_resiliencehub.types.document_name
    import capo_resiliencehub.types.entity_description
    import capo_resiliencehub.types.entity_id
    import capo_resiliencehub.types.entity_name255
    import capo_resiliencehub.types.recommendation_item_list
    import capo_resiliencehub.types.recommendation_status
    import capo_resiliencehub.types.spec_reference_id
    import capo_resiliencehub.types.string500
    import capo_resiliencehub.types.test_risk
    import capo_resiliencehub.types.test_type
    import capo_resiliencehub.types.uuid


class TestRecommendation(TypedDict, closed=True):
    recommendation_id: NotRequired["capo_resiliencehub.types.uuid.Uuid"]
    """<p>Identifier for the test recommendation.</p>"""
    reference_id: "capo_resiliencehub.types.spec_reference_id.SpecReferenceId"
    """<p>Reference identifier for the test recommendation.</p>"""
    app_component_id: NotRequired[
        "capo_resiliencehub.types.entity_name255.EntityName255"
    ]
    """<p>Indicates the identifier of the AppComponent.</p>"""
    app_component_name: NotRequired["capo_resiliencehub.types.entity_id.EntityId"]
    """<p>Name of the Application Component.</p>"""
    name: NotRequired["capo_resiliencehub.types.document_name.DocumentName"]
    """<p>Name of the test recommendation.</p>"""
    intent: NotRequired["capo_resiliencehub.types.entity_description.EntityDescription"]
    """<p>Intent of the test recommendation.</p>"""
    risk: NotRequired["capo_resiliencehub.types.test_risk.TestRisk"]
    """<p>Level of risk for this test recommendation.</p>"""
    type: NotRequired["capo_resiliencehub.types.test_type.TestType"]
    """<p>Type of test recommendation.</p>"""
    description: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>Description for the test recommendation.</p>"""
    items: NotRequired[
        "capo_resiliencehub.types.recommendation_item_list.RecommendationItemList"
    ]
    """<p>The test recommendation items.</p>"""
    prerequisite: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>Prerequisite of the test recommendation.</p>"""
    depends_on_alarms: NotRequired[
        "capo_resiliencehub.types.alarm_reference_id_list.AlarmReferenceIdList"
    ]
    """<p> A list of recommended alarms that are used in the test and must be exported before or with the test. </p>"""
    recommendation_status: NotRequired[
        "capo_resiliencehub.types.recommendation_status.RecommendationStatus"
    ]
    """<p>Status of the recommended test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRecommendation) -> dict:
    out: dict = {}
    if "recommendation_id" in value:
        out["recommendationId"] = value["recommendation_id"]
    out["referenceId"] = value["reference_id"]
    if "app_component_id" in value:
        out["appComponentId"] = value["app_component_id"]
    if "app_component_name" in value:
        out["appComponentName"] = value["app_component_name"]
    if "name" in value:
        out["name"] = value["name"]
    if "intent" in value:
        out["intent"] = value["intent"]
    if "risk" in value:
        import capo_resiliencehub.types.test_risk

        out["risk"] = capo_resiliencehub.types.test_risk.serialize_json(value["risk"])
    if "type" in value:
        import capo_resiliencehub.types.test_type

        out["type"] = capo_resiliencehub.types.test_type.serialize_json(value["type"])
    if "description" in value:
        out["description"] = value["description"]
    if "items" in value:
        import capo_resiliencehub.types.recommendation_item_list

        out["items"] = capo_resiliencehub.types.recommendation_item_list.serialize_json(
            value["items"]
        )
    if "prerequisite" in value:
        out["prerequisite"] = value["prerequisite"]
    if "depends_on_alarms" in value:
        import capo_resiliencehub.types.alarm_reference_id_list

        out["dependsOnAlarms"] = (
            capo_resiliencehub.types.alarm_reference_id_list.serialize_json(
                value["depends_on_alarms"]
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


def deserialize_json(data: dict) -> TestRecommendation:
    out: TestRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("recommendationId") is not None:
        out["recommendation_id"] = data["recommendationId"]
    if data.get("referenceId") is not None:
        out["reference_id"] = data["referenceId"]
    else:
        out["reference_id"] = ""
    if data.get("appComponentId") is not None:
        out["app_component_id"] = data["appComponentId"]
    if data.get("appComponentName") is not None:
        out["app_component_name"] = data["appComponentName"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("intent") is not None:
        out["intent"] = data["intent"]
    if data.get("risk") is not None:
        import capo_resiliencehub.types.test_risk

        out["risk"] = capo_resiliencehub.types.test_risk.deserialize_json(data["risk"])
    if data.get("type") is not None:
        import capo_resiliencehub.types.test_type

        out["type"] = capo_resiliencehub.types.test_type.deserialize_json(data["type"])
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("items") is not None:
        import capo_resiliencehub.types.recommendation_item_list

        out["items"] = (
            capo_resiliencehub.types.recommendation_item_list.deserialize_json(
                data["items"]
            )
        )
    if data.get("prerequisite") is not None:
        out["prerequisite"] = data["prerequisite"]
    if data.get("dependsOnAlarms") is not None:
        import capo_resiliencehub.types.alarm_reference_id_list

        out["depends_on_alarms"] = (
            capo_resiliencehub.types.alarm_reference_id_list.deserialize_json(
                data["dependsOnAlarms"]
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
