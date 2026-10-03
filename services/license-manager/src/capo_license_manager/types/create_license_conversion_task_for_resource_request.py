"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseConversionTaskForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.license_conversion_context


class CreateLicenseConversionTaskForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the resource you are converting the license type for.</p>"""
    source_license_context: (
        "capo_license_manager.types.license_conversion_context.LicenseConversionContext"
    )
    """<p>Information that identifies the license type you are converting from. For the structure of the source license, see <a href="https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-procedures.html#conversion-cli">Convert a license type using the CLI </a> in the <i>License Manager User Guide</i>.</p>"""
    destination_license_context: (
        "capo_license_manager.types.license_conversion_context.LicenseConversionContext"
    )
    """<p>Information that identifies the license type you are converting to. For the structure of the destination license, see <a href="https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-procedures.html#conversion-cli">Convert a license type using the CLI </a> in the <i>License Manager User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CreateLicenseConversionTaskForResourceRequest,
) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_license_manager.types.license_conversion_context

    out["SourceLicenseContext"] = (
        capo_license_manager.types.license_conversion_context.serialize_aws_json_1_1(
            value["source_license_context"]
        )
    )
    import capo_license_manager.types.license_conversion_context

    out["DestinationLicenseContext"] = (
        capo_license_manager.types.license_conversion_context.serialize_aws_json_1_1(
            value["destination_license_context"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateLicenseConversionTaskForResourceRequest:
    out: CreateLicenseConversionTaskForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "CreateLicenseConversionTaskForResourceRequest.resource_arn required"
        )
    if data.get("SourceLicenseContext") is not None:
        import capo_license_manager.types.license_conversion_context

        out["source_license_context"] = (
            capo_license_manager.types.license_conversion_context.deserialize_aws_json_1_1(
                data["SourceLicenseContext"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLicenseConversionTaskForResourceRequest.source_license_context required"
        )
    if data.get("DestinationLicenseContext") is not None:
        import capo_license_manager.types.license_conversion_context

        out["destination_license_context"] = (
            capo_license_manager.types.license_conversion_context.deserialize_aws_json_1_1(
                data["DestinationLicenseContext"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLicenseConversionTaskForResourceRequest.destination_license_context required"
        )
    return out
