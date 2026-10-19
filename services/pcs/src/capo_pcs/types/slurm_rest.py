"""Generated from Smithy shape ``com.amazonaws.pcs#SlurmRest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.slurm_rest_mode


class SlurmRest(TypedDict, closed=True):
    mode: "capo_pcs.types.slurm_rest_mode.SlurmRestMode"
    """<p>The default value for <code>mode</code> is <code>NONE</code>. A value of <code>STANDARD</code> means the Slurm REST API is enabled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SlurmRest) -> dict:
    out: dict = {}
    import capo_pcs.types.slurm_rest_mode

    out["mode"] = capo_pcs.types.slurm_rest_mode.serialize_aws_json_1_0(value["mode"])
    return out


def deserialize_aws_json_1_0(data: dict) -> SlurmRest:
    out: SlurmRest = {}  # type: ignore[typeddict-item]
    if data.get("mode") is not None:
        import capo_pcs.types.slurm_rest_mode

        out["mode"] = capo_pcs.types.slurm_rest_mode.deserialize_aws_json_1_0(
            data["mode"]
        )
    else:
        import typing

        out["mode"] = typing.cast("capo_pcs.types.slurm_rest_mode.SlurmRestMode", "")
    return out
