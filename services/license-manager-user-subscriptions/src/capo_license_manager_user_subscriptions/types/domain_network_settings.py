"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#DomainNetworkSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.subnets


class DomainNetworkSettings(TypedDict, closed=True):
    subnets: "capo_license_manager_user_subscriptions.types.subnets.Subnets"
    """<p>Contains a list of subnets that apply for the Active Directory domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainNetworkSettings) -> dict:
    out: dict = {}
    import capo_license_manager_user_subscriptions.types.subnets

    out["Subnets"] = (
        capo_license_manager_user_subscriptions.types.subnets.serialize_json(
            value["subnets"]
        )
    )
    return out


def deserialize_json(data: dict) -> DomainNetworkSettings:
    out: DomainNetworkSettings = {}  # type: ignore[typeddict-item]
    if data.get("Subnets") is not None:
        import capo_license_manager_user_subscriptions.types.subnets

        out["subnets"] = (
            capo_license_manager_user_subscriptions.types.subnets.deserialize_json(
                data["Subnets"]
            )
        )
    else:
        out["subnets"] = []
    return out
