"""Generated from Smithy shape ``com.amazonaws.inspector2#GcpScopeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.gcp_capability_scope


class GcpScopeConfiguration(TypedDict, closed=True):
    vm_scanning: NotRequired[
        "capo_inspector2.types.gcp_capability_scope.GcpCapabilityScope"
    ]
    """<p>The scope configuration for VM scanning.</p>"""
    container_image_scanning: NotRequired[
        "capo_inspector2.types.gcp_capability_scope.GcpCapabilityScope"
    ]
    """<p>The scope configuration for container image scanning.</p>"""
    serverless_scanning: NotRequired[
        "capo_inspector2.types.gcp_capability_scope.GcpCapabilityScope"
    ]
    """<p>The scope configuration for serverless scanning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GcpScopeConfiguration) -> dict:
    out: dict = {}
    if "vm_scanning" in value:
        import capo_inspector2.types.gcp_capability_scope

        out["vmScanning"] = capo_inspector2.types.gcp_capability_scope.serialize_json(
            value["vm_scanning"]
        )
    if "container_image_scanning" in value:
        import capo_inspector2.types.gcp_capability_scope

        out["containerImageScanning"] = (
            capo_inspector2.types.gcp_capability_scope.serialize_json(
                value["container_image_scanning"]
            )
        )
    if "serverless_scanning" in value:
        import capo_inspector2.types.gcp_capability_scope

        out["serverlessScanning"] = (
            capo_inspector2.types.gcp_capability_scope.serialize_json(
                value["serverless_scanning"]
            )
        )
    return out


def deserialize_json(data: dict) -> GcpScopeConfiguration:
    out: GcpScopeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("vmScanning") is not None:
        import capo_inspector2.types.gcp_capability_scope

        out["vm_scanning"] = (
            capo_inspector2.types.gcp_capability_scope.deserialize_json(
                data["vmScanning"]
            )
        )
    if data.get("containerImageScanning") is not None:
        import capo_inspector2.types.gcp_capability_scope

        out["container_image_scanning"] = (
            capo_inspector2.types.gcp_capability_scope.deserialize_json(
                data["containerImageScanning"]
            )
        )
    if data.get("serverlessScanning") is not None:
        import capo_inspector2.types.gcp_capability_scope

        out["serverless_scanning"] = (
            capo_inspector2.types.gcp_capability_scope.deserialize_json(
                data["serverlessScanning"]
            )
        )
    return out
