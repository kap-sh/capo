"""Generated from Smithy shape ``com.amazonaws.healthlake#StarterProfileSource``."""

from typing_extensions import TypedDict


class StarterProfileSource(TypedDict, closed=True):
    starter_profile_name: "str"
    """<p>The name of the built-in starter profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StarterProfileSource) -> dict:
    out: dict = {}
    out["StarterProfileName"] = value["starter_profile_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StarterProfileSource:
    out: StarterProfileSource = {}  # type: ignore[typeddict-item]
    if data.get("StarterProfileName") is not None:
        out["starter_profile_name"] = data["StarterProfileName"]
    else:
        out["starter_profile_name"] = ""
    return out
