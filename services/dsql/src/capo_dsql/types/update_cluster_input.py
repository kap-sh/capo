"""Generated from Smithy shape ``com.amazonaws.dsql#UpdateClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.client_token
    import capo_dsql.types.cluster_id
    import capo_dsql.types.deletion_protection_enabled
    import capo_dsql.types.kms_encryption_key
    import capo_dsql.types.metric_group_request_list
    import capo_dsql.types.multi_region_properties


class UpdateClusterInput(TypedDict, closed=True):
    identifier: "capo_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster you want to update.</p>"""
    deletion_protection_enabled: NotRequired[
        "capo_dsql.types.deletion_protection_enabled.DeletionProtectionEnabled"
    ]
    """<p>Specifies whether to enable deletion protection in your cluster.</p>"""
    kms_encryption_key: NotRequired[
        "capo_dsql.types.kms_encryption_key.KmsEncryptionKey"
    ]
    """<p>The KMS key that encrypts and protects the data on your cluster. You can specify the ARN, ID, or alias of an existing key or have Amazon Web Services create a default key for you.</p> <p>To switch to the key owned by Amazon Web Services, specify the reserved value <code>AWS_OWNED_KMS_KEY</code>.</p>"""
    client_token: NotRequired["capo_dsql.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully. The subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>"""
    multi_region_properties: NotRequired[
        "capo_dsql.types.multi_region_properties.MultiRegionProperties"
    ]
    """<p>The new multi-Region cluster configuration settings to be applied during an update operation.</p>"""
    metric_groups: NotRequired[
        "capo_dsql.types.metric_group_request_list.MetricGroupRequestList"
    ]
    """<p>The complete set of metric groups to enable for advanced monitoring on the cluster. This list replaces the current set, so any metric group that you don't include is disabled. To disable all metric groups, specify an empty list (<code>[]</code>). If you omit this parameter, the current setting doesn't change.</p> <p>To view the metric groups enabled on a cluster, use <i>GetCluster</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterInput) -> dict:
    out: dict = {}
    if "deletion_protection_enabled" in value:
        out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "kms_encryption_key" in value:
        out["kmsEncryptionKey"] = value["kms_encryption_key"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "multi_region_properties" in value:
        import capo_dsql.types.multi_region_properties

        out["multiRegionProperties"] = (
            capo_dsql.types.multi_region_properties.serialize_json(
                value["multi_region_properties"]
            )
        )
    if "metric_groups" in value:
        import capo_dsql.types.metric_group_request_list

        out["metricGroups"] = capo_dsql.types.metric_group_request_list.serialize_json(
            value["metric_groups"]
        )
    return out


def deserialize_json(data: dict) -> UpdateClusterInput:
    out: UpdateClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("deletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    if data.get("kmsEncryptionKey") is not None:
        out["kms_encryption_key"] = data["kmsEncryptionKey"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("multiRegionProperties") is not None:
        import capo_dsql.types.multi_region_properties

        out["multi_region_properties"] = (
            capo_dsql.types.multi_region_properties.deserialize_json(
                data["multiRegionProperties"]
            )
        )
    if data.get("metricGroups") is not None:
        import capo_dsql.types.metric_group_request_list

        out["metric_groups"] = (
            capo_dsql.types.metric_group_request_list.deserialize_json(
                data["metricGroups"]
            )
        )
    return out
