"""Generated from Smithy shape ``com.amazonaws.controlcatalog#RelatedControlMappingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.control_arn
    import capo_controlcatalog.types.control_relation_type


class RelatedControlMappingDetails(TypedDict, closed=True):
    control_arn: NotRequired["capo_controlcatalog.types.control_arn.ControlArn"]
    """<p>The unique identifier of a control.</p>"""
    relation_type: "capo_controlcatalog.types.control_relation_type.ControlRelationType"
    """<p>Returns an enumerated value that represents the relationship between two or more controls.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelatedControlMappingDetails) -> dict:
    out: dict = {}
    if "control_arn" in value:
        out["ControlArn"] = value["control_arn"]
    import capo_controlcatalog.types.control_relation_type

    out["RelationType"] = (
        capo_controlcatalog.types.control_relation_type.serialize_json(
            value["relation_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> RelatedControlMappingDetails:
    out: RelatedControlMappingDetails = {}  # type: ignore[typeddict-item]
    if data.get("ControlArn") is not None:
        out["control_arn"] = data["ControlArn"]
    if data.get("RelationType") is not None:
        import capo_controlcatalog.types.control_relation_type

        out["relation_type"] = (
            capo_controlcatalog.types.control_relation_type.deserialize_json(
                data["RelationType"]
            )
        )
    else:
        import typing

        out["relation_type"] = typing.cast(
            "capo_controlcatalog.types.control_relation_type.ControlRelationType", ""
        )
    return out
