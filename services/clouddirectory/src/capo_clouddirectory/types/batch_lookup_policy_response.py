"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchLookupPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.policy_to_path_list


class BatchLookupPolicyResponse(TypedDict, closed=True):
    policy_to_path_list: NotRequired[
        "capo_clouddirectory.types.policy_to_path_list.PolicyToPathList"
    ]
    """<p>Provides list of path to policies. Policies contain <code>PolicyId</code>, <code>ObjectIdentifier</code>, and <code>PolicyType</code>. For more information, see <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies">Policies</a>.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchLookupPolicyResponse) -> dict:
    out: dict = {}
    if "policy_to_path_list" in value:
        import capo_clouddirectory.types.policy_to_path_list

        out["PolicyToPathList"] = (
            capo_clouddirectory.types.policy_to_path_list.serialize_json(
                value["policy_to_path_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> BatchLookupPolicyResponse:
    out: BatchLookupPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("PolicyToPathList") is not None:
        import capo_clouddirectory.types.policy_to_path_list

        out["policy_to_path_list"] = (
            capo_clouddirectory.types.policy_to_path_list.deserialize_json(
                data["PolicyToPathList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
