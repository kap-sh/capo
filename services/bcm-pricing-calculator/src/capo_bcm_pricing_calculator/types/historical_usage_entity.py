"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#HistoricalUsageEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.account_id
    import capo_bcm_pricing_calculator.types.bill_interval
    import capo_bcm_pricing_calculator.types.expression
    import capo_bcm_pricing_calculator.types.operation
    import capo_bcm_pricing_calculator.types.service_code
    import capo_bcm_pricing_calculator.types.usage_type


class HistoricalUsageEntity(TypedDict, closed=True):
    service_code: "capo_bcm_pricing_calculator.types.service_code.ServiceCode"
    """<p> The Amazon Web Services service code associated with the usage. </p>"""
    usage_type: "capo_bcm_pricing_calculator.types.usage_type.UsageType"
    """<p> The type of usage. </p>"""
    operation: "capo_bcm_pricing_calculator.types.operation.Operation"
    """<p> The specific operation associated with the usage. </p>"""
    location: NotRequired["str"]
    """<p> The location associated with the usage. </p>"""
    usage_account_id: "capo_bcm_pricing_calculator.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID associated with the usage. </p>"""
    bill_interval: "capo_bcm_pricing_calculator.types.bill_interval.BillInterval"
    """<p> The time interval for the historical usage data. </p>"""
    filter_expression: "capo_bcm_pricing_calculator.types.expression.Expression"
    """<p> An optional filter expression to apply to the historical usage data. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HistoricalUsageEntity) -> dict:
    out: dict = {}
    out["serviceCode"] = value["service_code"]
    out["usageType"] = value["usage_type"]
    out["operation"] = value["operation"]
    if "location" in value:
        out["location"] = value["location"]
    out["usageAccountId"] = value["usage_account_id"]
    import capo_bcm_pricing_calculator.types.bill_interval

    out["billInterval"] = (
        capo_bcm_pricing_calculator.types.bill_interval.serialize_aws_json_1_0(
            value["bill_interval"]
        )
    )
    import capo_bcm_pricing_calculator.types.expression

    out["filterExpression"] = (
        capo_bcm_pricing_calculator.types.expression.serialize_aws_json_1_0(
            value["filter_expression"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> HistoricalUsageEntity:
    out: HistoricalUsageEntity = {}  # type: ignore[typeddict-item]
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    else:
        out["service_code"] = ""
    if data.get("usageType") is not None:
        out["usage_type"] = data["usageType"]
    else:
        out["usage_type"] = ""
    if data.get("operation") is not None:
        out["operation"] = data["operation"]
    else:
        out["operation"] = ""
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("usageAccountId") is not None:
        out["usage_account_id"] = data["usageAccountId"]
    else:
        out["usage_account_id"] = ""
    if data.get("billInterval") is not None:
        import capo_bcm_pricing_calculator.types.bill_interval

        out["bill_interval"] = (
            capo_bcm_pricing_calculator.types.bill_interval.deserialize_aws_json_1_0(
                data["billInterval"]
            )
        )
    else:
        raise DeserializationError("HistoricalUsageEntity.bill_interval required")
    if data.get("filterExpression") is not None:
        import capo_bcm_pricing_calculator.types.expression

        out["filter_expression"] = (
            capo_bcm_pricing_calculator.types.expression.deserialize_aws_json_1_0(
                data["filterExpression"]
            )
        )
    else:
        raise DeserializationError("HistoricalUsageEntity.filter_expression required")
    return out
