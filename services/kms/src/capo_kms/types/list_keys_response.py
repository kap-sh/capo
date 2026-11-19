"""Generated from Smithy shape ``com.amazonaws.kms#ListKeysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.boolean_type
    import capo_kms.types.key_list
    import capo_kms.types.marker_type


class ListKeysResponse(TypedDict, closed=True):
    keys: NotRequired["capo_kms.types.key_list.KeyList"]
    """<p>A list of KMS keys. For a KMS key that another Amazon Web Services account shared with you through RAM, the key ARN contains the account ID of the Amazon Web Services account that owns the KMS key.</p>"""
    next_marker: NotRequired["capo_kms.types.marker_type.MarkerType"]
    """<p>When <code>Truncated</code> is true, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent request.</p>"""
    truncated: "capo_kms.types.boolean_type.BooleanType"
    """<p>A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the <code>NextMarker</code> element in this response to the <code>Marker</code> parameter in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListKeysResponse) -> dict:
    out: dict = {}
    if "keys" in value:
        import capo_kms.types.key_list

        out["Keys"] = capo_kms.types.key_list.serialize_aws_json_1_1(value["keys"])
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    out["Truncated"] = value.get("truncated", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListKeysResponse:
    out: ListKeysResponse = {}  # type: ignore[typeddict-item]
    if data.get("Keys") is not None:
        import capo_kms.types.key_list

        out["keys"] = capo_kms.types.key_list.deserialize_aws_json_1_1(data["Keys"])
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    if data.get("Truncated") is not None:
        out["truncated"] = data["Truncated"]
    else:
        out["truncated"] = False
    return out
