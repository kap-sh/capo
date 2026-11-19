"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteImageBuilderResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.image_builder


class DeleteImageBuilderResult(TypedDict, closed=True):
    image_builder: NotRequired["capo_appstream.types.image_builder.ImageBuilder"]
    """<p>Information about the image builder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteImageBuilderResult) -> dict:
    out: dict = {}
    if "image_builder" in value:
        import capo_appstream.types.image_builder

        out["ImageBuilder"] = capo_appstream.types.image_builder.serialize_aws_json_1_1(
            value["image_builder"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteImageBuilderResult:
    out: DeleteImageBuilderResult = {}  # type: ignore[typeddict-item]
    if data.get("ImageBuilder") is not None:
        import capo_appstream.types.image_builder

        out["image_builder"] = (
            capo_appstream.types.image_builder.deserialize_aws_json_1_1(
                data["ImageBuilder"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteImageBuilderResult) -> dict:
    out: dict = {}
    if "image_builder" in value:
        import capo_appstream.types.image_builder

        out["ImageBuilder"] = capo_appstream.types.image_builder.serialize_cbor(
            value["image_builder"]
        )
    return out


def deserialize_cbor(data: dict) -> DeleteImageBuilderResult:
    out: DeleteImageBuilderResult = {}  # type: ignore[typeddict-item]
    if data.get("ImageBuilder") is not None:
        import capo_appstream.types.image_builder

        out["image_builder"] = capo_appstream.types.image_builder.deserialize_cbor(
            data["ImageBuilder"]
        )
    return out
