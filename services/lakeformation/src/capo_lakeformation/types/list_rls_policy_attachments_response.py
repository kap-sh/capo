"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListRLSPolicyAttachmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.rls_policy_attachment_list
    import capo_lakeformation.types.token


class ListRLSPolicyAttachmentsResponse(TypedDict, closed=True):
    rls_policy_attachments: NotRequired[
        "capo_lakeformation.types.rls_policy_attachment_list.RLSPolicyAttachmentList"
    ]
    """<p>A list of <code>RLSPolicyAttachment</code> structures.</p>"""
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token, if not all attachments have been returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRLSPolicyAttachmentsResponse) -> dict:
    out: dict = {}
    if "rls_policy_attachments" in value:
        import capo_lakeformation.types.rls_policy_attachment_list

        out["RLSPolicyAttachments"] = (
            capo_lakeformation.types.rls_policy_attachment_list.serialize_json(
                value["rls_policy_attachments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRLSPolicyAttachmentsResponse:
    out: ListRLSPolicyAttachmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("RLSPolicyAttachments") is not None:
        import capo_lakeformation.types.rls_policy_attachment_list

        out["rls_policy_attachments"] = (
            capo_lakeformation.types.rls_policy_attachment_list.deserialize_json(
                data["RLSPolicyAttachments"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
