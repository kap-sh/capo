"""Generated from Smithy shape ``com.amazonaws.kms#ListKeyPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.boolean_type
    import capo_kms.types.marker_type
    import capo_kms.types.policy_name_list


class ListKeyPoliciesResponse(TypedDict, closed=True):
    policy_names: NotRequired["capo_kms.types.policy_name_list.PolicyNameList"]
    """<p>A list of key policy names. Valid values are:</p> <dl> <dt>default</dt> <dd> <p>The key policy that you manage.</p> </dd> <dt>AWS_RAM</dt> <dd> <p>The key policy that RAM manages for KMS keys that you share through RAM.</p> </dd> </dl>"""
    next_marker: NotRequired["capo_kms.types.marker_type.MarkerType"]
    """<p>When <code>Truncated</code> is true, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent request.</p>"""
    truncated: "capo_kms.types.boolean_type.BooleanType"
    """<p>A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the <code>NextMarker</code> element in this response to the <code>Marker</code> parameter in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListKeyPoliciesResponse) -> dict:
    out: dict = {}
    if "policy_names" in value:
        import capo_kms.types.policy_name_list

        out["PolicyNames"] = capo_kms.types.policy_name_list.serialize_aws_json_1_1(
            value["policy_names"]
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    out["Truncated"] = value.get("truncated", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListKeyPoliciesResponse:
    out: ListKeyPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("PolicyNames") is not None:
        import capo_kms.types.policy_name_list

        out["policy_names"] = capo_kms.types.policy_name_list.deserialize_aws_json_1_1(
            data["PolicyNames"]
        )
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    if data.get("Truncated") is not None:
        out["truncated"] = data["Truncated"]
    else:
        out["truncated"] = False
    return out
