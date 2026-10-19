"""Generated from Smithy shape ``com.amazonaws.licensemanager#UpdateLicenseManagerReportGeneratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.client_request_token
    import capo_license_manager.types.report_context
    import capo_license_manager.types.report_frequency
    import capo_license_manager.types.report_generator_name
    import capo_license_manager.types.report_type_list
    import capo_license_manager.types.string


class UpdateLicenseManagerReportGeneratorRequest(TypedDict, closed=True):
    license_manager_report_generator_arn: "capo_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the report generator to update.</p>"""
    report_generator_name: (
        "capo_license_manager.types.report_generator_name.ReportGeneratorName"
    )
    """<p>Name of the report generator.</p>"""
    type: "capo_license_manager.types.report_type_list.ReportTypeList"
    """<p>Type of reports to generate. The following report types are supported:</p> <ul> <li> <p>License configuration report - Reports the number and details of consumed licenses for a license configuration.</p> </li> <li> <p>Resource report - Reports the tracked licenses and resource consumption for a license configuration.</p> </li> </ul>"""
    report_context: "capo_license_manager.types.report_context.ReportContext"
    """<p>The report context.</p>"""
    report_frequency: "capo_license_manager.types.report_frequency.ReportFrequency"
    """<p>Frequency by which reports are generated.</p>"""
    client_token: "capo_license_manager.types.client_request_token.ClientRequestToken"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    description: NotRequired["capo_license_manager.types.string.String"]
    """<p>Description of the report generator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLicenseManagerReportGeneratorRequest) -> dict:
    out: dict = {}
    out["LicenseManagerReportGeneratorArn"] = value[
        "license_manager_report_generator_arn"
    ]
    out["ReportGeneratorName"] = value["report_generator_name"]
    import capo_license_manager.types.report_type_list

    out["Type"] = capo_license_manager.types.report_type_list.serialize_aws_json_1_1(
        value["type"]
    )
    import capo_license_manager.types.report_context

    out["ReportContext"] = (
        capo_license_manager.types.report_context.serialize_aws_json_1_1(
            value["report_context"]
        )
    )
    import capo_license_manager.types.report_frequency

    out["ReportFrequency"] = (
        capo_license_manager.types.report_frequency.serialize_aws_json_1_1(
            value["report_frequency"]
        )
    )
    out["ClientToken"] = value["client_token"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLicenseManagerReportGeneratorRequest:
    out: UpdateLicenseManagerReportGeneratorRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseManagerReportGeneratorArn") is not None:
        out["license_manager_report_generator_arn"] = data[
            "LicenseManagerReportGeneratorArn"
        ]
    else:
        out["license_manager_report_generator_arn"] = ""
    if data.get("ReportGeneratorName") is not None:
        out["report_generator_name"] = data["ReportGeneratorName"]
    else:
        out["report_generator_name"] = ""
    if data.get("Type") is not None:
        import capo_license_manager.types.report_type_list

        out["type"] = (
            capo_license_manager.types.report_type_list.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        out["type"] = []
    if data.get("ReportContext") is not None:
        import capo_license_manager.types.report_context

        out["report_context"] = (
            capo_license_manager.types.report_context.deserialize_aws_json_1_1(
                data["ReportContext"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLicenseManagerReportGeneratorRequest.report_context required"
        )
    if data.get("ReportFrequency") is not None:
        import capo_license_manager.types.report_frequency

        out["report_frequency"] = (
            capo_license_manager.types.report_frequency.deserialize_aws_json_1_1(
                data["ReportFrequency"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLicenseManagerReportGeneratorRequest.report_frequency required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
