"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#CpuConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.architecture


class CpuConfiguration(TypedDict, closed=True):
    architecture: "capo_lambda_microvms.types.architecture.Architecture"
    """<p>The CPU architecture.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CpuConfiguration) -> dict:
    out: dict = {}
    import capo_lambda_microvms.types.architecture

    out["architecture"] = capo_lambda_microvms.types.architecture.serialize_json(
        value["architecture"]
    )
    return out


def deserialize_json(data: dict) -> CpuConfiguration:
    out: CpuConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("architecture") is not None:
        import capo_lambda_microvms.types.architecture

        out["architecture"] = capo_lambda_microvms.types.architecture.deserialize_json(
            data["architecture"]
        )
    else:
        import typing

        out["architecture"] = typing.cast(
            "capo_lambda_microvms.types.architecture.Architecture", ""
        )
    return out
