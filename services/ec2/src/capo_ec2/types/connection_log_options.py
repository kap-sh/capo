"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionLogOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string


class ConnectionLogOptions(TypedDict, closed=True):
    enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether connection logging is enabled.</p>"""
    cloudwatch_log_group: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the CloudWatch Logs log group. Required if connection logging is enabled.</p>"""
    cloudwatch_log_stream: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the CloudWatch Logs log stream to which the connection data is published.</p>"""
    include_authorization_policy_context: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to include the authorization policy evaluation context in the connection logs for the Client VPN endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ConnectionLogOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))
    if "cloudwatch_log_group" in value:
        pairs.append(
            (f"{key_prefix}CloudwatchLogGroup", str(value["cloudwatch_log_group"]))
        )
    if "cloudwatch_log_stream" in value:
        pairs.append(
            (f"{key_prefix}CloudwatchLogStream", str(value["cloudwatch_log_stream"]))
        )
    if "include_authorization_policy_context" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeAuthorizationPolicyContext",
                "true" if value["include_authorization_policy_context"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> ConnectionLogOptions:
    out: ConnectionLogOptions = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_cloudwatch_log_group = el.find("CloudwatchLogGroup")
    if child_cloudwatch_log_group is not None:
        out["cloudwatch_log_group"] = str(child_cloudwatch_log_group.text or "")
    child_cloudwatch_log_stream = el.find("CloudwatchLogStream")
    if child_cloudwatch_log_stream is not None:
        out["cloudwatch_log_stream"] = str(child_cloudwatch_log_stream.text or "")
    child_include_authorization_policy_context = el.find(
        "IncludeAuthorizationPolicyContext"
    )
    if child_include_authorization_policy_context is not None:
        out["include_authorization_policy_context"] = (
            child_include_authorization_policy_context.text or ""
        ).lower() == "true"
    return out
