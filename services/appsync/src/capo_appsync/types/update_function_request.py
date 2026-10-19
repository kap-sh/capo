"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.app_sync_runtime
    import capo_appsync.types.code
    import capo_appsync.types.mapping_template
    import capo_appsync.types.max_batch_size
    import capo_appsync.types.resource_name
    import capo_appsync.types.string
    import capo_appsync.types.sync_config


class UpdateFunctionRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The GraphQL API ID.</p>"""
    name: "capo_appsync.types.resource_name.ResourceName"
    """<p>The <code>Function</code> name.</p>"""
    description: NotRequired["capo_appsync.types.string.String"]
    """<p>The <code>Function</code> description.</p>"""
    function_id: "capo_appsync.types.resource_name.ResourceName"
    """<p>The function ID.</p>"""
    data_source_name: "capo_appsync.types.resource_name.ResourceName"
    """<p>The <code>Function</code> <code>DataSource</code> name.</p>"""
    request_mapping_template: NotRequired[
        "capo_appsync.types.mapping_template.MappingTemplate"
    ]
    """<p>The <code>Function</code> request mapping template. Functions support only the 2018-05-29 version of the request mapping template.</p>"""
    response_mapping_template: NotRequired[
        "capo_appsync.types.mapping_template.MappingTemplate"
    ]
    """<p>The <code>Function</code> request mapping template.</p>"""
    function_version: NotRequired["capo_appsync.types.string.String"]
    """<p>The <code>version</code> of the request mapping template. Currently, the supported value is 2018-05-29. Note that when using VTL and mapping templates, the <code>functionVersion</code> is required.</p>"""
    sync_config: NotRequired["capo_appsync.types.sync_config.SyncConfig"]
    max_batch_size: NotRequired["capo_appsync.types.max_batch_size.MaxBatchSize"]
    """<p>The maximum batching size for a resolver.</p>"""
    runtime: NotRequired["capo_appsync.types.app_sync_runtime.AppSyncRuntime"]
    code: NotRequired["capo_appsync.types.code.Code"]
    """<p>The <code>function</code> code that contains the request and response functions. When code is used, the <code>runtime</code> is required. The <code>runtime</code> value must be <code>APPSYNC_JS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFunctionRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["dataSourceName"] = value["data_source_name"]
    if "request_mapping_template" in value:
        out["requestMappingTemplate"] = value["request_mapping_template"]
    if "response_mapping_template" in value:
        out["responseMappingTemplate"] = value["response_mapping_template"]
    if "function_version" in value:
        out["functionVersion"] = value["function_version"]
    if "sync_config" in value:
        import capo_appsync.types.sync_config

        out["syncConfig"] = capo_appsync.types.sync_config.serialize_json(
            value["sync_config"]
        )
    if "max_batch_size" in value:
        out["maxBatchSize"] = value["max_batch_size"]
    if "runtime" in value:
        import capo_appsync.types.app_sync_runtime

        out["runtime"] = capo_appsync.types.app_sync_runtime.serialize_json(
            value["runtime"]
        )
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> UpdateFunctionRequest:
    out: UpdateFunctionRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("dataSourceName") is not None:
        out["data_source_name"] = data["dataSourceName"]
    else:
        out["data_source_name"] = ""
    if data.get("requestMappingTemplate") is not None:
        out["request_mapping_template"] = data["requestMappingTemplate"]
    if data.get("responseMappingTemplate") is not None:
        out["response_mapping_template"] = data["responseMappingTemplate"]
    if data.get("functionVersion") is not None:
        out["function_version"] = data["functionVersion"]
    if data.get("syncConfig") is not None:
        import capo_appsync.types.sync_config

        out["sync_config"] = capo_appsync.types.sync_config.deserialize_json(
            data["syncConfig"]
        )
    if data.get("maxBatchSize") is not None:
        out["max_batch_size"] = data["maxBatchSize"]
    if data.get("runtime") is not None:
        import capo_appsync.types.app_sync_runtime

        out["runtime"] = capo_appsync.types.app_sync_runtime.deserialize_json(
            data["runtime"]
        )
    if data.get("code") is not None:
        out["code"] = data["code"]
    return out
