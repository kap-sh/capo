"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetCodeReviewsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.code_review_id_list


class BatchGetCodeReviewsInput(TypedDict, closed=True):
    code_review_ids: "capo_securityagent.types.code_review_id_list.CodeReviewIdList"
    """<p>The list of code review identifiers to retrieve.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the code reviews.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCodeReviewsInput) -> dict:
    out: dict = {}
    import capo_securityagent.types.code_review_id_list

    out["codeReviewIds"] = capo_securityagent.types.code_review_id_list.serialize_json(
        value["code_review_ids"]
    )
    out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> BatchGetCodeReviewsInput:
    out: BatchGetCodeReviewsInput = {}  # type: ignore[typeddict-item]
    if data.get("codeReviewIds") is not None:
        import capo_securityagent.types.code_review_id_list

        out["code_review_ids"] = (
            capo_securityagent.types.code_review_id_list.deserialize_json(
                data["codeReviewIds"]
            )
        )
    else:
        out["code_review_ids"] = []
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    return out
