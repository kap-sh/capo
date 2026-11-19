"""Generated from Smithy shape ``com.amazonaws.acmpca#ListPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.next_token
    import capo_acm_pca.types.permission_list


class ListPermissionsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_acm_pca.types.next_token.NextToken"]
    """<p>When the list is truncated, this value is present and should be used for the <b>NextToken</b> parameter in a subsequent pagination request. </p>"""
    permissions: NotRequired["capo_acm_pca.types.permission_list.PermissionList"]
    """<p>Summary information about each permission assigned by the specified private CA, including the action enabled, the policy provided, and the time of creation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPermissionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "permissions" in value:
        import capo_acm_pca.types.permission_list

        out["Permissions"] = capo_acm_pca.types.permission_list.serialize_aws_json_1_1(
            value["permissions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPermissionsResponse:
    out: ListPermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Permissions") is not None:
        import capo_acm_pca.types.permission_list

        out["permissions"] = (
            capo_acm_pca.types.permission_list.deserialize_aws_json_1_1(
                data["Permissions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListPermissionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "permissions" in value:
        import capo_acm_pca.types.permission_list

        out["Permissions"] = capo_acm_pca.types.permission_list.serialize_cbor(
            value["permissions"]
        )
    return out


def deserialize_cbor(data: dict) -> ListPermissionsResponse:
    out: ListPermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Permissions") is not None:
        import capo_acm_pca.types.permission_list

        out["permissions"] = capo_acm_pca.types.permission_list.deserialize_cbor(
            data["Permissions"]
        )
    return out
