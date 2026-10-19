"""Generated from Smithy shape ``com.amazonaws.billing#CreditData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_billing.types.account_id
    import capo_billing.types.amount
    import capo_billing.types.application_type
    import capo_billing.types.credit_id
    import capo_billing.types.credit_sharing_type
    import capo_billing.types.credit_status
    import capo_billing.types.product_names
    import capo_billing.types.purchase_type_applications
    import capo_billing.types.shareable_account_ids


class CreditData(TypedDict, closed=True):
    credit_id: "capo_billing.types.credit_id.CreditId"
    """<p>The unique identifier for the credit.</p>"""
    account_id: "capo_billing.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID that owns the credit.</p>"""
    credit_type: "str"
    """<p>The type of credit. Examples: <code>Promotion</code>, <code>Refund</code>, <code>TrueUp</code>.</p>"""
    initial_amount: "capo_billing.types.amount.Amount"
    """<p>The initial amount of the credit when it was issued.</p>"""
    remaining_amount: "capo_billing.types.amount.Amount"
    """<p>The unused balance of the credit.</p>"""
    estimated_amount: NotRequired["capo_billing.types.amount.Amount"]
    """<p>The estimated remaining balance, including in-flight (open) bills that have not yet been finalized.</p>"""
    applicable_product_names: NotRequired[
        "capo_billing.types.product_names.ProductNames"
    ]
    """<p>The names of Amazon Web Services services this credit applies to.</p>"""
    description: "str"
    """<p>A human-readable description of the credit.</p>"""
    start_date: "datetime.datetime"
    """<p>The date the credit becomes valid, as Unix epoch seconds.</p>"""
    end_date: NotRequired["datetime.datetime"]
    """<p>The date the credit expires, as Unix epoch seconds.</p>"""
    exhaust_date: NotRequired["datetime.datetime"]
    """<p>The date the credit balance reached zero, as Unix epoch seconds.</p>"""
    application_type: NotRequired["capo_billing.types.application_type.ApplicationType"]
    """<p>When the credit is applied during bill computation. Valid values: <code>BEFORE_CROSS_SERVICE_DISCOUNTS</code>, <code>AFTER_DISCOUNTS</code>.</p>"""
    shareable_accounts: NotRequired[
        "capo_billing.types.shareable_account_ids.ShareableAccountIds"
    ]
    """<p>The Amazon Web Services account IDs entitled to apply this credit.</p>"""
    account_has_credit_sharing_enabled: NotRequired["bool"]
    """<p>Whether the owning account has account-level credit sharing turned on.</p>"""
    credit_console_visibility: NotRequired["str"]
    """<p>The display configuration for the credit in the Amazon Web Services Billing console.</p>"""
    credit_sharing_type: NotRequired[
        "capo_billing.types.credit_sharing_type.CreditSharingType"
    ]
    """<p>The sharing configuration for the credit. Valid values: <code>DEFAULT</code>, <code>DISABLED</code>, <code>CUSTOM</code>, <code>COST_CATEGORY_RULE</code>.</p>"""
    cost_category_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Cost Category controlling the credit's sharing scope. Present only when <code>creditSharingType</code> is <code>COST_CATEGORY_RULE</code>.</p>"""
    rule_name: NotRequired["str"]
    """<p>The rule name within the Cost Category. Present only when <code>creditSharingType</code> is <code>COST_CATEGORY_RULE</code>.</p>"""
    credit_status: NotRequired["capo_billing.types.credit_status.CreditStatus"]
    """<p>Whether the credit participates in billing runs. Valid values: <code>ENABLED</code>, <code>DISABLED</code>.</p>"""
    purchase_type_applications: NotRequired[
        "capo_billing.types.purchase_type_applications.PurchaseTypeApplications"
    ]
    """<p>Restricts which purchase types this credit applies to. When <code>null</code> or omitted, the credit applies to all purchase types.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreditData) -> dict:
    out: dict = {}
    out["creditId"] = value["credit_id"]
    out["accountId"] = value["account_id"]
    out["creditType"] = value["credit_type"]
    import capo_billing.types.amount

    out["initialAmount"] = capo_billing.types.amount.serialize_aws_json_1_0(
        value["initial_amount"]
    )
    import capo_billing.types.amount

    out["remainingAmount"] = capo_billing.types.amount.serialize_aws_json_1_0(
        value["remaining_amount"]
    )
    if "estimated_amount" in value:
        import capo_billing.types.amount

        out["estimatedAmount"] = capo_billing.types.amount.serialize_aws_json_1_0(
            value["estimated_amount"]
        )
    if "applicable_product_names" in value:
        import capo_billing.types.product_names

        out["applicableProductNames"] = (
            capo_billing.types.product_names.serialize_aws_json_1_0(
                value["applicable_product_names"]
            )
        )
    out["description"] = value["description"]
    import capo_billing.types._prelude.timestamp

    out["startDate"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
        value["start_date"]
    )
    if "end_date" in value:
        import capo_billing.types._prelude.timestamp

        out["endDate"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["end_date"]
        )
    if "exhaust_date" in value:
        import capo_billing.types._prelude.timestamp

        out["exhaustDate"] = (
            capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["exhaust_date"]
            )
        )
    if "application_type" in value:
        import capo_billing.types.application_type

        out["applicationType"] = (
            capo_billing.types.application_type.serialize_aws_json_1_0(
                value["application_type"]
            )
        )
    if "shareable_accounts" in value:
        import capo_billing.types.shareable_account_ids

        out["shareableAccounts"] = (
            capo_billing.types.shareable_account_ids.serialize_aws_json_1_0(
                value["shareable_accounts"]
            )
        )
    if "account_has_credit_sharing_enabled" in value:
        out["accountHasCreditSharingEnabled"] = value[
            "account_has_credit_sharing_enabled"
        ]
    if "credit_console_visibility" in value:
        out["creditConsoleVisibility"] = value["credit_console_visibility"]
    if "credit_sharing_type" in value:
        import capo_billing.types.credit_sharing_type

        out["creditSharingType"] = (
            capo_billing.types.credit_sharing_type.serialize_aws_json_1_0(
                value["credit_sharing_type"]
            )
        )
    if "cost_category_arn" in value:
        out["costCategoryArn"] = value["cost_category_arn"]
    if "rule_name" in value:
        out["ruleName"] = value["rule_name"]
    if "credit_status" in value:
        import capo_billing.types.credit_status

        out["creditStatus"] = capo_billing.types.credit_status.serialize_aws_json_1_0(
            value["credit_status"]
        )
    if "purchase_type_applications" in value:
        import capo_billing.types.purchase_type_applications

        out["purchaseTypeApplications"] = (
            capo_billing.types.purchase_type_applications.serialize_aws_json_1_0(
                value["purchase_type_applications"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreditData:
    out: CreditData = {}  # type: ignore[typeddict-item]
    if data.get("creditId") is not None:
        out["credit_id"] = data["creditId"]
    else:
        out["credit_id"] = ""
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("creditType") is not None:
        out["credit_type"] = data["creditType"]
    else:
        out["credit_type"] = ""
    if data.get("initialAmount") is not None:
        import capo_billing.types.amount

        out["initial_amount"] = capo_billing.types.amount.deserialize_aws_json_1_0(
            data["initialAmount"]
        )
    else:
        raise DeserializationError("CreditData.initial_amount required")
    if data.get("remainingAmount") is not None:
        import capo_billing.types.amount

        out["remaining_amount"] = capo_billing.types.amount.deserialize_aws_json_1_0(
            data["remainingAmount"]
        )
    else:
        raise DeserializationError("CreditData.remaining_amount required")
    if data.get("estimatedAmount") is not None:
        import capo_billing.types.amount

        out["estimated_amount"] = capo_billing.types.amount.deserialize_aws_json_1_0(
            data["estimatedAmount"]
        )
    if data.get("applicableProductNames") is not None:
        import capo_billing.types.product_names

        out["applicable_product_names"] = (
            capo_billing.types.product_names.deserialize_aws_json_1_0(
                data["applicableProductNames"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("startDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["start_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startDate"]
            )
        )
    else:
        import datetime

        out["start_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["end_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endDate"]
            )
        )
    if data.get("exhaustDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["exhaust_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["exhaustDate"]
            )
        )
    if data.get("applicationType") is not None:
        import capo_billing.types.application_type

        out["application_type"] = (
            capo_billing.types.application_type.deserialize_aws_json_1_0(
                data["applicationType"]
            )
        )
    if data.get("shareableAccounts") is not None:
        import capo_billing.types.shareable_account_ids

        out["shareable_accounts"] = (
            capo_billing.types.shareable_account_ids.deserialize_aws_json_1_0(
                data["shareableAccounts"]
            )
        )
    if data.get("accountHasCreditSharingEnabled") is not None:
        out["account_has_credit_sharing_enabled"] = data[
            "accountHasCreditSharingEnabled"
        ]
    if data.get("creditConsoleVisibility") is not None:
        out["credit_console_visibility"] = data["creditConsoleVisibility"]
    if data.get("creditSharingType") is not None:
        import capo_billing.types.credit_sharing_type

        out["credit_sharing_type"] = (
            capo_billing.types.credit_sharing_type.deserialize_aws_json_1_0(
                data["creditSharingType"]
            )
        )
    if data.get("costCategoryArn") is not None:
        out["cost_category_arn"] = data["costCategoryArn"]
    if data.get("ruleName") is not None:
        out["rule_name"] = data["ruleName"]
    if data.get("creditStatus") is not None:
        import capo_billing.types.credit_status

        out["credit_status"] = (
            capo_billing.types.credit_status.deserialize_aws_json_1_0(
                data["creditStatus"]
            )
        )
    if data.get("purchaseTypeApplications") is not None:
        import capo_billing.types.purchase_type_applications

        out["purchase_type_applications"] = (
            capo_billing.types.purchase_type_applications.deserialize_aws_json_1_0(
                data["purchaseTypeApplications"]
            )
        )
    return out
