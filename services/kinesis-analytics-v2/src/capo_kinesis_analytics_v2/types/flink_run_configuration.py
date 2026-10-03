"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#FlinkRunConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.boolean_object


class FlinkRunConfiguration(TypedDict, closed=True):
    allow_non_restored_state: NotRequired[
        "capo_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    ]
    """<p>When restoring from a snapshot, specifies whether the runtime is allowed to skip a state that cannot be mapped to the new program. This will happen if the program is updated between snapshots to remove stateful parameters, and state data in the snapshot no longer corresponds to valid application data. For more information, see <a href="https://nightlies.apache.org/flink/flink-docs-release-2.3/docs/ops/state/savepoints/#allowing-non-restored-state"> Allowing Non-Restored State</a> in the <a href="https://nightlies.apache.org/flink/flink-docs-release-2.3/">Apache Flink documentation</a>.</p> <note> <p>This value defaults to <code>false</code>. If you update your application without specifying this parameter, <code>AllowNonRestoredState</code> will be set to <code>false</code>, even if it was previously set to <code>true</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlinkRunConfiguration) -> dict:
    out: dict = {}
    if "allow_non_restored_state" in value:
        out["AllowNonRestoredState"] = value["allow_non_restored_state"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FlinkRunConfiguration:
    out: FlinkRunConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AllowNonRestoredState") is not None:
        out["allow_non_restored_state"] = data["AllowNonRestoredState"]
    return out
