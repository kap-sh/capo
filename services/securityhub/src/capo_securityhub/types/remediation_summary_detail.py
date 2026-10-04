"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationSummaryDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.kb_article_list
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.remediation_string_list


class RemediationSummaryDetail(TypedDict, closed=True):
    action: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A summarized action to take for the remediation target.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A description of the remediation target.</p>"""
    is_immediate: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Specifies whether the effect of this target is immediate.</p>"""
    post_remediation_steps: NotRequired[
        "capo_securityhub.types.remediation_string_list.RemediationStringList"
    ]
    """<p>An array of steps to be taken after remediation.</p>"""
    kb_articles: NotRequired["capo_securityhub.types.kb_article_list.KbArticleList"]
    """<p>An array of <code>KbArticle</code> objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationSummaryDetail) -> dict:
    out: dict = {}
    if "action" in value:
        out["Action"] = value["action"]
    if "description" in value:
        out["Description"] = value["description"]
    if "is_immediate" in value:
        out["IsImmediate"] = value["is_immediate"]
    if "post_remediation_steps" in value:
        import capo_securityhub.types.remediation_string_list

        out["PostRemediationSteps"] = (
            capo_securityhub.types.remediation_string_list.serialize_json(
                value["post_remediation_steps"]
            )
        )
    if "kb_articles" in value:
        import capo_securityhub.types.kb_article_list

        out["KbArticles"] = capo_securityhub.types.kb_article_list.serialize_json(
            value["kb_articles"]
        )
    return out


def deserialize_json(data: dict) -> RemediationSummaryDetail:
    out: RemediationSummaryDetail = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("IsImmediate") is not None:
        out["is_immediate"] = data["IsImmediate"]
    if data.get("PostRemediationSteps") is not None:
        import capo_securityhub.types.remediation_string_list

        out["post_remediation_steps"] = (
            capo_securityhub.types.remediation_string_list.deserialize_json(
                data["PostRemediationSteps"]
            )
        )
    if data.get("KbArticles") is not None:
        import capo_securityhub.types.kb_article_list

        out["kb_articles"] = capo_securityhub.types.kb_article_list.deserialize_json(
            data["KbArticles"]
        )
    return out
