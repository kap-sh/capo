"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListArchiveExportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.export_summary_list
    import capo_mailmanager.types.pagination_token


class ListArchiveExportsResponse(TypedDict, closed=True):
    exports: NotRequired["capo_mailmanager.types.export_summary_list.ExportSummaryList"]
    """<p>The list of export job identifiers and statuses.</p>"""
    next_token: NotRequired["capo_mailmanager.types.pagination_token.PaginationToken"]
    """<p>If present, use to retrieve the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListArchiveExportsResponse) -> dict:
    out: dict = {}
    if "exports" in value:
        import capo_mailmanager.types.export_summary_list

        out["Exports"] = (
            capo_mailmanager.types.export_summary_list.serialize_aws_json_1_0(
                value["exports"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListArchiveExportsResponse:
    out: ListArchiveExportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Exports") is not None:
        import capo_mailmanager.types.export_summary_list

        out["exports"] = (
            capo_mailmanager.types.export_summary_list.deserialize_aws_json_1_0(
                data["Exports"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListArchiveExportsResponse) -> dict:
    out: dict = {}
    if "exports" in value:
        import capo_mailmanager.types.export_summary_list

        out["Exports"] = capo_mailmanager.types.export_summary_list.serialize_cbor(
            value["exports"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListArchiveExportsResponse:
    out: ListArchiveExportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Exports") is not None:
        import capo_mailmanager.types.export_summary_list

        out["exports"] = capo_mailmanager.types.export_summary_list.deserialize_cbor(
            data["Exports"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
