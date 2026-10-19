"""Generated from Smithy shape ``com.amazonaws.amplify#SubDomainSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.branch_name
    import capo_amplify.types.domain_prefix


class SubDomainSetting(TypedDict, closed=True):
    prefix: "capo_amplify.types.domain_prefix.DomainPrefix"
    """<p> The prefix setting for the subdomain. </p>"""
    branch_name: "capo_amplify.types.branch_name.BranchName"
    """<p> The branch name setting for the subdomain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubDomainSetting) -> dict:
    out: dict = {}
    out["prefix"] = value["prefix"]
    out["branchName"] = value["branch_name"]
    return out


def deserialize_json(data: dict) -> SubDomainSetting:
    out: SubDomainSetting = {}  # type: ignore[typeddict-item]
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    else:
        out["prefix"] = ""
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    else:
        out["branch_name"] = ""
    return out
