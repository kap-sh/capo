"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_amazon_mq_broker_details
    import capo_securityhub.types.aws_api_gateway_rest_api_details
    import capo_securityhub.types.aws_api_gateway_stage_details
    import capo_securityhub.types.aws_api_gateway_v2_api_details
    import capo_securityhub.types.aws_api_gateway_v2_stage_details
    import capo_securityhub.types.aws_app_sync_graph_ql_api_details
    import capo_securityhub.types.aws_athena_work_group_details
    import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_details
    import capo_securityhub.types.aws_auto_scaling_launch_configuration_details
    import capo_securityhub.types.aws_backup_backup_plan_details
    import capo_securityhub.types.aws_backup_backup_vault_details
    import capo_securityhub.types.aws_backup_recovery_point_details
    import capo_securityhub.types.aws_certificate_manager_certificate_details
    import capo_securityhub.types.aws_cloud_formation_stack_details
    import capo_securityhub.types.aws_cloud_front_distribution_details
    import capo_securityhub.types.aws_cloud_trail_trail_details
    import capo_securityhub.types.aws_cloud_watch_alarm_details
    import capo_securityhub.types.aws_code_build_project_details
    import capo_securityhub.types.aws_dms_endpoint_details
    import capo_securityhub.types.aws_dms_replication_instance_details
    import capo_securityhub.types.aws_dms_replication_task_details
    import capo_securityhub.types.aws_dynamo_db_table_details
    import capo_securityhub.types.aws_ec2_client_vpn_endpoint_details
    import capo_securityhub.types.aws_ec2_eip_details
    import capo_securityhub.types.aws_ec2_instance_details
    import capo_securityhub.types.aws_ec2_launch_template_details
    import capo_securityhub.types.aws_ec2_network_acl_details
    import capo_securityhub.types.aws_ec2_network_interface_details
    import capo_securityhub.types.aws_ec2_route_table_details
    import capo_securityhub.types.aws_ec2_security_group_details
    import capo_securityhub.types.aws_ec2_subnet_details
    import capo_securityhub.types.aws_ec2_transit_gateway_details
    import capo_securityhub.types.aws_ec2_volume_details
    import capo_securityhub.types.aws_ec2_vpc_details
    import capo_securityhub.types.aws_ec2_vpc_endpoint_service_details
    import capo_securityhub.types.aws_ec2_vpc_peering_connection_details
    import capo_securityhub.types.aws_ec2_vpn_connection_details
    import capo_securityhub.types.aws_ecr_container_image_details
    import capo_securityhub.types.aws_ecr_repository_details
    import capo_securityhub.types.aws_ecs_cluster_details
    import capo_securityhub.types.aws_ecs_container_details
    import capo_securityhub.types.aws_ecs_service_details
    import capo_securityhub.types.aws_ecs_task_definition_details
    import capo_securityhub.types.aws_ecs_task_details
    import capo_securityhub.types.aws_efs_access_point_details
    import capo_securityhub.types.aws_eks_cluster_details
    import capo_securityhub.types.aws_elastic_beanstalk_environment_details
    import capo_securityhub.types.aws_elasticsearch_domain_details
    import capo_securityhub.types.aws_elb_load_balancer_details
    import capo_securityhub.types.aws_elbv2_load_balancer_details
    import capo_securityhub.types.aws_event_schemas_registry_details
    import capo_securityhub.types.aws_events_endpoint_details
    import capo_securityhub.types.aws_events_eventbus_details
    import capo_securityhub.types.aws_guard_duty_detector_details
    import capo_securityhub.types.aws_iam_access_key_details
    import capo_securityhub.types.aws_iam_group_details
    import capo_securityhub.types.aws_iam_policy_details
    import capo_securityhub.types.aws_iam_role_details
    import capo_securityhub.types.aws_iam_user_details
    import capo_securityhub.types.aws_kinesis_stream_details
    import capo_securityhub.types.aws_kms_key_details
    import capo_securityhub.types.aws_lambda_function_details
    import capo_securityhub.types.aws_lambda_layer_version_details
    import capo_securityhub.types.aws_msk_cluster_details
    import capo_securityhub.types.aws_network_firewall_firewall_details
    import capo_securityhub.types.aws_network_firewall_firewall_policy_details
    import capo_securityhub.types.aws_network_firewall_rule_group_details
    import capo_securityhub.types.aws_open_search_service_domain_details
    import capo_securityhub.types.aws_rds_db_cluster_details
    import capo_securityhub.types.aws_rds_db_cluster_snapshot_details
    import capo_securityhub.types.aws_rds_db_instance_details
    import capo_securityhub.types.aws_rds_db_security_group_details
    import capo_securityhub.types.aws_rds_db_snapshot_details
    import capo_securityhub.types.aws_rds_event_subscription_details
    import capo_securityhub.types.aws_redshift_cluster_details
    import capo_securityhub.types.aws_route53_hosted_zone_details
    import capo_securityhub.types.aws_s3_access_point_details
    import capo_securityhub.types.aws_s3_account_public_access_block_details
    import capo_securityhub.types.aws_s3_bucket_details
    import capo_securityhub.types.aws_s3_object_details
    import capo_securityhub.types.aws_sage_maker_notebook_instance_details
    import capo_securityhub.types.aws_secrets_manager_secret_details
    import capo_securityhub.types.aws_sns_topic_details
    import capo_securityhub.types.aws_sqs_queue_details
    import capo_securityhub.types.aws_ssm_patch_compliance_details
    import capo_securityhub.types.aws_step_function_state_machine_details
    import capo_securityhub.types.aws_waf_rate_based_rule_details
    import capo_securityhub.types.aws_waf_regional_rate_based_rule_details
    import capo_securityhub.types.aws_waf_regional_rule_details
    import capo_securityhub.types.aws_waf_regional_rule_group_details
    import capo_securityhub.types.aws_waf_regional_web_acl_details
    import capo_securityhub.types.aws_waf_rule_details
    import capo_securityhub.types.aws_waf_rule_group_details
    import capo_securityhub.types.aws_waf_web_acl_details
    import capo_securityhub.types.aws_wafv2_rule_group_details
    import capo_securityhub.types.aws_wafv2_web_acl_details
    import capo_securityhub.types.aws_xray_encryption_config_details
    import capo_securityhub.types.azure_resource_details
    import capo_securityhub.types.code_repository_details
    import capo_securityhub.types.container_details
    import capo_securityhub.types.field_map
    import capo_securityhub.types.gcp_resource_details


