"""Generated from Smithy shape ``com.amazonaws.fms#GetAppsListResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.apps_list_data
    import capo_fms.types.resource_arn


class GetAppsListResponse(TypedDict, closed=True):
    apps_list: NotRequired["capo_fms.types.apps_list_data.AppsListData"]
    """<p>Information about the specified Firewall Manager applications list.</p>"""
    apps_list_arn: NotRequired["capo_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the applications list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAppsListResponse) -> dict:
    out: dict = {}
    if "apps_list" in value:
        import capo_fms.types.apps_list_data

        out["AppsList"] = capo_fms.types.apps_list_data.serialize_aws_json_1_1(
            value["apps_list"]
        )
    if "apps_list_arn" in value:
        out["AppsListArn"] = value["apps_list_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAppsListResponse:
    out: GetAppsListResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppsList") is not None:
        import capo_fms.types.apps_list_data

        out["apps_list"] = capo_fms.types.apps_list_data.deserialize_aws_json_1_1(
            data["AppsList"]
        )
    if data.get("AppsListArn") is not None:
        out["apps_list_arn"] = data["AppsListArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAppsListResponse) -> dict:
    out: dict = {}
    if "apps_list" in value:
        import capo_fms.types.apps_list_data

        out["AppsList"] = capo_fms.types.apps_list_data.serialize_cbor(
            value["apps_list"]
        )
    if "apps_list_arn" in value:
        out["AppsListArn"] = value["apps_list_arn"]
    return out


def deserialize_cbor(data: dict) -> GetAppsListResponse:
    out: GetAppsListResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppsList") is not None:
        import capo_fms.types.apps_list_data

        out["apps_list"] = capo_fms.types.apps_list_data.deserialize_cbor(
            data["AppsList"]
        )
    if data.get("AppsListArn") is not None:
        out["apps_list_arn"] = data["AppsListArn"]
    return out
