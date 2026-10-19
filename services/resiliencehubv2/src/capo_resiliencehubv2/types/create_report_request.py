"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.client_token
    import capo_resiliencehubv2.types.report_type


class CreateReportRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    report_type: "capo_resiliencehubv2.types.report_type.ReportType"
    """<p>The type of report to generate.</p>"""
    client_token: NotRequired["capo_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateReportRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    import capo_resiliencehubv2.types.report_type

    out["reportType"] = capo_resiliencehubv2.types.report_type.serialize_json(
        value["report_type"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateReportRequest:
    out: CreateReportRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("reportType") is not None:
        import capo_resiliencehubv2.types.report_type

        out["report_type"] = capo_resiliencehubv2.types.report_type.deserialize_json(
            data["reportType"]
        )
    else:
        import typing

        out["report_type"] = typing.cast(
            "capo_resiliencehubv2.types.report_type.ReportType", ""
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
