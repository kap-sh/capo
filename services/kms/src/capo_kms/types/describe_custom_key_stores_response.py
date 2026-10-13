"""Generated from Smithy shape ``com.amazonaws.kms#DescribeCustomKeyStoresResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.boolean_type
    import capo_kms.types.custom_key_stores_list
    import capo_kms.types.marker_type


class DescribeCustomKeyStoresResponse(TypedDict, closed=True):
    custom_key_stores: NotRequired[
        "capo_kms.types.custom_key_stores_list.CustomKeyStoresList"
    ]
    """<p>Contains metadata about each custom key store.</p>"""
    next_marker: NotRequired["capo_kms.types.marker_type.MarkerType"]
    """<p>When <code>Truncated</code> is true, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent request.</p>"""
    truncated: "capo_kms.types.boolean_type.BooleanType"
    """<p>A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the <code>NextMarker</code> element in this response to the <code>Marker</code> parameter in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCustomKeyStoresResponse) -> dict:
    out: dict = {}
    if "custom_key_stores" in value:
        import capo_kms.types.custom_key_stores_list

        out["CustomKeyStores"] = (
            capo_kms.types.custom_key_stores_list.serialize_aws_json_1_1(
                value["custom_key_stores"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    out["Truncated"] = value.get("truncated", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCustomKeyStoresResponse:
    out: DescribeCustomKeyStoresResponse = {}  # type: ignore[typeddict-item]
    if data.get("CustomKeyStores") is not None:
        import capo_kms.types.custom_key_stores_list

        out["custom_key_stores"] = (
            capo_kms.types.custom_key_stores_list.deserialize_aws_json_1_1(
                data["CustomKeyStores"]
            )
        )
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    if data.get("Truncated") is not None:
        out["truncated"] = data["Truncated"]
    else:
        out["truncated"] = False
    return out


def redact_sensitive(value: DescribeCustomKeyStoresResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_key_stores" in value:
        import capo_kms.types.custom_key_stores_list

        out["custom_key_stores"] = (
            capo_kms.types.custom_key_stores_list.redact_sensitive(
                value["custom_key_stores"]
            )
        )
    return out
