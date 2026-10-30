"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#Datum``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemakertrainingsessionruntime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.model_input
    import capo_sagemakertrainingsessionruntime.types.tensor_data_map


class Datum(TypedDict, closed=True):
    model_input: "capo_sagemakertrainingsessionruntime.types.model_input.ModelInput"
    """<p>The tokenized input to feed to the model.</p>"""
    loss_fn_inputs: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.tensor_data_map.TensorDataMap"
    ]
    """<p>The tensor inputs for the loss function, keyed by name. Unsupported keys are rejected. Supported keys: <code>target_tokens</code>, <code>weights</code>, <code>advantages</code>, <code>logprobs</code>, <code>ref_log_prob</code>, <code>temperature</code>. Required keys depend on the loss function type: SFT (<code>cross_entropy</code>) requires <code>target_tokens</code> and <code>weights</code>; RL (<code>ppo</code>, <code>cispo</code>, <code>importance_sampling</code>) requires <code>target_tokens</code>, <code>weights</code>, <code>advantages</code>, and <code>logprobs</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Datum) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.model_input

    out["modelInput"] = (
        capo_sagemakertrainingsessionruntime.types.model_input.serialize_json(
            value["model_input"]
        )
    )
    if "loss_fn_inputs" in value:
        import capo_sagemakertrainingsessionruntime.types.tensor_data_map

        out["lossFnInputs"] = (
            capo_sagemakertrainingsessionruntime.types.tensor_data_map.serialize_json(
                value["loss_fn_inputs"]
            )
        )
    return out


def deserialize_json(data: dict) -> Datum:
    out: Datum = {}  # type: ignore[typeddict-item]
    if data.get("modelInput") is not None:
        import capo_sagemakertrainingsessionruntime.types.model_input

        out["model_input"] = (
            capo_sagemakertrainingsessionruntime.types.model_input.deserialize_json(
                data["modelInput"]
            )
        )
    else:
        raise DeserializationError("Datum.model_input required")
    if data.get("lossFnInputs") is not None:
        import capo_sagemakertrainingsessionruntime.types.tensor_data_map

        out["loss_fn_inputs"] = (
            capo_sagemakertrainingsessionruntime.types.tensor_data_map.deserialize_json(
                data["lossFnInputs"]
            )
        )
    return out
