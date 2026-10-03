"""Generated from Smithy shape ``com.amazonaws.rds#ScalingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class ScalingConfiguration(TypedDict, closed=True):
    min_capacity: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The minimum capacity for an Aurora DB cluster in <code>serverless</code> DB engine mode.</p> <p>For Aurora MySQL, valid capacity values are <code>1</code>, <code>2</code>, <code>4</code>, <code>8</code>, <code>16</code>, <code>32</code>, <code>64</code>, <code>128</code>, and <code>256</code>.</p> <p>For Aurora PostgreSQL, valid capacity values are <code>2</code>, <code>4</code>, <code>8</code>, <code>16</code>, <code>32</code>, <code>64</code>, <code>192</code>, and <code>384</code>.</p> <p>The minimum capacity must be less than or equal to the maximum capacity.</p>"""
    max_capacity: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum capacity for an Aurora DB cluster in <code>serverless</code> DB engine mode.</p> <p>For Aurora MySQL, valid capacity values are <code>1</code>, <code>2</code>, <code>4</code>, <code>8</code>, <code>16</code>, <code>32</code>, <code>64</code>, <code>128</code>, and <code>256</code>.</p> <p>For Aurora PostgreSQL, valid capacity values are <code>2</code>, <code>4</code>, <code>8</code>, <code>16</code>, <code>32</code>, <code>64</code>, <code>192</code>, and <code>384</code>.</p> <p>The maximum capacity must be greater than or equal to the minimum capacity.</p>"""
    auto_pause: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether to allow or disallow automatic pause for an Aurora DB cluster in <code>serverless</code> DB engine mode. A DB cluster can be paused only when it's idle (it has no connections).</p> <note> <p>If a DB cluster is paused for more than seven days, the DB cluster might be backed up with a snapshot. In this case, the DB cluster is restored when there is a request to connect to it.</p> </note>"""
    seconds_until_auto_pause: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The time, in seconds, before an Aurora DB cluster in <code>serverless</code> mode is paused.</p> <p>Specify a value between 300 and 86,400 seconds.</p>"""
    timeout_action: NotRequired["capo_rds.types.string.String"]
    """<p>The action to take when the timeout is reached, either <code>ForceApplyCapacityChange</code> or <code>RollbackCapacityChange</code>.</p> <p> <code>ForceApplyCapacityChange</code> sets the capacity to the specified value as soon as possible.</p> <p> <code>RollbackCapacityChange</code>, the default, ignores the capacity change if a scaling point isn't found in the timeout period.</p> <important> <p>If you specify <code>ForceApplyCapacityChange</code>, connections that prevent Aurora Serverless v1 from finding a scaling point might be dropped.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.how-it-works.auto-scaling"> Autoscaling for Aurora Serverless v1</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    seconds_before_timeout: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The amount of time, in seconds, that Aurora Serverless v1 tries to find a scaling point to perform seamless scaling before enforcing the timeout action. The default is 300.</p> <p>Specify a value between 60 and 600 seconds.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScalingConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "min_capacity" in value:
        pairs.append((f"{key_prefix}MinCapacity", str(value["min_capacity"])))
    if "max_capacity" in value:
        pairs.append((f"{key_prefix}MaxCapacity", str(value["max_capacity"])))
    if "auto_pause" in value:
        pairs.append(
            (f"{key_prefix}AutoPause", "true" if value["auto_pause"] else "false")
        )
    if "seconds_until_auto_pause" in value:
        pairs.append(
            (
                f"{key_prefix}SecondsUntilAutoPause",
                str(value["seconds_until_auto_pause"]),
            )
        )
    if "timeout_action" in value:
        pairs.append((f"{key_prefix}TimeoutAction", str(value["timeout_action"])))
    if "seconds_before_timeout" in value:
        pairs.append(
            (f"{key_prefix}SecondsBeforeTimeout", str(value["seconds_before_timeout"]))
        )


def deserialize_query(el: Element) -> ScalingConfiguration:
    out: ScalingConfiguration = {}  # type: ignore[typeddict-item]
    child_min_capacity = el.find("MinCapacity")
    if child_min_capacity is not None:
        out["min_capacity"] = int(child_min_capacity.text or "")
    child_max_capacity = el.find("MaxCapacity")
    if child_max_capacity is not None:
        out["max_capacity"] = int(child_max_capacity.text or "")
    child_auto_pause = el.find("AutoPause")
    if child_auto_pause is not None:
        out["auto_pause"] = (child_auto_pause.text or "").lower() == "true"
    child_seconds_until_auto_pause = el.find("SecondsUntilAutoPause")
    if child_seconds_until_auto_pause is not None:
        out["seconds_until_auto_pause"] = int(child_seconds_until_auto_pause.text or "")
    child_timeout_action = el.find("TimeoutAction")
    if child_timeout_action is not None:
        out["timeout_action"] = str(child_timeout_action.text or "")
    child_seconds_before_timeout = el.find("SecondsBeforeTimeout")
    if child_seconds_before_timeout is not None:
        out["seconds_before_timeout"] = int(child_seconds_before_timeout.text or "")
    return out
