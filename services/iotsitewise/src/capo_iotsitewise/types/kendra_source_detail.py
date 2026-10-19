"""Generated from Smithy shape ``com.amazonaws.iotsitewise#KendraSourceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn


class KendraSourceDetail(TypedDict, closed=True):
    knowledge_base_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <code>knowledgeBaseArn</code> details for the Kendra dataset source.</p>"""
    role_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <code>roleARN</code> details for the Kendra dataset source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KendraSourceDetail) -> dict:
    out: dict = {}
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> KendraSourceDetail:
    out: KendraSourceDetail = {}  # type: ignore[typeddict-item]
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        out["knowledge_base_arn"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
