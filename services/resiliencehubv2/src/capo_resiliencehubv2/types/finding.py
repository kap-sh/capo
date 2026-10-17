"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#Finding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.entity_description
    import capo_resiliencehubv2.types.failure_category
    import capo_resiliencehubv2.types.finding_severity
    import capo_resiliencehubv2.types.finding_status
    import capo_resiliencehubv2.types.functions_list
    import capo_resiliencehubv2.types.infrastructure_and_code_recommendations_list
    import capo_resiliencehubv2.types.observability_recommendations_list
    import capo_resiliencehubv2.types.policy_component
    import capo_resiliencehubv2.types.testing_recommendations_list
    import capo_resiliencehubv2.types.uuid


class Finding(TypedDict, closed=True):
    finding_id: NotRequired["capo_resiliencehubv2.types.uuid.Uuid"]
    """<p>The unique identifier of the finding.</p>"""
    name: NotRequired["str"]
    """<p>The name of the finding.</p>"""
    description: NotRequired[
        "capo_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    failure_category: NotRequired[
        "capo_resiliencehubv2.types.failure_category.FailureCategory"
    ]
    """<p>The failure category of the finding.</p>"""
    status: NotRequired["capo_resiliencehubv2.types.finding_status.FindingStatus"]
    """<p>The current status of the finding.</p>"""
    reasoning: NotRequired["str"]
    """<p>The reasoning behind the finding.</p>"""
    comment: NotRequired["str"]
    """<p>A user-provided comment about the finding.</p>"""
    severity: NotRequired["capo_resiliencehubv2.types.finding_severity.FindingSeverity"]
    """<p>The severity of the finding.</p>"""
    service_functions: NotRequired[
        "capo_resiliencehubv2.types.functions_list.FunctionsList"
    ]
    """<p>The service functions associated with the finding.</p>"""
    policy_component: NotRequired[
        "capo_resiliencehubv2.types.policy_component.PolicyComponent"
    ]
    """<p>The policy component associated with the finding.</p>"""
    infrastructure_and_code_recommendations: NotRequired[
        "capo_resiliencehubv2.types.infrastructure_and_code_recommendations_list.InfrastructureAndCodeRecommendationsList"
    ]
    """<p>Infrastructure and code recommendations to address the finding.</p>"""
    observability_recommendations: NotRequired[
        "capo_resiliencehubv2.types.observability_recommendations_list.ObservabilityRecommendationsList"
    ]
    """<p>Observability recommendations to address the finding.</p>"""
    testing_recommendations: NotRequired[
        "capo_resiliencehubv2.types.testing_recommendations_list.TestingRecommendationsList"
    ]
    """<p>Testing recommendations to address the finding.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the finding was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Finding) -> dict:
    out: dict = {}
    if "finding_id" in value:
        out["findingId"] = value["finding_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "failure_category" in value:
        import capo_resiliencehubv2.types.failure_category

        out["failureCategory"] = (
            capo_resiliencehubv2.types.failure_category.serialize_json(
                value["failure_category"]
            )
        )
    if "status" in value:
        import capo_resiliencehubv2.types.finding_status

        out["status"] = capo_resiliencehubv2.types.finding_status.serialize_json(
            value["status"]
        )
    if "reasoning" in value:
        out["reasoning"] = value["reasoning"]
    if "comment" in value:
        out["comment"] = value["comment"]
    if "severity" in value:
        import capo_resiliencehubv2.types.finding_severity

        out["severity"] = capo_resiliencehubv2.types.finding_severity.serialize_json(
            value["severity"]
        )
    if "service_functions" in value:
        import capo_resiliencehubv2.types.functions_list

        out["serviceFunctions"] = (
            capo_resiliencehubv2.types.functions_list.serialize_json(
                value["service_functions"]
            )
        )
    if "policy_component" in value:
        import capo_resiliencehubv2.types.policy_component

        out["policyComponent"] = (
            capo_resiliencehubv2.types.policy_component.serialize_json(
                value["policy_component"]
            )
        )
    if "infrastructure_and_code_recommendations" in value:
        import capo_resiliencehubv2.types.infrastructure_and_code_recommendations_list

        out["infrastructureAndCodeRecommendations"] = (
            capo_resiliencehubv2.types.infrastructure_and_code_recommendations_list.serialize_json(
                value["infrastructure_and_code_recommendations"]
            )
        )
    if "observability_recommendations" in value:
        import capo_resiliencehubv2.types.observability_recommendations_list

        out["observabilityRecommendations"] = (
            capo_resiliencehubv2.types.observability_recommendations_list.serialize_json(
                value["observability_recommendations"]
            )
        )
    if "testing_recommendations" in value:
        import capo_resiliencehubv2.types.testing_recommendations_list

        out["testingRecommendations"] = (
            capo_resiliencehubv2.types.testing_recommendations_list.serialize_json(
                value["testing_recommendations"]
            )
        )
    if "updated_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("failureCategory") is not None:
        import capo_resiliencehubv2.types.failure_category

        out["failure_category"] = (
            capo_resiliencehubv2.types.failure_category.deserialize_json(
                data["failureCategory"]
            )
        )
    if data.get("status") is not None:
        import capo_resiliencehubv2.types.finding_status

        out["status"] = capo_resiliencehubv2.types.finding_status.deserialize_json(
            data["status"]
        )
    if data.get("reasoning") is not None:
        out["reasoning"] = data["reasoning"]
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    if data.get("severity") is not None:
        import capo_resiliencehubv2.types.finding_severity

        out["severity"] = capo_resiliencehubv2.types.finding_severity.deserialize_json(
            data["severity"]
        )
    if data.get("serviceFunctions") is not None:
        import capo_resiliencehubv2.types.functions_list

        out["service_functions"] = (
            capo_resiliencehubv2.types.functions_list.deserialize_json(
                data["serviceFunctions"]
            )
        )
    if data.get("policyComponent") is not None:
        import capo_resiliencehubv2.types.policy_component

        out["policy_component"] = (
            capo_resiliencehubv2.types.policy_component.deserialize_json(
                data["policyComponent"]
            )
        )
    if data.get("infrastructureAndCodeRecommendations") is not None:
        import capo_resiliencehubv2.types.infrastructure_and_code_recommendations_list

        out["infrastructure_and_code_recommendations"] = (
            capo_resiliencehubv2.types.infrastructure_and_code_recommendations_list.deserialize_json(
                data["infrastructureAndCodeRecommendations"]
            )
        )
    if data.get("observabilityRecommendations") is not None:
        import capo_resiliencehubv2.types.observability_recommendations_list

        out["observability_recommendations"] = (
            capo_resiliencehubv2.types.observability_recommendations_list.deserialize_json(
                data["observabilityRecommendations"]
            )
        )
    if data.get("testingRecommendations") is not None:
        import capo_resiliencehubv2.types.testing_recommendations_list

        out["testing_recommendations"] = (
            capo_resiliencehubv2.types.testing_recommendations_list.deserialize_json(
                data["testingRecommendations"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
