"""Generated from Smithy shape ``com.amazonaws.textract#ListAdapterVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.adapter_version_list
    import capo_textract.types.pagination_token


class ListAdapterVersionsResponse(TypedDict, closed=True):
    adapter_versions: NotRequired[
        "capo_textract.types.adapter_version_list.AdapterVersionList"
    ]
    """<p>Adapter versions that match the filtering criteria specified when calling ListAdapters.</p>"""
    next_token: NotRequired["capo_textract.types.pagination_token.PaginationToken"]
    """<p>Identifies the next page of results to return when listing adapter versions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAdapterVersionsResponse) -> dict:
    out: dict = {}
    if "adapter_versions" in value:
        import capo_textract.types.adapter_version_list

        out["AdapterVersions"] = (
            capo_textract.types.adapter_version_list.serialize_aws_json_1_1(
                value["adapter_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAdapterVersionsResponse:
    out: ListAdapterVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdapterVersions") is not None:
        import capo_textract.types.adapter_version_list

        out["adapter_versions"] = (
            capo_textract.types.adapter_version_list.deserialize_aws_json_1_1(
                data["AdapterVersions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAdapterVersionsResponse) -> dict:
    out: dict = {}
    if "adapter_versions" in value:
        import capo_textract.types.adapter_version_list

        out["AdapterVersions"] = (
            capo_textract.types.adapter_version_list.serialize_cbor(
                value["adapter_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAdapterVersionsResponse:
    out: ListAdapterVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdapterVersions") is not None:
        import capo_textract.types.adapter_version_list

        out["adapter_versions"] = (
            capo_textract.types.adapter_version_list.deserialize_cbor(
                data["AdapterVersions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
