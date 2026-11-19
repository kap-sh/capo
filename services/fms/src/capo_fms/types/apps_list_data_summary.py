"""Generated from Smithy shape ``com.amazonaws.fms#AppsListDataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.apps_list
    import capo_fms.types.list_id
    import capo_fms.types.resource_arn
    import capo_fms.types.resource_name


class AppsListDataSummary(TypedDict, closed=True):
    list_arn: NotRequired["capo_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the applications list.</p>"""
    list_id: NotRequired["capo_fms.types.list_id.ListId"]
    """<p>The ID of the applications list.</p>"""
    list_name: NotRequired["capo_fms.types.resource_name.ResourceName"]
    """<p>The name of the applications list.</p>"""
    apps_list: NotRequired["capo_fms.types.apps_list.AppsList"]
    """<p>An array of <code>App</code> objects in the Firewall Manager applications list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppsListDataSummary) -> dict:
    out: dict = {}
    if "list_arn" in value:
        out["ListArn"] = value["list_arn"]
    if "list_id" in value:
        out["ListId"] = value["list_id"]
    if "list_name" in value:
        out["ListName"] = value["list_name"]
    if "apps_list" in value:
        import capo_fms.types.apps_list

        out["AppsList"] = capo_fms.types.apps_list.serialize_aws_json_1_1(
            value["apps_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AppsListDataSummary:
    out: AppsListDataSummary = {}  # type: ignore[typeddict-item]
    if data.get("ListArn") is not None:
        out["list_arn"] = data["ListArn"]
    if data.get("ListId") is not None:
        out["list_id"] = data["ListId"]
    if data.get("ListName") is not None:
        out["list_name"] = data["ListName"]
    if data.get("AppsList") is not None:
        import capo_fms.types.apps_list

        out["apps_list"] = capo_fms.types.apps_list.deserialize_aws_json_1_1(
            data["AppsList"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppsListDataSummary) -> dict:
    out: dict = {}
    if "list_arn" in value:
        out["ListArn"] = value["list_arn"]
    if "list_id" in value:
        out["ListId"] = value["list_id"]
    if "list_name" in value:
        out["ListName"] = value["list_name"]
    if "apps_list" in value:
        import capo_fms.types.apps_list

        out["AppsList"] = capo_fms.types.apps_list.serialize_cbor(value["apps_list"])
    return out


def deserialize_cbor(data: dict) -> AppsListDataSummary:
    out: AppsListDataSummary = {}  # type: ignore[typeddict-item]
    if data.get("ListArn") is not None:
        out["list_arn"] = data["ListArn"]
    if data.get("ListId") is not None:
        out["list_id"] = data["ListId"]
    if data.get("ListName") is not None:
        out["list_name"] = data["ListName"]
    if data.get("AppsList") is not None:
        import capo_fms.types.apps_list

        out["apps_list"] = capo_fms.types.apps_list.deserialize_cbor(data["AppsList"])
    return out
