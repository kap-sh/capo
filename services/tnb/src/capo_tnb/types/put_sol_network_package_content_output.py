"""Generated from Smithy shape ``com.amazonaws.tnb#PutSolNetworkPackageContentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_tnb.types.nsd_id
    import capo_tnb.types.nsd_info_arn
    import capo_tnb.types.nsd_info_id
    import capo_tnb.types.put_sol_network_package_content_metadata
    import capo_tnb.types.vnf_pkg_id_list


class PutSolNetworkPackageContentOutput(TypedDict, closed=True):
    id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>Network package ID.</p>"""
    arn: "capo_tnb.types.nsd_info_arn.NsdInfoArn"
    """<p>Network package ARN.</p>"""
    nsd_id: "capo_tnb.types.nsd_id.NsdId"
    """<p>Network service descriptor ID.</p>"""
    nsd_name: "str"
    """<p>Network service descriptor name.</p>"""
    nsd_version: "str"
    """<p>Network service descriptor version.</p>"""
    vnf_pkg_ids: "capo_tnb.types.vnf_pkg_id_list.VnfPkgIdList"
    """<p>Function package IDs.</p>"""
    metadata: "capo_tnb.types.put_sol_network_package_content_metadata.PutSolNetworkPackageContentMetadata"
    """<p>Network package metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSolNetworkPackageContentOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["nsdId"] = value["nsd_id"]
    out["nsdName"] = value["nsd_name"]
    out["nsdVersion"] = value["nsd_version"]
    import capo_tnb.types.vnf_pkg_id_list

    out["vnfPkgIds"] = capo_tnb.types.vnf_pkg_id_list.serialize_json(
        value["vnf_pkg_ids"]
    )
    import capo_tnb.types.put_sol_network_package_content_metadata

    out["metadata"] = (
        capo_tnb.types.put_sol_network_package_content_metadata.serialize_json(
            value["metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutSolNetworkPackageContentOutput:
    out: PutSolNetworkPackageContentOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("nsdId") is not None:
        out["nsd_id"] = data["nsdId"]
    else:
        out["nsd_id"] = ""
    if data.get("nsdName") is not None:
        out["nsd_name"] = data["nsdName"]
    else:
        out["nsd_name"] = ""
    if data.get("nsdVersion") is not None:
        out["nsd_version"] = data["nsdVersion"]
    else:
        out["nsd_version"] = ""
    if data.get("vnfPkgIds") is not None:
        import capo_tnb.types.vnf_pkg_id_list

        out["vnf_pkg_ids"] = capo_tnb.types.vnf_pkg_id_list.deserialize_json(
            data["vnfPkgIds"]
        )
    else:
        out["vnf_pkg_ids"] = []
    if data.get("metadata") is not None:
        import capo_tnb.types.put_sol_network_package_content_metadata

        out["metadata"] = (
            capo_tnb.types.put_sol_network_package_content_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError(
            "PutSolNetworkPackageContentOutput.metadata required"
        )
    return out
