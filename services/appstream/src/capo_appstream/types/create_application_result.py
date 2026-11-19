"""Generated from Smithy shape ``com.amazonaws.appstream#CreateApplicationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.application


class CreateApplicationResult(TypedDict, closed=True):
    application: NotRequired["capo_appstream.types.application.Application"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationResult) -> dict:
    out: dict = {}
    if "application" in value:
        import capo_appstream.types.application

        out["Application"] = capo_appstream.types.application.serialize_aws_json_1_1(
            value["application"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationResult:
    out: CreateApplicationResult = {}  # type: ignore[typeddict-item]
    if data.get("Application") is not None:
        import capo_appstream.types.application

        out["application"] = capo_appstream.types.application.deserialize_aws_json_1_1(
            data["Application"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateApplicationResult) -> dict:
    out: dict = {}
    if "application" in value:
        import capo_appstream.types.application

        out["Application"] = capo_appstream.types.application.serialize_cbor(
            value["application"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateApplicationResult:
    out: CreateApplicationResult = {}  # type: ignore[typeddict-item]
    if data.get("Application") is not None:
        import capo_appstream.types.application

        out["application"] = capo_appstream.types.application.deserialize_cbor(
            data["Application"]
        )
    return out
