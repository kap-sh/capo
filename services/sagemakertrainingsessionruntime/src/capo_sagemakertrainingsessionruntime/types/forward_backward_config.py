"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#ForwardBackwardConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.datum_list
    import capo_sagemakertrainingsessionruntime.types.loss_fn_name


class ForwardBackwardConfig(TypedDict, closed=True):
    loss_fn_name: "capo_sagemakertrainingsessionruntime.types.loss_fn_name.LossFnName"
    """<p>The name of the loss function to evaluate during the forward-backward pass.</p>"""
    datum_list: "capo_sagemakertrainingsessionruntime.types.datum_list.DatumList"
    """<p>The list of input data to feed through the model. Must contain at least one datum, and each datum must have a non-empty modelInput with at least one chunk.</p>"""
    loss_fn_config: NotRequired["object"]
    """<p>Additional loss function configuration passed to the engine. Supported keys are <code>clip_low_threshold</code> (valid range: 0 to 1) and <code>clip_high_threshold</code> (valid range: 1 to 10). Unsupported keys are rejected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForwardBackwardConfig) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.loss_fn_name

    out["lossFnName"] = (
        capo_sagemakertrainingsessionruntime.types.loss_fn_name.serialize_json(
            value["loss_fn_name"]
        )
    )
    import capo_sagemakertrainingsessionruntime.types.datum_list

    out["datumList"] = (
        capo_sagemakertrainingsessionruntime.types.datum_list.serialize_json(
            value["datum_list"]
        )
    )
    if "loss_fn_config" in value:
        out["lossFnConfig"] = value["loss_fn_config"]
    return out


def deserialize_json(data: dict) -> ForwardBackwardConfig:
    out: ForwardBackwardConfig = {}  # type: ignore[typeddict-item]
    if data.get("lossFnName") is not None:
        import capo_sagemakertrainingsessionruntime.types.loss_fn_name

        out["loss_fn_name"] = (
            capo_sagemakertrainingsessionruntime.types.loss_fn_name.deserialize_json(
                data["lossFnName"]
            )
        )
    else:
        import typing

        out["loss_fn_name"] = typing.cast(
            "capo_sagemakertrainingsessionruntime.types.loss_fn_name.LossFnName", ""
        )
    if data.get("datumList") is not None:
        import capo_sagemakertrainingsessionruntime.types.datum_list

        out["datum_list"] = (
            capo_sagemakertrainingsessionruntime.types.datum_list.deserialize_json(
                data["datumList"]
            )
        )
    else:
        out["datum_list"] = []
    if data.get("lossFnConfig") is not None:
        out["loss_fn_config"] = data["lossFnConfig"]
    return out


def redact_sensitive(value: ForwardBackwardConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "datum_list" in value:
        import capo_sagemakertrainingsessionruntime.types.datum_list

        out["datum_list"] = (
            capo_sagemakertrainingsessionruntime.types.datum_list.redact_sensitive(
                value["datum_list"]
            )
        )
    return out
