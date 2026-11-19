"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeProxyResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.create_time
    import capo_network_firewall.types.delete_time
    import capo_network_firewall.types.failure_code
    import capo_network_firewall.types.failure_message
    import capo_network_firewall.types.listener_properties
    import capo_network_firewall.types.nat_gateway_id
    import capo_network_firewall.types.private_dns_name
    import capo_network_firewall.types.proxy_modify_state
    import capo_network_firewall.types.proxy_state
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.tag_list
    import capo_network_firewall.types.tls_intercept_properties
    import capo_network_firewall.types.update_time
    import capo_network_firewall.types.vpc_endpoint_service_name


class DescribeProxyResource(TypedDict, closed=True):
    proxy_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the proxy. You can't change the name of a proxy after you create it.</p>"""
    proxy_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of a proxy.</p>"""
    proxy_configuration_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p>"""
    proxy_configuration_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy configuration.</p>"""
    nat_gateway_id: NotRequired[
        "capo_network_firewall.types.nat_gateway_id.NatGatewayId"
    ]
    """<p>The NAT Gateway for the proxy. </p>"""
    proxy_state: NotRequired["capo_network_firewall.types.proxy_state.ProxyState"]
    """<p>Current attachment/detachment status of the Proxy. </p>"""
    proxy_modify_state: NotRequired[
        "capo_network_firewall.types.proxy_modify_state.ProxyModifyState"
    ]
    """<p>Current modification status of the Proxy. </p>"""
    listener_properties: NotRequired[
        "capo_network_firewall.types.listener_properties.ListenerProperties"
    ]
    """<p>Listener properties for HTTP and HTTPS traffic. </p>"""
    tls_intercept_properties: NotRequired[
        "capo_network_firewall.types.tls_intercept_properties.TlsInterceptProperties"
    ]
    """<p>TLS decryption on traffic to filter on attributes in the HTTP header. </p>"""
    vpc_endpoint_service_name: NotRequired[
        "capo_network_firewall.types.vpc_endpoint_service_name.VpcEndpointServiceName"
    ]
    """<p>The service endpoint created in the VPC. </p>"""
    private_dns_name: NotRequired[
        "capo_network_firewall.types.private_dns_name.PrivateDNSName"
    ]
    """<p>The private DNS name of the Proxy. </p>"""
    create_time: NotRequired["capo_network_firewall.types.create_time.CreateTime"]
    """<p>Time the Proxy was created. </p>"""
    delete_time: NotRequired["capo_network_firewall.types.delete_time.DeleteTime"]
    """<p>Time the Proxy was deleted. </p>"""
    update_time: NotRequired["capo_network_firewall.types.update_time.UpdateTime"]
    """<p>Time the Proxy was updated. </p>"""
    failure_code: NotRequired["capo_network_firewall.types.failure_code.FailureCode"]
    """<p>Failure code for cases when the Proxy fails to attach or update. </p>"""
    failure_message: NotRequired[
        "capo_network_firewall.types.failure_message.FailureMessage"
    ]
    """<p>Failure message for cases when the Proxy fails to attach or update. </p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeProxyResource) -> dict:
    out: dict = {}
    if "proxy_name" in value:
        out["ProxyName"] = value["proxy_name"]
    if "proxy_arn" in value:
        out["ProxyArn"] = value["proxy_arn"]
    if "proxy_configuration_name" in value:
        out["ProxyConfigurationName"] = value["proxy_configuration_name"]
    if "proxy_configuration_arn" in value:
        out["ProxyConfigurationArn"] = value["proxy_configuration_arn"]
    if "nat_gateway_id" in value:
        out["NatGatewayId"] = value["nat_gateway_id"]
    if "proxy_state" in value:
        import capo_network_firewall.types.proxy_state

        out["ProxyState"] = (
            capo_network_firewall.types.proxy_state.serialize_aws_json_1_0(
                value["proxy_state"]
            )
        )
    if "proxy_modify_state" in value:
        import capo_network_firewall.types.proxy_modify_state

        out["ProxyModifyState"] = (
            capo_network_firewall.types.proxy_modify_state.serialize_aws_json_1_0(
                value["proxy_modify_state"]
            )
        )
    if "listener_properties" in value:
        import capo_network_firewall.types.listener_properties

        out["ListenerProperties"] = (
            capo_network_firewall.types.listener_properties.serialize_aws_json_1_0(
                value["listener_properties"]
            )
        )
    if "tls_intercept_properties" in value:
        import capo_network_firewall.types.tls_intercept_properties

        out["TlsInterceptProperties"] = (
            capo_network_firewall.types.tls_intercept_properties.serialize_aws_json_1_0(
                value["tls_intercept_properties"]
            )
        )
    if "vpc_endpoint_service_name" in value:
        out["VpcEndpointServiceName"] = value["vpc_endpoint_service_name"]
    if "private_dns_name" in value:
        out["PrivateDNSName"] = value["private_dns_name"]
    if "create_time" in value:
        import capo_network_firewall.types.create_time

        out["CreateTime"] = (
            capo_network_firewall.types.create_time.serialize_aws_json_1_0(
                value["create_time"]
            )
        )
    if "delete_time" in value:
        import capo_network_firewall.types.delete_time

        out["DeleteTime"] = (
            capo_network_firewall.types.delete_time.serialize_aws_json_1_0(
                value["delete_time"]
            )
        )
    if "update_time" in value:
        import capo_network_firewall.types.update_time

        out["UpdateTime"] = (
            capo_network_firewall.types.update_time.serialize_aws_json_1_0(
                value["update_time"]
            )
        )
    if "failure_code" in value:
        out["FailureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeProxyResource:
    out: DescribeProxyResource = {}  # type: ignore[typeddict-item]
    if data.get("ProxyName") is not None:
        out["proxy_name"] = data["ProxyName"]
    if data.get("ProxyArn") is not None:
        out["proxy_arn"] = data["ProxyArn"]
    if data.get("ProxyConfigurationName") is not None:
        out["proxy_configuration_name"] = data["ProxyConfigurationName"]
    if data.get("ProxyConfigurationArn") is not None:
        out["proxy_configuration_arn"] = data["ProxyConfigurationArn"]
    if data.get("NatGatewayId") is not None:
        out["nat_gateway_id"] = data["NatGatewayId"]
    if data.get("ProxyState") is not None:
        import capo_network_firewall.types.proxy_state

        out["proxy_state"] = (
            capo_network_firewall.types.proxy_state.deserialize_aws_json_1_0(
                data["ProxyState"]
            )
        )
    if data.get("ProxyModifyState") is not None:
        import capo_network_firewall.types.proxy_modify_state

        out["proxy_modify_state"] = (
            capo_network_firewall.types.proxy_modify_state.deserialize_aws_json_1_0(
                data["ProxyModifyState"]
            )
        )
    if data.get("ListenerProperties") is not None:
        import capo_network_firewall.types.listener_properties

        out["listener_properties"] = (
            capo_network_firewall.types.listener_properties.deserialize_aws_json_1_0(
                data["ListenerProperties"]
            )
        )
    if data.get("TlsInterceptProperties") is not None:
        import capo_network_firewall.types.tls_intercept_properties

        out["tls_intercept_properties"] = (
            capo_network_firewall.types.tls_intercept_properties.deserialize_aws_json_1_0(
                data["TlsInterceptProperties"]
            )
        )
    if data.get("VpcEndpointServiceName") is not None:
        out["vpc_endpoint_service_name"] = data["VpcEndpointServiceName"]
    if data.get("PrivateDNSName") is not None:
        out["private_dns_name"] = data["PrivateDNSName"]
    if data.get("CreateTime") is not None:
        import capo_network_firewall.types.create_time

        out["create_time"] = (
            capo_network_firewall.types.create_time.deserialize_aws_json_1_0(
                data["CreateTime"]
            )
        )
    if data.get("DeleteTime") is not None:
        import capo_network_firewall.types.delete_time

        out["delete_time"] = (
            capo_network_firewall.types.delete_time.deserialize_aws_json_1_0(
                data["DeleteTime"]
            )
        )
    if data.get("UpdateTime") is not None:
        import capo_network_firewall.types.update_time

        out["update_time"] = (
            capo_network_firewall.types.update_time.deserialize_aws_json_1_0(
                data["UpdateTime"]
            )
        )
    if data.get("FailureCode") is not None:
        out["failure_code"] = data["FailureCode"]
    if data.get("FailureMessage") is not None:
        out["failure_message"] = data["FailureMessage"]
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProxyResource) -> dict:
    out: dict = {}
    if "proxy_name" in value:
        out["ProxyName"] = value["proxy_name"]
    if "proxy_arn" in value:
        out["ProxyArn"] = value["proxy_arn"]
    if "proxy_configuration_name" in value:
        out["ProxyConfigurationName"] = value["proxy_configuration_name"]
    if "proxy_configuration_arn" in value:
        out["ProxyConfigurationArn"] = value["proxy_configuration_arn"]
    if "nat_gateway_id" in value:
        out["NatGatewayId"] = value["nat_gateway_id"]
    if "proxy_state" in value:
        import capo_network_firewall.types.proxy_state

        out["ProxyState"] = capo_network_firewall.types.proxy_state.serialize_cbor(
            value["proxy_state"]
        )
    if "proxy_modify_state" in value:
        import capo_network_firewall.types.proxy_modify_state

        out["ProxyModifyState"] = (
            capo_network_firewall.types.proxy_modify_state.serialize_cbor(
                value["proxy_modify_state"]
            )
        )
    if "listener_properties" in value:
        import capo_network_firewall.types.listener_properties

        out["ListenerProperties"] = (
            capo_network_firewall.types.listener_properties.serialize_cbor(
                value["listener_properties"]
            )
        )
    if "tls_intercept_properties" in value:
        import capo_network_firewall.types.tls_intercept_properties

        out["TlsInterceptProperties"] = (
            capo_network_firewall.types.tls_intercept_properties.serialize_cbor(
                value["tls_intercept_properties"]
            )
        )
    if "vpc_endpoint_service_name" in value:
        out["VpcEndpointServiceName"] = value["vpc_endpoint_service_name"]
    if "private_dns_name" in value:
        out["PrivateDNSName"] = value["private_dns_name"]
    if "create_time" in value:
        import capo_network_firewall.types.create_time

        out["CreateTime"] = capo_network_firewall.types.create_time.serialize_cbor(
            value["create_time"]
        )
    if "delete_time" in value:
        import capo_network_firewall.types.delete_time

        out["DeleteTime"] = capo_network_firewall.types.delete_time.serialize_cbor(
            value["delete_time"]
        )
    if "update_time" in value:
        import capo_network_firewall.types.update_time

        out["UpdateTime"] = capo_network_firewall.types.update_time.serialize_cbor(
            value["update_time"]
        )
    if "failure_code" in value:
        out["FailureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> DescribeProxyResource:
    out: DescribeProxyResource = {}  # type: ignore[typeddict-item]
    if data.get("ProxyName") is not None:
        out["proxy_name"] = data["ProxyName"]
    if data.get("ProxyArn") is not None:
        out["proxy_arn"] = data["ProxyArn"]
    if data.get("ProxyConfigurationName") is not None:
        out["proxy_configuration_name"] = data["ProxyConfigurationName"]
    if data.get("ProxyConfigurationArn") is not None:
        out["proxy_configuration_arn"] = data["ProxyConfigurationArn"]
    if data.get("NatGatewayId") is not None:
        out["nat_gateway_id"] = data["NatGatewayId"]
    if data.get("ProxyState") is not None:
        import capo_network_firewall.types.proxy_state

        out["proxy_state"] = capo_network_firewall.types.proxy_state.deserialize_cbor(
            data["ProxyState"]
        )
    if data.get("ProxyModifyState") is not None:
        import capo_network_firewall.types.proxy_modify_state

        out["proxy_modify_state"] = (
            capo_network_firewall.types.proxy_modify_state.deserialize_cbor(
                data["ProxyModifyState"]
            )
        )
    if data.get("ListenerProperties") is not None:
        import capo_network_firewall.types.listener_properties

        out["listener_properties"] = (
            capo_network_firewall.types.listener_properties.deserialize_cbor(
                data["ListenerProperties"]
            )
        )
    if data.get("TlsInterceptProperties") is not None:
        import capo_network_firewall.types.tls_intercept_properties

        out["tls_intercept_properties"] = (
            capo_network_firewall.types.tls_intercept_properties.deserialize_cbor(
                data["TlsInterceptProperties"]
            )
        )
    if data.get("VpcEndpointServiceName") is not None:
        out["vpc_endpoint_service_name"] = data["VpcEndpointServiceName"]
    if data.get("PrivateDNSName") is not None:
        out["private_dns_name"] = data["PrivateDNSName"]
    if data.get("CreateTime") is not None:
        import capo_network_firewall.types.create_time

        out["create_time"] = capo_network_firewall.types.create_time.deserialize_cbor(
            data["CreateTime"]
        )
    if data.get("DeleteTime") is not None:
        import capo_network_firewall.types.delete_time

        out["delete_time"] = capo_network_firewall.types.delete_time.deserialize_cbor(
            data["DeleteTime"]
        )
    if data.get("UpdateTime") is not None:
        import capo_network_firewall.types.update_time

        out["update_time"] = capo_network_firewall.types.update_time.deserialize_cbor(
            data["UpdateTime"]
        )
    if data.get("FailureCode") is not None:
        out["failure_code"] = data["FailureCode"]
    if data.get("FailureMessage") is not None:
        out["failure_message"] = data["FailureMessage"]
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_cbor(
            data["Tags"]
        )
    return out
