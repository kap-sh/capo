"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiGatewayV2StageDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_api_gateway_access_log_settings
    import capo_securityhub.types.aws_api_gateway_v2_route_settings
    import capo_securityhub.types.boolean
    import capo_securityhub.types.field_map
    import capo_securityhub.types.non_empty_string


class AwsApiGatewayV2StageDetails(TypedDict, closed=True):
    client_certificate_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of a client certificate for a stage. Supported only for WebSocket API calls.</p>"""
    created_date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the stage was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The description of the stage.</p>"""
    default_route_settings: NotRequired[
        "capo_securityhub.types.aws_api_gateway_v2_route_settings.AwsApiGatewayV2RouteSettings"
    ]
    """<p>Default route settings for the stage.</p>"""
    deployment_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the deployment that the stage is associated with. </p>"""
    last_updated_date: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates when the stage was most recently updated.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    route_settings: NotRequired[
        "capo_securityhub.types.aws_api_gateway_v2_route_settings.AwsApiGatewayV2RouteSettings"
    ]
    """<p>The route settings for the stage.</p>"""
    stage_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the stage.</p>"""
    stage_variables: NotRequired["capo_securityhub.types.field_map.FieldMap"]
    """<p>A map that defines the stage variables for the stage.</p> <p>Variable names can have alphanumeric and underscore characters.</p> <p>Variable values can contain the following characters:</p> <ul> <li> <p>Uppercase and lowercase letters</p> </li> <li> <p>Numbers</p> </li> <li> <p>Special characters -._~:/?#&=,</p> </li> </ul>"""
    access_log_settings: NotRequired[
        "capo_securityhub.types.aws_api_gateway_access_log_settings.AwsApiGatewayAccessLogSettings"
    ]
    """<p>Information about settings for logging access for the stage.</p>"""
    auto_deploy: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether updates to an API automatically trigger a new deployment.</p>"""
    last_deployment_status_message: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of the last deployment of a stage. Supported only if the stage has automatic deployment enabled.</p>"""
    api_gateway_managed: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the stage is managed by API Gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiGatewayV2StageDetails) -> dict:
    out: dict = {}
    if "client_certificate_id" in value:
        out["ClientCertificateId"] = value["client_certificate_id"]
    if "created_date" in value:
        out["CreatedDate"] = value["created_date"]
    if "description" in value:
        out["Description"] = value["description"]
    if "default_route_settings" in value:
        import capo_securityhub.types.aws_api_gateway_v2_route_settings

        out["DefaultRouteSettings"] = (
            capo_securityhub.types.aws_api_gateway_v2_route_settings.serialize_json(
                value["default_route_settings"]
            )
        )
    if "deployment_id" in value:
        out["DeploymentId"] = value["deployment_id"]
    if "last_updated_date" in value:
        out["LastUpdatedDate"] = value["last_updated_date"]
    if "route_settings" in value:
        import capo_securityhub.types.aws_api_gateway_v2_route_settings

        out["RouteSettings"] = (
            capo_securityhub.types.aws_api_gateway_v2_route_settings.serialize_json(
                value["route_settings"]
            )
        )
    if "stage_name" in value:
        out["StageName"] = value["stage_name"]
    if "stage_variables" in value:
        import capo_securityhub.types.field_map

        out["StageVariables"] = capo_securityhub.types.field_map.serialize_json(
            value["stage_variables"]
        )
    if "access_log_settings" in value:
        import capo_securityhub.types.aws_api_gateway_access_log_settings

        out["AccessLogSettings"] = (
            capo_securityhub.types.aws_api_gateway_access_log_settings.serialize_json(
                value["access_log_settings"]
            )
        )
    if "auto_deploy" in value:
        out["AutoDeploy"] = value["auto_deploy"]
    if "last_deployment_status_message" in value:
        out["LastDeploymentStatusMessage"] = value["last_deployment_status_message"]
    if "api_gateway_managed" in value:
        out["ApiGatewayManaged"] = value["api_gateway_managed"]
    return out


def deserialize_json(data: dict) -> AwsApiGatewayV2StageDetails:
    out: AwsApiGatewayV2StageDetails = {}  # type: ignore[typeddict-item]
    if data.get("ClientCertificateId") is not None:
        out["client_certificate_id"] = data["ClientCertificateId"]
    if data.get("CreatedDate") is not None:
        out["created_date"] = data["CreatedDate"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DefaultRouteSettings") is not None:
        import capo_securityhub.types.aws_api_gateway_v2_route_settings

        out["default_route_settings"] = (
            capo_securityhub.types.aws_api_gateway_v2_route_settings.deserialize_json(
                data["DefaultRouteSettings"]
            )
        )
    if data.get("DeploymentId") is not None:
        out["deployment_id"] = data["DeploymentId"]
    if data.get("LastUpdatedDate") is not None:
        out["last_updated_date"] = data["LastUpdatedDate"]
    if data.get("RouteSettings") is not None:
        import capo_securityhub.types.aws_api_gateway_v2_route_settings

        out["route_settings"] = (
            capo_securityhub.types.aws_api_gateway_v2_route_settings.deserialize_json(
                data["RouteSettings"]
            )
        )
    if data.get("StageName") is not None:
        out["stage_name"] = data["StageName"]
    if data.get("StageVariables") is not None:
        import capo_securityhub.types.field_map

        out["stage_variables"] = capo_securityhub.types.field_map.deserialize_json(
            data["StageVariables"]
        )
    if data.get("AccessLogSettings") is not None:
        import capo_securityhub.types.aws_api_gateway_access_log_settings

        out["access_log_settings"] = (
            capo_securityhub.types.aws_api_gateway_access_log_settings.deserialize_json(
                data["AccessLogSettings"]
            )
        )
    if data.get("AutoDeploy") is not None:
        out["auto_deploy"] = data["AutoDeploy"]
    if data.get("LastDeploymentStatusMessage") is not None:
        out["last_deployment_status_message"] = data["LastDeploymentStatusMessage"]
    if data.get("ApiGatewayManaged") is not None:
        out["api_gateway_managed"] = data["ApiGatewayManaged"]
    return out
