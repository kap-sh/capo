"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.boolean
    import capo_license_manager.types.client_token
    import capo_license_manager.types.consumption_configuration
    import capo_license_manager.types.datetime_range
    import capo_license_manager.types.entitlement_list
    import capo_license_manager.types.issuer
    import capo_license_manager.types.license_status
    import capo_license_manager.types.metadata_list
    import capo_license_manager.types.string


class CreateLicenseVersionRequest(TypedDict, closed=True):
    license_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license.</p>"""
    license_name: "capo_license_manager.types.string.String"
    """<p>License name.</p>"""
    product_name: "capo_license_manager.types.string.String"
    """<p>Product name.</p>"""
    issuer: "capo_license_manager.types.issuer.Issuer"
    """<p>License issuer.</p>"""
    home_region: "capo_license_manager.types.string.String"
    """<p>Home Region of the license.</p>"""
    validity: "capo_license_manager.types.datetime_range.DatetimeRange"
    """<p>Date and time range during which the license is valid, in ISO8601-UTC format.</p>"""
    license_metadata: NotRequired[
        "capo_license_manager.types.metadata_list.MetadataList"
    ]
    """<p>Information about the license.</p>"""
    entitlements: "capo_license_manager.types.entitlement_list.EntitlementList"
    """<p>License entitlements.</p>"""
    consumption_configuration: (
        "capo_license_manager.types.consumption_configuration.ConsumptionConfiguration"
    )
    """<p>Configuration for consumption of the license. Choose a provisional configuration for workloads running with continuous connectivity. Choose a borrow configuration for workloads with offline usage.</p>"""
    status: "capo_license_manager.types.license_status.LicenseStatus"
    """<p>License status.</p>"""
    client_token: "capo_license_manager.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    source_version: NotRequired["capo_license_manager.types.string.String"]
    """<p>Current version of the license.</p>"""
    reset_usage: NotRequired["capo_license_manager.types.boolean.Boolean"]
    """<p>Specifies whether to reset the license usage for the new license version. If you don't specify a value, the license usage is not reset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseVersionRequest) -> dict:
    out: dict = {}
    out["LicenseArn"] = value["license_arn"]
    out["LicenseName"] = value["license_name"]
    out["ProductName"] = value["product_name"]
    import capo_license_manager.types.issuer

    out["Issuer"] = capo_license_manager.types.issuer.serialize_aws_json_1_1(
        value["issuer"]
    )
    out["HomeRegion"] = value["home_region"]
    import capo_license_manager.types.datetime_range

    out["Validity"] = capo_license_manager.types.datetime_range.serialize_aws_json_1_1(
        value["validity"]
    )
    if "license_metadata" in value:
        import capo_license_manager.types.metadata_list

        out["LicenseMetadata"] = (
            capo_license_manager.types.metadata_list.serialize_aws_json_1_1(
                value["license_metadata"]
            )
        )
    import capo_license_manager.types.entitlement_list

    out["Entitlements"] = (
        capo_license_manager.types.entitlement_list.serialize_aws_json_1_1(
            value["entitlements"]
        )
    )
    import capo_license_manager.types.consumption_configuration

    out["ConsumptionConfiguration"] = (
        capo_license_manager.types.consumption_configuration.serialize_aws_json_1_1(
            value["consumption_configuration"]
        )
    )
    import capo_license_manager.types.license_status

    out["Status"] = capo_license_manager.types.license_status.serialize_aws_json_1_1(
        value["status"]
    )
    out["ClientToken"] = value["client_token"]
    if "source_version" in value:
        out["SourceVersion"] = value["source_version"]
    if "reset_usage" in value:
        out["ResetUsage"] = value["reset_usage"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseVersionRequest:
    out: CreateLicenseVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseArn") is not None:
        out["license_arn"] = data["LicenseArn"]
    else:
        out["license_arn"] = ""
    if data.get("LicenseName") is not None:
        out["license_name"] = data["LicenseName"]
    else:
        out["license_name"] = ""
    if data.get("ProductName") is not None:
        out["product_name"] = data["ProductName"]
    else:
        out["product_name"] = ""
    if data.get("Issuer") is not None:
        import capo_license_manager.types.issuer

        out["issuer"] = capo_license_manager.types.issuer.deserialize_aws_json_1_1(
            data["Issuer"]
        )
    else:
        raise DeserializationError("CreateLicenseVersionRequest.issuer required")
    if data.get("HomeRegion") is not None:
        out["home_region"] = data["HomeRegion"]
    else:
        out["home_region"] = ""
    if data.get("Validity") is not None:
        import capo_license_manager.types.datetime_range

        out["validity"] = (
            capo_license_manager.types.datetime_range.deserialize_aws_json_1_1(
                data["Validity"]
            )
        )
    else:
        raise DeserializationError("CreateLicenseVersionRequest.validity required")
    if data.get("LicenseMetadata") is not None:
        import capo_license_manager.types.metadata_list

        out["license_metadata"] = (
            capo_license_manager.types.metadata_list.deserialize_aws_json_1_1(
                data["LicenseMetadata"]
            )
        )
    if data.get("Entitlements") is not None:
        import capo_license_manager.types.entitlement_list

        out["entitlements"] = (
            capo_license_manager.types.entitlement_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    else:
        out["entitlements"] = []
    if data.get("ConsumptionConfiguration") is not None:
        import capo_license_manager.types.consumption_configuration

        out["consumption_configuration"] = (
            capo_license_manager.types.consumption_configuration.deserialize_aws_json_1_1(
                data["ConsumptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLicenseVersionRequest.consumption_configuration required"
        )
    if data.get("Status") is not None:
        import capo_license_manager.types.license_status

        out["status"] = (
            capo_license_manager.types.license_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_license_manager.types.license_status.LicenseStatus", ""
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("SourceVersion") is not None:
        out["source_version"] = data["SourceVersion"]
    if data.get("ResetUsage") is not None:
        out["reset_usage"] = data["ResetUsage"]
    return out
