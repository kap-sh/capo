"""Generated from Smithy shape ``com.amazonaws.kendraranking#Document``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra_ranking.types.body_tokens_list
    import capo_kendra_ranking.types.document_body
    import capo_kendra_ranking.types.document_id
    import capo_kendra_ranking.types.document_title
    import capo_kendra_ranking.types.float
    import capo_kendra_ranking.types.group_id
    import capo_kendra_ranking.types.title_tokens_list


class Document(TypedDict, closed=True):
    id: "capo_kendra_ranking.types.document_id.DocumentId"
    """<p>The identifier of the document from the search service.</p>"""
    group_id: NotRequired["capo_kendra_ranking.types.group_id.GroupId"]
    """<p>The optional group identifier of the document from the search service. Documents with the same group identifier are grouped together and processed as one document within the service.</p>"""
    title: NotRequired["capo_kendra_ranking.types.document_title.DocumentTitle"]
    """<p>The title of the search service's document.</p>"""
    body: NotRequired["capo_kendra_ranking.types.document_body.DocumentBody"]
    """<p>The body text of the search service's document.</p>"""
    tokenized_title: NotRequired[
        "capo_kendra_ranking.types.title_tokens_list.TitleTokensList"
    ]
    """<p>The title of the search service's document represented as a list of tokens or words. You must choose to provide <code>Title</code> or <code>TokenizedTitle</code>. You cannot provide both.</p>"""
    tokenized_body: NotRequired[
        "capo_kendra_ranking.types.body_tokens_list.BodyTokensList"
    ]
    """<p>The body text of the search service's document represented as a list of tokens or words. You must choose to provide <code>Body</code> or <code>TokenizedBody</code>. You cannot provide both.</p>"""
    original_score: "capo_kendra_ranking.types.float.Float"
    """<p>The original document score or rank from the search service. Amazon Kendra Intelligent Ranking gives the document a new score or rank based on its intelligent search algorithms.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Document) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "body" in value:
        out["Body"] = value["body"]
    if "tokenized_title" in value:
        import capo_kendra_ranking.types.title_tokens_list

        out["TokenizedTitle"] = (
            capo_kendra_ranking.types.title_tokens_list.serialize_aws_json_1_0(
                value["tokenized_title"]
            )
        )
    if "tokenized_body" in value:
        import capo_kendra_ranking.types.body_tokens_list

        out["TokenizedBody"] = (
            capo_kendra_ranking.types.body_tokens_list.serialize_aws_json_1_0(
                value["tokenized_body"]
            )
        )
    out["OriginalScore"] = (
        "NaN"
        if value["original_score"] != value["original_score"]
        else "Infinity"
        if value["original_score"] == float("inf")
        else "-Infinity"
        if value["original_score"] == float("-inf")
        else value["original_score"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> Document:
    out: Document = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    if data.get("TokenizedTitle") is not None:
        import capo_kendra_ranking.types.title_tokens_list

        out["tokenized_title"] = (
            capo_kendra_ranking.types.title_tokens_list.deserialize_aws_json_1_0(
                data["TokenizedTitle"]
            )
        )
    if data.get("TokenizedBody") is not None:
        import capo_kendra_ranking.types.body_tokens_list

        out["tokenized_body"] = (
            capo_kendra_ranking.types.body_tokens_list.deserialize_aws_json_1_0(
                data["TokenizedBody"]
            )
        )
    if data.get("OriginalScore") is not None:
        out["original_score"] = float(data["OriginalScore"])
    else:
        out["original_score"] = 0.0
    return out
