"""Generated from Smithy shape ``com.amazonaws.resiliencehub#GroupingRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.double
    import capo_resiliencehub.types.grouping_app_component
    import capo_resiliencehub.types.grouping_recommendation_confidence_level
    import capo_resiliencehub.types.grouping_recommendation_rejection_reason
    import capo_resiliencehub.types.grouping_recommendation_status_type
    import capo_resiliencehub.types.grouping_resource_list
    import capo_resiliencehub.types.string255
    import capo_resiliencehub.types.string255_list
    import capo_resiliencehub.types.time_stamp


class GroupingRecommendation(TypedDict, closed=True):
    grouping_recommendation_id: "capo_resiliencehub.types.string255.String255"
    """<p>Indicates all the reasons available for rejecting a grouping recommendation.</p>"""
    grouping_app_component: (
        "capo_resiliencehub.types.grouping_app_component.GroupingAppComponent"
    )
    """<p>Indicates the name of the recommended Application Component (AppComponent).</p>"""
    resources: "capo_resiliencehub.types.grouping_resource_list.GroupingResourceList"
    """<p>Indicates the resources that are grouped in a recommended AppComponent.</p>"""
    score: "capo_resiliencehub.types.double.Double"
    """<p>Indicates the confidence level of the grouping recommendation.</p>"""
    recommendation_reasons: "capo_resiliencehub.types.string255_list.String255List"
    """<p>Indicates all the reasons available for rejecting a grouping recommendation.</p>"""
    status: "capo_resiliencehub.types.grouping_recommendation_status_type.GroupingRecommendationStatusType"
    """<p>Indicates the status of grouping resources into AppComponents.</p>"""
    confidence_level: "capo_resiliencehub.types.grouping_recommendation_confidence_level.GroupingRecommendationConfidenceLevel"
    """<p>Indicates the confidence level of Resilience Hub on the grouping recommendation.</p>"""
    creation_time: "capo_resiliencehub.types.time_stamp.TimeStamp"
    """<p>Indicates the creation time of the grouping recommendation.</p>"""
    rejection_reason: NotRequired[
        "capo_resiliencehub.types.grouping_recommendation_rejection_reason.GroupingRecommendationRejectionReason"
    ]
    """<p>Indicates the reason you had selected while rejecting a grouping recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupingRecommendation) -> dict:
    out: dict = {}
    out["groupingRecommendationId"] = value["grouping_recommendation_id"]
    import capo_resiliencehub.types.grouping_app_component

    out["groupingAppComponent"] = (
        capo_resiliencehub.types.grouping_app_component.serialize_json(
            value["grouping_app_component"]
        )
    )
    import capo_resiliencehub.types.grouping_resource_list

    out["resources"] = capo_resiliencehub.types.grouping_resource_list.serialize_json(
        value["resources"]
    )
    out["score"] = (
        "NaN"
        if value.get("score", 0) != value.get("score", 0)
        else "Infinity"
        if value.get("score", 0) == float("inf")
        else "-Infinity"
        if value.get("score", 0) == float("-inf")
        else value.get("score", 0)
    )
    import capo_resiliencehub.types.string255_list

    out["recommendationReasons"] = (
        capo_resiliencehub.types.string255_list.serialize_json(
            value["recommendation_reasons"]
        )
    )
    import capo_resiliencehub.types.grouping_recommendation_status_type

    out["status"] = (
        capo_resiliencehub.types.grouping_recommendation_status_type.serialize_json(
            value["status"]
        )
    )
    import capo_resiliencehub.types.grouping_recommendation_confidence_level

    out["confidenceLevel"] = (
        capo_resiliencehub.types.grouping_recommendation_confidence_level.serialize_json(
            value["confidence_level"]
        )
    )
    import capo_resiliencehub.types.time_stamp

    out["creationTime"] = capo_resiliencehub.types.time_stamp.serialize_json(
        value["creation_time"]
    )
    if "rejection_reason" in value:
        import capo_resiliencehub.types.grouping_recommendation_rejection_reason

        out["rejectionReason"] = (
            capo_resiliencehub.types.grouping_recommendation_rejection_reason.serialize_json(
                value["rejection_reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> GroupingRecommendation:
    out: GroupingRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("groupingRecommendationId") is not None:
        out["grouping_recommendation_id"] = data["groupingRecommendationId"]
    else:
        out["grouping_recommendation_id"] = ""
    if data.get("groupingAppComponent") is not None:
        import capo_resiliencehub.types.grouping_app_component

        out["grouping_app_component"] = (
            capo_resiliencehub.types.grouping_app_component.deserialize_json(
                data["groupingAppComponent"]
            )
        )
    else:
        raise DeserializationError(
            "GroupingRecommendation.grouping_app_component required"
        )
    if data.get("resources") is not None:
        import capo_resiliencehub.types.grouping_resource_list

        out["resources"] = (
            capo_resiliencehub.types.grouping_resource_list.deserialize_json(
                data["resources"]
            )
        )
    else:
        out["resources"] = []
    if data.get("score") is not None:
        out["score"] = float(data["score"])
    else:
        out["score"] = 0
    if data.get("recommendationReasons") is not None:
        import capo_resiliencehub.types.string255_list

        out["recommendation_reasons"] = (
            capo_resiliencehub.types.string255_list.deserialize_json(
                data["recommendationReasons"]
            )
        )
    else:
        out["recommendation_reasons"] = []
    if data.get("status") is not None:
        import capo_resiliencehub.types.grouping_recommendation_status_type

        out["status"] = (
            capo_resiliencehub.types.grouping_recommendation_status_type.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_resiliencehub.types.grouping_recommendation_status_type.GroupingRecommendationStatusType",
            "",
        )
    if data.get("confidenceLevel") is not None:
        import capo_resiliencehub.types.grouping_recommendation_confidence_level

        out["confidence_level"] = (
            capo_resiliencehub.types.grouping_recommendation_confidence_level.deserialize_json(
                data["confidenceLevel"]
            )
        )
    else:
        import typing

        out["confidence_level"] = typing.cast(
            "capo_resiliencehub.types.grouping_recommendation_confidence_level.GroupingRecommendationConfidenceLevel",
            "",
        )
    if data.get("creationTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["creation_time"] = capo_resiliencehub.types.time_stamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("rejectionReason") is not None:
        import capo_resiliencehub.types.grouping_recommendation_rejection_reason

        out["rejection_reason"] = (
            capo_resiliencehub.types.grouping_recommendation_rejection_reason.deserialize_json(
                data["rejectionReason"]
            )
        )
    return out
