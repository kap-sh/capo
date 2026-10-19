"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#IssueDetectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.rule_name


class IssueDetectionConfiguration(TypedDict, closed=True):
    rule_name: "capo_chime_sdk_media_pipelines.types.rule_name.RuleName"
    """<p>The name of the issue detection rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IssueDetectionConfiguration) -> dict:
    out: dict = {}
    out["RuleName"] = value["rule_name"]
    return out


def deserialize_json(data: dict) -> IssueDetectionConfiguration:
    out: IssueDetectionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    else:
        out["rule_name"] = ""
    return out
