"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CloudWatchLogGroupLogDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.cloud_watch_log_group_arn
    import capo_lex_models_v2.types.log_prefix


class CloudWatchLogGroupLogDestination(TypedDict, closed=True):
    cloud_watch_log_group_arn: (
        "capo_lex_models_v2.types.cloud_watch_log_group_arn.CloudWatchLogGroupArn"
    )
    """<p>The Amazon Resource Name (ARN) of the log group where text and metadata logs are delivered.</p>"""
    log_prefix: "capo_lex_models_v2.types.log_prefix.LogPrefix"
    """<p>The prefix of the log stream name within the log group that you specified </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogGroupLogDestination) -> dict:
    out: dict = {}
    out["cloudWatchLogGroupArn"] = value["cloud_watch_log_group_arn"]
    out["logPrefix"] = value["log_prefix"]
    return out


def deserialize_json(data: dict) -> CloudWatchLogGroupLogDestination:
    out: CloudWatchLogGroupLogDestination = {}  # type: ignore[typeddict-item]
    if data.get("cloudWatchLogGroupArn") is not None:
        out["cloud_watch_log_group_arn"] = data["cloudWatchLogGroupArn"]
    else:
        out["cloud_watch_log_group_arn"] = ""
    if data.get("logPrefix") is not None:
        out["log_prefix"] = data["logPrefix"]
    else:
        out["log_prefix"] = ""
    return out
