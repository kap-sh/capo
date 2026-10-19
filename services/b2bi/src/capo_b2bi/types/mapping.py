"""Generated from Smithy shape ``com.amazonaws.b2bi#Mapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.mapping_template
    import capo_b2bi.types.mapping_template_language


class Mapping(TypedDict, closed=True):
    template_language: (
        "capo_b2bi.types.mapping_template_language.MappingTemplateLanguage"
    )
    """<p>The transformation language for the template, either XSLT or JSONATA.</p>"""
    template: NotRequired["capo_b2bi.types.mapping_template.MappingTemplate"]
    """<p>A string that represents the mapping template, in the transformation language specified in <code>templateLanguage</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Mapping) -> dict:
    out: dict = {}
    import capo_b2bi.types.mapping_template_language

    out["templateLanguage"] = (
        capo_b2bi.types.mapping_template_language.serialize_aws_json_1_0(
            value["template_language"]
        )
    )
    if "template" in value:
        out["template"] = value["template"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Mapping:
    out: Mapping = {}  # type: ignore[typeddict-item]
    if data.get("templateLanguage") is not None:
        import capo_b2bi.types.mapping_template_language

        out["template_language"] = (
            capo_b2bi.types.mapping_template_language.deserialize_aws_json_1_0(
                data["templateLanguage"]
            )
        )
    else:
        import typing

        out["template_language"] = typing.cast(
            "capo_b2bi.types.mapping_template_language.MappingTemplateLanguage", ""
        )
    if data.get("template") is not None:
        out["template"] = data["template"]
    return out
