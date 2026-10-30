"""Generated from Smithy shape ``com.amazonaws.continuum#EnvironmentSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_repository_sources
    import capo_continuum.types.environment_s3_sources


class EnvironmentSourceConfiguration(TypedDict, closed=True):
    s3_sources: NotRequired[
        "capo_continuum.types.environment_s3_sources.EnvironmentS3Sources"
    ]
    """S3 sources backed by previously-created S3 integrations."""
    repository_sources: NotRequired[
        "capo_continuum.types.environment_repository_sources.EnvironmentRepositorySources"
    ]
    """Explicit repository selections from previously-created integrations."""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentSourceConfiguration) -> dict:
    out: dict = {}
    if "s3_sources" in value:
        import capo_continuum.types.environment_s3_sources

        out["s3Sources"] = capo_continuum.types.environment_s3_sources.serialize_json(
            value["s3_sources"]
        )
    if "repository_sources" in value:
        import capo_continuum.types.environment_repository_sources

        out["repositorySources"] = (
            capo_continuum.types.environment_repository_sources.serialize_json(
                value["repository_sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnvironmentSourceConfiguration:
    out: EnvironmentSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("s3Sources") is not None:
        import capo_continuum.types.environment_s3_sources

        out["s3_sources"] = (
            capo_continuum.types.environment_s3_sources.deserialize_json(
                data["s3Sources"]
            )
        )
    if data.get("repositorySources") is not None:
        import capo_continuum.types.environment_repository_sources

        out["repository_sources"] = (
            capo_continuum.types.environment_repository_sources.deserialize_json(
                data["repositorySources"]
            )
        )
    return out
