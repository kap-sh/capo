"""Generated from Smithy shape ``com.amazonaws.fms#PutProtocolsListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.protocols_list_data
    import capo_fms.types.tag_list


class PutProtocolsListRequest(TypedDict, closed=True):
    protocols_list: "capo_fms.types.protocols_list_data.ProtocolsListData"
    """<p>The details of the Firewall Manager protocols list to be created.</p>"""
    tag_list: NotRequired["capo_fms.types.tag_list.TagList"]
    """<p>The tags associated with the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutProtocolsListRequest) -> dict:
    out: dict = {}
    import capo_fms.types.protocols_list_data

    out["ProtocolsList"] = capo_fms.types.protocols_list_data.serialize_aws_json_1_1(
        value["protocols_list"]
    )
    if "tag_list" in value:
        import capo_fms.types.tag_list

        out["TagList"] = capo_fms.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutProtocolsListRequest:
    out: PutProtocolsListRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProtocolsList") is not None:
        import capo_fms.types.protocols_list_data

        out["protocols_list"] = (
            capo_fms.types.protocols_list_data.deserialize_aws_json_1_1(
                data["ProtocolsList"]
            )
        )
    else:
        raise DeserializationError("PutProtocolsListRequest.protocols_list required")
    if data.get("TagList") is not None:
        import capo_fms.types.tag_list

        out["tag_list"] = capo_fms.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutProtocolsListRequest) -> dict:
    out: dict = {}
    import capo_fms.types.protocols_list_data

    out["ProtocolsList"] = capo_fms.types.protocols_list_data.serialize_cbor(
        value["protocols_list"]
    )
    if "tag_list" in value:
        import capo_fms.types.tag_list

        out["TagList"] = capo_fms.types.tag_list.serialize_cbor(value["tag_list"])
    return out


def deserialize_cbor(data: dict) -> PutProtocolsListRequest:
    out: PutProtocolsListRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProtocolsList") is not None:
        import capo_fms.types.protocols_list_data

        out["protocols_list"] = capo_fms.types.protocols_list_data.deserialize_cbor(
            data["ProtocolsList"]
        )
    else:
        raise DeserializationError("PutProtocolsListRequest.protocols_list required")
    if data.get("TagList") is not None:
        import capo_fms.types.tag_list

        out["tag_list"] = capo_fms.types.tag_list.deserialize_cbor(data["TagList"])
    return out
