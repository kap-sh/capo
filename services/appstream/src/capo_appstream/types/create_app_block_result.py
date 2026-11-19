"""Generated from Smithy shape ``com.amazonaws.appstream#CreateAppBlockResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.app_block


class CreateAppBlockResult(TypedDict, closed=True):
    app_block: NotRequired["capo_appstream.types.app_block.AppBlock"]
    """<p>The app block.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAppBlockResult) -> dict:
    out: dict = {}
    if "app_block" in value:
        import capo_appstream.types.app_block

        out["AppBlock"] = capo_appstream.types.app_block.serialize_aws_json_1_1(
            value["app_block"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAppBlockResult:
    out: CreateAppBlockResult = {}  # type: ignore[typeddict-item]
    if data.get("AppBlock") is not None:
        import capo_appstream.types.app_block

        out["app_block"] = capo_appstream.types.app_block.deserialize_aws_json_1_1(
            data["AppBlock"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAppBlockResult) -> dict:
    out: dict = {}
    if "app_block" in value:
        import capo_appstream.types.app_block

        out["AppBlock"] = capo_appstream.types.app_block.serialize_cbor(
            value["app_block"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateAppBlockResult:
    out: CreateAppBlockResult = {}  # type: ignore[typeddict-item]
    if data.get("AppBlock") is not None:
        import capo_appstream.types.app_block

        out["app_block"] = capo_appstream.types.app_block.deserialize_cbor(
            data["AppBlock"]
        )
    return out
