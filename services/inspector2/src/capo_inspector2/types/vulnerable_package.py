"""Generated from Smithy shape ``com.amazonaws.inspector2#VulnerablePackage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.file_path
    import capo_inspector2.types.lambda_layer_arn
    import capo_inspector2.types.package_architecture
    import capo_inspector2.types.package_epoch
    import capo_inspector2.types.package_manager
    import capo_inspector2.types.package_name
    import capo_inspector2.types.package_release
    import capo_inspector2.types.package_version
    import capo_inspector2.types.source_layer_hash
    import capo_inspector2.types.vulnerable_package_remediation


class VulnerablePackage(TypedDict, closed=True):
    name: "capo_inspector2.types.package_name.PackageName"
    """<p>The name of the vulnerable package.</p>"""
    version: "capo_inspector2.types.package_version.PackageVersion"
    """<p>The version of the vulnerable package.</p>"""
    source_layer_hash: NotRequired[
        "capo_inspector2.types.source_layer_hash.SourceLayerHash"
    ]
    """<p>The source layer hash of the vulnerable package.</p>"""
    epoch: "capo_inspector2.types.package_epoch.PackageEpoch"
    """<p>The epoch of the vulnerable package.</p>"""
    release: NotRequired["capo_inspector2.types.package_release.PackageRelease"]
    """<p>The release of the vulnerable package.</p>"""
    arch: NotRequired["capo_inspector2.types.package_architecture.PackageArchitecture"]
    """<p>The architecture of the vulnerable package.</p>"""
    package_manager: NotRequired["capo_inspector2.types.package_manager.PackageManager"]
    """<p>The package manager of the vulnerable package.</p>"""
    file_path: NotRequired["capo_inspector2.types.file_path.FilePath"]
    """<p>The file path of the vulnerable package.</p>"""
    fixed_in_version: NotRequired[
        "capo_inspector2.types.package_version.PackageVersion"
    ]
    """<p>The version of the package that contains the vulnerability fix.</p>"""
    remediation: NotRequired[
        "capo_inspector2.types.vulnerable_package_remediation.VulnerablePackageRemediation"
    ]
    """<p>The code to run in your environment to update packages with a fix available.</p>"""
    source_lambda_layer_arn: NotRequired[
        "capo_inspector2.types.lambda_layer_arn.LambdaLayerArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the Amazon Web Services Lambda function affected by a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VulnerablePackage) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["version"] = value["version"]
    if "source_layer_hash" in value:
        out["sourceLayerHash"] = value["source_layer_hash"]
    out["epoch"] = value.get("epoch", 0)
    if "release" in value:
        out["release"] = value["release"]
    if "arch" in value:
        out["arch"] = value["arch"]
    if "package_manager" in value:
        out["packageManager"] = value["package_manager"]
    if "file_path" in value:
        out["filePath"] = value["file_path"]
    if "fixed_in_version" in value:
        out["fixedInVersion"] = value["fixed_in_version"]
    if "remediation" in value:
        out["remediation"] = value["remediation"]
    if "source_lambda_layer_arn" in value:
        out["sourceLambdaLayerArn"] = value["source_lambda_layer_arn"]
    return out


def deserialize_json(data: dict) -> VulnerablePackage:
    out: VulnerablePackage = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("sourceLayerHash") is not None:
        out["source_layer_hash"] = data["sourceLayerHash"]
    if data.get("epoch") is not None:
        out["epoch"] = data["epoch"]
    else:
        out["epoch"] = 0
    if data.get("release") is not None:
        out["release"] = data["release"]
    if data.get("arch") is not None:
        out["arch"] = data["arch"]
    if data.get("packageManager") is not None:
        out["package_manager"] = data["packageManager"]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    if data.get("fixedInVersion") is not None:
        out["fixed_in_version"] = data["fixedInVersion"]
    if data.get("remediation") is not None:
        out["remediation"] = data["remediation"]
    if data.get("sourceLambdaLayerArn") is not None:
        out["source_lambda_layer_arn"] = data["sourceLambdaLayerArn"]
    return out
