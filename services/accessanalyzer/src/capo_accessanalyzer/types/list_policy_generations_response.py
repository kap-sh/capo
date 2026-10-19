"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListPolicyGenerationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.policy_generation_list
    import capo_accessanalyzer.types.token


class ListPolicyGenerationsResponse(TypedDict, closed=True):
    policy_generations: (
        "capo_accessanalyzer.types.policy_generation_list.PolicyGenerationList"
    )
    """<p>A <code>PolicyGeneration</code> object that contains details about the generated policy.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyGenerationsResponse) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.policy_generation_list

    out["policyGenerations"] = (
        capo_accessanalyzer.types.policy_generation_list.serialize_json(
            value["policy_generations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPolicyGenerationsResponse:
    out: ListPolicyGenerationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyGenerations") is not None:
        import capo_accessanalyzer.types.policy_generation_list

        out["policy_generations"] = (
            capo_accessanalyzer.types.policy_generation_list.deserialize_json(
                data["policyGenerations"]
            )
        )
    else:
        out["policy_generations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
