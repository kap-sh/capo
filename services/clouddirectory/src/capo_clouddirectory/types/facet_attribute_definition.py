"""Generated from Smithy shape ``com.amazonaws.clouddirectory#FacetAttributeDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.bool
    import capo_clouddirectory.types.facet_attribute_type
    import capo_clouddirectory.types.rule_map
    import capo_clouddirectory.types.typed_attribute_value


class FacetAttributeDefinition(TypedDict, closed=True):
    type: "capo_clouddirectory.types.facet_attribute_type.FacetAttributeType"
    """<p>The type of the attribute.</p>"""
    default_value: NotRequired[
        "capo_clouddirectory.types.typed_attribute_value.TypedAttributeValue"
    ]
    """<p>The default value of the attribute (if configured).</p>"""
    is_immutable: "capo_clouddirectory.types.bool.Bool"
    """<p>Whether the attribute is mutable or not.</p>"""
    rules: NotRequired["capo_clouddirectory.types.rule_map.RuleMap"]
    """<p>Validation rules attached to the attribute definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FacetAttributeDefinition) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.facet_attribute_type

    out["Type"] = capo_clouddirectory.types.facet_attribute_type.serialize_json(
        value["type"]
    )
    if "default_value" in value:
        import capo_clouddirectory.types.typed_attribute_value

        out["DefaultValue"] = (
            capo_clouddirectory.types.typed_attribute_value.serialize_json(
                value["default_value"]
            )
        )
    out["IsImmutable"] = value.get("is_immutable", False)
    if "rules" in value:
        import capo_clouddirectory.types.rule_map

        out["Rules"] = capo_clouddirectory.types.rule_map.serialize_json(value["rules"])
    return out


def deserialize_json(data: dict) -> FacetAttributeDefinition:
    out: FacetAttributeDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_clouddirectory.types.facet_attribute_type

        out["type"] = capo_clouddirectory.types.facet_attribute_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_clouddirectory.types.facet_attribute_type.FacetAttributeType", ""
        )
    if data.get("DefaultValue") is not None:
        import capo_clouddirectory.types.typed_attribute_value

        out["default_value"] = (
            capo_clouddirectory.types.typed_attribute_value.deserialize_json(
                data["DefaultValue"]
            )
        )
    if data.get("IsImmutable") is not None:
        out["is_immutable"] = data["IsImmutable"]
    else:
        out["is_immutable"] = False
    if data.get("Rules") is not None:
        import capo_clouddirectory.types.rule_map

        out["rules"] = capo_clouddirectory.types.rule_map.deserialize_json(
            data["Rules"]
        )
    return out
