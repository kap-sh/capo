"""Generated from Smithy shape ``com.amazonaws.comprehend#WarningsListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer
    import capo_comprehend.types.page_based_warning_code
    import capo_comprehend.types.string


class WarningsListItem(TypedDict, closed=True):
    page: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>Page number in the input document.</p>"""
    warn_code: NotRequired[
        "capo_comprehend.types.page_based_warning_code.PageBasedWarningCode"
    ]
    """<p>The type of warning.</p>"""
    warn_message: NotRequired["capo_comprehend.types.string.String"]
    """<p>Text message associated with the warning.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WarningsListItem) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "warn_code" in value:
        import capo_comprehend.types.page_based_warning_code

        out["WarnCode"] = (
            capo_comprehend.types.page_based_warning_code.serialize_aws_json_1_1(
                value["warn_code"]
            )
        )
    if "warn_message" in value:
        out["WarnMessage"] = value["warn_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WarningsListItem:
    out: WarningsListItem = {}  # type: ignore[typeddict-item]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("WarnCode") is not None:
        import capo_comprehend.types.page_based_warning_code

        out["warn_code"] = (
            capo_comprehend.types.page_based_warning_code.deserialize_aws_json_1_1(
                data["WarnCode"]
            )
        )
    if data.get("WarnMessage") is not None:
        out["warn_message"] = data["WarnMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WarningsListItem) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "warn_code" in value:
        import capo_comprehend.types.page_based_warning_code

        out["WarnCode"] = capo_comprehend.types.page_based_warning_code.serialize_cbor(
            value["warn_code"]
        )
    if "warn_message" in value:
        out["WarnMessage"] = value["warn_message"]
    return out


def deserialize_cbor(data: dict) -> WarningsListItem:
    out: WarningsListItem = {}  # type: ignore[typeddict-item]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    if data.get("WarnCode") is not None:
        import capo_comprehend.types.page_based_warning_code

        out["warn_code"] = (
            capo_comprehend.types.page_based_warning_code.deserialize_cbor(
                data["WarnCode"]
            )
        )
    if data.get("WarnMessage") is not None:
        out["warn_message"] = data["WarnMessage"]
    return out
