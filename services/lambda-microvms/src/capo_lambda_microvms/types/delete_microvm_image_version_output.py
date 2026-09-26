"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#DeleteMicrovmImageVersionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_image_identifier
    import capo_lambda_microvms.types.microvm_image_version_state
    import capo_lambda_microvms.types.non_blank_string


class DeleteMicrovmImageVersionOutput(TypedDict, closed=True):
    image_identifier: (
        "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
    )
    """<p>The identifier of the MicroVM image.</p>"""
    image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The version that was deleted.</p>"""
    state: "capo_lambda_microvms.types.microvm_image_version_state.MicrovmImageVersionState"
    """<p>The current state of the MicroVM image version after deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMicrovmImageVersionOutput) -> dict:
    out: dict = {}
    out["imageIdentifier"] = value["image_identifier"]
    out["imageVersion"] = value["image_version"]
    import capo_lambda_microvms.types.microvm_image_version_state

    out["state"] = (
        capo_lambda_microvms.types.microvm_image_version_state.serialize_json(
            value["state"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteMicrovmImageVersionOutput:
    out: DeleteMicrovmImageVersionOutput = {}  # type: ignore[typeddict-item]
    if data.get("imageIdentifier") is not None:
        out["image_identifier"] = data["imageIdentifier"]
    else:
        raise DeserializationError(
            "DeleteMicrovmImageVersionOutput.image_identifier required"
        )
    if data.get("imageVersion") is not None:
        out["image_version"] = data["imageVersion"]
    else:
        raise DeserializationError(
            "DeleteMicrovmImageVersionOutput.image_version required"
        )
    if data.get("state") is not None:
        import capo_lambda_microvms.types.microvm_image_version_state

        out["state"] = (
            capo_lambda_microvms.types.microvm_image_version_state.deserialize_json(
                data["state"]
            )
        )
    else:
        raise DeserializationError("DeleteMicrovmImageVersionOutput.state required")
    return out
