"""Generated from Smithy shape ``com.amazonaws.ivs#UpdateFailoverSlateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.failover_slate_activation_threshold_seconds
    import capo_ivs.types.failover_slate_configuration_arn
    import capo_ivs.types.failover_slate_configuration_name
    import capo_ivs.types.failover_slate_max_display_seconds
    import capo_ivs.types.failover_slate_min_display_seconds


class UpdateFailoverSlateConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs.types.failover_slate_configuration_arn.FailoverSlateConfigurationArn"
    """<p>ARN of the failover slate configuration to be updated.</p>"""
    name: NotRequired[
        "capo_ivs.types.failover_slate_configuration_name.FailoverSlateConfigurationName"
    ]
    """<p>Failover-slate-configuration name. The value does not need to be unique.</p>"""
    activation_threshold_seconds: NotRequired[
        "capo_ivs.types.failover_slate_activation_threshold_seconds.FailoverSlateActivationThresholdSeconds"
    ]
    """<p>Number of seconds of ingest interruption before the failover slate activates. Default: <code>3</code>.</p>"""
    min_slate_display_seconds: NotRequired[
        "capo_ivs.types.failover_slate_min_display_seconds.FailoverSlateMinDisplaySeconds"
    ]
    """<p>Minimum number of seconds that the failover slate displays after activation. Default: <code>3</code>.</p>"""
    max_slate_display_seconds: NotRequired[
        "capo_ivs.types.failover_slate_max_display_seconds.FailoverSlateMaxDisplaySeconds"
    ]
    """<p>Maximum number of seconds that the failover slate displays. Default: <code>60</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFailoverSlateConfigurationRequest) -> dict:
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
    return out


def deserialize_json(data: dict) -> UpdateFailoverSlateConfigurationRequest:
    out: UpdateFailoverSlateConfigurationRequest = {}  # type: ignore[typeddict-item]
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
    return out
