"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceReportConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.report_output_configuration_list


class ServiceReportConfiguration(TypedDict, closed=True):
    report_outputs: "capo_resiliencehubv2.types.report_output_configuration_list.ReportOutputConfigurationList"
    """<p>Output destinations for generated reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceReportConfiguration) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.report_output_configuration_list

    out["reportOutputs"] = (
        capo_resiliencehubv2.types.report_output_configuration_list.serialize_json(
            value["report_outputs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ServiceReportConfiguration:
    out: ServiceReportConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("reportOutputs") is not None:
        import capo_resiliencehubv2.types.report_output_configuration_list

        out["report_outputs"] = (
            capo_resiliencehubv2.types.report_output_configuration_list.deserialize_json(
                data["reportOutputs"]
            )
        )
    else:
        out["report_outputs"] = []
    return out
