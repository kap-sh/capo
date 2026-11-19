"""Generated from Smithy shape ``com.amazonaws.appstream#ImageBuilderStateChangeReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.image_builder_state_change_reason_code
    import capo_appstream.types.string


class ImageBuilderStateChangeReason(TypedDict, closed=True):
    code: NotRequired[
        "capo_appstream.types.image_builder_state_change_reason_code.ImageBuilderStateChangeReasonCode"
    ]
    """<p>The state change reason code.</p>"""
    message: NotRequired["capo_appstream.types.string.String"]
    """<p>The state change reason message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageBuilderStateChangeReason) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_appstream.types.image_builder_state_change_reason_code

        out["Code"] = (
            capo_appstream.types.image_builder_state_change_reason_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageBuilderStateChangeReason:
    out: ImageBuilderStateChangeReason = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_appstream.types.image_builder_state_change_reason_code

        out["code"] = (
            capo_appstream.types.image_builder_state_change_reason_code.deserialize_aws_json_1_1(
                data["Code"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageBuilderStateChangeReason) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_appstream.types.image_builder_state_change_reason_code

        out["Code"] = (
            capo_appstream.types.image_builder_state_change_reason_code.serialize_cbor(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> ImageBuilderStateChangeReason:
    out: ImageBuilderStateChangeReason = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_appstream.types.image_builder_state_change_reason_code

        out["code"] = (
            capo_appstream.types.image_builder_state_change_reason_code.deserialize_cbor(
                data["Code"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
