"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkAttributeDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_name
    import capo_clouddirectory.types.bool
    import capo_clouddirectory.types.facet_attribute_type
    import capo_clouddirectory.types.required_attribute_behavior
    import capo_clouddirectory.types.rule_map
    import capo_clouddirectory.types.typed_attribute_value


class TypedLinkAttributeDefinition(TypedDict, closed=True):
    name: "capo_clouddirectory.types.attribute_name.AttributeName"
    """<p>The unique name of the typed link attribute.</p>"""
    type: "capo_clouddirectory.types.facet_attribute_type.FacetAttributeType"
    """<p>The type of the attribute.</p>"""
    default_value: NotRequired[
        "capo_clouddirectory.types.typed_attribute_value.TypedAttributeValue"
    ]
    """<p>The default value of the attribute (if configured).</p>"""
    is_immutable: "capo_clouddirectory.types.bool.Bool"
    """<p>Whether the attribute is mutable or not.</p>"""
    rules: NotRequired["capo_clouddirectory.types.rule_map.RuleMap"]
    """<p>Validation rules that are attached to the attribute definition.</p>"""
    required_behavior: "capo_clouddirectory.types.required_attribute_behavior.RequiredAttributeBehavior"
    """<p>The required behavior of the <code>TypedLinkAttributeDefinition</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkAttributeDefinition) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
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
    import capo_clouddirectory.types.required_attribute_behavior

    out["RequiredBehavior"] = (
        capo_clouddirectory.types.required_attribute_behavior.serialize_json(
            value["required_behavior"]
        )
    )
    return out


def deserialize_json(data: dict) -> TypedLinkAttributeDefinition:
    out: TypedLinkAttributeDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
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
    if data.get("RequiredBehavior") is not None:
        import capo_clouddirectory.types.required_attribute_behavior

        out["required_behavior"] = (
            capo_clouddirectory.types.required_attribute_behavior.deserialize_json(
                data["RequiredBehavior"]
            )
        )
    else:
        import typing

        out["required_behavior"] = typing.cast(
            "capo_clouddirectory.types.required_attribute_behavior.RequiredAttributeBehavior",
            "",
        )
    return out
