"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#VersionCreatedBySource``."""

from typing_extensions import NotRequired, TypedDict


class VersionCreatedBySource(TypedDict, closed=True):
    name: "str"
    """<p>The name of the source (for example, <code>user</code>, <code>optimization-job</code>, or <code>system</code>).</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the source, if applicable (for example, a user ARN or optimization job ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VersionCreatedBySource) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> VersionCreatedBySource:
    out: VersionCreatedBySource = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
