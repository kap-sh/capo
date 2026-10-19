"""Generated from Smithy shape ``com.amazonaws.cloudtrail#AggregationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.event_category_aggregation
    import capo_cloudtrail.types.templates


class AggregationConfiguration(TypedDict, closed=True):
    templates: "capo_cloudtrail.types.templates.Templates"
    """<p>A list of aggregation templates that can be used to configure event aggregation.</p>"""
    event_category: (
        "capo_cloudtrail.types.event_category_aggregation.EventCategoryAggregation"
    )
    """<p>Specifies the event category for which aggregation should be performed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregationConfiguration) -> dict:
    out: dict = {}
    import capo_cloudtrail.types.templates

    out["Templates"] = capo_cloudtrail.types.templates.serialize_aws_json_1_1(
        value["templates"]
    )
    import capo_cloudtrail.types.event_category_aggregation

    out["EventCategory"] = (
        capo_cloudtrail.types.event_category_aggregation.serialize_aws_json_1_1(
            value["event_category"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregationConfiguration:
    out: AggregationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Templates") is not None:
        import capo_cloudtrail.types.templates

        out["templates"] = capo_cloudtrail.types.templates.deserialize_aws_json_1_1(
            data["Templates"]
        )
    else:
        out["templates"] = []
    if data.get("EventCategory") is not None:
        import capo_cloudtrail.types.event_category_aggregation

        out["event_category"] = (
            capo_cloudtrail.types.event_category_aggregation.deserialize_aws_json_1_1(
                data["EventCategory"]
            )
        )
    else:
        import typing

        out["event_category"] = typing.cast(
            "capo_cloudtrail.types.event_category_aggregation.EventCategoryAggregation",
            "",
        )
    return out
