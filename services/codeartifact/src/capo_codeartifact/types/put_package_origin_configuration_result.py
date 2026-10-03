"""Generated from Smithy shape ``com.amazonaws.codeartifact#PutPackageOriginConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.package_origin_configuration


class PutPackageOriginConfigurationResult(TypedDict, closed=True):
    origin_configuration: NotRequired[
        "capo_codeartifact.types.package_origin_configuration.PackageOriginConfiguration"
    ]
    """<p>A <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginConfiguration.html">PackageOriginConfiguration</a> object that describes the origin configuration set for the package. It contains a <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html">PackageOriginRestrictions</a> object that describes how new versions of the package can be introduced to the repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutPackageOriginConfigurationResult) -> dict:
    out: dict = {}
    if "origin_configuration" in value:
        import capo_codeartifact.types.package_origin_configuration

        out["originConfiguration"] = (
            capo_codeartifact.types.package_origin_configuration.serialize_json(
                value["origin_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutPackageOriginConfigurationResult:
    out: PutPackageOriginConfigurationResult = {}  # type: ignore[typeddict-item]
    if data.get("originConfiguration") is not None:
        import capo_codeartifact.types.package_origin_configuration

        out["origin_configuration"] = (
            capo_codeartifact.types.package_origin_configuration.deserialize_json(
                data["originConfiguration"]
            )
        )
    return out