class ResourceDetails(TypedDict, closed=True):
    aws_auto_scaling_auto_scaling_group: NotRequired[
        "capo_securityhub.types.aws_auto_scaling_auto_scaling_group_details.AwsAutoScalingAutoScalingGroupDetails"
    ]
    """<p>Details for an autoscaling group.</p>"""
    aws_code_build_project: NotRequired[
        "capo_securityhub.types.aws_code_build_project_details.AwsCodeBuildProjectDetails"
    ]
    """<p>Details for an CodeBuild project.</p>"""
    aws_cloud_front_distribution: NotRequired[
        "capo_securityhub.types.aws_cloud_front_distribution_details.AwsCloudFrontDistributionDetails"
    ]
    """<p>Details about a CloudFront distribution.</p>"""
    aws_ec2_instance: NotRequired[
        "capo_securityhub.types.aws_ec2_instance_details.AwsEc2InstanceDetails"
    ]
    """<p>Details about an EC2 instance related to a finding.</p>"""
    aws_ec2_network_interface: NotRequired[
        "capo_securityhub.types.aws_ec2_network_interface_details.AwsEc2NetworkInterfaceDetails"
    ]
    """<p>Details for an EC2 network interface.</p>"""
    aws_ec2_security_group: NotRequired[
        "capo_securityhub.types.aws_ec2_security_group_details.AwsEc2SecurityGroupDetails"
    ]
    """<p>Details for an EC2 security group.</p>"""
    aws_ec2_volume: NotRequired[
        "capo_securityhub.types.aws_ec2_volume_details.AwsEc2VolumeDetails"
    ]
    """<p>Details for an Amazon EC2 volume.</p>"""
    aws_ec2_vpc: NotRequired[
        "capo_securityhub.types.aws_ec2_vpc_details.AwsEc2VpcDetails"
    ]
    """<p>Details for an Amazon EC2 VPC.</p>"""
    aws_ec2_eip: NotRequired[
        "capo_securityhub.types.aws_ec2_eip_details.AwsEc2EipDetails"
    ]
    """<p>Details about an Elastic IP address.</p>"""
    aws_ec2_subnet: NotRequired[
        "capo_securityhub.types.aws_ec2_subnet_details.AwsEc2SubnetDetails"
    ]
    """<p>Details about a subnet in Amazon EC2.</p>"""
    aws_ec2_network_acl: NotRequired[
        "capo_securityhub.types.aws_ec2_network_acl_details.AwsEc2NetworkAclDetails"
    ]
    """<p>Details about an EC2 network access control list (ACL).</p>"""
    aws_elbv2_load_balancer: NotRequired[
        "capo_securityhub.types.aws_elbv2_load_balancer_details.AwsElbv2LoadBalancerDetails"
    ]
    """<p>Details about a load balancer.</p>"""
    aws_elastic_beanstalk_environment: NotRequired[
        "capo_securityhub.types.aws_elastic_beanstalk_environment_details.AwsElasticBeanstalkEnvironmentDetails"
    ]
    """<p>Details about an Elastic Beanstalk environment.</p>"""
    aws_elasticsearch_domain: NotRequired[
        "capo_securityhub.types.aws_elasticsearch_domain_details.AwsElasticsearchDomainDetails"
    ]
    """<p>Details for an Elasticsearch domain.</p>"""
    aws_s3_bucket: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_details.AwsS3BucketDetails"
    ]
    """<p>Details about an S3 bucket related to a finding.</p>"""
    aws_s3_account_public_access_block: NotRequired[
        "capo_securityhub.types.aws_s3_account_public_access_block_details.AwsS3AccountPublicAccessBlockDetails"
    ]
    """<p>Details about the Amazon S3 Public Access Block configuration for an account.</p>"""
    aws_s3_object: NotRequired[
        "capo_securityhub.types.aws_s3_object_details.AwsS3ObjectDetails"
    ]
    """<p>Details about an S3 object related to a finding.</p>"""
    aws_secrets_manager_secret: NotRequired[
        "capo_securityhub.types.aws_secrets_manager_secret_details.AwsSecretsManagerSecretDetails"
    ]
    """<p>Details about a Secrets Manager secret.</p>"""
    aws_iam_access_key: NotRequired[
        "capo_securityhub.types.aws_iam_access_key_details.AwsIamAccessKeyDetails"
    ]
    """<p>Details about an IAM access key related to a finding.</p>"""
    aws_iam_user: NotRequired[
        "capo_securityhub.types.aws_iam_user_details.AwsIamUserDetails"
    ]
    """<p>Details about an IAM user.</p>"""
    aws_iam_policy: NotRequired[
        "capo_securityhub.types.aws_iam_policy_details.AwsIamPolicyDetails"
    ]
    """<p>Details about an IAM permissions policy.</p>"""
    aws_api_gateway_v2_stage: NotRequired[
        "capo_securityhub.types.aws_api_gateway_v2_stage_details.AwsApiGatewayV2StageDetails"
    ]
    """<p>Provides information about a version 2 stage for Amazon API Gateway.</p>"""
    aws_api_gateway_v2_api: NotRequired[
        "capo_securityhub.types.aws_api_gateway_v2_api_details.AwsApiGatewayV2ApiDetails"
    ]
    """<p>Provides information about a version 2 API in Amazon API Gateway.</p>"""
    aws_dynamo_db_table: NotRequired[
        "capo_securityhub.types.aws_dynamo_db_table_details.AwsDynamoDbTableDetails"
    ]
    """<p>Details about a DynamoDB table.</p>"""
    aws_api_gateway_stage: NotRequired[
        "capo_securityhub.types.aws_api_gateway_stage_details.AwsApiGatewayStageDetails"
    ]
    """<p>Provides information about a version 1 Amazon API Gateway stage.</p>"""
    aws_api_gateway_rest_api: NotRequired[
        "capo_securityhub.types.aws_api_gateway_rest_api_details.AwsApiGatewayRestApiDetails"
    ]
    """<p>Provides information about a REST API in version 1 of Amazon API Gateway.</p>"""
    aws_cloud_trail_trail: NotRequired[
        "capo_securityhub.types.aws_cloud_trail_trail_details.AwsCloudTrailTrailDetails"
    ]
    """<p>Provides details about a CloudTrail trail.</p>"""
    aws_ssm_patch_compliance: NotRequired[
        "capo_securityhub.types.aws_ssm_patch_compliance_details.AwsSsmPatchComplianceDetails"
    ]
    """<p>Provides information about the state of a patch on an instance based on the patch baseline that was used to patch the instance.</p>"""
    aws_certificate_manager_certificate: NotRequired[
        "capo_securityhub.types.aws_certificate_manager_certificate_details.AwsCertificateManagerCertificateDetails"
    ]
    """<p>Provides details about an Certificate Manager certificate.</p>"""
    aws_redshift_cluster: NotRequired[
        "capo_securityhub.types.aws_redshift_cluster_details.AwsRedshiftClusterDetails"
    ]
    """<p>Contains details about an Amazon Redshift cluster.</p>"""
    aws_elb_load_balancer: NotRequired[
        "capo_securityhub.types.aws_elb_load_balancer_details.AwsElbLoadBalancerDetails"
    ]
    """<p>Contains details about a Classic Load Balancer.</p>"""
    aws_iam_group: NotRequired[
        "capo_securityhub.types.aws_iam_group_details.AwsIamGroupDetails"
    ]
    """<p>Contains details about an IAM group.</p>"""
    aws_iam_role: NotRequired[
        "capo_securityhub.types.aws_iam_role_details.AwsIamRoleDetails"
    ]
    """<p>Details about an IAM role.</p>"""
    aws_kms_key: NotRequired[
        "capo_securityhub.types.aws_kms_key_details.AwsKmsKeyDetails"
    ]
    """<p>Details about an KMS key.</p>"""
    aws_lambda_function: NotRequired[
        "capo_securityhub.types.aws_lambda_function_details.AwsLambdaFunctionDetails"
    ]
    """<p>Details about a Lambda function.</p>"""
    aws_lambda_layer_version: NotRequired[
        "capo_securityhub.types.aws_lambda_layer_version_details.AwsLambdaLayerVersionDetails"
    ]
    """<p>Details for a Lambda layer version.</p>"""
    aws_rds_db_instance: NotRequired[
        "capo_securityhub.types.aws_rds_db_instance_details.AwsRdsDbInstanceDetails"
    ]
    """<p>Details about an Amazon RDS database instance.</p>"""
    aws_sns_topic: NotRequired[
        "capo_securityhub.types.aws_sns_topic_details.AwsSnsTopicDetails"
    ]
    """<p>Details about an SNS topic.</p>"""
    aws_sqs_queue: NotRequired[
        "capo_securityhub.types.aws_sqs_queue_details.AwsSqsQueueDetails"
    ]
    """<p>Details about an SQS queue.</p>"""
    aws_waf_web_acl: NotRequired[
        "capo_securityhub.types.aws_waf_web_acl_details.AwsWafWebAclDetails"
    ]
    """<p>Details for an WAF web ACL.</p>"""
    aws_rds_db_snapshot: NotRequired[
        "capo_securityhub.types.aws_rds_db_snapshot_details.AwsRdsDbSnapshotDetails"
    ]
    """<p>Details about an Amazon RDS database snapshot.</p>"""
    aws_rds_db_cluster_snapshot: NotRequired[
        "capo_securityhub.types.aws_rds_db_cluster_snapshot_details.AwsRdsDbClusterSnapshotDetails"
    ]
    """<p>Details about an Amazon RDS database cluster snapshot.</p>"""
    aws_rds_db_cluster: NotRequired[
        "capo_securityhub.types.aws_rds_db_cluster_details.AwsRdsDbClusterDetails"
    ]
    """<p>Details about an Amazon RDS database cluster.</p>"""
    aws_ecs_cluster: NotRequired[
        "capo_securityhub.types.aws_ecs_cluster_details.AwsEcsClusterDetails"
    ]
    """<p>Details about an Amazon ECS cluster.</p>"""
    aws_ecs_container: NotRequired[
        "capo_securityhub.types.aws_ecs_container_details.AwsEcsContainerDetails"
    ]
    """<p>Provides information about a Docker container that's part of a task. </p>"""
    aws_ecs_task_definition: NotRequired[
        "capo_securityhub.types.aws_ecs_task_definition_details.AwsEcsTaskDefinitionDetails"
    ]
    """<p>Details about a task definition. A task definition describes the container and volume definitions of an Amazon Elastic Container Service task.</p>"""
    container: NotRequired["capo_securityhub.types.container_details.ContainerDetails"]
    """<p>Details about a container resource related to a finding.</p>"""
    other: NotRequired["capo_securityhub.types.field_map.FieldMap"]
    """<p>Details about a resource that are not available in a type-specific details object. Use the <code>Other</code> object in the following cases.</p> <ul> <li> <p>The type-specific object does not contain all of the fields that you want to populate. In this case, first use the type-specific object to populate those fields. Use the <code>Other</code> object to populate the fields that are missing from the type-specific object.</p> </li> <li> <p>The resource type does not have a corresponding object. This includes resources for which the type is <code>Other</code>. </p> </li> </ul>"""
    aws_rds_event_subscription: NotRequired[
        "capo_securityhub.types.aws_rds_event_subscription_details.AwsRdsEventSubscriptionDetails"
    ]
    """<p>Details about an RDS event notification subscription.</p>"""
    aws_ecs_service: NotRequired[
        "capo_securityhub.types.aws_ecs_service_details.AwsEcsServiceDetails"
    ]
    """<p>Details about a service within an ECS cluster.</p>"""
    aws_auto_scaling_launch_configuration: NotRequired[
        "capo_securityhub.types.aws_auto_scaling_launch_configuration_details.AwsAutoScalingLaunchConfigurationDetails"
    ]
    """<p>Provides details about a launch configuration.</p>"""
    aws_ec2_vpn_connection: NotRequired[
        "capo_securityhub.types.aws_ec2_vpn_connection_details.AwsEc2VpnConnectionDetails"
    ]
    """<p>Details about an Amazon EC2 VPN connection.</p>"""
    aws_ecr_container_image: NotRequired[
        "capo_securityhub.types.aws_ecr_container_image_details.AwsEcrContainerImageDetails"
    ]
    """<p>Information about an Amazon ECR image.</p>"""
    aws_open_search_service_domain: NotRequired[
        "capo_securityhub.types.aws_open_search_service_domain_details.AwsOpenSearchServiceDomainDetails"
    ]
    """<p>Details about an Amazon OpenSearch Service domain.</p>"""
    aws_ec2_vpc_endpoint_service: NotRequired[
        "capo_securityhub.types.aws_ec2_vpc_endpoint_service_details.AwsEc2VpcEndpointServiceDetails"
    ]
    """<p>Details about the service configuration for a VPC endpoint service.</p>"""
    aws_xray_encryption_config: NotRequired[
        "capo_securityhub.types.aws_xray_encryption_config_details.AwsXrayEncryptionConfigDetails"
    ]
    """<p>Information about the encryption configuration for X-Ray.</p>"""
    aws_waf_rate_based_rule: NotRequired[
        "capo_securityhub.types.aws_waf_rate_based_rule_details.AwsWafRateBasedRuleDetails"
    ]
    """<p>Details about a rate-based rule for global resources.</p>"""
    aws_waf_regional_rate_based_rule: NotRequired[
        "capo_securityhub.types.aws_waf_regional_rate_based_rule_details.AwsWafRegionalRateBasedRuleDetails"
    ]
    """<p>Details about a rate-based rule for Regional resources.</p>"""
    aws_ecr_repository: NotRequired[
        "capo_securityhub.types.aws_ecr_repository_details.AwsEcrRepositoryDetails"
    ]
    """<p>Information about an Amazon Elastic Container Registry repository.</p>"""
    aws_eks_cluster: NotRequired[
        "capo_securityhub.types.aws_eks_cluster_details.AwsEksClusterDetails"
    ]
    """<p>Details about an Amazon EKS cluster.</p>"""
    aws_network_firewall_firewall_policy: NotRequired[
        "capo_securityhub.types.aws_network_firewall_firewall_policy_details.AwsNetworkFirewallFirewallPolicyDetails"
    ]
    """<p>Details about an Network Firewall firewall policy.</p>"""
    aws_network_firewall_firewall: NotRequired[
        "capo_securityhub.types.aws_network_firewall_firewall_details.AwsNetworkFirewallFirewallDetails"
    ]
    """<p>Details about an Network Firewall firewall.</p>"""
    aws_network_firewall_rule_group: NotRequired[
        "capo_securityhub.types.aws_network_firewall_rule_group_details.AwsNetworkFirewallRuleGroupDetails"
    ]
    """<p>Details about an Network Firewall rule group.</p>"""
    aws_rds_db_security_group: NotRequired[
        "capo_securityhub.types.aws_rds_db_security_group_details.AwsRdsDbSecurityGroupDetails"
    ]
    """<p>Details about an Amazon RDS DB security group.</p>"""
    aws_kinesis_stream: NotRequired[
        "capo_securityhub.types.aws_kinesis_stream_details.AwsKinesisStreamDetails"
    ]
    """<p>Details about an Amazon Kinesis data stream.</p>"""
    aws_ec2_transit_gateway: NotRequired[
        "capo_securityhub.types.aws_ec2_transit_gateway_details.AwsEc2TransitGatewayDetails"
    ]
    """<p>Details about an Amazon EC2 transit gateway that interconnects your virtual private clouds (VPC) and on-premises networks.</p>"""
    aws_efs_access_point: NotRequired[
        "capo_securityhub.types.aws_efs_access_point_details.AwsEfsAccessPointDetails"
    ]
    """<p>Details about an Amazon EFS access point. An access point is an application-specific view into an EFS file system that applies an operating system user and group, and a file system path, to any file system request made through the access point. </p>"""
    aws_cloud_formation_stack: NotRequired[
        "capo_securityhub.types.aws_cloud_formation_stack_details.AwsCloudFormationStackDetails"
    ]
    """<p>Details about an CloudFormation stack. A stack is a collection of Amazon Web Services resources that you can manage as a single unit.</p>"""
    aws_cloud_watch_alarm: NotRequired[
        "capo_securityhub.types.aws_cloud_watch_alarm_details.AwsCloudWatchAlarmDetails"
    ]
    """<p>Details about an Amazon CloudWatch alarm. An alarm allows you to monitor and receive alerts about your Amazon Web Services resources and applications across multiple Regions.</p>"""
    aws_ec2_vpc_peering_connection: NotRequired[
        "capo_securityhub.types.aws_ec2_vpc_peering_connection_details.AwsEc2VpcPeeringConnectionDetails"
    ]
    """<p>Details about an Amazon EC2 VPC peering connection. A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them privately. </p>"""
    aws_waf_regional_rule_group: NotRequired[
        "capo_securityhub.types.aws_waf_regional_rule_group_details.AwsWafRegionalRuleGroupDetails"
    ]
    """<p>Details about an WAF rule group for Regional resources. </p>"""
    aws_waf_regional_rule: NotRequired[
        "capo_securityhub.types.aws_waf_regional_rule_details.AwsWafRegionalRuleDetails"
    ]
    """<p>Details about an WAF rule for Regional resources. </p>"""
    aws_waf_regional_web_acl: NotRequired[
        "capo_securityhub.types.aws_waf_regional_web_acl_details.AwsWafRegionalWebAclDetails"
    ]
    """<p>Details about an WAF web access control list (web ACL) for Regional resources. </p>"""
    aws_waf_rule: NotRequired[
        "capo_securityhub.types.aws_waf_rule_details.AwsWafRuleDetails"
    ]
    """<p>Details about an WAF rule for global resources. </p>"""
    aws_waf_rule_group: NotRequired[
        "capo_securityhub.types.aws_waf_rule_group_details.AwsWafRuleGroupDetails"
    ]
    """<p>Details about an WAF rule group for global resources. </p>"""
    aws_ecs_task: NotRequired[
        "capo_securityhub.types.aws_ecs_task_details.AwsEcsTaskDetails"
    ]
    """<p>Details about a task in a cluster. </p>"""
    aws_backup_backup_vault: NotRequired[
        "capo_securityhub.types.aws_backup_backup_vault_details.AwsBackupBackupVaultDetails"
    ]
    """<p>Provides details about an Backup backup vault. </p>"""
    aws_backup_backup_plan: NotRequired[
        "capo_securityhub.types.aws_backup_backup_plan_details.AwsBackupBackupPlanDetails"
    ]
    """<p>Provides details about an Backup backup plan. </p>"""
    aws_backup_recovery_point: NotRequired[
        "capo_securityhub.types.aws_backup_recovery_point_details.AwsBackupRecoveryPointDetails"
    ]
    """<p>Provides details about an Backup backup, or recovery point. </p>"""
    aws_ec2_launch_template: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_details.AwsEc2LaunchTemplateDetails"
    ]
    aws_sage_maker_notebook_instance: NotRequired[
        "capo_securityhub.types.aws_sage_maker_notebook_instance_details.AwsSageMakerNotebookInstanceDetails"
    ]
    aws_wafv2_web_acl: NotRequired[
        "capo_securityhub.types.aws_wafv2_web_acl_details.AwsWafv2WebAclDetails"
    ]
    aws_wafv2_rule_group: NotRequired[
        "capo_securityhub.types.aws_wafv2_rule_group_details.AwsWafv2RuleGroupDetails"
    ]
    aws_ec2_route_table: NotRequired[
        "capo_securityhub.types.aws_ec2_route_table_details.AwsEc2RouteTableDetails"
    ]
    """<p> Provides details about a route table. A route table contains a set of rules, called routes, that determine where to direct network traffic from your subnet or gateway. </p>"""
    aws_amazon_mq_broker: NotRequired[
        "capo_securityhub.types.aws_amazon_mq_broker_details.AwsAmazonMqBrokerDetails"
    ]
    """<p> Provides details about AppSync message broker. A message broker allows software applications and components to communicate using various programming languages, operating systems, and formal messaging protocols. </p>"""
    aws_app_sync_graph_ql_api: NotRequired[
        "capo_securityhub.types.aws_app_sync_graph_ql_api_details.AwsAppSyncGraphQlApiDetails"
    ]
    """<p> Provides details about an AppSync Graph QL API, which lets you query multiple databases, microservices, and APIs from a single GraphQL endpoint. </p>"""
    aws_event_schemas_registry: NotRequired[
        "capo_securityhub.types.aws_event_schemas_registry_details.AwsEventSchemasRegistryDetails"
    ]
    """<p> A schema defines the structure of events that are sent to Amazon EventBridge. Schema registries are containers for schemas. They collect and organize schemas so that your schemas are in logical groups. </p>"""
    aws_guard_duty_detector: NotRequired[
        "capo_securityhub.types.aws_guard_duty_detector_details.AwsGuardDutyDetectorDetails"
    ]
    """<p> Provides details about an Amazon GuardDuty detector. A detector is an object that represents the GuardDuty service. A detector is required for GuardDuty to become operational. </p>"""
    aws_step_function_state_machine: NotRequired[
        "capo_securityhub.types.aws_step_function_state_machine_details.AwsStepFunctionStateMachineDetails"
    ]
    """<p> Provides details about an Step Functions state machine, which is a workflow consisting of a series of event-driven steps. </p>"""
    aws_athena_work_group: NotRequired[
        "capo_securityhub.types.aws_athena_work_group_details.AwsAthenaWorkGroupDetails"
    ]
    """<p> Provides information about an Amazon Athena workgroup. A workgroup helps you separate users, teams, applications, or workloads. It also helps you set limits on data processing and track costs. </p>"""
    aws_events_eventbus: NotRequired[
        "capo_securityhub.types.aws_events_eventbus_details.AwsEventsEventbusDetails"
    ]
    """<p> Provides details about Amazon EventBridge event bus for an endpoint. An event bus is a router that receives events and delivers them to zero or more destinations, or targets.</p>"""
    aws_dms_endpoint: NotRequired[
        "capo_securityhub.types.aws_dms_endpoint_details.AwsDmsEndpointDetails"
    ]
    """<p> Provides details about an Database Migration Service (DMS) endpoint. An endpoint provides connection, data store type, and location information about your data store.</p>"""
    aws_events_endpoint: NotRequired[
        "capo_securityhub.types.aws_events_endpoint_details.AwsEventsEndpointDetails"
    ]
    """<p> Provides details about an Amazon EventBridge global endpoint. The endpoint can improve your application’s availability by making it Regional-fault tolerant.</p>"""
    aws_dms_replication_task: NotRequired[
        "capo_securityhub.types.aws_dms_replication_task_details.AwsDmsReplicationTaskDetails"
    ]
    """<p> Provides details about an DMS replication task. A replication task moves a set of data from the source endpoint to the target endpoint.</p>"""
    aws_dms_replication_instance: NotRequired[
        "capo_securityhub.types.aws_dms_replication_instance_details.AwsDmsReplicationInstanceDetails"
    ]
    """<p> Provides details about an DMS replication instance. DMS uses a replication instance to connect to your source data store, read the source data, and format the data for consumption by the target data store.</p>"""
    aws_route53_hosted_zone: NotRequired[
        "capo_securityhub.types.aws_route53_hosted_zone_details.AwsRoute53HostedZoneDetails"
    ]
    """<p> Provides details about an Amazon Route 53 hosted zone, including the four name servers assigned to the hosted zone. A hosted zone represents a collection of records that can be managed together, belonging to a single parent domain name.</p>"""
    aws_msk_cluster: NotRequired[
        "capo_securityhub.types.aws_msk_cluster_details.AwsMskClusterDetails"
    ]
    """<p> Provides details about an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster.</p>"""
    aws_s3_access_point: NotRequired[
        "capo_securityhub.types.aws_s3_access_point_details.AwsS3AccessPointDetails"
    ]
    """<p> Provides details about an Amazon Simple Storage Service (Amazon S3) access point. S3 access points are named network endpoints that are attached to S3 buckets that you can use to perform S3 object operations. </p>"""
    aws_ec2_client_vpn_endpoint: NotRequired[
        "capo_securityhub.types.aws_ec2_client_vpn_endpoint_details.AwsEc2ClientVpnEndpointDetails"
    ]
    """<p> Provides details about an Client VPN endpoint. A Client VPN endpoint is the resource that you create and configure to enable and manage client VPN sessions. It's the termination point for all client VPN sessions. </p>"""
    code_repository: NotRequired[
        "capo_securityhub.types.code_repository_details.CodeRepositoryDetails"
    ]
    """<p> Details about an external code repository with which you can connect your Amazon Web Services resources. The connection is established through Amazon Inspector. </p>"""
    azure_resource: NotRequired[
        "capo_securityhub.types.azure_resource_details.AzureResourceDetails"
    ]
    """<p>Details about an Azure resource that is related to a finding.</p>"""
    gcp_resource: NotRequired[
        "capo_securityhub.types.gcp_resource_details.GcpResourceDetails"
    ]
    """<p>Details about a GCP resource that is related to a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDetails) -> dict:
    out: dict = {}
    if "aws_auto_scaling_auto_scaling_group" in value:
        import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_details

        out["AwsAutoScalingAutoScalingGroup"] = (
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_details.serialize_json(
                value["aws_auto_scaling_auto_scaling_group"]
            )
        )
    if "aws_code_build_project" in value:
        import capo_securityhub.types.aws_code_build_project_details

        out["AwsCodeBuildProject"] = (
            capo_securityhub.types.aws_code_build_project_details.serialize_json(
                value["aws_code_build_project"]
            )
        )
    if "aws_cloud_front_distribution" in value:
        import capo_securityhub.types.aws_cloud_front_distribution_details

        out["AwsCloudFrontDistribution"] = (
            capo_securityhub.types.aws_cloud_front_distribution_details.serialize_json(
                value["aws_cloud_front_distribution"]
            )
        )
    if "aws_ec2_instance" in value:
        import capo_securityhub.types.aws_ec2_instance_details

        out["AwsEc2Instance"] = (
            capo_securityhub.types.aws_ec2_instance_details.serialize_json(
                value["aws_ec2_instance"]
            )
        )
    if "aws_ec2_network_interface" in value:
        import capo_securityhub.types.aws_ec2_network_interface_details

        out["AwsEc2NetworkInterface"] = (
            capo_securityhub.types.aws_ec2_network_interface_details.serialize_json(
                value["aws_ec2_network_interface"]
            )
        )
    if "aws_ec2_security_group" in value:
        import capo_securityhub.types.aws_ec2_security_group_details

        out["AwsEc2SecurityGroup"] = (
            capo_securityhub.types.aws_ec2_security_group_details.serialize_json(
                value["aws_ec2_security_group"]
            )
        )
    if "aws_ec2_volume" in value:
        import capo_securityhub.types.aws_ec2_volume_details

        out["AwsEc2Volume"] = (
            capo_securityhub.types.aws_ec2_volume_details.serialize_json(
                value["aws_ec2_volume"]
            )
        )
    if "aws_ec2_vpc" in value:
        import capo_securityhub.types.aws_ec2_vpc_details

        out["AwsEc2Vpc"] = capo_securityhub.types.aws_ec2_vpc_details.serialize_json(
            value["aws_ec2_vpc"]
        )
    if "aws_ec2_eip" in value:
        import capo_securityhub.types.aws_ec2_eip_details

        out["AwsEc2Eip"] = capo_securityhub.types.aws_ec2_eip_details.serialize_json(
            value["aws_ec2_eip"]
        )
    if "aws_ec2_subnet" in value:
        import capo_securityhub.types.aws_ec2_subnet_details

        out["AwsEc2Subnet"] = (
            capo_securityhub.types.aws_ec2_subnet_details.serialize_json(
                value["aws_ec2_subnet"]
            )
        )
    if "aws_ec2_network_acl" in value:
        import capo_securityhub.types.aws_ec2_network_acl_details

        out["AwsEc2NetworkAcl"] = (
            capo_securityhub.types.aws_ec2_network_acl_details.serialize_json(
                value["aws_ec2_network_acl"]
            )
        )
    if "aws_elbv2_load_balancer" in value:
        import capo_securityhub.types.aws_elbv2_load_balancer_details

        out["AwsElbv2LoadBalancer"] = (
            capo_securityhub.types.aws_elbv2_load_balancer_details.serialize_json(
                value["aws_elbv2_load_balancer"]
            )
        )
    if "aws_elastic_beanstalk_environment" in value:
        import capo_securityhub.types.aws_elastic_beanstalk_environment_details

        out["AwsElasticBeanstalkEnvironment"] = (
            capo_securityhub.types.aws_elastic_beanstalk_environment_details.serialize_json(
                value["aws_elastic_beanstalk_environment"]
            )
        )
    if "aws_elasticsearch_domain" in value:
        import capo_securityhub.types.aws_elasticsearch_domain_details

        out["AwsElasticsearchDomain"] = (
            capo_securityhub.types.aws_elasticsearch_domain_details.serialize_json(
                value["aws_elasticsearch_domain"]
            )
        )
    if "aws_s3_bucket" in value:
        import capo_securityhub.types.aws_s3_bucket_details

        out["AwsS3Bucket"] = (
            capo_securityhub.types.aws_s3_bucket_details.serialize_json(
                value["aws_s3_bucket"]
            )
        )
    if "aws_s3_account_public_access_block" in value:
        import capo_securityhub.types.aws_s3_account_public_access_block_details

        out["AwsS3AccountPublicAccessBlock"] = (
            capo_securityhub.types.aws_s3_account_public_access_block_details.serialize_json(
                value["aws_s3_account_public_access_block"]
            )
        )
    if "aws_s3_object" in value:
        import capo_securityhub.types.aws_s3_object_details

        out["AwsS3Object"] = (
            capo_securityhub.types.aws_s3_object_details.serialize_json(
                value["aws_s3_object"]
            )
        )
    if "aws_secrets_manager_secret" in value:
        import capo_securityhub.types.aws_secrets_manager_secret_details

        out["AwsSecretsManagerSecret"] = (
            capo_securityhub.types.aws_secrets_manager_secret_details.serialize_json(
                value["aws_secrets_manager_secret"]
            )
        )
    if "aws_iam_access_key" in value:
        import capo_securityhub.types.aws_iam_access_key_details

        out["AwsIamAccessKey"] = (
            capo_securityhub.types.aws_iam_access_key_details.serialize_json(
                value["aws_iam_access_key"]
            )
        )
    if "aws_iam_user" in value:
        import capo_securityhub.types.aws_iam_user_details

        out["AwsIamUser"] = capo_securityhub.types.aws_iam_user_details.serialize_json(
            value["aws_iam_user"]
        )
    if "aws_iam_policy" in value:
        import capo_securityhub.types.aws_iam_policy_details

        out["AwsIamPolicy"] = (
            capo_securityhub.types.aws_iam_policy_details.serialize_json(
                value["aws_iam_policy"]
            )
        )
    if "aws_api_gateway_v2_stage" in value:
        import capo_securityhub.types.aws_api_gateway_v2_stage_details

        out["AwsApiGatewayV2Stage"] = (
            capo_securityhub.types.aws_api_gateway_v2_stage_details.serialize_json(
                value["aws_api_gateway_v2_stage"]
            )
        )
    if "aws_api_gateway_v2_api" in value:
        import capo_securityhub.types.aws_api_gateway_v2_api_details

        out["AwsApiGatewayV2Api"] = (
            capo_securityhub.types.aws_api_gateway_v2_api_details.serialize_json(
                value["aws_api_gateway_v2_api"]
            )
        )
    if "aws_dynamo_db_table" in value:
        import capo_securityhub.types.aws_dynamo_db_table_details

        out["AwsDynamoDbTable"] = (
            capo_securityhub.types.aws_dynamo_db_table_details.serialize_json(
                value["aws_dynamo_db_table"]
            )
        )
    if "aws_api_gateway_stage" in value:
        import capo_securityhub.types.aws_api_gateway_stage_details

        out["AwsApiGatewayStage"] = (
            capo_securityhub.types.aws_api_gateway_stage_details.serialize_json(
                value["aws_api_gateway_stage"]
            )
        )
    if "aws_api_gateway_rest_api" in value:
        import capo_securityhub.types.aws_api_gateway_rest_api_details

        out["AwsApiGatewayRestApi"] = (
            capo_securityhub.types.aws_api_gateway_rest_api_details.serialize_json(
                value["aws_api_gateway_rest_api"]
            )
        )
    if "aws_cloud_trail_trail" in value:
        import capo_securityhub.types.aws_cloud_trail_trail_details

        out["AwsCloudTrailTrail"] = (
            capo_securityhub.types.aws_cloud_trail_trail_details.serialize_json(
                value["aws_cloud_trail_trail"]
            )
        )
    if "aws_ssm_patch_compliance" in value:
        import capo_securityhub.types.aws_ssm_patch_compliance_details

        out["AwsSsmPatchCompliance"] = (
            capo_securityhub.types.aws_ssm_patch_compliance_details.serialize_json(
                value["aws_ssm_patch_compliance"]
            )
        )
    if "aws_certificate_manager_certificate" in value:
        import capo_securityhub.types.aws_certificate_manager_certificate_details

        out["AwsCertificateManagerCertificate"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_details.serialize_json(
                value["aws_certificate_manager_certificate"]
            )
        )
    if "aws_redshift_cluster" in value:
        import capo_securityhub.types.aws_redshift_cluster_details

        out["AwsRedshiftCluster"] = (
            capo_securityhub.types.aws_redshift_cluster_details.serialize_json(
                value["aws_redshift_cluster"]
            )
        )
    if "aws_elb_load_balancer" in value:
        import capo_securityhub.types.aws_elb_load_balancer_details

        out["AwsElbLoadBalancer"] = (
            capo_securityhub.types.aws_elb_load_balancer_details.serialize_json(
                value["aws_elb_load_balancer"]
            )
        )
    if "aws_iam_group" in value:
        import capo_securityhub.types.aws_iam_group_details

        out["AwsIamGroup"] = (
            capo_securityhub.types.aws_iam_group_details.serialize_json(
                value["aws_iam_group"]
            )
        )
    if "aws_iam_role" in value:
        import capo_securityhub.types.aws_iam_role_details

        out["AwsIamRole"] = capo_securityhub.types.aws_iam_role_details.serialize_json(
            value["aws_iam_role"]
        )
    if "aws_kms_key" in value:
        import capo_securityhub.types.aws_kms_key_details

        out["AwsKmsKey"] = capo_securityhub.types.aws_kms_key_details.serialize_json(
            value["aws_kms_key"]
        )
    if "aws_lambda_function" in value:
        import capo_securityhub.types.aws_lambda_function_details

        out["AwsLambdaFunction"] = (
            capo_securityhub.types.aws_lambda_function_details.serialize_json(
                value["aws_lambda_function"]
            )
        )
    if "aws_lambda_layer_version" in value:
        import capo_securityhub.types.aws_lambda_layer_version_details

        out["AwsLambdaLayerVersion"] = (
            capo_securityhub.types.aws_lambda_layer_version_details.serialize_json(
                value["aws_lambda_layer_version"]
            )
        )
    if "aws_rds_db_instance" in value:
        import capo_securityhub.types.aws_rds_db_instance_details

        out["AwsRdsDbInstance"] = (
            capo_securityhub.types.aws_rds_db_instance_details.serialize_json(
                value["aws_rds_db_instance"]
            )
        )
    if "aws_sns_topic" in value:
        import capo_securityhub.types.aws_sns_topic_details

        out["AwsSnsTopic"] = (
            capo_securityhub.types.aws_sns_topic_details.serialize_json(
                value["aws_sns_topic"]
            )
        )
    if "aws_sqs_queue" in value:
        import capo_securityhub.types.aws_sqs_queue_details

        out["AwsSqsQueue"] = (
            capo_securityhub.types.aws_sqs_queue_details.serialize_json(
                value["aws_sqs_queue"]
            )
        )
    if "aws_waf_web_acl" in value:
        import capo_securityhub.types.aws_waf_web_acl_details

        out["AwsWafWebAcl"] = (
            capo_securityhub.types.aws_waf_web_acl_details.serialize_json(
                value["aws_waf_web_acl"]
            )
        )
    if "aws_rds_db_snapshot" in value:
        import capo_securityhub.types.aws_rds_db_snapshot_details

        out["AwsRdsDbSnapshot"] = (
            capo_securityhub.types.aws_rds_db_snapshot_details.serialize_json(
                value["aws_rds_db_snapshot"]
            )
        )
    if "aws_rds_db_cluster_snapshot" in value:
        import capo_securityhub.types.aws_rds_db_cluster_snapshot_details

        out["AwsRdsDbClusterSnapshot"] = (
            capo_securityhub.types.aws_rds_db_cluster_snapshot_details.serialize_json(
                value["aws_rds_db_cluster_snapshot"]
            )
        )
    if "aws_rds_db_cluster" in value:
        import capo_securityhub.types.aws_rds_db_cluster_details

        out["AwsRdsDbCluster"] = (
            capo_securityhub.types.aws_rds_db_cluster_details.serialize_json(
                value["aws_rds_db_cluster"]
            )
        )
    if "aws_ecs_cluster" in value:
        import capo_securityhub.types.aws_ecs_cluster_details

        out["AwsEcsCluster"] = (
            capo_securityhub.types.aws_ecs_cluster_details.serialize_json(
                value["aws_ecs_cluster"]
            )
        )
    if "aws_ecs_container" in value:
        import capo_securityhub.types.aws_ecs_container_details

        out["AwsEcsContainer"] = (
            capo_securityhub.types.aws_ecs_container_details.serialize_json(
                value["aws_ecs_container"]
            )
        )
    if "aws_ecs_task_definition" in value:
        import capo_securityhub.types.aws_ecs_task_definition_details

        out["AwsEcsTaskDefinition"] = (
            capo_securityhub.types.aws_ecs_task_definition_details.serialize_json(
                value["aws_ecs_task_definition"]
            )
        )
    if "container" in value:
        import capo_securityhub.types.container_details

        out["Container"] = capo_securityhub.types.container_details.serialize_json(
            value["container"]
        )
    if "other" in value:
        import capo_securityhub.types.field_map

        out["Other"] = capo_securityhub.types.field_map.serialize_json(value["other"])
    if "aws_rds_event_subscription" in value:
        import capo_securityhub.types.aws_rds_event_subscription_details

        out["AwsRdsEventSubscription"] = (
            capo_securityhub.types.aws_rds_event_subscription_details.serialize_json(
                value["aws_rds_event_subscription"]
            )
        )
    if "aws_ecs_service" in value:
        import capo_securityhub.types.aws_ecs_service_details

        out["AwsEcsService"] = (
            capo_securityhub.types.aws_ecs_service_details.serialize_json(
                value["aws_ecs_service"]
            )
        )
    if "aws_auto_scaling_launch_configuration" in value:
        import capo_securityhub.types.aws_auto_scaling_launch_configuration_details

        out["AwsAutoScalingLaunchConfiguration"] = (
            capo_securityhub.types.aws_auto_scaling_launch_configuration_details.serialize_json(
                value["aws_auto_scaling_launch_configuration"]
            )
        )
    if "aws_ec2_vpn_connection" in value:
        import capo_securityhub.types.aws_ec2_vpn_connection_details

        out["AwsEc2VpnConnection"] = (
            capo_securityhub.types.aws_ec2_vpn_connection_details.serialize_json(
                value["aws_ec2_vpn_connection"]
            )
        )
    if "aws_ecr_container_image" in value:
        import capo_securityhub.types.aws_ecr_container_image_details

        out["AwsEcrContainerImage"] = (
            capo_securityhub.types.aws_ecr_container_image_details.serialize_json(
                value["aws_ecr_container_image"]
            )
        )
    if "aws_open_search_service_domain" in value:
        import capo_securityhub.types.aws_open_search_service_domain_details

        out["AwsOpenSearchServiceDomain"] = (
            capo_securityhub.types.aws_open_search_service_domain_details.serialize_json(
                value["aws_open_search_service_domain"]
            )
        )
    if "aws_ec2_vpc_endpoint_service" in value:
        import capo_securityhub.types.aws_ec2_vpc_endpoint_service_details

        out["AwsEc2VpcEndpointService"] = (
            capo_securityhub.types.aws_ec2_vpc_endpoint_service_details.serialize_json(
                value["aws_ec2_vpc_endpoint_service"]
            )
        )
    if "aws_xray_encryption_config" in value:
        import capo_securityhub.types.aws_xray_encryption_config_details

        out["AwsXrayEncryptionConfig"] = (
            capo_securityhub.types.aws_xray_encryption_config_details.serialize_json(
                value["aws_xray_encryption_config"]
            )
        )
    if "aws_waf_rate_based_rule" in value:
        import capo_securityhub.types.aws_waf_rate_based_rule_details

        out["AwsWafRateBasedRule"] = (
            capo_securityhub.types.aws_waf_rate_based_rule_details.serialize_json(
                value["aws_waf_rate_based_rule"]
            )
        )
    if "aws_waf_regional_rate_based_rule" in value:
        import capo_securityhub.types.aws_waf_regional_rate_based_rule_details

        out["AwsWafRegionalRateBasedRule"] = (
            capo_securityhub.types.aws_waf_regional_rate_based_rule_details.serialize_json(
                value["aws_waf_regional_rate_based_rule"]
            )
        )
    if "aws_ecr_repository" in value:
        import capo_securityhub.types.aws_ecr_repository_details

        out["AwsEcrRepository"] = (
            capo_securityhub.types.aws_ecr_repository_details.serialize_json(
                value["aws_ecr_repository"]
            )
        )
    if "aws_eks_cluster" in value:
        import capo_securityhub.types.aws_eks_cluster_details

        out["AwsEksCluster"] = (
            capo_securityhub.types.aws_eks_cluster_details.serialize_json(
                value["aws_eks_cluster"]
            )
        )
    if "aws_network_firewall_firewall_policy" in value:
        import capo_securityhub.types.aws_network_firewall_firewall_policy_details

        out["AwsNetworkFirewallFirewallPolicy"] = (
            capo_securityhub.types.aws_network_firewall_firewall_policy_details.serialize_json(
                value["aws_network_firewall_firewall_policy"]
            )
        )
    if "aws_network_firewall_firewall" in value:
        import capo_securityhub.types.aws_network_firewall_firewall_details

        out["AwsNetworkFirewallFirewall"] = (
            capo_securityhub.types.aws_network_firewall_firewall_details.serialize_json(
                value["aws_network_firewall_firewall"]
            )
        )
    if "aws_network_firewall_rule_group" in value:
        import capo_securityhub.types.aws_network_firewall_rule_group_details

        out["AwsNetworkFirewallRuleGroup"] = (
            capo_securityhub.types.aws_network_firewall_rule_group_details.serialize_json(
                value["aws_network_firewall_rule_group"]
            )
        )
    if "aws_rds_db_security_group" in value:
        import capo_securityhub.types.aws_rds_db_security_group_details

        out["AwsRdsDbSecurityGroup"] = (
            capo_securityhub.types.aws_rds_db_security_group_details.serialize_json(
                value["aws_rds_db_security_group"]
            )
        )
    if "aws_kinesis_stream" in value:
        import capo_securityhub.types.aws_kinesis_stream_details

        out["AwsKinesisStream"] = (
            capo_securityhub.types.aws_kinesis_stream_details.serialize_json(
                value["aws_kinesis_stream"]
            )
        )
    if "aws_ec2_transit_gateway" in value:
        import capo_securityhub.types.aws_ec2_transit_gateway_details

        out["AwsEc2TransitGateway"] = (
            capo_securityhub.types.aws_ec2_transit_gateway_details.serialize_json(
                value["aws_ec2_transit_gateway"]
            )
        )
    if "aws_efs_access_point" in value:
        import capo_securityhub.types.aws_efs_access_point_details

        out["AwsEfsAccessPoint"] = (
            capo_securityhub.types.aws_efs_access_point_details.serialize_json(
                value["aws_efs_access_point"]
            )
        )
    if "aws_cloud_formation_stack" in value:
        import capo_securityhub.types.aws_cloud_formation_stack_details

        out["AwsCloudFormationStack"] = (
            capo_securityhub.types.aws_cloud_formation_stack_details.serialize_json(
                value["aws_cloud_formation_stack"]
            )
        )
    if "aws_cloud_watch_alarm" in value:
        import capo_securityhub.types.aws_cloud_watch_alarm_details

        out["AwsCloudWatchAlarm"] = (
            capo_securityhub.types.aws_cloud_watch_alarm_details.serialize_json(
                value["aws_cloud_watch_alarm"]
            )
        )
    if "aws_ec2_vpc_peering_connection" in value:
        import capo_securityhub.types.aws_ec2_vpc_peering_connection_details

        out["AwsEc2VpcPeeringConnection"] = (
            capo_securityhub.types.aws_ec2_vpc_peering_connection_details.serialize_json(
                value["aws_ec2_vpc_peering_connection"]
            )
        )
    if "aws_waf_regional_rule_group" in value:
        import capo_securityhub.types.aws_waf_regional_rule_group_details

        out["AwsWafRegionalRuleGroup"] = (
            capo_securityhub.types.aws_waf_regional_rule_group_details.serialize_json(
                value["aws_waf_regional_rule_group"]
            )
        )
    if "aws_waf_regional_rule" in value:
        import capo_securityhub.types.aws_waf_regional_rule_details

        out["AwsWafRegionalRule"] = (
            capo_securityhub.types.aws_waf_regional_rule_details.serialize_json(
                value["aws_waf_regional_rule"]
            )
        )
    if "aws_waf_regional_web_acl" in value:
        import capo_securityhub.types.aws_waf_regional_web_acl_details

        out["AwsWafRegionalWebAcl"] = (
            capo_securityhub.types.aws_waf_regional_web_acl_details.serialize_json(
                value["aws_waf_regional_web_acl"]
            )
        )
    if "aws_waf_rule" in value:
        import capo_securityhub.types.aws_waf_rule_details

        out["AwsWafRule"] = capo_securityhub.types.aws_waf_rule_details.serialize_json(
            value["aws_waf_rule"]
        )
    if "aws_waf_rule_group" in value:
        import capo_securityhub.types.aws_waf_rule_group_details

        out["AwsWafRuleGroup"] = (
            capo_securityhub.types.aws_waf_rule_group_details.serialize_json(
                value["aws_waf_rule_group"]
            )
        )
    if "aws_ecs_task" in value:
        import capo_securityhub.types.aws_ecs_task_details

        out["AwsEcsTask"] = capo_securityhub.types.aws_ecs_task_details.serialize_json(
            value["aws_ecs_task"]
        )
    if "aws_backup_backup_vault" in value:
        import capo_securityhub.types.aws_backup_backup_vault_details

        out["AwsBackupBackupVault"] = (
            capo_securityhub.types.aws_backup_backup_vault_details.serialize_json(
                value["aws_backup_backup_vault"]
            )
        )
    if "aws_backup_backup_plan" in value:
        import capo_securityhub.types.aws_backup_backup_plan_details

        out["AwsBackupBackupPlan"] = (
            capo_securityhub.types.aws_backup_backup_plan_details.serialize_json(
                value["aws_backup_backup_plan"]
            )
        )
    if "aws_backup_recovery_point" in value:
        import capo_securityhub.types.aws_backup_recovery_point_details

        out["AwsBackupRecoveryPoint"] = (
            capo_securityhub.types.aws_backup_recovery_point_details.serialize_json(
                value["aws_backup_recovery_point"]
            )
        )
    if "aws_ec2_launch_template" in value:
        import capo_securityhub.types.aws_ec2_launch_template_details

        out["AwsEc2LaunchTemplate"] = (
            capo_securityhub.types.aws_ec2_launch_template_details.serialize_json(
                value["aws_ec2_launch_template"]
            )
        )
    if "aws_sage_maker_notebook_instance" in value:
        import capo_securityhub.types.aws_sage_maker_notebook_instance_details

        out["AwsSageMakerNotebookInstance"] = (
            capo_securityhub.types.aws_sage_maker_notebook_instance_details.serialize_json(
                value["aws_sage_maker_notebook_instance"]
            )
        )
    if "aws_wafv2_web_acl" in value:
        import capo_securityhub.types.aws_wafv2_web_acl_details

        out["AwsWafv2WebAcl"] = (
            capo_securityhub.types.aws_wafv2_web_acl_details.serialize_json(
                value["aws_wafv2_web_acl"]
            )
        )
    if "aws_wafv2_rule_group" in value:
        import capo_securityhub.types.aws_wafv2_rule_group_details

        out["AwsWafv2RuleGroup"] = (
            capo_securityhub.types.aws_wafv2_rule_group_details.serialize_json(
                value["aws_wafv2_rule_group"]
            )
        )
    if "aws_ec2_route_table" in value:
        import capo_securityhub.types.aws_ec2_route_table_details

        out["AwsEc2RouteTable"] = (
            capo_securityhub.types.aws_ec2_route_table_details.serialize_json(
                value["aws_ec2_route_table"]
            )
        )
    if "aws_amazon_mq_broker" in value:
        import capo_securityhub.types.aws_amazon_mq_broker_details

        out["AwsAmazonMqBroker"] = (
            capo_securityhub.types.aws_amazon_mq_broker_details.serialize_json(
                value["aws_amazon_mq_broker"]
            )
        )
    if "aws_app_sync_graph_ql_api" in value:
        import capo_securityhub.types.aws_app_sync_graph_ql_api_details

        out["AwsAppSyncGraphQlApi"] = (
            capo_securityhub.types.aws_app_sync_graph_ql_api_details.serialize_json(
                value["aws_app_sync_graph_ql_api"]
            )
        )
    if "aws_event_schemas_registry" in value:
        import capo_securityhub.types.aws_event_schemas_registry_details

        out["AwsEventSchemasRegistry"] = (
            capo_securityhub.types.aws_event_schemas_registry_details.serialize_json(
                value["aws_event_schemas_registry"]
            )
        )
    if "aws_guard_duty_detector" in value:
        import capo_securityhub.types.aws_guard_duty_detector_details

        out["AwsGuardDutyDetector"] = (
            capo_securityhub.types.aws_guard_duty_detector_details.serialize_json(
                value["aws_guard_duty_detector"]
            )
        )
    if "aws_step_function_state_machine" in value:
        import capo_securityhub.types.aws_step_function_state_machine_details

        out["AwsStepFunctionStateMachine"] = (
            capo_securityhub.types.aws_step_function_state_machine_details.serialize_json(
                value["aws_step_function_state_machine"]
            )
        )
    if "aws_athena_work_group" in value:
        import capo_securityhub.types.aws_athena_work_group_details

        out["AwsAthenaWorkGroup"] = (
            capo_securityhub.types.aws_athena_work_group_details.serialize_json(
                value["aws_athena_work_group"]
            )
        )
    if "aws_events_eventbus" in value:
        import capo_securityhub.types.aws_events_eventbus_details

        out["AwsEventsEventbus"] = (
            capo_securityhub.types.aws_events_eventbus_details.serialize_json(
                value["aws_events_eventbus"]
            )
        )
    if "aws_dms_endpoint" in value:
        import capo_securityhub.types.aws_dms_endpoint_details

        out["AwsDmsEndpoint"] = (
            capo_securityhub.types.aws_dms_endpoint_details.serialize_json(
                value["aws_dms_endpoint"]
            )
        )
    if "aws_events_endpoint" in value:
        import capo_securityhub.types.aws_events_endpoint_details

        out["AwsEventsEndpoint"] = (
            capo_securityhub.types.aws_events_endpoint_details.serialize_json(
                value["aws_events_endpoint"]
            )
        )
    if "aws_dms_replication_task" in value:
        import capo_securityhub.types.aws_dms_replication_task_details

        out["AwsDmsReplicationTask"] = (
            capo_securityhub.types.aws_dms_replication_task_details.serialize_json(
                value["aws_dms_replication_task"]
            )
        )
    if "aws_dms_replication_instance" in value:
        import capo_securityhub.types.aws_dms_replication_instance_details

        out["AwsDmsReplicationInstance"] = (
            capo_securityhub.types.aws_dms_replication_instance_details.serialize_json(
                value["aws_dms_replication_instance"]
            )
        )
    if "aws_route53_hosted_zone" in value:
        import capo_securityhub.types.aws_route53_hosted_zone_details

        out["AwsRoute53HostedZone"] = (
            capo_securityhub.types.aws_route53_hosted_zone_details.serialize_json(
                value["aws_route53_hosted_zone"]
            )
        )
    if "aws_msk_cluster" in value:
        import capo_securityhub.types.aws_msk_cluster_details

        out["AwsMskCluster"] = (
            capo_securityhub.types.aws_msk_cluster_details.serialize_json(
                value["aws_msk_cluster"]
            )
        )
    if "aws_s3_access_point" in value:
        import capo_securityhub.types.aws_s3_access_point_details

        out["AwsS3AccessPoint"] = (
            capo_securityhub.types.aws_s3_access_point_details.serialize_json(
                value["aws_s3_access_point"]
            )
        )
    if "aws_ec2_client_vpn_endpoint" in value:
        import capo_securityhub.types.aws_ec2_client_vpn_endpoint_details

        out["AwsEc2ClientVpnEndpoint"] = (
            capo_securityhub.types.aws_ec2_client_vpn_endpoint_details.serialize_json(
                value["aws_ec2_client_vpn_endpoint"]
            )
        )
    if "code_repository" in value:
        import capo_securityhub.types.code_repository_details

        out["CodeRepository"] = (
            capo_securityhub.types.code_repository_details.serialize_json(
                value["code_repository"]
            )
        )
    if "azure_resource" in value:
        out["AzureResource"] = value["azure_resource"]
    if "gcp_resource" in value:
        out["GcpResource"] = value["gcp_resource"]
    return out


def deserialize_json(data: dict) -> ResourceDetails:
    out: ResourceDetails = {}  # type: ignore[typeddict-item]
    if data.get("AwsAutoScalingAutoScalingGroup") is not None:
        import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_details

        out["aws_auto_scaling_auto_scaling_group"] = (
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_details.deserialize_json(
                data["AwsAutoScalingAutoScalingGroup"]
            )
        )
    if data.get("AwsCodeBuildProject") is not None:
        import capo_securityhub.types.aws_code_build_project_details

        out["aws_code_build_project"] = (
            capo_securityhub.types.aws_code_build_project_details.deserialize_json(
                data["AwsCodeBuildProject"]
            )
        )
    if data.get("AwsCloudFrontDistribution") is not None:
        import capo_securityhub.types.aws_cloud_front_distribution_details

        out["aws_cloud_front_distribution"] = (
            capo_securityhub.types.aws_cloud_front_distribution_details.deserialize_json(
                data["AwsCloudFrontDistribution"]
            )
        )
    if data.get("AwsEc2Instance") is not None:
        import capo_securityhub.types.aws_ec2_instance_details

        out["aws_ec2_instance"] = (
            capo_securityhub.types.aws_ec2_instance_details.deserialize_json(
                data["AwsEc2Instance"]
            )
        )
    if data.get("AwsEc2NetworkInterface") is not None:
        import capo_securityhub.types.aws_ec2_network_interface_details

        out["aws_ec2_network_interface"] = (
            capo_securityhub.types.aws_ec2_network_interface_details.deserialize_json(
                data["AwsEc2NetworkInterface"]
            )
        )
    if data.get("AwsEc2SecurityGroup") is not None:
        import capo_securityhub.types.aws_ec2_security_group_details

        out["aws_ec2_security_group"] = (
            capo_securityhub.types.aws_ec2_security_group_details.deserialize_json(
                data["AwsEc2SecurityGroup"]
            )
        )
    if data.get("AwsEc2Volume") is not None:
        import capo_securityhub.types.aws_ec2_volume_details

        out["aws_ec2_volume"] = (
            capo_securityhub.types.aws_ec2_volume_details.deserialize_json(
                data["AwsEc2Volume"]
            )
        )
    if data.get("AwsEc2Vpc") is not None:
        import capo_securityhub.types.aws_ec2_vpc_details

        out["aws_ec2_vpc"] = (
            capo_securityhub.types.aws_ec2_vpc_details.deserialize_json(
                data["AwsEc2Vpc"]
            )
        )
    if data.get("AwsEc2Eip") is not None:
        import capo_securityhub.types.aws_ec2_eip_details

        out["aws_ec2_eip"] = (
            capo_securityhub.types.aws_ec2_eip_details.deserialize_json(
                data["AwsEc2Eip"]
            )
        )
    if data.get("AwsEc2Subnet") is not None:
        import capo_securityhub.types.aws_ec2_subnet_details

        out["aws_ec2_subnet"] = (
            capo_securityhub.types.aws_ec2_subnet_details.deserialize_json(
                data["AwsEc2Subnet"]
            )
        )
    if data.get("AwsEc2NetworkAcl") is not None:
        import capo_securityhub.types.aws_ec2_network_acl_details

        out["aws_ec2_network_acl"] = (
            capo_securityhub.types.aws_ec2_network_acl_details.deserialize_json(
                data["AwsEc2NetworkAcl"]
            )
        )
    if data.get("AwsElbv2LoadBalancer") is not None:
        import capo_securityhub.types.aws_elbv2_load_balancer_details

        out["aws_elbv2_load_balancer"] = (
            capo_securityhub.types.aws_elbv2_load_balancer_details.deserialize_json(
                data["AwsElbv2LoadBalancer"]
            )
        )
    if data.get("AwsElasticBeanstalkEnvironment") is not None:
        import capo_securityhub.types.aws_elastic_beanstalk_environment_details

        out["aws_elastic_beanstalk_environment"] = (
            capo_securityhub.types.aws_elastic_beanstalk_environment_details.deserialize_json(
                data["AwsElasticBeanstalkEnvironment"]
            )
        )
    if data.get("AwsElasticsearchDomain") is not None:
        import capo_securityhub.types.aws_elasticsearch_domain_details

        out["aws_elasticsearch_domain"] = (
            capo_securityhub.types.aws_elasticsearch_domain_details.deserialize_json(
                data["AwsElasticsearchDomain"]
            )
        )
    if data.get("AwsS3Bucket") is not None:
        import capo_securityhub.types.aws_s3_bucket_details

        out["aws_s3_bucket"] = (
            capo_securityhub.types.aws_s3_bucket_details.deserialize_json(
                data["AwsS3Bucket"]
            )
        )
    if data.get("AwsS3AccountPublicAccessBlock") is not None:
        import capo_securityhub.types.aws_s3_account_public_access_block_details

        out["aws_s3_account_public_access_block"] = (
            capo_securityhub.types.aws_s3_account_public_access_block_details.deserialize_json(
                data["AwsS3AccountPublicAccessBlock"]
            )
        )
    if data.get("AwsS3Object") is not None:
        import capo_securityhub.types.aws_s3_object_details

        out["aws_s3_object"] = (
            capo_securityhub.types.aws_s3_object_details.deserialize_json(
                data["AwsS3Object"]
            )
        )
    if data.get("AwsSecretsManagerSecret") is not None:
        import capo_securityhub.types.aws_secrets_manager_secret_details

        out["aws_secrets_manager_secret"] = (
            capo_securityhub.types.aws_secrets_manager_secret_details.deserialize_json(
                data["AwsSecretsManagerSecret"]
            )
        )
    if data.get("AwsIamAccessKey") is not None:
        import capo_securityhub.types.aws_iam_access_key_details

        out["aws_iam_access_key"] = (
            capo_securityhub.types.aws_iam_access_key_details.deserialize_json(
                data["AwsIamAccessKey"]
            )
        )
    if data.get("AwsIamUser") is not None:
        import capo_securityhub.types.aws_iam_user_details

        out["aws_iam_user"] = (
            capo_securityhub.types.aws_iam_user_details.deserialize_json(
                data["AwsIamUser"]
            )
        )
    if data.get("AwsIamPolicy") is not None:
        import capo_securityhub.types.aws_iam_policy_details

        out["aws_iam_policy"] = (
            capo_securityhub.types.aws_iam_policy_details.deserialize_json(
                data["AwsIamPolicy"]
            )
        )
    if data.get("AwsApiGatewayV2Stage") is not None:
        import capo_securityhub.types.aws_api_gateway_v2_stage_details

        out["aws_api_gateway_v2_stage"] = (
            capo_securityhub.types.aws_api_gateway_v2_stage_details.deserialize_json(
                data["AwsApiGatewayV2Stage"]
            )
        )
    if data.get("AwsApiGatewayV2Api") is not None:
        import capo_securityhub.types.aws_api_gateway_v2_api_details

        out["aws_api_gateway_v2_api"] = (
            capo_securityhub.types.aws_api_gateway_v2_api_details.deserialize_json(
                data["AwsApiGatewayV2Api"]
            )
        )
    if data.get("AwsDynamoDbTable") is not None:
        import capo_securityhub.types.aws_dynamo_db_table_details

        out["aws_dynamo_db_table"] = (
            capo_securityhub.types.aws_dynamo_db_table_details.deserialize_json(
                data["AwsDynamoDbTable"]
            )
        )
    if data.get("AwsApiGatewayStage") is not None:
        import capo_securityhub.types.aws_api_gateway_stage_details

        out["aws_api_gateway_stage"] = (
            capo_securityhub.types.aws_api_gateway_stage_details.deserialize_json(
                data["AwsApiGatewayStage"]
            )
        )
    if data.get("AwsApiGatewayRestApi") is not None:
        import capo_securityhub.types.aws_api_gateway_rest_api_details

        out["aws_api_gateway_rest_api"] = (
            capo_securityhub.types.aws_api_gateway_rest_api_details.deserialize_json(
                data["AwsApiGatewayRestApi"]
            )
        )
    if data.get("AwsCloudTrailTrail") is not None:
        import capo_securityhub.types.aws_cloud_trail_trail_details

        out["aws_cloud_trail_trail"] = (
            capo_securityhub.types.aws_cloud_trail_trail_details.deserialize_json(
                data["AwsCloudTrailTrail"]
            )
        )
    if data.get("AwsSsmPatchCompliance") is not None:
        import capo_securityhub.types.aws_ssm_patch_compliance_details

        out["aws_ssm_patch_compliance"] = (
            capo_securityhub.types.aws_ssm_patch_compliance_details.deserialize_json(
                data["AwsSsmPatchCompliance"]
            )
        )
    if data.get("AwsCertificateManagerCertificate") is not None:
        import capo_securityhub.types.aws_certificate_manager_certificate_details

        out["aws_certificate_manager_certificate"] = (
            capo_securityhub.types.aws_certificate_manager_certificate_details.deserialize_json(
                data["AwsCertificateManagerCertificate"]
            )
        )
    if data.get("AwsRedshiftCluster") is not None:
        import capo_securityhub.types.aws_redshift_cluster_details

        out["aws_redshift_cluster"] = (
            capo_securityhub.types.aws_redshift_cluster_details.deserialize_json(
                data["AwsRedshiftCluster"]
            )
        )
    if data.get("AwsElbLoadBalancer") is not None:
        import capo_securityhub.types.aws_elb_load_balancer_details

        out["aws_elb_load_balancer"] = (
            capo_securityhub.types.aws_elb_load_balancer_details.deserialize_json(
                data["AwsElbLoadBalancer"]
            )
        )
    if data.get("AwsIamGroup") is not None:
        import capo_securityhub.types.aws_iam_group_details

        out["aws_iam_group"] = (
            capo_securityhub.types.aws_iam_group_details.deserialize_json(
                data["AwsIamGroup"]
            )
        )
    if data.get("AwsIamRole") is not None:
        import capo_securityhub.types.aws_iam_role_details

        out["aws_iam_role"] = (
            capo_securityhub.types.aws_iam_role_details.deserialize_json(
                data["AwsIamRole"]
            )
        )
    if data.get("AwsKmsKey") is not None:
        import capo_securityhub.types.aws_kms_key_details

        out["aws_kms_key"] = (
            capo_securityhub.types.aws_kms_key_details.deserialize_json(
                data["AwsKmsKey"]
            )
        )
    if data.get("AwsLambdaFunction") is not None:
        import capo_securityhub.types.aws_lambda_function_details

        out["aws_lambda_function"] = (
            capo_securityhub.types.aws_lambda_function_details.deserialize_json(
                data["AwsLambdaFunction"]
            )
        )
    if data.get("AwsLambdaLayerVersion") is not None:
        import capo_securityhub.types.aws_lambda_layer_version_details

        out["aws_lambda_layer_version"] = (
            capo_securityhub.types.aws_lambda_layer_version_details.deserialize_json(
                data["AwsLambdaLayerVersion"]
            )
        )
    if data.get("AwsRdsDbInstance") is not None:
        import capo_securityhub.types.aws_rds_db_instance_details

        out["aws_rds_db_instance"] = (
            capo_securityhub.types.aws_rds_db_instance_details.deserialize_json(
                data["AwsRdsDbInstance"]
            )
        )
    if data.get("AwsSnsTopic") is not None:
        import capo_securityhub.types.aws_sns_topic_details

        out["aws_sns_topic"] = (
            capo_securityhub.types.aws_sns_topic_details.deserialize_json(
                data["AwsSnsTopic"]
            )
        )
    if data.get("AwsSqsQueue") is not None:
        import capo_securityhub.types.aws_sqs_queue_details

        out["aws_sqs_queue"] = (
            capo_securityhub.types.aws_sqs_queue_details.deserialize_json(
                data["AwsSqsQueue"]
            )
        )
    if data.get("AwsWafWebAcl") is not None:
        import capo_securityhub.types.aws_waf_web_acl_details

        out["aws_waf_web_acl"] = (
            capo_securityhub.types.aws_waf_web_acl_details.deserialize_json(
                data["AwsWafWebAcl"]
            )
        )
    if data.get("AwsRdsDbSnapshot") is not None:
        import capo_securityhub.types.aws_rds_db_snapshot_details

        out["aws_rds_db_snapshot"] = (
            capo_securityhub.types.aws_rds_db_snapshot_details.deserialize_json(
                data["AwsRdsDbSnapshot"]
            )
        )
    if data.get("AwsRdsDbClusterSnapshot") is not None:
        import capo_securityhub.types.aws_rds_db_cluster_snapshot_details

        out["aws_rds_db_cluster_snapshot"] = (
            capo_securityhub.types.aws_rds_db_cluster_snapshot_details.deserialize_json(
                data["AwsRdsDbClusterSnapshot"]
            )
        )
    if data.get("AwsRdsDbCluster") is not None:
        import capo_securityhub.types.aws_rds_db_cluster_details

        out["aws_rds_db_cluster"] = (
            capo_securityhub.types.aws_rds_db_cluster_details.deserialize_json(
                data["AwsRdsDbCluster"]
            )
        )
    if data.get("AwsEcsCluster") is not None:
        import capo_securityhub.types.aws_ecs_cluster_details

        out["aws_ecs_cluster"] = (
            capo_securityhub.types.aws_ecs_cluster_details.deserialize_json(
                data["AwsEcsCluster"]
            )
        )
    if data.get("AwsEcsContainer") is not None:
        import capo_securityhub.types.aws_ecs_container_details

        out["aws_ecs_container"] = (
            capo_securityhub.types.aws_ecs_container_details.deserialize_json(
                data["AwsEcsContainer"]
            )
        )
    if data.get("AwsEcsTaskDefinition") is not None:
        import capo_securityhub.types.aws_ecs_task_definition_details

        out["aws_ecs_task_definition"] = (
            capo_securityhub.types.aws_ecs_task_definition_details.deserialize_json(
                data["AwsEcsTaskDefinition"]
            )
        )
    if data.get("Container") is not None:
        import capo_securityhub.types.container_details

        out["container"] = capo_securityhub.types.container_details.deserialize_json(
            data["Container"]
        )
    if data.get("Other") is not None:
        import capo_securityhub.types.field_map

        out["other"] = capo_securityhub.types.field_map.deserialize_json(data["Other"])
    if data.get("AwsRdsEventSubscription") is not None:
        import capo_securityhub.types.aws_rds_event_subscription_details

        out["aws_rds_event_subscription"] = (
            capo_securityhub.types.aws_rds_event_subscription_details.deserialize_json(
                data["AwsRdsEventSubscription"]
            )
        )
    if data.get("AwsEcsService") is not None:
        import capo_securityhub.types.aws_ecs_service_details

        out["aws_ecs_service"] = (
            capo_securityhub.types.aws_ecs_service_details.deserialize_json(
                data["AwsEcsService"]
            )
        )
    if data.get("AwsAutoScalingLaunchConfiguration") is not None:
        import capo_securityhub.types.aws_auto_scaling_launch_configuration_details

        out["aws_auto_scaling_launch_configuration"] = (
            capo_securityhub.types.aws_auto_scaling_launch_configuration_details.deserialize_json(
                data["AwsAutoScalingLaunchConfiguration"]
            )
        )
    if data.get("AwsEc2VpnConnection") is not None:
        import capo_securityhub.types.aws_ec2_vpn_connection_details

        out["aws_ec2_vpn_connection"] = (
            capo_securityhub.types.aws_ec2_vpn_connection_details.deserialize_json(
                data["AwsEc2VpnConnection"]
            )
        )
    if data.get("AwsEcrContainerImage") is not None:
        import capo_securityhub.types.aws_ecr_container_image_details

        out["aws_ecr_container_image"] = (
            capo_securityhub.types.aws_ecr_container_image_details.deserialize_json(
                data["AwsEcrContainerImage"]
            )
        )
    if data.get("AwsOpenSearchServiceDomain") is not None:
        import capo_securityhub.types.aws_open_search_service_domain_details

        out["aws_open_search_service_domain"] = (
            capo_securityhub.types.aws_open_search_service_domain_details.deserialize_json(
                data["AwsOpenSearchServiceDomain"]
            )
        )
    if data.get("AwsEc2VpcEndpointService") is not None:
        import capo_securityhub.types.aws_ec2_vpc_endpoint_service_details

        out["aws_ec2_vpc_endpoint_service"] = (
            capo_securityhub.types.aws_ec2_vpc_endpoint_service_details.deserialize_json(
                data["AwsEc2VpcEndpointService"]
            )
        )
    if data.get("AwsXrayEncryptionConfig") is not None:
        import capo_securityhub.types.aws_xray_encryption_config_details

        out["aws_xray_encryption_config"] = (
            capo_securityhub.types.aws_xray_encryption_config_details.deserialize_json(
                data["AwsXrayEncryptionConfig"]
            )
        )
    if data.get("AwsWafRateBasedRule") is not None:
        import capo_securityhub.types.aws_waf_rate_based_rule_details

        out["aws_waf_rate_based_rule"] = (
            capo_securityhub.types.aws_waf_rate_based_rule_details.deserialize_json(
                data["AwsWafRateBasedRule"]
            )
        )
    if data.get("AwsWafRegionalRateBasedRule") is not None:
        import capo_securityhub.types.aws_waf_regional_rate_based_rule_details

        out["aws_waf_regional_rate_based_rule"] = (
            capo_securityhub.types.aws_waf_regional_rate_based_rule_details.deserialize_json(
                data["AwsWafRegionalRateBasedRule"]
            )
        )
    if data.get("AwsEcrRepository") is not None:
        import capo_securityhub.types.aws_ecr_repository_details

        out["aws_ecr_repository"] = (
            capo_securityhub.types.aws_ecr_repository_details.deserialize_json(
                data["AwsEcrRepository"]
            )
        )
    if data.get("AwsEksCluster") is not None:
        import capo_securityhub.types.aws_eks_cluster_details

        out["aws_eks_cluster"] = (
            capo_securityhub.types.aws_eks_cluster_details.deserialize_json(
                data["AwsEksCluster"]
            )
        )
    if data.get("AwsNetworkFirewallFirewallPolicy") is not None:
        import capo_securityhub.types.aws_network_firewall_firewall_policy_details

        out["aws_network_firewall_firewall_policy"] = (
            capo_securityhub.types.aws_network_firewall_firewall_policy_details.deserialize_json(
                data["AwsNetworkFirewallFirewallPolicy"]
            )
        )
    if data.get("AwsNetworkFirewallFirewall") is not None:
        import capo_securityhub.types.aws_network_firewall_firewall_details

        out["aws_network_firewall_firewall"] = (
            capo_securityhub.types.aws_network_firewall_firewall_details.deserialize_json(
                data["AwsNetworkFirewallFirewall"]
            )
        )
    if data.get("AwsNetworkFirewallRuleGroup") is not None:
        import capo_securityhub.types.aws_network_firewall_rule_group_details

        out["aws_network_firewall_rule_group"] = (
            capo_securityhub.types.aws_network_firewall_rule_group_details.deserialize_json(
                data["AwsNetworkFirewallRuleGroup"]
            )
        )
    if data.get("AwsRdsDbSecurityGroup") is not None:
        import capo_securityhub.types.aws_rds_db_security_group_details

        out["aws_rds_db_security_group"] = (
            capo_securityhub.types.aws_rds_db_security_group_details.deserialize_json(
                data["AwsRdsDbSecurityGroup"]
            )
        )
    if data.get("AwsKinesisStream") is not None:
        import capo_securityhub.types.aws_kinesis_stream_details

        out["aws_kinesis_stream"] = (
            capo_securityhub.types.aws_kinesis_stream_details.deserialize_json(
                data["AwsKinesisStream"]
            )
        )
    if data.get("AwsEc2TransitGateway") is not None:
        import capo_securityhub.types.aws_ec2_transit_gateway_details

        out["aws_ec2_transit_gateway"] = (
            capo_securityhub.types.aws_ec2_transit_gateway_details.deserialize_json(
                data["AwsEc2TransitGateway"]
            )
        )
    if data.get("AwsEfsAccessPoint") is not None:
        import capo_securityhub.types.aws_efs_access_point_details

        out["aws_efs_access_point"] = (
            capo_securityhub.types.aws_efs_access_point_details.deserialize_json(
                data["AwsEfsAccessPoint"]
            )
        )
    if data.get("AwsCloudFormationStack") is not None:
        import capo_securityhub.types.aws_cloud_formation_stack_details

        out["aws_cloud_formation_stack"] = (
            capo_securityhub.types.aws_cloud_formation_stack_details.deserialize_json(
                data["AwsCloudFormationStack"]
            )
        )
    if data.get("AwsCloudWatchAlarm") is not None:
        import capo_securityhub.types.aws_cloud_watch_alarm_details

        out["aws_cloud_watch_alarm"] = (
            capo_securityhub.types.aws_cloud_watch_alarm_details.deserialize_json(
                data["AwsCloudWatchAlarm"]
            )
        )
    if data.get("AwsEc2VpcPeeringConnection") is not None:
        import capo_securityhub.types.aws_ec2_vpc_peering_connection_details

        out["aws_ec2_vpc_peering_connection"] = (
            capo_securityhub.types.aws_ec2_vpc_peering_connection_details.deserialize_json(
                data["AwsEc2VpcPeeringConnection"]
            )
        )
    if data.get("AwsWafRegionalRuleGroup") is not None:
        import capo_securityhub.types.aws_waf_regional_rule_group_details

        out["aws_waf_regional_rule_group"] = (
            capo_securityhub.types.aws_waf_regional_rule_group_details.deserialize_json(
                data["AwsWafRegionalRuleGroup"]
            )
        )
    if data.get("AwsWafRegionalRule") is not None:
        import capo_securityhub.types.aws_waf_regional_rule_details

        out["aws_waf_regional_rule"] = (
            capo_securityhub.types.aws_waf_regional_rule_details.deserialize_json(
                data["AwsWafRegionalRule"]
            )
        )
    if data.get("AwsWafRegionalWebAcl") is not None:
        import capo_securityhub.types.aws_waf_regional_web_acl_details

        out["aws_waf_regional_web_acl"] = (
            capo_securityhub.types.aws_waf_regional_web_acl_details.deserialize_json(
                data["AwsWafRegionalWebAcl"]
            )
        )
    if data.get("AwsWafRule") is not None:
        import capo_securityhub.types.aws_waf_rule_details

        out["aws_waf_rule"] = (
            capo_securityhub.types.aws_waf_rule_details.deserialize_json(
                data["AwsWafRule"]
            )
        )
    if data.get("AwsWafRuleGroup") is not None:
        import capo_securityhub.types.aws_waf_rule_group_details

        out["aws_waf_rule_group"] = (
            capo_securityhub.types.aws_waf_rule_group_details.deserialize_json(
                data["AwsWafRuleGroup"]
            )
        )
    if data.get("AwsEcsTask") is not None:
        import capo_securityhub.types.aws_ecs_task_details

        out["aws_ecs_task"] = (
            capo_securityhub.types.aws_ecs_task_details.deserialize_json(
                data["AwsEcsTask"]
            )
        )
    if data.get("AwsBackupBackupVault") is not None:
        import capo_securityhub.types.aws_backup_backup_vault_details

        out["aws_backup_backup_vault"] = (
            capo_securityhub.types.aws_backup_backup_vault_details.deserialize_json(
                data["AwsBackupBackupVault"]
            )
        )
    if data.get("AwsBackupBackupPlan") is not None:
        import capo_securityhub.types.aws_backup_backup_plan_details

        out["aws_backup_backup_plan"] = (
            capo_securityhub.types.aws_backup_backup_plan_details.deserialize_json(
                data["AwsBackupBackupPlan"]
            )
        )
    if data.get("AwsBackupRecoveryPoint") is not None:
        import capo_securityhub.types.aws_backup_recovery_point_details

        out["aws_backup_recovery_point"] = (
            capo_securityhub.types.aws_backup_recovery_point_details.deserialize_json(
                data["AwsBackupRecoveryPoint"]
            )
        )
    if data.get("AwsEc2LaunchTemplate") is not None:
        import capo_securityhub.types.aws_ec2_launch_template_details

        out["aws_ec2_launch_template"] = (
            capo_securityhub.types.aws_ec2_launch_template_details.deserialize_json(
                data["AwsEc2LaunchTemplate"]
            )
        )
    if data.get("AwsSageMakerNotebookInstance") is not None:
        import capo_securityhub.types.aws_sage_maker_notebook_instance_details

        out["aws_sage_maker_notebook_instance"] = (
            capo_securityhub.types.aws_sage_maker_notebook_instance_details.deserialize_json(
                data["AwsSageMakerNotebookInstance"]
            )
        )
    if data.get("AwsWafv2WebAcl") is not None:
        import capo_securityhub.types.aws_wafv2_web_acl_details

        out["aws_wafv2_web_acl"] = (
            capo_securityhub.types.aws_wafv2_web_acl_details.deserialize_json(
                data["AwsWafv2WebAcl"]
            )
        )
    if data.get("AwsWafv2RuleGroup") is not None:
        import capo_securityhub.types.aws_wafv2_rule_group_details

        out["aws_wafv2_rule_group"] = (
            capo_securityhub.types.aws_wafv2_rule_group_details.deserialize_json(
                data["AwsWafv2RuleGroup"]
            )
        )
    if data.get("AwsEc2RouteTable") is not None:
        import capo_securityhub.types.aws_ec2_route_table_details

        out["aws_ec2_route_table"] = (
            capo_securityhub.types.aws_ec2_route_table_details.deserialize_json(
                data["AwsEc2RouteTable"]
            )
        )
    if data.get("AwsAmazonMqBroker") is not None:
        import capo_securityhub.types.aws_amazon_mq_broker_details

        out["aws_amazon_mq_broker"] = (
            capo_securityhub.types.aws_amazon_mq_broker_details.deserialize_json(
                data["AwsAmazonMqBroker"]
            )
        )
    if data.get("AwsAppSyncGraphQlApi") is not None:
        import capo_securityhub.types.aws_app_sync_graph_ql_api_details

        out["aws_app_sync_graph_ql_api"] = (
            capo_securityhub.types.aws_app_sync_graph_ql_api_details.deserialize_json(
                data["AwsAppSyncGraphQlApi"]
            )
        )
    if data.get("AwsEventSchemasRegistry") is not None:
        import capo_securityhub.types.aws_event_schemas_registry_details

        out["aws_event_schemas_registry"] = (
            capo_securityhub.types.aws_event_schemas_registry_details.deserialize_json(
                data["AwsEventSchemasRegistry"]
            )
        )
    if data.get("AwsGuardDutyDetector") is not None:
        import capo_securityhub.types.aws_guard_duty_detector_details

        out["aws_guard_duty_detector"] = (
            capo_securityhub.types.aws_guard_duty_detector_details.deserialize_json(
                data["AwsGuardDutyDetector"]
            )
        )
    if data.get("AwsStepFunctionStateMachine") is not None:
        import capo_securityhub.types.aws_step_function_state_machine_details

        out["aws_step_function_state_machine"] = (
            capo_securityhub.types.aws_step_function_state_machine_details.deserialize_json(
                data["AwsStepFunctionStateMachine"]
            )
        )
    if data.get("AwsAthenaWorkGroup") is not None:
        import capo_securityhub.types.aws_athena_work_group_details

        out["aws_athena_work_group"] = (
            capo_securityhub.types.aws_athena_work_group_details.deserialize_json(
                data["AwsAthenaWorkGroup"]
            )
        )
    if data.get("AwsEventsEventbus") is not None:
        import capo_securityhub.types.aws_events_eventbus_details

        out["aws_events_eventbus"] = (
            capo_securityhub.types.aws_events_eventbus_details.deserialize_json(
                data["AwsEventsEventbus"]
            )
        )
    if data.get("AwsDmsEndpoint") is not None:
        import capo_securityhub.types.aws_dms_endpoint_details

        out["aws_dms_endpoint"] = (
            capo_securityhub.types.aws_dms_endpoint_details.deserialize_json(
                data["AwsDmsEndpoint"]
            )
        )
    if data.get("AwsEventsEndpoint") is not None:
        import capo_securityhub.types.aws_events_endpoint_details

        out["aws_events_endpoint"] = (
            capo_securityhub.types.aws_events_endpoint_details.deserialize_json(
                data["AwsEventsEndpoint"]
            )
        )
    if data.get("AwsDmsReplicationTask") is not None:
        import capo_securityhub.types.aws_dms_replication_task_details

        out["aws_dms_replication_task"] = (
            capo_securityhub.types.aws_dms_replication_task_details.deserialize_json(
                data["AwsDmsReplicationTask"]
            )
        )
    if data.get("AwsDmsReplicationInstance") is not None:
        import capo_securityhub.types.aws_dms_replication_instance_details

        out["aws_dms_replication_instance"] = (
            capo_securityhub.types.aws_dms_replication_instance_details.deserialize_json(
                data["AwsDmsReplicationInstance"]
            )
        )
    if data.get("AwsRoute53HostedZone") is not None:
        import capo_securityhub.types.aws_route53_hosted_zone_details

        out["aws_route53_hosted_zone"] = (
            capo_securityhub.types.aws_route53_hosted_zone_details.deserialize_json(
                data["AwsRoute53HostedZone"]
            )
        )
    if data.get("AwsMskCluster") is not None:
        import capo_securityhub.types.aws_msk_cluster_details

        out["aws_msk_cluster"] = (
            capo_securityhub.types.aws_msk_cluster_details.deserialize_json(
                data["AwsMskCluster"]
            )
        )
    if data.get("AwsS3AccessPoint") is not None:
        import capo_securityhub.types.aws_s3_access_point_details

        out["aws_s3_access_point"] = (
            capo_securityhub.types.aws_s3_access_point_details.deserialize_json(
                data["AwsS3AccessPoint"]
            )
        )
    if data.get("AwsEc2ClientVpnEndpoint") is not None:
        import capo_securityhub.types.aws_ec2_client_vpn_endpoint_details

        out["aws_ec2_client_vpn_endpoint"] = (
            capo_securityhub.types.aws_ec2_client_vpn_endpoint_details.deserialize_json(
                data["AwsEc2ClientVpnEndpoint"]
            )
        )
    if data.get("CodeRepository") is not None:
        import capo_securityhub.types.code_repository_details

        out["code_repository"] = (
            capo_securityhub.types.code_repository_details.deserialize_json(
                data["CodeRepository"]
            )
        )
    if data.get("AzureResource") is not None:
        out["azure_resource"] = data["AzureResource"]
    if data.get("GcpResource") is not None:
        out["gcp_resource"] = data["GcpResource"]
    return out
