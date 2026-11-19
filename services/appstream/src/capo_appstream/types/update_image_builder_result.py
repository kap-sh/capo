"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateImageBuilderResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.image_builder


class UpdateImageBuilderResult(TypedDict, closed=True):
    image_builder: NotRequired["capo_appstream.types.image_builder.ImageBuilder"]
    """<p>Information about the image builder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateImageBuilderResult) -> dict:
    out: dict = {}
    if "image_builder" in value:
        import capo_appstream.types.image_builder

        out["ImageBuilder"] = capo_appstream.types.image_builder.serialize_aws_json_1_1(
            value["image_builder"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateImageBuilderResult:
    out: UpdateImageBuilderResult = {}  # type: ignore[typeddict-item]
    if data.get("ImageBuilder") is not None:
        import capo_appstream.types.image_builder

        out["image_builder"] = (
            capo_appstream.types.image_builder.deserialize_aws_json_1_1(
                data["ImageBuilder"]
            )
        )
    return out
