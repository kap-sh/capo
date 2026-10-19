"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeCopyProductStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id


class DescribeCopyProductStatusInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    copy_product_token: "capo_service_catalog.types.id.Id"
    """<p>The token for the copy product operation. This token is returned by <a>CopyProduct</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCopyProductStatusInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["CopyProductToken"] = value["copy_product_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCopyProductStatusInput:
    out: DescribeCopyProductStatusInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("CopyProductToken") is not None:
        out["copy_product_token"] = data["CopyProductToken"]
    else:
        out["copy_product_token"] = ""
    return out
