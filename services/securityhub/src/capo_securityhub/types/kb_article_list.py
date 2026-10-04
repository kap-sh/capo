"""Generated from Smithy shape ``com.amazonaws.securityhub#KbArticleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.kb_article

KbArticleList: TypeAlias = list["capo_securityhub.types.kb_article.KbArticle"]


# --- restJson1 ser/de ---
def serialize_json(value: KbArticleList) -> list:
    import capo_securityhub.types.kb_article

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.kb_article.serialize_json(item))
    return out


def deserialize_json(data: list) -> KbArticleList:
    import capo_securityhub.types.kb_article

    out: KbArticleList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.kb_article.deserialize_json(item))
    return out
