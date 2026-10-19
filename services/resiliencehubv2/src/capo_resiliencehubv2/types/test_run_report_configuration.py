"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunReportConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.report_output_configuration_list


class TestRunReportConfiguration(TypedDict, closed=True):
    report_output: "capo_resiliencehubv2.types.report_output_configuration_list.ReportOutputConfigurationList"
    """<p>The output destinations for generated reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRunReportConfiguration) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.report_output_configuration_list

    out["reportOutput"] = (
        capo_resiliencehubv2.types.report_output_configuration_list.serialize_json(
            value["report_output"]
        )
    )
    return out


def deserialize_json(data: dict) -> TestRunReportConfiguration:
    out: TestRunReportConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("reportOutput") is not None:
        import capo_resiliencehubv2.types.report_output_configuration_list

        out["report_output"] = (
            capo_resiliencehubv2.types.report_output_configuration_list.deserialize_json(
                data["reportOutput"]
            )
        )
    else:
        out["report_output"] = []
    return out
