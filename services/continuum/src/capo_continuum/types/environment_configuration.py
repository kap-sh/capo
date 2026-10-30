"""Generated from Smithy shape ``com.amazonaws.continuum#EnvironmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_network_configuration
    import capo_continuum.types.patch_creation_policy
    import capo_continuum.types.scan_frequency


class EnvironmentConfiguration(TypedDict, closed=True):
    network: NotRequired[
        "capo_continuum.types.environment_network_configuration.EnvironmentNetworkConfiguration"
    ]
    """Network policy for agent execution."""
    scan_frequency: NotRequired["capo_continuum.types.scan_frequency.ScanFrequency"]
    """Recurring scan interval: P1D (1 day), P2D (2 days), or P7D (7 days). PT0H disables recurring scans. Defaults to P1D when creating an environment."""
    patch_creation_policy: NotRequired[
        "capo_continuum.types.patch_creation_policy.PatchCreationPolicy"
    ]
    """Whether Continuum creates a patch for a proposed remediation. Defaults to DISABLED."""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfiguration) -> dict:
    out: dict = {}
    if "network" in value:
        import capo_continuum.types.environment_network_configuration

        out["network"] = (
            capo_continuum.types.environment_network_configuration.serialize_json(
                value["network"]
            )
        )
    if "scan_frequency" in value:
        out["scanFrequency"] = value["scan_frequency"]
    if "patch_creation_policy" in value:
        import capo_continuum.types.patch_creation_policy

        out["patchCreationPolicy"] = (
            capo_continuum.types.patch_creation_policy.serialize_json(
                value["patch_creation_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnvironmentConfiguration:
    out: EnvironmentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("network") is not None:
        import capo_continuum.types.environment_network_configuration

        out["network"] = (
            capo_continuum.types.environment_network_configuration.deserialize_json(
                data["network"]
            )
        )
    if data.get("scanFrequency") is not None:
        out["scan_frequency"] = data["scanFrequency"]
    if data.get("patchCreationPolicy") is not None:
        import capo_continuum.types.patch_creation_policy

        out["patch_creation_policy"] = (
            capo_continuum.types.patch_creation_policy.deserialize_json(
                data["patchCreationPolicy"]
            )
        )
    return out
