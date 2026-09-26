"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ManagedMicrovmImageVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_lambda_microvms.types.managed_microvm_image_version_status
    import capo_lambda_microvms.types.non_blank_string


class ManagedMicrovmImageVersion(TypedDict, closed=True):
    image_arn: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The ARN of the managed MicroVM image.</p>"""
    image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The version of the managed MicroVM image.</p>"""
    status: NotRequired[
        "capo_lambda_microvms.types.managed_microvm_image_version_status.ManagedMicrovmImageVersionStatus"
    ]
    """<p>The lifecycle status of the managed MicroVM image version. Valid values: AVAILABLE (the version is available for use) or DEPRECATED (the version is deprecated; do not use it for new MicroVM images).</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the version was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the version was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedMicrovmImageVersion) -> dict:
    out: dict = {}
    out["imageArn"] = value["image_arn"]
    out["imageVersion"] = value["image_version"]
    if "status" in value:
        import capo_lambda_microvms.types.managed_microvm_image_version_status

        out["status"] = (
            capo_lambda_microvms.types.managed_microvm_image_version_status.serialize_json(
                value["status"]
            )
        )
    import capo_lambda_microvms.types._prelude.timestamp

    out["createdAt"] = capo_lambda_microvms.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "updated_at" in value:
        import capo_lambda_microvms.types._prelude.timestamp

        out["updatedAt"] = capo_lambda_microvms.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ManagedMicrovmImageVersion:
    out: ManagedMicrovmImageVersion = {}  # type: ignore[typeddict-item]
    if data.get("imageArn") is not None:
        out["image_arn"] = data["imageArn"]
    else:
        raise DeserializationError("ManagedMicrovmImageVersion.image_arn required")
    if data.get("imageVersion") is not None:
        out["image_version"] = data["imageVersion"]
    else:
        raise DeserializationError("ManagedMicrovmImageVersion.image_version required")
    if data.get("status") is not None:
        import capo_lambda_microvms.types.managed_microvm_image_version_status

        out["status"] = (
            capo_lambda_microvms.types.managed_microvm_image_version_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_lambda_microvms.types._prelude.timestamp

        out["created_at"] = (
            capo_lambda_microvms.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ManagedMicrovmImageVersion.created_at required")
    if data.get("updatedAt") is not None:
        import capo_lambda_microvms.types._prelude.timestamp

        out["updated_at"] = (
            capo_lambda_microvms.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
