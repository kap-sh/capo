"""Generated from Smithy shape ``com.amazonaws.fms#PutAppsListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.apps_list_data
    import capo_fms.types.tag_list


class PutAppsListRequest(TypedDict, closed=True):
    apps_list: "capo_fms.types.apps_list_data.AppsListData"
    """<p>The details of the Firewall Manager applications list to be created.</p>"""
    tag_list: NotRequired["capo_fms.types.tag_list.TagList"]
    """<p>The tags associated with the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAppsListRequest) -> dict:
    out: dict = {}
    import capo_fms.types.apps_list_data

    out["AppsList"] = capo_fms.types.apps_list_data.serialize_aws_json_1_1(
        value["apps_list"]
    )
    if "tag_list" in value:
        import capo_fms.types.tag_list

        out["TagList"] = capo_fms.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAppsListRequest:
    out: PutAppsListRequest = {}  # type: ignore[typeddict-item]
    if data.get("AppsList") is not None:
        import capo_fms.types.apps_list_data

        out["apps_list"] = capo_fms.types.apps_list_data.deserialize_aws_json_1_1(
            data["AppsList"]
        )
    else:
        raise DeserializationError("PutAppsListRequest.apps_list required")
    if data.get("TagList") is not None:
        import capo_fms.types.tag_list

        out["tag_list"] = capo_fms.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutAppsListRequest) -> dict:
    out: dict = {}
    import capo_fms.types.apps_list_data

    out["AppsList"] = capo_fms.types.apps_list_data.serialize_cbor(value["apps_list"])
    if "tag_list" in value:
        import capo_fms.types.tag_list

        out["TagList"] = capo_fms.types.tag_list.serialize_cbor(value["tag_list"])
    return out


def deserialize_cbor(data: dict) -> PutAppsListRequest:
    out: PutAppsListRequest = {}  # type: ignore[typeddict-item]
    if data.get("AppsList") is not None:
        import capo_fms.types.apps_list_data

        out["apps_list"] = capo_fms.types.apps_list_data.deserialize_cbor(
            data["AppsList"]
        )
    else:
        raise DeserializationError("PutAppsListRequest.apps_list required")
    if data.get("TagList") is not None:
        import capo_fms.types.tag_list

        out["tag_list"] = capo_fms.types.tag_list.deserialize_cbor(data["TagList"])
    return out
