"""Generated from Smithy shape ``com.amazonaws.eks#CreateEksAnywhereSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.boolean
    import capo_eks.types.eks_anywhere_subscription_license_type
    import capo_eks.types.eks_anywhere_subscription_name
    import capo_eks.types.eks_anywhere_subscription_term
    import capo_eks.types.integer
    import capo_eks.types.string
    import capo_eks.types.tag_map


class CreateEksAnywhereSubscriptionRequest(TypedDict, closed=True):
    name: "capo_eks.types.eks_anywhere_subscription_name.EksAnywhereSubscriptionName"
    """<p>The unique name for your subscription. It must be unique in your Amazon Web Services account in the Amazon Web Services Region you're creating the subscription in. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphabetic character and can't be longer than 100 characters.</p>"""
    term: "capo_eks.types.eks_anywhere_subscription_term.EksAnywhereSubscriptionTerm"
    """<p>An object representing the term duration and term unit type of your subscription. This determines the term length of your subscription. Valid values are MONTHS for term unit and 12 or 36 for term duration, indicating a 12 month or 36 month subscription. This value cannot be changed after creating the subscription.</p>"""
    license_quantity: NotRequired["capo_eks.types.integer.Integer"]
    """<p>The number of licenses to purchase with the subscription. Valid values are between 1 and 100. This value can't be changed after creating the subscription.</p>"""
    license_type: NotRequired[
        "capo_eks.types.eks_anywhere_subscription_license_type.EksAnywhereSubscriptionLicenseType"
    ]
    """<p>The license type for all licenses in the subscription. Valid value is CLUSTER. With the CLUSTER license type, each license covers support for a single EKS Anywhere cluster.</p>"""
    auto_renew: NotRequired["capo_eks.types.boolean.Boolean"]
    """<p>A boolean indicating whether the subscription auto renews at the end of the term.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["capo_eks.types.tag_map.TagMap"]
    """<p>The metadata for a subscription to assist with categorization and organization. Each tag consists of a key and an optional value. Subscription tags don't propagate to any other resources associated with the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEksAnywhereSubscriptionRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_eks.types.eks_anywhere_subscription_term

    out["term"] = capo_eks.types.eks_anywhere_subscription_term.serialize_json(
        value["term"]
    )
    if "license_quantity" in value:
        out["licenseQuantity"] = value["license_quantity"]
    if "license_type" in value:
        import capo_eks.types.eks_anywhere_subscription_license_type

        out["licenseType"] = (
            capo_eks.types.eks_anywhere_subscription_license_type.serialize_json(
                value["license_type"]
            )
        )
    if "auto_renew" in value:
        out["autoRenew"] = value["auto_renew"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateEksAnywhereSubscriptionRequest:
    out: CreateEksAnywhereSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEksAnywhereSubscriptionRequest.name required")
    if data.get("term") is not None:
        import capo_eks.types.eks_anywhere_subscription_term

        out["term"] = capo_eks.types.eks_anywhere_subscription_term.deserialize_json(
            data["term"]
        )
    else:
        raise DeserializationError("CreateEksAnywhereSubscriptionRequest.term required")
    if data.get("licenseQuantity") is not None:
        out["license_quantity"] = data["licenseQuantity"]
    if data.get("licenseType") is not None:
        import capo_eks.types.eks_anywhere_subscription_license_type

        out["license_type"] = (
            capo_eks.types.eks_anywhere_subscription_license_type.deserialize_json(
                data["licenseType"]
            )
        )
    if data.get("autoRenew") is not None:
        out["auto_renew"] = data["autoRenew"]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("tags") is not None:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.deserialize_json(data["tags"])
    return out
