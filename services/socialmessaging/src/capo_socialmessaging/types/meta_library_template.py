"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaLibraryTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.library_template_body_inputs
    import capo_socialmessaging.types.meta_library_template_button_inputs
    import capo_socialmessaging.types.meta_template_category
    import capo_socialmessaging.types.meta_template_language
    import capo_socialmessaging.types.meta_template_name


class MetaLibraryTemplate(TypedDict, closed=True):
    template_name: "capo_socialmessaging.types.meta_template_name.MetaTemplateName"
    """<p>The name to assign to the template.</p>"""
    library_template_name: (
        "capo_socialmessaging.types.meta_template_name.MetaTemplateName"
    )
    """<p>The name of the template in Meta's library.</p>"""
    template_category: (
        "capo_socialmessaging.types.meta_template_category.MetaTemplateCategory"
    )
    """<p>The category of the template (for example, UTILITY or MARKETING).</p>"""
    template_language: (
        "capo_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
    )
    """<p>The language code for the template (for example, en_US).</p>"""
    library_template_button_inputs: NotRequired[
        "capo_socialmessaging.types.meta_library_template_button_inputs.MetaLibraryTemplateButtonInputs"
    ]
    """<p>Button customizations for the template.</p>"""
    library_template_body_inputs: NotRequired[
        "capo_socialmessaging.types.library_template_body_inputs.LibraryTemplateBodyInputs"
    ]
    """<p>Body text customizations for the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaLibraryTemplate) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["libraryTemplateName"] = value["library_template_name"]
    out["templateCategory"] = value["template_category"]
    out["templateLanguage"] = value["template_language"]
    if "library_template_button_inputs" in value:
        import capo_socialmessaging.types.meta_library_template_button_inputs

        out["libraryTemplateButtonInputs"] = (
            capo_socialmessaging.types.meta_library_template_button_inputs.serialize_json(
                value["library_template_button_inputs"]
            )
        )
    if "library_template_body_inputs" in value:
        import capo_socialmessaging.types.library_template_body_inputs

        out["libraryTemplateBodyInputs"] = (
            capo_socialmessaging.types.library_template_body_inputs.serialize_json(
                value["library_template_body_inputs"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetaLibraryTemplate:
    out: MetaLibraryTemplate = {}  # type: ignore[typeddict-item]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        out["template_name"] = ""
    if data.get("libraryTemplateName") is not None:
        out["library_template_name"] = data["libraryTemplateName"]
    else:
        out["library_template_name"] = ""
    if data.get("templateCategory") is not None:
        out["template_category"] = data["templateCategory"]
    else:
        out["template_category"] = ""
    if data.get("templateLanguage") is not None:
        out["template_language"] = data["templateLanguage"]
    else:
        out["template_language"] = ""
    if data.get("libraryTemplateButtonInputs") is not None:
        import capo_socialmessaging.types.meta_library_template_button_inputs

        out["library_template_button_inputs"] = (
            capo_socialmessaging.types.meta_library_template_button_inputs.deserialize_json(
                data["libraryTemplateButtonInputs"]
            )
        )
    if data.get("libraryTemplateBodyInputs") is not None:
        import capo_socialmessaging.types.library_template_body_inputs

        out["library_template_body_inputs"] = (
            capo_socialmessaging.types.library_template_body_inputs.deserialize_json(
                data["libraryTemplateBodyInputs"]
            )
        )
    return out
