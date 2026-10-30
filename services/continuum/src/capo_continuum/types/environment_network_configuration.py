"""Generated from Smithy shape ``com.amazonaws.continuum#EnvironmentNetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.domain_names


class EnvironmentNetworkConfiguration(TypedDict, closed=True):
    allowed_domains: NotRequired["capo_continuum.types.domain_names.DomainNames"]
    """Domains that an environment's agent execution may contact."""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentNetworkConfiguration) -> dict:
    out: dict = {}
    if "allowed_domains" in value:
        import capo_continuum.types.domain_names

        out["allowedDomains"] = capo_continuum.types.domain_names.serialize_json(
            value["allowed_domains"]
        )
    return out


def deserialize_json(data: dict) -> EnvironmentNetworkConfiguration:
    out: EnvironmentNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("allowedDomains") is not None:
        import capo_continuum.types.domain_names

        out["allowed_domains"] = capo_continuum.types.domain_names.deserialize_json(
            data["allowedDomains"]
        )
    return out
