"""Generated from Smithy shape ``com.amazonaws.socialmessaging#TemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_template_category
    import capo_socialmessaging.types.meta_template_id
    import capo_socialmessaging.types.meta_template_language
    import capo_socialmessaging.types.meta_template_name
    import capo_socialmessaging.types.meta_template_quality_score
    import capo_socialmessaging.types.meta_template_source
    import capo_socialmessaging.types.meta_template_status


class TemplateSummary(TypedDict, closed=True):
    template_name: NotRequired[
        "capo_socialmessaging.types.meta_template_name.MetaTemplateName"
    ]
    """<p>The name of the template.</p>"""
    meta_template_id: NotRequired[
        "capo_socialmessaging.types.meta_template_id.MetaTemplateId"
    ]
    """<p>The numeric ID assigned to the template by Meta.</p>"""
    template_status: NotRequired[
        "capo_socialmessaging.types.meta_template_status.MetaTemplateStatus"
    ]
    """<p>The current status of the template (for example, APPROVED, PENDING, or REJECTED).</p>"""
    template_quality_score: NotRequired[
        "capo_socialmessaging.types.meta_template_quality_score.MetaTemplateQualityScore"
    ]
    """<p>The quality score assigned to the template by Meta.</p>"""
    template_language: NotRequired[
        "capo_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
    ]
    """<p>The language code of the template (for example, en_US).</p>"""
    template_category: NotRequired[
        "capo_socialmessaging.types.meta_template_category.MetaTemplateCategory"
    ]
    """<p>The category of the template (for example, UTILITY or MARKETING).</p>"""
    template_source: NotRequired[
        "capo_socialmessaging.types.meta_template_source.MetaTemplateSource"
    ]
    """<p>The source of the template. A value of AUTO_GENERATED indicates that the template was created automatically from a message that you sent. This field is not present for templates that you created manually.</p>"""
    correct_category: NotRequired[
        "capo_socialmessaging.types.meta_template_category.MetaTemplateCategory"
    ]
    """<p>The category that the template content actually belongs to, when it differs from the template's current category. This field is present only when the template has been flagged as miscategorized.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSummary) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["templateName"] = value["template_name"]
    if "meta_template_id" in value:
        out["metaTemplateId"] = value["meta_template_id"]
    if "template_status" in value:
        out["templateStatus"] = value["template_status"]
    if "template_quality_score" in value:
        out["templateQualityScore"] = value["template_quality_score"]
    if "template_language" in value:
        out["templateLanguage"] = value["template_language"]
    if "template_category" in value:
        out["templateCategory"] = value["template_category"]
    if "template_source" in value:
        out["templateSource"] = value["template_source"]
    if "correct_category" in value:
        out["correctCategory"] = value["correct_category"]
    return out


def deserialize_json(data: dict) -> TemplateSummary:
    out: TemplateSummary = {}  # type: ignore[typeddict-item]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    if data.get("metaTemplateId") is not None:
        out["meta_template_id"] = data["metaTemplateId"]
    if data.get("templateStatus") is not None:
        out["template_status"] = data["templateStatus"]
    if data.get("templateQualityScore") is not None:
        out["template_quality_score"] = data["templateQualityScore"]
    if data.get("templateLanguage") is not None:
        out["template_language"] = data["templateLanguage"]
    if data.get("templateCategory") is not None:
        out["template_category"] = data["templateCategory"]
    if data.get("templateSource") is not None:
        out["template_source"] = data["templateSource"]
    if data.get("correctCategory") is not None:
        out["correct_category"] = data["correctCategory"]
    return out
