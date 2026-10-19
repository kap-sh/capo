"""Generated from Smithy shape ``com.amazonaws.detective#UpdateOrganizationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.boolean
    import capo_detective.types.graph_arn


class UpdateOrganizationConfigurationRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the organization behavior graph.</p>"""
    auto_enable: NotRequired["capo_detective.types.boolean.Boolean"]
    """<p>Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOrganizationConfigurationRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    if "auto_enable" in value:
        out["AutoEnable"] = value["auto_enable"]
    return out


def deserialize_json(data: dict) -> UpdateOrganizationConfigurationRequest:
    out: UpdateOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("GraphArn") is not None:
        out["graph_arn"] = data["GraphArn"]
    else:
        out["graph_arn"] = ""
    if data.get("AutoEnable") is not None:
        out["auto_enable"] = data["AutoEnable"]
    return out
