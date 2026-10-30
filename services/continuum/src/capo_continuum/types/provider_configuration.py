"""Generated from Smithy shape ``com.amazonaws.continuum#ProviderConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_continuum.errors import DeserializationError, SerializationError
from capo_continuum.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_continuum.types.git_hub_configuration
    import capo_continuum.types.git_lab_configuration
    import capo_continuum.types.s3_configuration


class ProviderConfigurationGithubMember(TypedDict, closed=True):
    github: "capo_continuum.types.git_hub_configuration.GitHubConfiguration"


class ProviderConfigurationGitlabMember(TypedDict, closed=True):
    gitlab: "capo_continuum.types.git_lab_configuration.GitLabConfiguration"


class ProviderConfigurationS3Member(TypedDict, closed=True):
    s3: "capo_continuum.types.s3_configuration.S3Configuration"


ProviderConfiguration: TypeAlias = (
    ProviderConfigurationGithubMember
    | ProviderConfigurationGitlabMember
    | ProviderConfigurationS3Member
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProviderConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "github" in value:
        import capo_continuum.types.git_hub_configuration

        return {
            "github": capo_continuum.types.git_hub_configuration.serialize_json(
                value["github"]
            )
        }
    elif "gitlab" in value:
        import capo_continuum.types.git_lab_configuration

        return {
            "gitlab": capo_continuum.types.git_lab_configuration.serialize_json(
                value["gitlab"]
            )
        }
    elif "s3" in value:
        import capo_continuum.types.s3_configuration

        return {"s3": capo_continuum.types.s3_configuration.serialize_json(value["s3"])}
    else:
        raise SerializationError("ProviderConfiguration: no variant present")


def deserialize_json(data: dict) -> ProviderConfiguration:
    if data.get("github") is not None:
        import capo_continuum.types.git_hub_configuration

        return {
            "github": capo_continuum.types.git_hub_configuration.deserialize_json(
                data["github"]
            )
        }
    elif data.get("gitlab") is not None:
        import capo_continuum.types.git_lab_configuration

        return {
            "gitlab": capo_continuum.types.git_lab_configuration.deserialize_json(
                data["gitlab"]
            )
        }
    elif data.get("s3") is not None:
        import capo_continuum.types.s3_configuration

        return {
            "s3": capo_continuum.types.s3_configuration.deserialize_json(data["s3"])
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ProviderConfiguration: no recognized variant key")


def redact_sensitive(value: ProviderConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "github" in value:
        import capo_continuum.types.git_hub_configuration

        out["github"] = capo_continuum.types.git_hub_configuration.redact_sensitive(
            value["github"]
        )
    if "gitlab" in value:
        import capo_continuum.types.git_lab_configuration

        out["gitlab"] = capo_continuum.types.git_lab_configuration.redact_sensitive(
            value["gitlab"]
        )
    if "s3" in value:
        import capo_continuum.types.s3_configuration

        out["s3"] = capo_continuum.types.s3_configuration.redact_sensitive(value["s3"])
    return out
