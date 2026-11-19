"""Generated from Smithy shape ``com.amazonaws.fms#GetProtectionStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.aws_account_id
    import capo_fms.types.pagination_token
    import capo_fms.types.protection_data
    import capo_fms.types.security_service_type


class GetProtectionStatusResponse(TypedDict, closed=True):
    admin_account_id: NotRequired["capo_fms.types.aws_account_id.AWSAccountId"]
    """<p>The ID of the Firewall Manager administrator account for this policy.</p>"""
    service_type: NotRequired[
        "capo_fms.types.security_service_type.SecurityServiceType"
    ]
    """<p>The service type that is protected by the policy. Currently, this is always <code>SHIELD_ADVANCED</code>.</p>"""
    data: NotRequired["capo_fms.types.protection_data.ProtectionData"]
    """<p>Details about the attack, including the following:</p> <ul> <li> <p>Attack type</p> </li> <li> <p>Account ID</p> </li> <li> <p>ARN of the resource attacked</p> </li> <li> <p>Start time of the attack</p> </li> <li> <p>End time of the attack (ongoing attacks will not have an end time)</p> </li> </ul> <p>The details are in JSON format. </p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>If you have more objects than the number that you specified for <code>MaxResults</code> in the request, the response includes a <code>NextToken</code> value. To list more objects, submit another <code>GetProtectionStatus</code> request, and specify the <code>NextToken</code> value from the response in the <code>NextToken</code> value in the next request.</p> <p>Amazon Web Services SDKs provide auto-pagination that identify <code>NextToken</code> in a response and make subsequent request calls automatically on your behalf. However, this feature is not supported by <code>GetProtectionStatus</code>. You must submit subsequent requests with <code>NextToken</code> using your own processes. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProtectionStatusResponse) -> dict:
    out: dict = {}
    if "admin_account_id" in value:
        out["AdminAccountId"] = value["admin_account_id"]
    if "service_type" in value:
        import capo_fms.types.security_service_type

        out["ServiceType"] = (
            capo_fms.types.security_service_type.serialize_aws_json_1_1(
                value["service_type"]
            )
        )
    if "data" in value:
        out["Data"] = value["data"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProtectionStatusResponse:
    out: GetProtectionStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdminAccountId") is not None:
        out["admin_account_id"] = data["AdminAccountId"]
    if data.get("ServiceType") is not None:
        import capo_fms.types.security_service_type

        out["service_type"] = (
            capo_fms.types.security_service_type.deserialize_aws_json_1_1(
                data["ServiceType"]
            )
        )
    if data.get("Data") is not None:
        out["data"] = data["Data"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetProtectionStatusResponse) -> dict:
    out: dict = {}
    if "admin_account_id" in value:
        out["AdminAccountId"] = value["admin_account_id"]
    if "service_type" in value:
        import capo_fms.types.security_service_type

        out["ServiceType"] = capo_fms.types.security_service_type.serialize_cbor(
            value["service_type"]
        )
    if "data" in value:
        out["Data"] = value["data"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> GetProtectionStatusResponse:
    out: GetProtectionStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("AdminAccountId") is not None:
        out["admin_account_id"] = data["AdminAccountId"]
    if data.get("ServiceType") is not None:
        import capo_fms.types.security_service_type

        out["service_type"] = capo_fms.types.security_service_type.deserialize_cbor(
            data["ServiceType"]
        )
    if data.get("Data") is not None:
        out["data"] = data["Data"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
