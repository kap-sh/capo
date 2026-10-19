"""Generated from Smithy shape ``com.amazonaws.omics#InlineSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.aws_account_id
    import capo_omics.types.engine_settings
    import capo_omics.types.run_name
    import capo_omics.types.run_output_uri
    import capo_omics.types.run_parameters
    import capo_omics.types.run_setting_id
    import capo_omics.types.tag_map


class InlineSetting(TypedDict, closed=True):
    run_setting_id: "capo_omics.types.run_setting_id.RunSettingId"
    """<p>A customer-provided unique identifier for this run configuration within the batch. After submission, use <code>ListRunsInBatch</code> to map each <code>runSettingId</code> to the HealthOmics-generated <code>runId</code>.</p>"""
    name: NotRequired["capo_omics.types.run_name.RunName"]
    """<p>An optional user-friendly name for this run.</p>"""
    output_uri: NotRequired["capo_omics.types.run_output_uri.RunOutputUri"]
    """<p>Override the destination S3 URI for this run's outputs.</p>"""
    priority: NotRequired["int"]
    """<p>Override the priority for this run.</p>"""
    parameters: NotRequired["capo_omics.types.run_parameters.RunParameters"]
    """<p>Per-run workflow parameters. Merged with <code>defaultRunSetting.parameters</code>; values in this object take precedence when keys overlap.</p>"""
    output_bucket_owner_id: NotRequired["capo_omics.types.aws_account_id.AwsAccountId"]
    """<p>The expected Amazon Web Services account ID of the owner of the output S3 bucket for this run.</p>"""
    run_tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>Per-run Amazon Web Services tags. Merged with <code>defaultRunSetting.runTags</code>; values in this object take precedence when keys overlap.</p>"""
    engine_settings: NotRequired["capo_omics.types.engine_settings.EngineSettings"]
    """<p>Per-run engine-specific settings. Use this field to specify configuration options that are specific to the workflow engine (for example, Nextflow profiles). Overrides <code>defaultRunSetting.engineSettings</code> for this run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineSetting) -> dict:
    out: dict = {}
    out["runSettingId"] = value["run_setting_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "output_uri" in value:
        out["outputUri"] = value["output_uri"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "parameters" in value:
        out["parameters"] = value["parameters"]
    if "output_bucket_owner_id" in value:
        out["outputBucketOwnerId"] = value["output_bucket_owner_id"]
    if "run_tags" in value:
        import capo_omics.types.tag_map

        out["runTags"] = capo_omics.types.tag_map.serialize_json(value["run_tags"])
    if "engine_settings" in value:
        out["engineSettings"] = value["engine_settings"]
    return out


def deserialize_json(data: dict) -> InlineSetting:
    out: InlineSetting = {}  # type: ignore[typeddict-item]
    if data.get("runSettingId") is not None:
        out["run_setting_id"] = data["runSettingId"]
    else:
        out["run_setting_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("outputUri") is not None:
        out["output_uri"] = data["outputUri"]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("parameters") is not None:
        out["parameters"] = data["parameters"]
    if data.get("outputBucketOwnerId") is not None:
        out["output_bucket_owner_id"] = data["outputBucketOwnerId"]
    if data.get("runTags") is not None:
        import capo_omics.types.tag_map

        out["run_tags"] = capo_omics.types.tag_map.deserialize_json(data["runTags"])
    if data.get("engineSettings") is not None:
        out["engine_settings"] = data["engineSettings"]
    return out
