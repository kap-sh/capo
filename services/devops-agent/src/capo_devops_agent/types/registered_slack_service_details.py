"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredSlackServiceDetails``."""

from typing_extensions import TypedDict


class RegisteredSlackServiceDetails(TypedDict, closed=True):
    team_id: "str"
    """<p>The Slack team ID.</p>"""
    team_name: "str"
    """<p>The Slack team name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredSlackServiceDetails) -> dict:
    out: dict = {}
    out["teamId"] = value["team_id"]
    out["teamName"] = value["team_name"]
    return out


def deserialize_json(data: dict) -> RegisteredSlackServiceDetails:
    out: RegisteredSlackServiceDetails = {}  # type: ignore[typeddict-item]
    if data.get("teamId") is not None:
        out["team_id"] = data["teamId"]
    else:
        out["team_id"] = ""
    if data.get("teamName") is not None:
        out["team_name"] = data["teamName"]
    else:
        out["team_name"] = ""
    return out
