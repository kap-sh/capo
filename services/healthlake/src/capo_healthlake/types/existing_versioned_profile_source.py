"""Generated from Smithy shape ``com.amazonaws.healthlake#ExistingVersionedProfileSource``."""

from typing_extensions import TypedDict


class ExistingVersionedProfileSource(TypedDict, closed=True):
    profile_id: "str"
    """<p>The unique identifier of the existing profile to clone from.</p>"""
    version: "int"
    """<p>The version number of the existing profile to clone from.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExistingVersionedProfileSource) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExistingVersionedProfileSource:
    out: ExistingVersionedProfileSource = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    return out
