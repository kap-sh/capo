"""Generated from Smithy shape ``com.amazonaws.lambdacore#Platform``."""

from typing_extensions import TypedDict


class Platform(TypedDict, closed=True):
    architecture: "str"
    """The CPU architecture of the platform, for example x86_64 or arm64."""
    os: "str"
    """The operating system of the platform."""
    digest: "str"
    """The content digest of the platform-specific image."""


# --- restJson1 ser/de ---
def serialize_json(value: Platform) -> dict:
    out: dict = {}
    out["Architecture"] = value["architecture"]
    out["Os"] = value["os"]
    out["Digest"] = value["digest"]
    return out


def deserialize_json(data: dict) -> Platform:
    out: Platform = {}  # type: ignore[typeddict-item]
    if data.get("Architecture") is not None:
        out["architecture"] = data["Architecture"]
    else:
        out["architecture"] = ""
    if data.get("Os") is not None:
        out["os"] = data["Os"]
    else:
        out["os"] = ""
    if data.get("Digest") is not None:
        out["digest"] = data["Digest"]
    else:
        out["digest"] = ""
    return out
