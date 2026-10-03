"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.cluster_setting_name
    import capo_ecs.types.string


class ClusterSetting(TypedDict, closed=True):
    name: NotRequired["capo_ecs.types.cluster_setting_name.ClusterSettingName"]
    """<p>The name of the cluster setting. The value is <code>containerInsights</code>.</p>"""
    value: NotRequired["capo_ecs.types.string.String"]
    """<p>The value to set for the cluster setting. The supported values are <code>enhanced</code>, <code>enabled</code>, and <code>disabled</code>. </p> <p>To use Container Insights with enhanced observability, set the <code>containerInsights</code> account setting to <code>enhanced</code>.</p> <p>To use Container Insights, set the <code>containerInsights</code> account setting to <code>enabled</code>.</p> <p>If a cluster value is specified, it will override the <code>containerInsights</code> value set with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html">PutAccountSetting</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html">PutAccountSettingDefault</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSetting) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_ecs.types.cluster_setting_name

        out["name"] = capo_ecs.types.cluster_setting_name.serialize_aws_json_1_1(
            value["name"]
        )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterSetting:
    out: ClusterSetting = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_ecs.types.cluster_setting_name

        out["name"] = capo_ecs.types.cluster_setting_name.deserialize_aws_json_1_1(
            data["name"]
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
