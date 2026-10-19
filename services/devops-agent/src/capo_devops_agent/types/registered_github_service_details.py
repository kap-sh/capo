"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredGithubServiceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.github_repo_owner_type


class RegisteredGithubServiceDetails(TypedDict, closed=True):
    owner: "str"
    """<p>The GitHub repository owner name.</p>"""
    owner_type: "capo_devops_agent.types.github_repo_owner_type.GithubRepoOwnerType"
    """<p>The GitHub repository owner type.</p>"""
    target_url: NotRequired["str"]
    """<p>The GitHub Enterprise Server instance URL (absent for github.com).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredGithubServiceDetails) -> dict:
    out: dict = {}
    out["owner"] = value["owner"]
    import capo_devops_agent.types.github_repo_owner_type

    out["ownerType"] = capo_devops_agent.types.github_repo_owner_type.serialize_json(
        value["owner_type"]
    )
    if "target_url" in value:
        out["targetUrl"] = value["target_url"]
    return out


def deserialize_json(data: dict) -> RegisteredGithubServiceDetails:
    out: RegisteredGithubServiceDetails = {}  # type: ignore[typeddict-item]
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    else:
        out["owner"] = ""
    if data.get("ownerType") is not None:
        import capo_devops_agent.types.github_repo_owner_type

        out["owner_type"] = (
            capo_devops_agent.types.github_repo_owner_type.deserialize_json(
                data["ownerType"]
            )
        )
    else:
        import typing

        out["owner_type"] = typing.cast(
            "capo_devops_agent.types.github_repo_owner_type.GithubRepoOwnerType", ""
        )
    if data.get("targetUrl") is not None:
        out["target_url"] = data["targetUrl"]
    return out
