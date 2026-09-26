"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#GetMicrovmImageOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_lambda_microvms.types.image_name
    import capo_lambda_microvms.types.microvm_image_state
    import capo_lambda_microvms.types.non_blank_string
    import capo_lambda_microvms.types.tags


class GetMicrovmImageOutput(TypedDict, closed=True):
    image_arn: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The ARN of the MicroVM image.</p>"""
    name: "capo_lambda_microvms.types.image_name.ImageName"
    """<p>The name of the MicroVM image.</p>"""
    state: "capo_lambda_microvms.types.microvm_image_state.MicrovmImageState"
    """<p>The current state of the MicroVM image.</p>"""
    latest_active_image_version: NotRequired[
        "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    ]
    """<p>The latest active version of the MicroVM image.</p>"""
    latest_failed_image_version: NotRequired[
        "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    ]
    """<p>The latest failed version of the MicroVM image, if any.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the MicroVM image was created.</p>"""
    tags: NotRequired["capo_lambda_microvms.types.tags.Tags"]
    """<p>A set of key-value pairs that you can attach to the resource. Use tags to categorize resources for cost allocation, access control (ABAC), and organization.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the MicroVM image was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMicrovmImageOutput) -> dict:
    out: dict = {}
    out["imageArn"] = value["image_arn"]
    out["name"] = value["name"]
    import capo_lambda_microvms.types.microvm_image_state

    out["state"] = capo_lambda_microvms.types.microvm_image_state.serialize_json(
        value["state"]
    )
    if "latest_active_image_version" in value:
        out["latestActiveImageVersion"] = value["latest_active_image_version"]
    if "latest_failed_image_version" in value:
        out["latestFailedImageVersion"] = value["latest_failed_image_version"]
    import capo_lambda_microvms.types._prelude.timestamp

    out["createdAt"] = capo_lambda_microvms.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "tags" in value:
        import capo_lambda_microvms.types.tags

        out["tags"] = capo_lambda_microvms.types.tags.serialize_json(value["tags"])
    if "updated_at" in value:
        import capo_lambda_microvms.types._prelude.timestamp

        out["updatedAt"] = capo_lambda_microvms.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetMicrovmImageOutput:
    out: GetMicrovmImageOutput = {}  # type: ignore[typeddict-item]
    if data.get("imageArn") is not None:
        out["image_arn"] = data["imageArn"]
    else:
        raise DeserializationError("GetMicrovmImageOutput.image_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetMicrovmImageOutput.name required")
    if data.get("state") is not None:
        import capo_lambda_microvms.types.microvm_image_state

        out["state"] = capo_lambda_microvms.types.microvm_image_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("GetMicrovmImageOutput.state required")
    if data.get("latestActiveImageVersion") is not None:
        out["latest_active_image_version"] = data["latestActiveImageVersion"]
    if data.get("latestFailedImageVersion") is not None:
        out["latest_failed_image_version"] = data["latestFailedImageVersion"]
    if data.get("createdAt") is not None:
        import capo_lambda_microvms.types._prelude.timestamp

        out["created_at"] = (
            capo_lambda_microvms.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetMicrovmImageOutput.created_at required")
    if data.get("tags") is not None:
        import capo_lambda_microvms.types.tags

        out["tags"] = capo_lambda_microvms.types.tags.deserialize_json(data["tags"])
    if data.get("updatedAt") is not None:
        import capo_lambda_microvms.types._prelude.timestamp

        out["updated_at"] = (
            capo_lambda_microvms.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
