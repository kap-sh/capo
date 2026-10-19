"""Generated from Smithy shape ``com.amazonaws.launchwizard#DelegatedAdminConstraint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.service_principal_type


class DelegatedAdminConstraint(TypedDict, closed=True):
    service_principal: (
        "capo_launch_wizard.types.service_principal_type.ServicePrincipalType"
    )
    """The service principal for which the account must be a delegated administrator. For example, `stacksets.cloudformation.amazonaws.com`."""


# --- restJson1 ser/de ---
def serialize_json(value: DelegatedAdminConstraint) -> dict:
    out: dict = {}
    out["servicePrincipal"] = value["service_principal"]
    return out


def deserialize_json(data: dict) -> DelegatedAdminConstraint:
    out: DelegatedAdminConstraint = {}  # type: ignore[typeddict-item]
    if data.get("servicePrincipal") is not None:
        out["service_principal"] = data["servicePrincipal"]
    else:
        out["service_principal"] = ""
    return out
