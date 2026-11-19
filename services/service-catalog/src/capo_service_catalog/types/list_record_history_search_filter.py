"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListRecordHistorySearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.search_filter_key
    import capo_service_catalog.types.search_filter_value


class ListRecordHistorySearchFilter(TypedDict, closed=True):
    key: NotRequired["capo_service_catalog.types.search_filter_key.SearchFilterKey"]
    """<p>The filter key.</p> <ul> <li> <p> <code>product</code> - Filter results based on the specified product identifier.</p> </li> <li> <p> <code>provisionedproduct</code> - Filter results based on the provisioned product identifier.</p> </li> </ul>"""
    value: NotRequired[
        "capo_service_catalog.types.search_filter_value.SearchFilterValue"
    ]
    """<p>The filter value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRecordHistorySearchFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRecordHistorySearchFilter:
    out: ListRecordHistorySearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRecordHistorySearchFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> ListRecordHistorySearchFilter:
    out: ListRecordHistorySearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
