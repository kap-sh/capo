"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListTagOptionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.tag_option_details


class ListTagOptionsOutput(TypedDict, closed=True):
    tag_option_details: NotRequired[
        "capo_service_catalog.types.tag_option_details.TagOptionDetails"
    ]
    """<p>Information about the TagOptions.</p>"""
    page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagOptionsOutput) -> dict:
    out: dict = {}
    if "tag_option_details" in value:
        import capo_service_catalog.types.tag_option_details

        out["TagOptionDetails"] = (
            capo_service_catalog.types.tag_option_details.serialize_aws_json_1_1(
                value["tag_option_details"]
            )
        )
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagOptionsOutput:
    out: ListTagOptionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("TagOptionDetails") is not None:
        import capo_service_catalog.types.tag_option_details

        out["tag_option_details"] = (
            capo_service_catalog.types.tag_option_details.deserialize_aws_json_1_1(
                data["TagOptionDetails"]
            )
        )
    if data.get("PageToken") is not None:
        out["page_token"] = data["PageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagOptionsOutput) -> dict:
    out: dict = {}
    if "tag_option_details" in value:
        import capo_service_catalog.types.tag_option_details

        out["TagOptionDetails"] = (
            capo_service_catalog.types.tag_option_details.serialize_cbor(
                value["tag_option_details"]
            )
        )
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_cbor(data: dict) -> ListTagOptionsOutput:
    out: ListTagOptionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("TagOptionDetails") is not None:
        import capo_service_catalog.types.tag_option_details

        out["tag_option_details"] = (
            capo_service_catalog.types.tag_option_details.deserialize_cbor(
                data["TagOptionDetails"]
            )
        )
    if data.get("PageToken") is not None:
        out["page_token"] = data["PageToken"]
    return out
