"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.client_token
    import capo_license_manager.types.consumption_configuration
    import capo_license_manager.types.datetime_range
    import capo_license_manager.types.entitlement_list
    import capo_license_manager.types.issuer
    import capo_license_manager.types.metadata_list
    import capo_license_manager.types.string
    import capo_license_manager.types.tag_list


class CreateLicenseRequest(TypedDict, closed=True):
    license_name: "capo_license_manager.types.string.String"
    """<p>License name.</p>"""
    product_name: "capo_license_manager.types.string.String"
    """<p>Product name.</p>"""
    product_sku: "capo_license_manager.types.string.String"
    """<p>Product SKU.</p>"""
    issuer: "capo_license_manager.types.issuer.Issuer"
    """<p>License issuer.</p>"""
    home_region: "capo_license_manager.types.string.String"
    """<p>Home Region for the license.</p>"""
    validity: "capo_license_manager.types.datetime_range.DatetimeRange"
    """<p>Date and time range during which the license is valid, in ISO8601-UTC format.</p>"""
    entitlements: "capo_license_manager.types.entitlement_list.EntitlementList"
    """<p>License entitlements.</p>"""
    beneficiary: "capo_license_manager.types.string.String"
    """<p>License beneficiary.</p>"""
    consumption_configuration: (
        "capo_license_manager.types.consumption_configuration.ConsumptionConfiguration"
    )
    """<p>Configuration for consumption of the license. Choose a provisional configuration for workloads running with continuous connectivity. Choose a borrow configuration for workloads with offline usage.</p>"""
    license_metadata: NotRequired[
        "capo_license_manager.types.metadata_list.MetadataList"
    ]
    """<p>Information about the license.</p>"""
    client_token: "capo_license_manager.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["capo_license_manager.types.tag_list.TagList"]
    """<p>Tags to add to the license. For more information about tagging support in License Manager, see the <a href="https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html">TagResource</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseRequest) -> dict:
    out: dict = {}
    out["LicenseName"] = value["license_name"]
    out["ProductName"] = value["product_name"]
    out["ProductSKU"] = value["product_sku"]
    import capo_license_manager.types.issuer

    out["Issuer"] = capo_license_manager.types.issuer.serialize_aws_json_1_1(
        value["issuer"]
    )
    out["HomeRegion"] = value["home_region"]
    import capo_license_manager.types.datetime_range

    out["Validity"] = capo_license_manager.types.datetime_range.serialize_aws_json_1_1(
        value["validity"]
    )
    import capo_license_manager.types.entitlement_list

    out["Entitlements"] = (
        capo_license_manager.types.entitlement_list.serialize_aws_json_1_1(
            value["entitlements"]
        )
    )
    out["Beneficiary"] = value["beneficiary"]
    import capo_license_manager.types.consumption_configuration

    out["ConsumptionConfiguration"] = (
        capo_license_manager.types.consumption_configuration.serialize_aws_json_1_1(
            value["consumption_configuration"]
        )
    )
    if "license_metadata" in value:
        import capo_license_manager.types.metadata_list

        out["LicenseMetadata"] = (
            capo_license_manager.types.metadata_list.serialize_aws_json_1_1(
                value["license_metadata"]
            )
        )
    out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_license_manager.types.tag_list

        out["Tags"] = capo_license_manager.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseRequest:
    out: CreateLicenseRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseName") is not None:
        out["license_name"] = data["LicenseName"]
    else:
        out["license_name"] = ""
    if data.get("ProductName") is not None:
        out["product_name"] = data["ProductName"]
    else:
        out["product_name"] = ""
    if data.get("ProductSKU") is not None:
        out["product_sku"] = data["ProductSKU"]
    else:
        out["product_sku"] = ""
    if data.get("Issuer") is not None:
        import capo_license_manager.types.issuer

        out["issuer"] = capo_license_manager.types.issuer.deserialize_aws_json_1_1(
            data["Issuer"]
        )
    else:
        raise DeserializationError("CreateLicenseRequest.issuer required")
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
        raise DeserializationError("CreateLicenseRequest.validity required")
    if data.get("Entitlements") is not None:
        import capo_license_manager.types.entitlement_list

        out["entitlements"] = (
            capo_license_manager.types.entitlement_list.deserialize_aws_json_1_1(
                data["Entitlements"]
            )
        )
    else:
        out["entitlements"] = []
    if data.get("Beneficiary") is not None:
        out["beneficiary"] = data["Beneficiary"]
    else:
        out["beneficiary"] = ""
    if data.get("ConsumptionConfiguration") is not None:
        import capo_license_manager.types.consumption_configuration

        out["consumption_configuration"] = (
            capo_license_manager.types.consumption_configuration.deserialize_aws_json_1_1(
                data["ConsumptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLicenseRequest.consumption_configuration required"
        )
    if data.get("LicenseMetadata") is not None:
        import capo_license_manager.types.metadata_list

        out["license_metadata"] = (
            capo_license_manager.types.metadata_list.deserialize_aws_json_1_1(
                data["LicenseMetadata"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("Tags") is not None:
        import capo_license_manager.types.tag_list

        out["tags"] = capo_license_manager.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
