"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#ForwardResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.metrics_map
    import capo_sagemakertrainingsessionruntime.types.tensor_data_map_list
    import capo_sagemakertrainingsessionruntime.types.training_token_usage


class ForwardResult(TypedDict, closed=True):
    loss_fn_output_type: NotRequired["str"]
    """<p>The data type of the loss function output tensors.</p>"""
    loss_fn_outputs: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.tensor_data_map_list.TensorDataMapList"
    ]
    """<p>The loss function output tensors, keyed by name.</p>"""
    metrics: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.metrics_map.MetricsMap"
    ]
    """<p>The training metrics emitted by the engine, such as loss values.</p>"""
    token_usage: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.training_token_usage.TrainingTokenUsage"
    ]
    """<p>The token usage statistics for metering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForwardResult) -> dict:
    out: dict = {}
    if "loss_fn_output_type" in value:
        out["lossFnOutputType"] = value["loss_fn_output_type"]
    if "loss_fn_outputs" in value:
        import capo_sagemakertrainingsessionruntime.types.tensor_data_map_list

        out["lossFnOutputs"] = (
            capo_sagemakertrainingsessionruntime.types.tensor_data_map_list.serialize_json(
                value["loss_fn_outputs"]
            )
        )
    if "metrics" in value:
        import capo_sagemakertrainingsessionruntime.types.metrics_map

        out["metrics"] = (
            capo_sagemakertrainingsessionruntime.types.metrics_map.serialize_json(
                value["metrics"]
            )
        )
    if "token_usage" in value:
        import capo_sagemakertrainingsessionruntime.types.training_token_usage

        out["tokenUsage"] = (
            capo_sagemakertrainingsessionruntime.types.training_token_usage.serialize_json(
                value["token_usage"]
            )
        )
    return out


def deserialize_json(data: dict) -> ForwardResult:
    out: ForwardResult = {}  # type: ignore[typeddict-item]
    if data.get("lossFnOutputType") is not None:
        out["loss_fn_output_type"] = data["lossFnOutputType"]
    if data.get("lossFnOutputs") is not None:
        import capo_sagemakertrainingsessionruntime.types.tensor_data_map_list

        out["loss_fn_outputs"] = (
            capo_sagemakertrainingsessionruntime.types.tensor_data_map_list.deserialize_json(
                data["lossFnOutputs"]
            )
        )
    if data.get("metrics") is not None:
        import capo_sagemakertrainingsessionruntime.types.metrics_map

        out["metrics"] = (
            capo_sagemakertrainingsessionruntime.types.metrics_map.deserialize_json(
                data["metrics"]
            )
        )
    if data.get("tokenUsage") is not None:
        import capo_sagemakertrainingsessionruntime.types.training_token_usage

        out["token_usage"] = (
            capo_sagemakertrainingsessionruntime.types.training_token_usage.deserialize_json(
                data["tokenUsage"]
            )
        )
    return out
