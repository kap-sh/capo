"""Generated from Smithy shape ``com.amazonaws.shield#Protection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.application_layer_automatic_response_configuration
    import capo_shield.types.health_check_ids
    import capo_shield.types.protection_id
    import capo_shield.types.protection_name
    import capo_shield.types.resource_arn


class Protection(TypedDict, closed=True):
    id: NotRequired["capo_shield.types.protection_id.ProtectionId"]
    """<p>The unique identifier (ID) of the protection.</p>"""
    name: NotRequired["capo_shield.types.protection_name.ProtectionName"]
    """<p>The name of the protection. For example, <code>My CloudFront distributions</code>.</p>"""
    resource_arn: NotRequired["capo_shield.types.resource_arn.ResourceArn"]
    """<p>The ARN (Amazon Resource Name) of the Amazon Web Services resource that is protected.</p>"""
    health_check_ids: NotRequired["capo_shield.types.health_check_ids.HealthCheckIds"]
    """<p>The unique identifier (ID) for the Route 53 health check that's associated with the protection. </p>"""
    protection_arn: NotRequired["capo_shield.types.resource_arn.ResourceArn"]
    """<p>The ARN (Amazon Resource Name) of the protection.</p>"""
    application_layer_automatic_response_configuration: NotRequired[
        "capo_shield.types.application_layer_automatic_response_configuration.ApplicationLayerAutomaticResponseConfiguration"
    ]
    """<p>The automatic application layer DDoS mitigation settings for the protection. This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Protection) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "health_check_ids" in value:
        import capo_shield.types.health_check_ids

        out["HealthCheckIds"] = (
            capo_shield.types.health_check_ids.serialize_aws_json_1_1(
                value["health_check_ids"]
            )
        )
    if "protection_arn" in value:
        out["ProtectionArn"] = value["protection_arn"]
    if "application_layer_automatic_response_configuration" in value:
        import capo_shield.types.application_layer_automatic_response_configuration

        out["ApplicationLayerAutomaticResponseConfiguration"] = (
            capo_shield.types.application_layer_automatic_response_configuration.serialize_aws_json_1_1(
                value["application_layer_automatic_response_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Protection:
    out: Protection = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("HealthCheckIds") is not None:
        import capo_shield.types.health_check_ids

        out["health_check_ids"] = (
            capo_shield.types.health_check_ids.deserialize_aws_json_1_1(
                data["HealthCheckIds"]
            )
        )
    if data.get("ProtectionArn") is not None:
        out["protection_arn"] = data["ProtectionArn"]
    if data.get("ApplicationLayerAutomaticResponseConfiguration") is not None:
        import capo_shield.types.application_layer_automatic_response_configuration

        out["application_layer_automatic_response_configuration"] = (
            capo_shield.types.application_layer_automatic_response_configuration.deserialize_aws_json_1_1(
                data["ApplicationLayerAutomaticResponseConfiguration"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Protection) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "health_check_ids" in value:
        import capo_shield.types.health_check_ids

        out["HealthCheckIds"] = capo_shield.types.health_check_ids.serialize_cbor(
            value["health_check_ids"]
        )
    if "protection_arn" in value:
        out["ProtectionArn"] = value["protection_arn"]
    if "application_layer_automatic_response_configuration" in value:
        import capo_shield.types.application_layer_automatic_response_configuration

        out["ApplicationLayerAutomaticResponseConfiguration"] = (
            capo_shield.types.application_layer_automatic_response_configuration.serialize_cbor(
                value["application_layer_automatic_response_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Protection:
    out: Protection = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("HealthCheckIds") is not None:
        import capo_shield.types.health_check_ids

        out["health_check_ids"] = capo_shield.types.health_check_ids.deserialize_cbor(
            data["HealthCheckIds"]
        )
    if data.get("ProtectionArn") is not None:
        out["protection_arn"] = data["ProtectionArn"]
    if data.get("ApplicationLayerAutomaticResponseConfiguration") is not None:
        import capo_shield.types.application_layer_automatic_response_configuration

        out["application_layer_automatic_response_configuration"] = (
            capo_shield.types.application_layer_automatic_response_configuration.deserialize_cbor(
                data["ApplicationLayerAutomaticResponseConfiguration"]
            )
        )
    return out
