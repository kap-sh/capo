"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkOperationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_tnb.types.instantiate_metadata
    import capo_tnb.types.modify_vnf_info_metadata
    import capo_tnb.types.update_ns_metadata


class GetSolNetworkOperationMetadata(TypedDict, closed=True):
    update_ns_metadata: NotRequired[
        "capo_tnb.types.update_ns_metadata.UpdateNsMetadata"
    ]
    """<p>Metadata related to the network operation occurrence for network instance updates. This is populated only if the lcmOperationType is <code>UPDATE</code> and the updateType is <code>UPDATE_NS</code>.</p>"""
    modify_vnf_info_metadata: NotRequired[
        "capo_tnb.types.modify_vnf_info_metadata.ModifyVnfInfoMetadata"
    ]
    """<p>Metadata related to the network operation occurrence for network function updates in a network instance. This is populated only if the lcmOperationType is <code>UPDATE</code> and the updateType is <code>MODIFY_VNF_INFORMATION</code>.</p>"""
    instantiate_metadata: NotRequired[
        "capo_tnb.types.instantiate_metadata.InstantiateMetadata"
    ]
    """<p>Metadata related to the network operation occurrence for network instantiation. This is populated only if the lcmOperationType is <code>INSTANTIATE</code>.</p>"""
    created_at: "datetime.datetime"
    """<p>The date that the resource was created.</p>"""
    last_modified: "datetime.datetime"
    """<p>The date that the resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkOperationMetadata) -> dict:
    out: dict = {}
    if "update_ns_metadata" in value:
        import capo_tnb.types.update_ns_metadata

        out["updateNsMetadata"] = capo_tnb.types.update_ns_metadata.serialize_json(
            value["update_ns_metadata"]
        )
    if "modify_vnf_info_metadata" in value:
        import capo_tnb.types.modify_vnf_info_metadata

        out["modifyVnfInfoMetadata"] = (
            capo_tnb.types.modify_vnf_info_metadata.serialize_json(
                value["modify_vnf_info_metadata"]
            )
        )
    if "instantiate_metadata" in value:
        import capo_tnb.types.instantiate_metadata

        out["instantiateMetadata"] = capo_tnb.types.instantiate_metadata.serialize_json(
            value["instantiate_metadata"]
        )
    import capo_tnb._protocol.serialize

    out["createdAt"] = capo_tnb._protocol.serialize.fmt_date_time(value["created_at"])
    import capo_tnb._protocol.serialize

    out["lastModified"] = capo_tnb._protocol.serialize.fmt_date_time(
        value["last_modified"]
    )
    return out


def deserialize_json(data: dict) -> GetSolNetworkOperationMetadata:
    out: GetSolNetworkOperationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("updateNsMetadata") is not None:
        import capo_tnb.types.update_ns_metadata

        out["update_ns_metadata"] = capo_tnb.types.update_ns_metadata.deserialize_json(
            data["updateNsMetadata"]
        )
    if data.get("modifyVnfInfoMetadata") is not None:
        import capo_tnb.types.modify_vnf_info_metadata

        out["modify_vnf_info_metadata"] = (
            capo_tnb.types.modify_vnf_info_metadata.deserialize_json(
                data["modifyVnfInfoMetadata"]
            )
        )
    if data.get("instantiateMetadata") is not None:
        import capo_tnb.types.instantiate_metadata

        out["instantiate_metadata"] = (
            capo_tnb.types.instantiate_metadata.deserialize_json(
                data["instantiateMetadata"]
            )
        )
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
