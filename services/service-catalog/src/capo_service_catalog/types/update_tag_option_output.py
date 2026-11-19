"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateTagOptionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.tag_option_detail


class UpdateTagOptionOutput(TypedDict, closed=True):
    tag_option_detail: NotRequired[
        "capo_service_catalog.types.tag_option_detail.TagOptionDetail"
    ]
    """<p>Information about the TagOption.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTagOptionOutput) -> dict:
    out: dict = {}
    if "tag_option_detail" in value:
        import capo_service_catalog.types.tag_option_detail

        out["TagOptionDetail"] = (
            capo_service_catalog.types.tag_option_detail.serialize_aws_json_1_1(
                value["tag_option_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTagOptionOutput:
    out: UpdateTagOptionOutput = {}  # type: ignore[typeddict-item]
    if data.get("TagOptionDetail") is not None:
        import capo_service_catalog.types.tag_option_detail

        out["tag_option_detail"] = (
            capo_service_catalog.types.tag_option_detail.deserialize_aws_json_1_1(
                data["TagOptionDetail"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateTagOptionOutput) -> dict:
    out: dict = {}
    if "tag_option_detail" in value:
        import capo_service_catalog.types.tag_option_detail

        out["TagOptionDetail"] = (
            capo_service_catalog.types.tag_option_detail.serialize_cbor(
                value["tag_option_detail"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateTagOptionOutput:
    out: UpdateTagOptionOutput = {}  # type: ignore[typeddict-item]
    if data.get("TagOptionDetail") is not None:
        import capo_service_catalog.types.tag_option_detail

        out["tag_option_detail"] = (
            capo_service_catalog.types.tag_option_detail.deserialize_cbor(
                data["TagOptionDetail"]
            )
        )
    return out
