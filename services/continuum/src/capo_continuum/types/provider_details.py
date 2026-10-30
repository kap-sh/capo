"""Generated from Smithy shape ``com.amazonaws.continuum#ProviderDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_continuum.errors import DeserializationError, SerializationError
from capo_continuum.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_continuum.types.git_hub_details
    import capo_continuum.types.git_lab_details
    import capo_continuum.types.s3_details


class ProviderDetailsGithubMember(TypedDict, closed=True):
    github: "capo_continuum.types.git_hub_details.GitHubDetails"


class ProviderDetailsGitlabMember(TypedDict, closed=True):
    gitlab: "capo_continuum.types.git_lab_details.GitLabDetails"


class ProviderDetailsS3Member(TypedDict, closed=True):
    s3: "capo_continuum.types.s3_details.S3Details"


ProviderDetails: TypeAlias = (
    ProviderDetailsGithubMember
    | ProviderDetailsGitlabMember
    | ProviderDetailsS3Member
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProviderDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "github" in value:
        import capo_continuum.types.git_hub_details

        return {
            "github": capo_continuum.types.git_hub_details.serialize_json(
                value["github"]
            )
        }
    elif "gitlab" in value:
        import capo_continuum.types.git_lab_details

        return {
            "gitlab": capo_continuum.types.git_lab_details.serialize_json(
                value["gitlab"]
            )
        }
    elif "s3" in value:
        import capo_continuum.types.s3_details

        return {"s3": capo_continuum.types.s3_details.serialize_json(value["s3"])}
    else:
        raise SerializationError("ProviderDetails: no variant present")


def deserialize_json(data: dict) -> ProviderDetails:
    if data.get("github") is not None:
        import capo_continuum.types.git_hub_details

        return {
            "github": capo_continuum.types.git_hub_details.deserialize_json(
                data["github"]
            )
        }
    elif data.get("gitlab") is not None:
        import capo_continuum.types.git_lab_details

        return {
            "gitlab": capo_continuum.types.git_lab_details.deserialize_json(
                data["gitlab"]
            )
        }
    elif data.get("s3") is not None:
        import capo_continuum.types.s3_details

        return {"s3": capo_continuum.types.s3_details.deserialize_json(data["s3"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ProviderDetails: no recognized variant key")
