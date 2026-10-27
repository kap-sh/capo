"""Generated from Smithy shape ``com.amazonaws.ivs#FailoverSlateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.failover_slate_activation_threshold_seconds
    import capo_ivs.types.failover_slate_configuration_arn
    import capo_ivs.types.failover_slate_configuration_name
    import capo_ivs.types.failover_slate_configuration_state
    import capo_ivs.types.failover_slate_max_display_seconds
    import capo_ivs.types.failover_slate_min_display_seconds
    import capo_ivs.types.tags


class FailoverSlateConfiguration(TypedDict, closed=True):
    arn: "capo_ivs.types.failover_slate_configuration_arn.FailoverSlateConfigurationArn"
    """<p>Failover-slate-configuration ARN.</p>"""
    name: NotRequired[
        "capo_ivs.types.failover_slate_configuration_name.FailoverSlateConfigurationName"
    ]
    """<p>Failover-slate-configuration name.</p>"""
    activation_threshold_seconds: NotRequired[
        "capo_ivs.types.failover_slate_activation_threshold_seconds.FailoverSlateActivationThresholdSeconds"
    ]
    """<p>Number of seconds of ingest interruption before the failover slate activates. Minimum: <code>3</code>. Maximum: <code>5</code>. Default: <code>3</code>.</p>"""
    min_slate_display_seconds: NotRequired[
        "capo_ivs.types.failover_slate_min_display_seconds.FailoverSlateMinDisplaySeconds"
    ]
    """<p>Minimum number of seconds that the failover slate displays after activation. Minimum: <code>3</code>. Maximum: <code>10</code>. Default: <code>3</code>.</p>"""
    max_slate_display_seconds: NotRequired[
        "capo_ivs.types.failover_slate_max_display_seconds.FailoverSlateMaxDisplaySeconds"
    ]
    """<p>Maximum number of seconds that the failover slate displays. Minimum: <code>60</code>. Maximum: <code>180</code>. Default: <code>60</code>.</p>"""
    state: "capo_ivs.types.failover_slate_configuration_state.FailoverSlateConfigurationState"
    """<p>Current state of the failover slate configuration.</p>"""
    tags: NotRequired["capo_ivs.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailoverSlateConfiguration) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "activation_threshold_seconds" in value:
        out["activationThresholdSeconds"] = value["activation_threshold_seconds"]
    if "min_slate_display_seconds" in value:
        out["minSlateDisplaySeconds"] = value["min_slate_display_seconds"]
    if "max_slate_display_seconds" in value:
        out["maxSlateDisplaySeconds"] = value["max_slate_display_seconds"]
    out["state"] = value["state"]
    if "tags" in value:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> FailoverSlateConfiguration:
    out: FailoverSlateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("activationThresholdSeconds") is not None:
        out["activation_threshold_seconds"] = data["activationThresholdSeconds"]
    if data.get("minSlateDisplaySeconds") is not None:
        out["min_slate_display_seconds"] = data["minSlateDisplaySeconds"]
    if data.get("maxSlateDisplaySeconds") is not None:
        out["max_slate_display_seconds"] = data["maxSlateDisplaySeconds"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    if data.get("tags") is not None:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.deserialize_json(data["tags"])
    return out
