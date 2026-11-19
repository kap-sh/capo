"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AutoRemediation``."""

from typing_extensions import NotRequired, TypedDict


class AutoRemediation(TypedDict, closed=True):
    deep_link: NotRequired["str"]
    """<p>A deep link to the SSM runbook execution page in the AWS Management Console for this resource, with the execution parameters prefilled.</p>"""
    cli_command: NotRequired["str"]
    """<p>The AWS CLI command that triggers the same SSM runbook execution for this resource. You can copy and run this command as-is.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoRemediation) -> dict:
    out: dict = {}
    if "deep_link" in value:
        out["deepLink"] = value["deep_link"]
    if "cli_command" in value:
        out["cliCommand"] = value["cli_command"]
    return out


def deserialize_json(data: dict) -> AutoRemediation:
    out: AutoRemediation = {}  # type: ignore[typeddict-item]
    if data.get("deepLink") is not None:
        out["deep_link"] = data["deepLink"]
    if data.get("cliCommand") is not None:
        out["cli_command"] = data["cliCommand"]
    return out
