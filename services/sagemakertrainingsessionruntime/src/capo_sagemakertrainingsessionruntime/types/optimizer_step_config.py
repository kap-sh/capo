"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#OptimizerStepConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sagemakertrainingsessionruntime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.adam_params_config


class OptimizerStepConfig(TypedDict, closed=True):
    adam_params_config: (
        "capo_sagemakertrainingsessionruntime.types.adam_params_config.AdamParamsConfig"
    )
    """<p>The Adam optimizer hyperparameters for this step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OptimizerStepConfig) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.adam_params_config

    out["adamParamsConfig"] = (
        capo_sagemakertrainingsessionruntime.types.adam_params_config.serialize_json(
            value["adam_params_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> OptimizerStepConfig:
    out: OptimizerStepConfig = {}  # type: ignore[typeddict-item]
    if data.get("adamParamsConfig") is not None:
        import capo_sagemakertrainingsessionruntime.types.adam_params_config

        out["adam_params_config"] = (
            capo_sagemakertrainingsessionruntime.types.adam_params_config.deserialize_json(
                data["adamParamsConfig"]
            )
        )
    else:
        raise DeserializationError("OptimizerStepConfig.adam_params_config required")
    return out
