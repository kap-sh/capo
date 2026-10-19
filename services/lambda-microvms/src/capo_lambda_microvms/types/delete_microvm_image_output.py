"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#DeleteMicrovmImageOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_image_identifier
    import capo_lambda_microvms.types.microvm_image_state


class DeleteMicrovmImageOutput(TypedDict, closed=True):
    image_identifier: (
        "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
    )
    """<p>The identifier of the deleted MicroVM image.</p>"""
    state: "capo_lambda_microvms.types.microvm_image_state.MicrovmImageState"
    """<p>The current state of the MicroVM image after deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMicrovmImageOutput) -> dict:
    out: dict = {}
    out["imageIdentifier"] = value["image_identifier"]
    import capo_lambda_microvms.types.microvm_image_state

    out["state"] = capo_lambda_microvms.types.microvm_image_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> DeleteMicrovmImageOutput:
    out: DeleteMicrovmImageOutput = {}  # type: ignore[typeddict-item]
    if data.get("imageIdentifier") is not None:
        out["image_identifier"] = data["imageIdentifier"]
    else:
        out["image_identifier"] = ""
    if data.get("state") is not None:
        import capo_lambda_microvms.types.microvm_image_state

        out["state"] = capo_lambda_microvms.types.microvm_image_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_lambda_microvms.types.microvm_image_state.MicrovmImageState", ""
        )
    return out
