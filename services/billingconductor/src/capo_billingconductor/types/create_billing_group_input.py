"""Generated from Smithy shape ``com.amazonaws.billingconductor#CreateBillingGroupInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.account_grouping
    import capo_billingconductor.types.account_id
    import capo_billingconductor.types.billing_group_description
    import capo_billingconductor.types.billing_group_name
    import capo_billingconductor.types.client_token
    import capo_billingconductor.types.computation_preference
    import capo_billingconductor.types.tag_map


class CreateBillingGroupInput(TypedDict, closed=True):
    client_token: NotRequired["capo_billingconductor.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>"""
    name: "capo_billingconductor.types.billing_group_name.BillingGroupName"
    """<p> The billing group name. The names must be unique. </p>"""
    account_grouping: "capo_billingconductor.types.account_grouping.AccountGrouping"
    """<p> The set of accounts that will be under the billing group. The set of accounts resemble the linked accounts in a consolidated billing family. </p>"""
    computation_preference: (
        "capo_billingconductor.types.computation_preference.ComputationPreference"
    )
    """<p> The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group. </p>"""
    primary_account_id: NotRequired["capo_billingconductor.types.account_id.AccountId"]
    """<p> The account ID that serves as the main account in a billing group. </p>"""
    description: NotRequired[
        "capo_billingconductor.types.billing_group_description.BillingGroupDescription"
    ]
    """<p>The description of the billing group. </p>"""
    tags: NotRequired["capo_billingconductor.types.tag_map.TagMap"]
    """<p> A map that contains tag keys and tag values that are attached to a billing group. This feature isn't available during the beta. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBillingGroupInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_billingconductor.types.account_grouping

    out["AccountGrouping"] = (
        capo_billingconductor.types.account_grouping.serialize_json(
            value["account_grouping"]
        )
    )
    import capo_billingconductor.types.computation_preference

    out["ComputationPreference"] = (
        capo_billingconductor.types.computation_preference.serialize_json(
            value["computation_preference"]
        )
    )
    if "primary_account_id" in value:
        out["PrimaryAccountId"] = value["primary_account_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_billingconductor.types.tag_map

        out["Tags"] = capo_billingconductor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateBillingGroupInput:
    out: CreateBillingGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateBillingGroupInput.name required")
    if data.get("AccountGrouping") is not None:
        import capo_billingconductor.types.account_grouping

        out["account_grouping"] = (
            capo_billingconductor.types.account_grouping.deserialize_json(
                data["AccountGrouping"]
            )
        )
    else:
        raise DeserializationError("CreateBillingGroupInput.account_grouping required")
    if data.get("ComputationPreference") is not None:
        import capo_billingconductor.types.computation_preference

        out["computation_preference"] = (
            capo_billingconductor.types.computation_preference.deserialize_json(
                data["ComputationPreference"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBillingGroupInput.computation_preference required"
        )
    if data.get("PrimaryAccountId") is not None:
        out["primary_account_id"] = data["PrimaryAccountId"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_billingconductor.types.tag_map

        out["tags"] = capo_billingconductor.types.tag_map.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: CreateBillingGroupInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
