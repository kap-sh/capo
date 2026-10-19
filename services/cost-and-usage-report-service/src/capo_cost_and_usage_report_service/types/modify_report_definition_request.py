"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#ModifyReportDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cost_and_usage_report_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.report_definition
    import capo_cost_and_usage_report_service.types.report_name


class ModifyReportDefinitionRequest(TypedDict, closed=True):
    report_name: "capo_cost_and_usage_report_service.types.report_name.ReportName"
    report_definition: (
        "capo_cost_and_usage_report_service.types.report_definition.ReportDefinition"
    )


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyReportDefinitionRequest) -> dict:
    out: dict = {}
    out["ReportName"] = value["report_name"]
    import capo_cost_and_usage_report_service.types.report_definition

    out["ReportDefinition"] = (
        capo_cost_and_usage_report_service.types.report_definition.serialize_aws_json_1_1(
            value["report_definition"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyReportDefinitionRequest:
    out: ModifyReportDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReportName") is not None:
        out["report_name"] = data["ReportName"]
    else:
        out["report_name"] = ""
    if data.get("ReportDefinition") is not None:
        import capo_cost_and_usage_report_service.types.report_definition

        out["report_definition"] = (
            capo_cost_and_usage_report_service.types.report_definition.deserialize_aws_json_1_1(
                data["ReportDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "ModifyReportDefinitionRequest.report_definition required"
        )
    return out
