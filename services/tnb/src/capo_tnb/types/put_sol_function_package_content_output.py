"""Generated from Smithy shape ``com.amazonaws.tnb#PutSolFunctionPackageContentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_tnb.types.put_sol_function_package_content_metadata
    import capo_tnb.types.vnf_pkg_id
    import capo_tnb.types.vnfd_id


class PutSolFunctionPackageContentOutput(TypedDict, closed=True):
    id: "capo_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>Function package ID.</p>"""
    vnfd_id: "capo_tnb.types.vnfd_id.VnfdId"
    """<p>Function package descriptor ID.</p>"""
    vnf_product_name: "str"
    """<p>Function product name.</p>"""
    vnf_provider: "str"
    """<p>Function provider.</p>"""
    vnfd_version: "str"
    """<p>Function package descriptor version.</p>"""
    metadata: "capo_tnb.types.put_sol_function_package_content_metadata.PutSolFunctionPackageContentMetadata"
    """<p>Function package metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSolFunctionPackageContentOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["vnfdId"] = value["vnfd_id"]
    out["vnfProductName"] = value["vnf_product_name"]
    out["vnfProvider"] = value["vnf_provider"]
    out["vnfdVersion"] = value["vnfd_version"]
    import capo_tnb.types.put_sol_function_package_content_metadata

    out["metadata"] = (
        capo_tnb.types.put_sol_function_package_content_metadata.serialize_json(
            value["metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutSolFunctionPackageContentOutput:
    out: PutSolFunctionPackageContentOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("vnfdId") is not None:
        out["vnfd_id"] = data["vnfdId"]
    else:
        out["vnfd_id"] = ""
    if data.get("vnfProductName") is not None:
        out["vnf_product_name"] = data["vnfProductName"]
    else:
        out["vnf_product_name"] = ""
    if data.get("vnfProvider") is not None:
        out["vnf_provider"] = data["vnfProvider"]
    else:
        out["vnf_provider"] = ""
    if data.get("vnfdVersion") is not None:
        out["vnfd_version"] = data["vnfdVersion"]
    else:
        out["vnfd_version"] = ""
    if data.get("metadata") is not None:
        import capo_tnb.types.put_sol_function_package_content_metadata

        out["metadata"] = (
            capo_tnb.types.put_sol_function_package_content_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError(
            "PutSolFunctionPackageContentOutput.metadata required"
        )
    return out
