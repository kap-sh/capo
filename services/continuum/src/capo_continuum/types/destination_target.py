"""Generated from Smithy shape ``com.amazonaws.continuum#DestinationTarget``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_continuum.errors import DeserializationError, SerializationError
from capo_continuum.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_continuum.types.git_hub_target
    import capo_continuum.types.s3_target


class DestinationTargetS3Member(TypedDict, closed=True):
    s3: "capo_continuum.types.s3_target.S3Target"


class DestinationTargetGithubMember(TypedDict, closed=True):
    github: "capo_continuum.types.git_hub_target.GitHubTarget"


DestinationTarget: TypeAlias = (
    DestinationTargetS3Member | DestinationTargetGithubMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DestinationTarget) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DestinationTarget: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_continuum.types.s3_target

        return {"s3": capo_continuum.types.s3_target.serialize_json(value["s3"])}
    elif "github" in value:
        import capo_continuum.types.git_hub_target

        return {
            "github": capo_continuum.types.git_hub_target.serialize_json(
                value["github"]
            )
        }
    else:
        raise SerializationError("DestinationTarget: no variant present")


def deserialize_json(data: dict) -> DestinationTarget:
    if data.get("s3") is not None:
        import capo_continuum.types.s3_target

        return {"s3": capo_continuum.types.s3_target.deserialize_json(data["s3"])}
    elif data.get("github") is not None:
        import capo_continuum.types.git_hub_target

        return {
            "github": capo_continuum.types.git_hub_target.deserialize_json(
                data["github"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DestinationTarget: no recognized variant key")
