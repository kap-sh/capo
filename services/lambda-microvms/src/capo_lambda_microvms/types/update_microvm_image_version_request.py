"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#UpdateMicrovmImageVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_image_identifier
    import capo_lambda_microvms.types.microvm_image_version_status
    import capo_lambda_microvms.types.non_blank_string


class UpdateMicrovmImageVersionRequest(TypedDict, closed=True):
    image_identifier: (
        "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
    )
    """<p>The unique identifier (ARN or ID) of the MicroVM image.</p>"""
    image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The version of the MicroVM image to update.</p>"""
    status: "capo_lambda_microvms.types.microvm_image_version_status.MicrovmImageVersionStatus"
    """<p>The new status to set for the MicroVM image version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMicrovmImageVersionRequest) -> dict:
    out: dict = {}
    import capo_lambda_microvms.types.microvm_image_version_status

    out["status"] = (
        capo_lambda_microvms.types.microvm_image_version_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateMicrovmImageVersionRequest:
    out: UpdateMicrovmImageVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_lambda_microvms.types.microvm_image_version_status

        out["status"] = (
            capo_lambda_microvms.types.microvm_image_version_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateMicrovmImageVersionRequest.status required")
    return out
