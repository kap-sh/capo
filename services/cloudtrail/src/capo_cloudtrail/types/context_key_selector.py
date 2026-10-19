"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ContextKeySelector``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.operator_target_list
    import capo_cloudtrail.types.type


class ContextKeySelector(TypedDict, closed=True):
    type: "capo_cloudtrail.types.type.Type"
    """<p>Specifies the type of the event record field in ContextKeySelector. Valid values include RequestContext, TagContext.</p>"""
    equals: "capo_cloudtrail.types.operator_target_list.OperatorTargetList"
    """<p>A list of keys defined by Type to be included in CloudTrail enriched events. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContextKeySelector) -> dict:
    out: dict = {}
    import capo_cloudtrail.types.type

    out["Type"] = capo_cloudtrail.types.type.serialize_aws_json_1_1(value["type"])
    import capo_cloudtrail.types.operator_target_list

    out["Equals"] = capo_cloudtrail.types.operator_target_list.serialize_aws_json_1_1(
        value["equals"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContextKeySelector:
    out: ContextKeySelector = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_cloudtrail.types.type

        out["type"] = capo_cloudtrail.types.type.deserialize_aws_json_1_1(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_cloudtrail.types.type.Type", "")
    if data.get("Equals") is not None:
        import capo_cloudtrail.types.operator_target_list

        out["equals"] = (
            capo_cloudtrail.types.operator_target_list.deserialize_aws_json_1_1(
                data["Equals"]
            )
        )
    else:
        out["equals"] = []
    return out
