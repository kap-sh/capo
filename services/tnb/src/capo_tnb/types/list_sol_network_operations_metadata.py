"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkOperationsMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_tnb.types.nsd_info_id
    import capo_tnb.types.vnf_instance_id


class ListSolNetworkOperationsMetadata(TypedDict, closed=True):
    nsd_info_id: NotRequired["capo_tnb.types.nsd_info_id.NsdInfoId"]
    """<p>The network service descriptor id used for the operation.</p> <p>Only present if the updateType is <code>UPDATE_NS</code>.</p>"""
    vnf_instance_id: NotRequired["capo_tnb.types.vnf_instance_id.VnfInstanceId"]
    """<p>The network function id used for the operation.</p> <p>Only present if the updateType is <code>MODIFY_VNF_INFO</code>.</p>"""
    created_at: "datetime.datetime"
    """<p>The date that the resource was created.</p>"""
    last_modified: "datetime.datetime"
    """<p>The date that the resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkOperationsMetadata) -> dict:
    out: dict = {}
    if "nsd_info_id" in value:
        out["nsdInfoId"] = value["nsd_info_id"]
    if "vnf_instance_id" in value:
        out["vnfInstanceId"] = value["vnf_instance_id"]
    import capo_tnb._protocol.serialize

    out["createdAt"] = capo_tnb._protocol.serialize.fmt_date_time(value["created_at"])
    import capo_tnb._protocol.serialize

    out["lastModified"] = capo_tnb._protocol.serialize.fmt_date_time(
        value["last_modified"]
    )
    return out


def deserialize_json(data: dict) -> ListSolNetworkOperationsMetadata:
    out: ListSolNetworkOperationsMetadata = {}  # type: ignore[typeddict-item]
    if data.get("nsdInfoId") is not None:
        out["nsd_info_id"] = data["nsdInfoId"]
    if data.get("vnfInstanceId") is not None:
        out["vnf_instance_id"] = data["vnfInstanceId"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastModified") is not None:
        import datetime

        out["last_modified"] = datetime.datetime.fromisoformat(
            data["lastModified"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["last_modified"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
