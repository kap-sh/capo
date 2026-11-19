"""Generated from Smithy shape ``com.amazonaws.inspector2#GcpScopeConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.gcp_capability_scope_input


class GcpScopeConfigurationInput(TypedDict, closed=True):
    vm_scanning: NotRequired[
        "capo_inspector2.types.gcp_capability_scope_input.GcpCapabilityScopeInput"
    ]
    """<p>The scope configuration input for VM scanning.</p>"""
    container_image_scanning: NotRequired[
        "capo_inspector2.types.gcp_capability_scope_input.GcpCapabilityScopeInput"
    ]
    """<p>The scope configuration input for container image scanning.</p>"""
    serverless_scanning: NotRequired[
        "capo_inspector2.types.gcp_capability_scope_input.GcpCapabilityScopeInput"
    ]
    """<p>The scope configuration input for serverless scanning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GcpScopeConfigurationInput) -> dict:
    out: dict = {}
    if "vm_scanning" in value:
        import capo_inspector2.types.gcp_capability_scope_input

        out["vmScanning"] = (
            capo_inspector2.types.gcp_capability_scope_input.serialize_json(
                value["vm_scanning"]
            )
        )
    if "container_image_scanning" in value:
        import capo_inspector2.types.gcp_capability_scope_input

        out["containerImageScanning"] = (
            capo_inspector2.types.gcp_capability_scope_input.serialize_json(
                value["container_image_scanning"]
            )
        )
    if "serverless_scanning" in value:
        import capo_inspector2.types.gcp_capability_scope_input

        out["serverlessScanning"] = (
            capo_inspector2.types.gcp_capability_scope_input.serialize_json(
                value["serverless_scanning"]
            )
        )
    return out


def deserialize_json(data: dict) -> GcpScopeConfigurationInput:
    out: GcpScopeConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("vmScanning") is not None:
        import capo_inspector2.types.gcp_capability_scope_input

        out["vm_scanning"] = (
            capo_inspector2.types.gcp_capability_scope_input.deserialize_json(
                data["vmScanning"]
            )
        )
    if data.get("containerImageScanning") is not None:
        import capo_inspector2.types.gcp_capability_scope_input

        out["container_image_scanning"] = (
            capo_inspector2.types.gcp_capability_scope_input.deserialize_json(
                data["containerImageScanning"]
            )
        )
    if data.get("serverlessScanning") is not None:
        import capo_inspector2.types.gcp_capability_scope_input

        out["serverless_scanning"] = (
            capo_inspector2.types.gcp_capability_scope_input.deserialize_json(
                data["serverlessScanning"]
            )
        )
    return out
