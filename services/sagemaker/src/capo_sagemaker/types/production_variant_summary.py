"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.deployed_images
    import capo_sagemaker.types.instance_pool_summary_list
    import capo_sagemaker.types.production_variant_capacity_reservation_summary
    import capo_sagemaker.types.production_variant_managed_instance_scaling
    import capo_sagemaker.types.production_variant_routing_config
    import capo_sagemaker.types.production_variant_serverless_config
    import capo_sagemaker.types.production_variant_status_list
    import capo_sagemaker.types.task_count
    import capo_sagemaker.types.variant_name
    import capo_sagemaker.types.variant_weight


class ProductionVariantSummary(TypedDict, closed=True):
    variant_name: NotRequired["capo_sagemaker.types.variant_name.VariantName"]
    """<p>The name of the variant.</p>"""
    deployed_images: NotRequired["capo_sagemaker.types.deployed_images.DeployedImages"]
    """<p>An array of <code>DeployedImage</code> objects that specify the Amazon EC2 Container Registry paths of the inference images deployed on instances of this <code>ProductionVariant</code>.</p>"""
    current_weight: NotRequired["capo_sagemaker.types.variant_weight.VariantWeight"]
    """<p>The weight associated with the variant.</p>"""
    desired_weight: NotRequired["capo_sagemaker.types.variant_weight.VariantWeight"]
    """<p>The requested weight, as specified in the <code>UpdateEndpointWeightsAndCapacities</code> request. </p>"""
    current_instance_count: NotRequired["capo_sagemaker.types.task_count.TaskCount"]
    """<p>The number of instances associated with the variant.</p>"""
    desired_instance_count: NotRequired["capo_sagemaker.types.task_count.TaskCount"]
    """<p>The number of instances requested in the <code>UpdateEndpointWeightsAndCapacities</code> request. </p>"""
    instance_pools: NotRequired[
        "capo_sagemaker.types.instance_pool_summary_list.InstancePoolSummaryList"
    ]
    """<p>A list of instance pools for the production variant. Each pool indicates the instance type and the current number of instances of that type.</p>"""
    variant_status: NotRequired[
        "capo_sagemaker.types.production_variant_status_list.ProductionVariantStatusList"
    ]
    """<p>The endpoint variant status which describes the current deployment stage status or operational status.</p>"""
    current_serverless_config: NotRequired[
        "capo_sagemaker.types.production_variant_serverless_config.ProductionVariantServerlessConfig"
    ]
    """<p>The serverless configuration for the endpoint.</p>"""
    desired_serverless_config: NotRequired[
        "capo_sagemaker.types.production_variant_serverless_config.ProductionVariantServerlessConfig"
    ]
    """<p>The serverless configuration requested for the endpoint update.</p>"""
    managed_instance_scaling: NotRequired[
        "capo_sagemaker.types.production_variant_managed_instance_scaling.ProductionVariantManagedInstanceScaling"
    ]
    """<p>Settings that control the range in the number of instances that the endpoint provisions as it scales up or down to accommodate traffic. </p>"""
    routing_config: NotRequired[
        "capo_sagemaker.types.production_variant_routing_config.ProductionVariantRoutingConfig"
    ]
    """<p>Settings that control how the endpoint routes incoming traffic to the instances that the endpoint hosts.</p>"""
    capacity_reservation_config: NotRequired[
        "capo_sagemaker.types.production_variant_capacity_reservation_summary.ProductionVariantCapacityReservationSummary"
    ]
    """<p>Settings for the capacity reservation for the compute instances that SageMaker AI reserves for an endpoint. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariantSummary) -> dict:
    out: dict = {}
    if "variant_name" in value:
        out["VariantName"] = value["variant_name"]
    if "deployed_images" in value:
        import capo_sagemaker.types.deployed_images

        out["DeployedImages"] = (
            capo_sagemaker.types.deployed_images.serialize_aws_json_1_1(
                value["deployed_images"]
            )
        )
    if "current_weight" in value:
        out["CurrentWeight"] = (
            "NaN"
            if value["current_weight"] != value["current_weight"]
            else "Infinity"
            if value["current_weight"] == float("inf")
            else "-Infinity"
            if value["current_weight"] == float("-inf")
            else value["current_weight"]
        )
    if "desired_weight" in value:
        out["DesiredWeight"] = (
            "NaN"
            if value["desired_weight"] != value["desired_weight"]
            else "Infinity"
            if value["desired_weight"] == float("inf")
            else "-Infinity"
            if value["desired_weight"] == float("-inf")
            else value["desired_weight"]
        )
    if "current_instance_count" in value:
        out["CurrentInstanceCount"] = value["current_instance_count"]
    if "desired_instance_count" in value:
        out["DesiredInstanceCount"] = value["desired_instance_count"]
    if "instance_pools" in value:
        import capo_sagemaker.types.instance_pool_summary_list

        out["InstancePools"] = (
            capo_sagemaker.types.instance_pool_summary_list.serialize_aws_json_1_1(
                value["instance_pools"]
            )
        )
    if "variant_status" in value:
        import capo_sagemaker.types.production_variant_status_list

        out["VariantStatus"] = (
            capo_sagemaker.types.production_variant_status_list.serialize_aws_json_1_1(
                value["variant_status"]
            )
        )
    if "current_serverless_config" in value:
        import capo_sagemaker.types.production_variant_serverless_config

        out["CurrentServerlessConfig"] = (
            capo_sagemaker.types.production_variant_serverless_config.serialize_aws_json_1_1(
                value["current_serverless_config"]
            )
        )
    if "desired_serverless_config" in value:
        import capo_sagemaker.types.production_variant_serverless_config

        out["DesiredServerlessConfig"] = (
            capo_sagemaker.types.production_variant_serverless_config.serialize_aws_json_1_1(
                value["desired_serverless_config"]
            )
        )
    if "managed_instance_scaling" in value:
        import capo_sagemaker.types.production_variant_managed_instance_scaling

        out["ManagedInstanceScaling"] = (
            capo_sagemaker.types.production_variant_managed_instance_scaling.serialize_aws_json_1_1(
                value["managed_instance_scaling"]
            )
        )
    if "routing_config" in value:
        import capo_sagemaker.types.production_variant_routing_config

        out["RoutingConfig"] = (
            capo_sagemaker.types.production_variant_routing_config.serialize_aws_json_1_1(
                value["routing_config"]
            )
        )
    if "capacity_reservation_config" in value:
        import capo_sagemaker.types.production_variant_capacity_reservation_summary

        out["CapacityReservationConfig"] = (
            capo_sagemaker.types.production_variant_capacity_reservation_summary.serialize_aws_json_1_1(
                value["capacity_reservation_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductionVariantSummary:
    out: ProductionVariantSummary = {}  # type: ignore[typeddict-item]
    if data.get("VariantName") is not None:
        out["variant_name"] = data["VariantName"]
    if data.get("DeployedImages") is not None:
        import capo_sagemaker.types.deployed_images

        out["deployed_images"] = (
            capo_sagemaker.types.deployed_images.deserialize_aws_json_1_1(
                data["DeployedImages"]
            )
        )
    if data.get("CurrentWeight") is not None:
        out["current_weight"] = float(data["CurrentWeight"])
    if data.get("DesiredWeight") is not None:
        out["desired_weight"] = float(data["DesiredWeight"])
    if data.get("CurrentInstanceCount") is not None:
        out["current_instance_count"] = data["CurrentInstanceCount"]
    if data.get("DesiredInstanceCount") is not None:
        out["desired_instance_count"] = data["DesiredInstanceCount"]
    if data.get("InstancePools") is not None:
        import capo_sagemaker.types.instance_pool_summary_list

        out["instance_pools"] = (
            capo_sagemaker.types.instance_pool_summary_list.deserialize_aws_json_1_1(
                data["InstancePools"]
            )
        )
    if data.get("VariantStatus") is not None:
        import capo_sagemaker.types.production_variant_status_list

        out["variant_status"] = (
            capo_sagemaker.types.production_variant_status_list.deserialize_aws_json_1_1(
                data["VariantStatus"]
            )
        )
    if data.get("CurrentServerlessConfig") is not None:
        import capo_sagemaker.types.production_variant_serverless_config

        out["current_serverless_config"] = (
            capo_sagemaker.types.production_variant_serverless_config.deserialize_aws_json_1_1(
                data["CurrentServerlessConfig"]
            )
        )
    if data.get("DesiredServerlessConfig") is not None:
        import capo_sagemaker.types.production_variant_serverless_config

        out["desired_serverless_config"] = (
            capo_sagemaker.types.production_variant_serverless_config.deserialize_aws_json_1_1(
                data["DesiredServerlessConfig"]
            )
        )
    if data.get("ManagedInstanceScaling") is not None:
        import capo_sagemaker.types.production_variant_managed_instance_scaling

        out["managed_instance_scaling"] = (
            capo_sagemaker.types.production_variant_managed_instance_scaling.deserialize_aws_json_1_1(
                data["ManagedInstanceScaling"]
            )
        )
    if data.get("RoutingConfig") is not None:
        import capo_sagemaker.types.production_variant_routing_config

        out["routing_config"] = (
            capo_sagemaker.types.production_variant_routing_config.deserialize_aws_json_1_1(
                data["RoutingConfig"]
            )
        )
    if data.get("CapacityReservationConfig") is not None:
        import capo_sagemaker.types.production_variant_capacity_reservation_summary

        out["capacity_reservation_config"] = (
            capo_sagemaker.types.production_variant_capacity_reservation_summary.deserialize_aws_json_1_1(
                data["CapacityReservationConfig"]
            )
        )
    return out
