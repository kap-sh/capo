"""Generated from Smithy shape ``com.amazonaws.ses#ListIdentityPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.policy_name_list


class ListIdentityPoliciesResponse(TypedDict, closed=True):
    policy_names: "capo_ses.types.policy_name_list.PolicyNameList"
    """<p>A list of names of policies that apply to the specified identity.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListIdentityPoliciesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.policy_name_list

    capo_ses.types.policy_name_list.serialize_query(
        value["policy_names"], pairs, f"{key_prefix}PolicyNames"
    )


def deserialize_query(el: Element) -> ListIdentityPoliciesResponse:
    out: ListIdentityPoliciesResponse = {}  # type: ignore[typeddict-item]
    child_policy_names = el.find("PolicyNames")
    if child_policy_names is not None:
        import capo_ses.types.policy_name_list

        out["policy_names"] = capo_ses.types.policy_name_list.deserialize_query(
            child_policy_names
        )
    else:
        out["policy_names"] = []
    return out
