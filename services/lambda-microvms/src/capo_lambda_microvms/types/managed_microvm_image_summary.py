"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ManagedMicrovmImageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_lambda_microvms.types.non_blank_string


class ManagedMicrovmImageSummary(TypedDict, closed=True):
    image_arn: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The ARN of the managed MicroVM image.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the managed MicroVM image was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the managed MicroVM image was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedMicrovmImageSummary) -> dict:
    out: dict = {}
    out["imageArn"] = value["image_arn"]
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


def deserialize_json(data: dict) -> ManagedMicrovmImageSummary:
    out: ManagedMicrovmImageSummary = {}  # type: ignore[typeddict-item]
    if data.get("imageArn") is not None:
        out["image_arn"] = data["imageArn"]
    else:
        out["image_arn"] = ""
    if data.get("createdAt") is not None:
        import capo_lambda_microvms.types._prelude.timestamp

        out["created_at"] = (
            capo_lambda_microvms.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_lambda_microvms.types._prelude.timestamp

        out["updated_at"] = (
            capo_lambda_microvms.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
