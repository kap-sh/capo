"""Generated from Smithy shape ``com.amazonaws.panorama#PackageImportJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.node_package_id
    import capo_panorama.types.node_package_patch_version
    import capo_panorama.types.node_package_version
    import capo_panorama.types.out_put_s3_location


class PackageImportJobOutput(TypedDict, closed=True):
    package_id: "capo_panorama.types.node_package_id.NodePackageId"
    """<p>The package's ID.</p>"""
    package_version: "capo_panorama.types.node_package_version.NodePackageVersion"
    """<p>The package's version.</p>"""
    patch_version: (
        "capo_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    )
    """<p>The package's patch version.</p>"""
    output_s3_location: "capo_panorama.types.out_put_s3_location.OutPutS3Location"
    """<p>The package's output location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageImportJobOutput) -> dict:
    out: dict = {}
    out["PackageId"] = value["package_id"]
    out["PackageVersion"] = value["package_version"]
    out["PatchVersion"] = value["patch_version"]
    import capo_panorama.types.out_put_s3_location

    out["OutputS3Location"] = capo_panorama.types.out_put_s3_location.serialize_json(
        value["output_s3_location"]
    )
    return out


def deserialize_json(data: dict) -> PackageImportJobOutput:
    out: PackageImportJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("PackageId") is not None:
        out["package_id"] = data["PackageId"]
    else:
        out["package_id"] = ""
    if data.get("PackageVersion") is not None:
        out["package_version"] = data["PackageVersion"]
    else:
        out["package_version"] = ""
    if data.get("PatchVersion") is not None:
        out["patch_version"] = data["PatchVersion"]
    else:
        out["patch_version"] = ""
    if data.get("OutputS3Location") is not None:
        import capo_panorama.types.out_put_s3_location

        out["output_s3_location"] = (
            capo_panorama.types.out_put_s3_location.deserialize_json(
                data["OutputS3Location"]
            )
        )
    else:
        raise DeserializationError("PackageImportJobOutput.output_s3_location required")
    return out
