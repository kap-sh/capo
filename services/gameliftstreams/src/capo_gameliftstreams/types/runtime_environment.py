"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#RuntimeEnvironment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.runtime_environment_type
    import capo_gameliftstreams.types.runtime_environment_version


class RuntimeEnvironment(TypedDict, closed=True):
    type: "capo_gameliftstreams.types.runtime_environment_type.RuntimeEnvironmentType"
    """<p>The operating system and other drivers. For Proton, this also includes the Proton compatibility layer.</p>"""
    version: "capo_gameliftstreams.types.runtime_environment_version.RuntimeEnvironmentVersion"
    """<p>Versioned container environment for the application operating system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeEnvironment) -> dict:
    out: dict = {}
    import capo_gameliftstreams.types.runtime_environment_type

    out["Type"] = capo_gameliftstreams.types.runtime_environment_type.serialize_json(
        value["type"]
    )
    out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> RuntimeEnvironment:
    out: RuntimeEnvironment = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_gameliftstreams.types.runtime_environment_type

        out["type"] = (
            capo_gameliftstreams.types.runtime_environment_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_gameliftstreams.types.runtime_environment_type.RuntimeEnvironmentType",
            "",
        )
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = ""
    return out
