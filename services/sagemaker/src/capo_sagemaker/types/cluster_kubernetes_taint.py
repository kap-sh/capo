"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterKubernetesTaint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_kubernetes_taint_effect
    import capo_sagemaker.types.cluster_kubernetes_taint_key
    import capo_sagemaker.types.cluster_kubernetes_taint_value


class ClusterKubernetesTaint(TypedDict, closed=True):
    key: "capo_sagemaker.types.cluster_kubernetes_taint_key.ClusterKubernetesTaintKey"
    """<p>The key of the taint.</p>"""
    value: NotRequired[
        "capo_sagemaker.types.cluster_kubernetes_taint_value.ClusterKubernetesTaintValue"
    ]
    """<p>The value of the taint.</p>"""
    effect: "capo_sagemaker.types.cluster_kubernetes_taint_effect.ClusterKubernetesTaintEffect"
    """<p>The effect of the taint. Valid values are <code>NoSchedule</code>, <code>PreferNoSchedule</code>, and <code>NoExecute</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterKubernetesTaint) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    import capo_sagemaker.types.cluster_kubernetes_taint_effect

    out["Effect"] = (
        capo_sagemaker.types.cluster_kubernetes_taint_effect.serialize_aws_json_1_1(
            value["effect"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterKubernetesTaint:
    out: ClusterKubernetesTaint = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Effect") is not None:
        import capo_sagemaker.types.cluster_kubernetes_taint_effect

        out["effect"] = (
            capo_sagemaker.types.cluster_kubernetes_taint_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    else:
        import typing

        out["effect"] = typing.cast(
            "capo_sagemaker.types.cluster_kubernetes_taint_effect.ClusterKubernetesTaintEffect",
            "",
        )
    return out
