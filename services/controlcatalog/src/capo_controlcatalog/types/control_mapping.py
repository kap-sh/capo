"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.control_arn
    import capo_controlcatalog.types.mapping
    import capo_controlcatalog.types.mapping_type


class ControlMapping(TypedDict, closed=True):
    control_arn: "capo_controlcatalog.types.control_arn.ControlArn"
    """<p>The Amazon Resource Name (ARN) that identifies the control in the mapping.</p>"""
    mapping_type: "capo_controlcatalog.types.mapping_type.MappingType"
    """<p>The type of mapping relationship between the control and other entities.</p>"""
    mapping: "capo_controlcatalog.types.mapping.Mapping"
    """<p>The details of the mapping relationship, for example, containing framework, common control, or related control information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlMapping) -> dict:
    out: dict = {}
    out["ControlArn"] = value["control_arn"]
    import capo_controlcatalog.types.mapping_type

    out["MappingType"] = capo_controlcatalog.types.mapping_type.serialize_json(
        value["mapping_type"]
    )
    import capo_controlcatalog.types.mapping

    out["Mapping"] = capo_controlcatalog.types.mapping.serialize_json(value["mapping"])
    return out


def deserialize_json(data: dict) -> ControlMapping:
    out: ControlMapping = {}  # type: ignore[typeddict-item]
    if data.get("ControlArn") is not None:
        out["control_arn"] = data["ControlArn"]
    else:
        out["control_arn"] = ""
    if data.get("MappingType") is not None:
        import capo_controlcatalog.types.mapping_type

        out["mapping_type"] = capo_controlcatalog.types.mapping_type.deserialize_json(
            data["MappingType"]
        )
    else:
        import typing

        out["mapping_type"] = typing.cast(
            "capo_controlcatalog.types.mapping_type.MappingType", ""
        )
    if data.get("Mapping") is not None:
        import capo_controlcatalog.types.mapping

        out["mapping"] = capo_controlcatalog.types.mapping.deserialize_json(
            data["Mapping"]
        )
    else:
        import capo_controlcatalog.types._unknown

        out["mapping"] = capo_controlcatalog.types._unknown.UnknownUnionMember("")
    return out
