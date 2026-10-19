"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ApplicationPolicies``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.application_policy_list


class ApplicationPolicies(TypedDict, closed=True):
    critical: NotRequired["bool"]
    """<p>Marks the application policy extension as critical.</p>"""
    policies: (
        "capo_pca_connector_ad.types.application_policy_list.ApplicationPolicyList"
    )
    """<p>Application policies describe what the certificate can be used for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationPolicies) -> dict:
    out: dict = {}
    if "critical" in value:
        out["Critical"] = value["critical"]
    import capo_pca_connector_ad.types.application_policy_list

    out["Policies"] = (
        capo_pca_connector_ad.types.application_policy_list.serialize_json(
            value["policies"]
        )
    )
    return out


def deserialize_json(data: dict) -> ApplicationPolicies:
    out: ApplicationPolicies = {}  # type: ignore[typeddict-item]
    if data.get("Critical") is not None:
        out["critical"] = data["Critical"]
    if data.get("Policies") is not None:
        import capo_pca_connector_ad.types.application_policy_list

        out["policies"] = (
            capo_pca_connector_ad.types.application_policy_list.deserialize_json(
                data["Policies"]
            )
        )
    else:
        out["policies"] = []
    return out
