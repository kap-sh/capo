"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#PutRecommendationPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_compute_optimizer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer.types.enhanced_infrastructure_metrics
    import capo_compute_optimizer.types.external_metrics_preference
    import capo_compute_optimizer.types.inferred_workload_types_preference
    import capo_compute_optimizer.types.look_back_period_preference
    import capo_compute_optimizer.types.preferred_resources
    import capo_compute_optimizer.types.resource_type
    import capo_compute_optimizer.types.savings_estimation_mode
    import capo_compute_optimizer.types.scope
    import capo_compute_optimizer.types.utilization_preferences


class PutRecommendationPreferencesRequest(TypedDict, closed=True):
    resource_type: "capo_compute_optimizer.types.resource_type.ResourceType"
    """<p>The target resource type of the recommendation preference to create.</p> <p>The <code>Ec2Instance</code> option encompasses standalone instances and instances that are part of Auto Scaling groups. The <code>AutoScalingGroup</code> option encompasses only instances that are part of an Auto Scaling group.</p>"""
    scope: NotRequired["capo_compute_optimizer.types.scope.Scope"]
    """<p>An object that describes the scope of the recommendation preference to create.</p> <p>You can create recommendation preferences at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Activating enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p> <note> <p>You cannot create recommendation preferences for Auto Scaling groups at the organization and account levels. You can create recommendation preferences for Auto Scaling groups only at the resource level by specifying a scope name of <code>ResourceArn</code> and a scope value of the Auto Scaling group Amazon Resource Name (ARN). This will configure the preference for all instances that are part of the specified Auto Scaling group. You also cannot create recommendation preferences at the resource level for instances that are part of an Auto Scaling group. You can create recommendation preferences at the resource level only for standalone instances.</p> </note>"""
    enhanced_infrastructure_metrics: NotRequired[
        "capo_compute_optimizer.types.enhanced_infrastructure_metrics.EnhancedInfrastructureMetrics"
    ]
    """<p>The status of the enhanced infrastructure metrics recommendation preference to create or update.</p> <p>Specify the <code>Active</code> status to activate the preference, or specify <code>Inactive</code> to deactivate the preference.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    inferred_workload_types: NotRequired[
        "capo_compute_optimizer.types.inferred_workload_types_preference.InferredWorkloadTypesPreference"
    ]
    """<p>The status of the inferred workload types recommendation preference to create or update.</p> <note> <p>The inferred workload type feature is active by default. To deactivate it, create a recommendation preference.</p> </note> <p>Specify the <code>Inactive</code> status to deactivate the feature, or specify <code>Active</code> to activate it.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/inferred-workload-types.html">Inferred workload types</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    external_metrics_preference: NotRequired[
        "capo_compute_optimizer.types.external_metrics_preference.ExternalMetricsPreference"
    ]
    """<p>The provider of the external metrics recommendation preference to create or update.</p> <p>Specify a valid provider in the <code>source</code> field to activate the preference. To delete this preference, see the <a>DeleteRecommendationPreferences</a> action.</p> <p>This preference can only be set for the <code>Ec2Instance</code> resource type.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion.html">External metrics ingestion</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    look_back_period: NotRequired[
        "capo_compute_optimizer.types.look_back_period_preference.LookBackPeriodPreference"
    ]
    """<p> The preference to control the number of days the utilization metrics of the Amazon Web Services resource are analyzed. When this preference isn't specified, we use the default value <code>DAYS_14</code>. </p> <p>You can only set this preference for the Amazon EC2 instance, Auto Scaling group, Amazon EBS volume, Amazon ECS service on Fargate, Amazon RDS DB instance, and Aurora DB cluster storage resource types. </p> <note> <ul> <li> <p>Lookback period preferences for Amazon EC2 instances, Amazon EBS volumes, Amazon ECS services, Amazon RDS DB instances, and Aurora DB cluster storage resource types can be set at the organization, account, and resource levels.</p> </li> <li> <p>Auto Scaling group lookback preferences can only be set at the resource level.</p> </li> <li> <p>Amazon EBS volume lookback preferences can be set at the organization, account, and resource levels.</p> </li> <li> <p>Amazon ECS service on Fargate lookback preferences can be set at the organization, account, and resource levels.</p> </li> <li> <p>Amazon RDS DB instance lookback preferences can be set at the organization, account, and resource levels.</p> </li> <li> <p>Aurora DB cluster storage lookback preferences can be set at the organization, account, and resource levels.</p> </li> <li> <p>Changing the lookback period for Amazon EBS volumes to 14 days does not affect the 32-day lookback period used to determine whether an Amazon EBS volume is unattached.</p> </li> </ul> </note>"""
    utilization_preferences: NotRequired[
        "capo_compute_optimizer.types.utilization_preferences.UtilizationPreferences"
    ]
    """<p> The preference to control the resource’s CPU utilization threshold, CPU utilization headroom, and memory utilization headroom. When this preference isn't specified, we use the following default values. </p> <p>CPU utilization:</p> <ul> <li> <p> <code>P99_5</code> for threshold</p> </li> <li> <p> <code>PERCENT_20</code> for headroom</p> </li> </ul> <p>Memory utilization:</p> <ul> <li> <p> <code>PERCENT_20</code> for headroom</p> </li> </ul> <note> <ul> <li> <p>You can only set CPU and memory utilization preferences for the Amazon EC2 instance resource type.</p> </li> <li> <p>The threshold setting isn’t available for memory utilization.</p> </li> </ul> </note>"""
    preferred_resources: NotRequired[
        "capo_compute_optimizer.types.preferred_resources.PreferredResources"
    ]
    """<p> The preference to control which resource type values are considered when generating rightsizing recommendations. You can specify this preference as a combination of include and exclude lists. You must specify either an <code>includeList</code> or <code>excludeList</code>. If the preference is an empty set of resource type values, an error occurs. </p> <note> <p>You can only set this preference for the Amazon EC2 instance, Auto Scaling group, Amazon EBS volume, Amazon ECS service, Amazon RDS DB instance, and Aurora DB cluster storage resource types.</p> </note>"""
    savings_estimation_mode: NotRequired[
        "capo_compute_optimizer.types.savings_estimation_mode.SavingsEstimationMode"
    ]
    """<p> The status of the savings estimation mode preference to create or update. </p> <p>Specify the <code>AfterDiscounts</code> status to activate the preference, or specify <code>BeforeDiscounts</code> to deactivate the preference.</p> <p>Only the account manager or delegated administrator of your organization can activate this preference.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode.html"> Savings estimation mode</a> in the <i>Compute Optimizer User Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutRecommendationPreferencesRequest) -> dict:
    out: dict = {}
    import capo_compute_optimizer.types.resource_type

    out["resourceType"] = (
        capo_compute_optimizer.types.resource_type.serialize_aws_json_1_0(
            value["resource_type"]
        )
    )
    if "scope" in value:
        import capo_compute_optimizer.types.scope

        out["scope"] = capo_compute_optimizer.types.scope.serialize_aws_json_1_0(
            value["scope"]
        )
    if "enhanced_infrastructure_metrics" in value:
        import capo_compute_optimizer.types.enhanced_infrastructure_metrics

        out["enhancedInfrastructureMetrics"] = (
            capo_compute_optimizer.types.enhanced_infrastructure_metrics.serialize_aws_json_1_0(
                value["enhanced_infrastructure_metrics"]
            )
        )
    if "inferred_workload_types" in value:
        import capo_compute_optimizer.types.inferred_workload_types_preference

        out["inferredWorkloadTypes"] = (
            capo_compute_optimizer.types.inferred_workload_types_preference.serialize_aws_json_1_0(
                value["inferred_workload_types"]
            )
        )
    if "external_metrics_preference" in value:
        import capo_compute_optimizer.types.external_metrics_preference

        out["externalMetricsPreference"] = (
            capo_compute_optimizer.types.external_metrics_preference.serialize_aws_json_1_0(
                value["external_metrics_preference"]
            )
        )
    if "look_back_period" in value:
        import capo_compute_optimizer.types.look_back_period_preference

        out["lookBackPeriod"] = (
            capo_compute_optimizer.types.look_back_period_preference.serialize_aws_json_1_0(
                value["look_back_period"]
            )
        )
    if "utilization_preferences" in value:
        import capo_compute_optimizer.types.utilization_preferences

        out["utilizationPreferences"] = (
            capo_compute_optimizer.types.utilization_preferences.serialize_aws_json_1_0(
                value["utilization_preferences"]
            )
        )
    if "preferred_resources" in value:
        import capo_compute_optimizer.types.preferred_resources

        out["preferredResources"] = (
            capo_compute_optimizer.types.preferred_resources.serialize_aws_json_1_0(
                value["preferred_resources"]
            )
        )
    if "savings_estimation_mode" in value:
        import capo_compute_optimizer.types.savings_estimation_mode

        out["savingsEstimationMode"] = (
            capo_compute_optimizer.types.savings_estimation_mode.serialize_aws_json_1_0(
                value["savings_estimation_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutRecommendationPreferencesRequest:
    out: PutRecommendationPreferencesRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        import capo_compute_optimizer.types.resource_type

        out["resource_type"] = (
            capo_compute_optimizer.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError(
            "PutRecommendationPreferencesRequest.resource_type required"
        )
    if data.get("scope") is not None:
        import capo_compute_optimizer.types.scope

        out["scope"] = capo_compute_optimizer.types.scope.deserialize_aws_json_1_0(
            data["scope"]
        )
    if data.get("enhancedInfrastructureMetrics") is not None:
        import capo_compute_optimizer.types.enhanced_infrastructure_metrics

        out["enhanced_infrastructure_metrics"] = (
            capo_compute_optimizer.types.enhanced_infrastructure_metrics.deserialize_aws_json_1_0(
                data["enhancedInfrastructureMetrics"]
            )
        )
    if data.get("inferredWorkloadTypes") is not None:
        import capo_compute_optimizer.types.inferred_workload_types_preference

        out["inferred_workload_types"] = (
            capo_compute_optimizer.types.inferred_workload_types_preference.deserialize_aws_json_1_0(
                data["inferredWorkloadTypes"]
            )
        )
    if data.get("externalMetricsPreference") is not None:
        import capo_compute_optimizer.types.external_metrics_preference

        out["external_metrics_preference"] = (
            capo_compute_optimizer.types.external_metrics_preference.deserialize_aws_json_1_0(
                data["externalMetricsPreference"]
            )
        )
    if data.get("lookBackPeriod") is not None:
        import capo_compute_optimizer.types.look_back_period_preference

        out["look_back_period"] = (
            capo_compute_optimizer.types.look_back_period_preference.deserialize_aws_json_1_0(
                data["lookBackPeriod"]
            )
        )
    if data.get("utilizationPreferences") is not None:
        import capo_compute_optimizer.types.utilization_preferences

        out["utilization_preferences"] = (
            capo_compute_optimizer.types.utilization_preferences.deserialize_aws_json_1_0(
                data["utilizationPreferences"]
            )
        )
    if data.get("preferredResources") is not None:
        import capo_compute_optimizer.types.preferred_resources

        out["preferred_resources"] = (
            capo_compute_optimizer.types.preferred_resources.deserialize_aws_json_1_0(
                data["preferredResources"]
            )
        )
    if data.get("savingsEstimationMode") is not None:
        import capo_compute_optimizer.types.savings_estimation_mode

        out["savings_estimation_mode"] = (
            capo_compute_optimizer.types.savings_estimation_mode.deserialize_aws_json_1_0(
                data["savingsEstimationMode"]
            )
        )
    return out
