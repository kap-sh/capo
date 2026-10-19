"""Generated from Smithy shape ``com.amazonaws.omics#StartRunBatchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.batch_name
    import capo_omics.types.batch_request_id
    import capo_omics.types.batch_run_settings
    import capo_omics.types.default_run_setting
    import capo_omics.types.tag_map


class StartRunBatchRequest(TypedDict, closed=True):
    batch_name: NotRequired["capo_omics.types.batch_name.BatchName"]
    """<p>An optional user-friendly name for the run batch.</p>"""
    request_id: "capo_omics.types.batch_request_id.BatchRequestId"
    """<p>A client token used to deduplicate retry requests and prevent duplicate batches from being created.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>Amazon Web Services tags to associate with the batch resource. These tags are not inherited by individual runs. To tag individual runs, use <code>defaultRunSetting.runTags</code>.</p>"""
    default_run_setting: "capo_omics.types.default_run_setting.DefaultRunSetting"
    """<p>Shared configuration applied to all runs in the batch. See <code>DefaultRunSetting</code>.</p>"""
    batch_run_settings: "capo_omics.types.batch_run_settings.BatchRunSettings"
    """<p>The individual run configurations. Specify exactly one of <code>inlineSettings</code> or <code>s3UriSettings</code>. See <code>BatchRunSettings</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRunBatchRequest) -> dict:
    out: dict = {}
    if "batch_name" in value:
        out["batchName"] = value["batch_name"]
    out["requestId"] = value["request_id"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    import capo_omics.types.default_run_setting

    out["defaultRunSetting"] = capo_omics.types.default_run_setting.serialize_json(
        value["default_run_setting"]
    )
    import capo_omics.types.batch_run_settings

    out["batchRunSettings"] = capo_omics.types.batch_run_settings.serialize_json(
        value["batch_run_settings"]
    )
    return out


def deserialize_json(data: dict) -> StartRunBatchRequest:
    out: StartRunBatchRequest = {}  # type: ignore[typeddict-item]
    if data.get("batchName") is not None:
        out["batch_name"] = data["batchName"]
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    else:
        out["request_id"] = ""
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if data.get("defaultRunSetting") is not None:
        import capo_omics.types.default_run_setting

        out["default_run_setting"] = (
            capo_omics.types.default_run_setting.deserialize_json(
                data["defaultRunSetting"]
            )
        )
    else:
        raise DeserializationError("StartRunBatchRequest.default_run_setting required")
    if data.get("batchRunSettings") is not None:
        import capo_omics.types.batch_run_settings

        out["batch_run_settings"] = (
            capo_omics.types.batch_run_settings.deserialize_json(
                data["batchRunSettings"]
            )
        )
    else:
        import capo_omics.types._unknown

        out["batch_run_settings"] = capo_omics.types._unknown.UnknownUnionMember("")
    return out
