"""Generated from Smithy shape ``com.amazonaws.devopsagent#ApprovalPattern``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.approval_argument_pins
    import capo_devops_agent.types.tool_identifier


class ApprovalPattern(TypedDict, closed=True):
    tool: "capo_devops_agent.types.tool_identifier.ToolIdentifier"
    """<p>Identifier of the tool the pattern applies to (e.g. `use_aws` for AWS actions, or a third-party tool name).</p>"""
    argument_pins: "capo_devops_agent.types.approval_argument_pins.ApprovalArgumentPins"
    """<p>Argument constraints that narrow which tool invocations the pattern matches. For AWS tools, the map must include `operation` (the IAM action, e.g. `ec2:AuthorizeSecurityGroupIngress`) and `resource_arn` (the resource ARN or ARN glob); additional narrowing arguments go in further pin keys. The same `{tool, argumentPins}` shape is used uniformly for AWS and third-party tools, with tool-specific keys for third-party tools. Requests whose argument pins are collectively too large are rejected with a ValidationException.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalPattern) -> dict:
    out: dict = {}
    out["tool"] = value["tool"]
    import capo_devops_agent.types.approval_argument_pins

    out["argumentPins"] = capo_devops_agent.types.approval_argument_pins.serialize_json(
        value["argument_pins"]
    )
    return out


def deserialize_json(data: dict) -> ApprovalPattern:
    out: ApprovalPattern = {}  # type: ignore[typeddict-item]
    if data.get("tool") is not None:
        out["tool"] = data["tool"]
    else:
        out["tool"] = ""
    if data.get("argumentPins") is not None:
        import capo_devops_agent.types.approval_argument_pins

        out["argument_pins"] = (
            capo_devops_agent.types.approval_argument_pins.deserialize_json(
                data["argumentPins"]
            )
        )
    else:
        out["argument_pins"] = {}
    return out
