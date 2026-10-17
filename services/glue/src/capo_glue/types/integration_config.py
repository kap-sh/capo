"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.continuous_sync
    import capo_glue.types.integration_source_properties_map
    import capo_glue.types.string128
    import capo_glue.types.target_namespace


class IntegrationConfig(TypedDict, closed=True):
    refresh_interval: NotRequired["capo_glue.types.string128.String128"]
    """<p>Specifies the frequency at which CDC (Change Data Capture) pulls or incremental loads should occur. This parameter provides flexibility to align the refresh rate with your specific data update patterns, system load considerations, and performance optimization goals. Time increment can be set from 15 minutes to 8640 minutes (six days).</p>"""
    source_properties: NotRequired[
        "capo_glue.types.integration_source_properties_map.IntegrationSourcePropertiesMap"
    ]
    """<p> A collection of key-value pairs that specify additional properties for the integration source. These properties provide configuration options that can be used to customize the behavior of the ODB source during data integration operations. </p>"""
    continuous_sync: NotRequired["capo_glue.types.continuous_sync.ContinuousSync"]
    """<p>Enables continuous synchronization for on-demand data extractions from SaaS applications to Amazon Web Services data services like Amazon Redshift and Amazon S3.</p>"""
    target_namespace: NotRequired["capo_glue.types.target_namespace.TargetNamespace"]
    """<p>An optional custom namespace for the integration's target. Supply this parameter only when the target is an Amazon S3 Tables table bucket; it is not accepted for other target types. The integration replicates data into the namespace you specify, reusing it if it already exists. If you omit this parameter, the target namespace defaults to <code>zetl_</code> followed by the integration ID, with hyphens converted to underscores.</p> <p>The value is immutable after the integration is created; <code>ModifyIntegration</code> rejects changes to it. It must be a valid Amazon S3 Tables namespace name: 1 to 255 characters using lowercase letters, numbers, and underscores, with no leading or trailing underscore and no reserved <code>aws</code> prefix.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationConfig) -> dict:
    out: dict = {}
    if "refresh_interval" in value:
        out["RefreshInterval"] = value["refresh_interval"]
    if "source_properties" in value:
        import capo_glue.types.integration_source_properties_map

        out["SourceProperties"] = (
            capo_glue.types.integration_source_properties_map.serialize_aws_json_1_1(
                value["source_properties"]
            )
        )
    if "continuous_sync" in value:
        out["ContinuousSync"] = value["continuous_sync"]
    if "target_namespace" in value:
        out["TargetNamespace"] = value["target_namespace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegrationConfig:
    out: IntegrationConfig = {}  # type: ignore[typeddict-item]
    if data.get("RefreshInterval") is not None:
        out["refresh_interval"] = data["RefreshInterval"]
    if data.get("SourceProperties") is not None:
        import capo_glue.types.integration_source_properties_map

        out["source_properties"] = (
            capo_glue.types.integration_source_properties_map.deserialize_aws_json_1_1(
                data["SourceProperties"]
            )
        )
    if data.get("ContinuousSync") is not None:
        out["continuous_sync"] = data["ContinuousSync"]
    if data.get("TargetNamespace") is not None:
        out["target_namespace"] = data["TargetNamespace"]
    return out
