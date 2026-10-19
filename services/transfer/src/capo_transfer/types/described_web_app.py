"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedWebApp``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.described_web_app_endpoint_details
    import capo_transfer.types.described_web_app_identity_provider_details
    import capo_transfer.types.tags
    import capo_transfer.types.web_app_access_endpoint
    import capo_transfer.types.web_app_endpoint
    import capo_transfer.types.web_app_endpoint_policy
    import capo_transfer.types.web_app_endpoint_type
    import capo_transfer.types.web_app_id
    import capo_transfer.types.web_app_units


class DescribedWebApp(TypedDict, closed=True):
    arn: "capo_transfer.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the web app.</p>"""
    web_app_id: "capo_transfer.types.web_app_id.WebAppId"
    """<p>The unique identifier for the web app.</p>"""
    described_identity_provider_details: NotRequired[
        "capo_transfer.types.described_web_app_identity_provider_details.DescribedWebAppIdentityProviderDetails"
    ]
    """<p>A structure that contains the details for the identity provider used by the web app.</p>"""
    access_endpoint: NotRequired[
        "capo_transfer.types.web_app_access_endpoint.WebAppAccessEndpoint"
    ]
    """<p>The <code>AccessEndpoint</code> is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.</p>"""
    web_app_endpoint: NotRequired["capo_transfer.types.web_app_endpoint.WebAppEndpoint"]
    """<p>The <code>WebAppEndpoint</code> is the unique URL for your Transfer Family web app. This is the value that you use when you configure <b>Origins</b> on CloudFront.</p>"""
    web_app_units: NotRequired["capo_transfer.types.web_app_units.WebAppUnits"]
    """<p>A union that contains the value for number of concurrent connections or the user sessions on your web app.</p>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for web apps. Tags are metadata attached to web apps for any purpose.</p>"""
    web_app_endpoint_policy: NotRequired[
        "capo_transfer.types.web_app_endpoint_policy.WebAppEndpointPolicy"
    ]
    """<p> Setting for the type of endpoint policy for the web app. The default value is <code>STANDARD</code>. </p> <p>If your web app was created in an Amazon Web Services GovCloud (US) Region, the value of this parameter can be <code>FIPS</code>, which indicates the web app endpoint is FIPS-compliant.</p>"""
    endpoint_type: NotRequired[
        "capo_transfer.types.web_app_endpoint_type.WebAppEndpointType"
    ]
    """<p>The type of endpoint hosting the web app. Valid values are <code>PUBLIC</code> for publicly accessible endpoints and <code>VPC</code> for VPC-hosted endpoints that provide network isolation.</p>"""
    described_endpoint_details: NotRequired[
        "capo_transfer.types.described_web_app_endpoint_details.DescribedWebAppEndpointDetails"
    ]
    """<p>The endpoint configuration details for the web app, including VPC settings if the endpoint is hosted within a VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedWebApp) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["WebAppId"] = value["web_app_id"]
    if "described_identity_provider_details" in value:
        import capo_transfer.types.described_web_app_identity_provider_details

        out["DescribedIdentityProviderDetails"] = (
            capo_transfer.types.described_web_app_identity_provider_details.serialize_aws_json_1_1(
                value["described_identity_provider_details"]
            )
        )
    if "access_endpoint" in value:
        out["AccessEndpoint"] = value["access_endpoint"]
    if "web_app_endpoint" in value:
        out["WebAppEndpoint"] = value["web_app_endpoint"]
    if "web_app_units" in value:
        import capo_transfer.types.web_app_units

        out["WebAppUnits"] = capo_transfer.types.web_app_units.serialize_aws_json_1_1(
            value["web_app_units"]
        )
    if "tags" in value:
        import capo_transfer.types.tags

        out["Tags"] = capo_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    if "web_app_endpoint_policy" in value:
        import capo_transfer.types.web_app_endpoint_policy

        out["WebAppEndpointPolicy"] = (
            capo_transfer.types.web_app_endpoint_policy.serialize_aws_json_1_1(
                value["web_app_endpoint_policy"]
            )
        )
    if "endpoint_type" in value:
        import capo_transfer.types.web_app_endpoint_type

        out["EndpointType"] = (
            capo_transfer.types.web_app_endpoint_type.serialize_aws_json_1_1(
                value["endpoint_type"]
            )
        )
    if "described_endpoint_details" in value:
        import capo_transfer.types.described_web_app_endpoint_details

        out["DescribedEndpointDetails"] = (
            capo_transfer.types.described_web_app_endpoint_details.serialize_aws_json_1_1(
                value["described_endpoint_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedWebApp:
    out: DescribedWebApp = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("WebAppId") is not None:
        out["web_app_id"] = data["WebAppId"]
    else:
        out["web_app_id"] = ""
    if data.get("DescribedIdentityProviderDetails") is not None:
        import capo_transfer.types.described_web_app_identity_provider_details

        out["described_identity_provider_details"] = (
            capo_transfer.types.described_web_app_identity_provider_details.deserialize_aws_json_1_1(
                data["DescribedIdentityProviderDetails"]
            )
        )
    if data.get("AccessEndpoint") is not None:
        out["access_endpoint"] = data["AccessEndpoint"]
    if data.get("WebAppEndpoint") is not None:
        out["web_app_endpoint"] = data["WebAppEndpoint"]
    if data.get("WebAppUnits") is not None:
        import capo_transfer.types.web_app_units

        out["web_app_units"] = (
            capo_transfer.types.web_app_units.deserialize_aws_json_1_1(
                data["WebAppUnits"]
            )
        )
    if data.get("Tags") is not None:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("WebAppEndpointPolicy") is not None:
        import capo_transfer.types.web_app_endpoint_policy

        out["web_app_endpoint_policy"] = (
            capo_transfer.types.web_app_endpoint_policy.deserialize_aws_json_1_1(
                data["WebAppEndpointPolicy"]
            )
        )
    if data.get("EndpointType") is not None:
        import capo_transfer.types.web_app_endpoint_type

        out["endpoint_type"] = (
            capo_transfer.types.web_app_endpoint_type.deserialize_aws_json_1_1(
                data["EndpointType"]
            )
        )
    if data.get("DescribedEndpointDetails") is not None:
        import capo_transfer.types.described_web_app_endpoint_details

        out["described_endpoint_details"] = (
            capo_transfer.types.described_web_app_endpoint_details.deserialize_aws_json_1_1(
                data["DescribedEndpointDetails"]
            )
        )
    return out
