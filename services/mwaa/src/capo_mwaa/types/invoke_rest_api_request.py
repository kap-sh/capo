"""Generated from Smithy shape ``com.amazonaws.mwaa#InvokeRestApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mwaa.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mwaa.types.environment_name
    import capo_mwaa.types.rest_api_method
    import capo_mwaa.types.rest_api_path
    import capo_mwaa.types.rest_api_request_body


class InvokeRestApiRequest(TypedDict, closed=True):
    name: "capo_mwaa.types.environment_name.EnvironmentName"
    """<p>The name of the Amazon MWAA environment. For example, <code>MyMWAAEnvironment</code>.</p>"""
    path: "capo_mwaa.types.rest_api_path.RestApiPath"
    """<p>The Apache Airflow REST API endpoint path to be called. For example, <code>/dags/123456/clearTaskInstances</code>. For more information, see <a href="https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html">Apache Airflow API</a> </p>"""
    method: "capo_mwaa.types.rest_api_method.RestApiMethod"
    """<p>The HTTP method used for making Airflow REST API calls. For example, <code>POST</code>. </p>"""
    query_parameters: NotRequired["object"]
    """<p>Query parameters to be included in the Apache Airflow REST API call, provided as a JSON object. </p>"""
    body: NotRequired["capo_mwaa.types.rest_api_request_body.RestApiRequestBody"]
    """<p>The request body for the Apache Airflow REST API call, provided as a JSON object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeRestApiRequest) -> dict:
    out: dict = {}
    out["Path"] = value["path"]
    out["Method"] = value["method"]
    if "query_parameters" in value:
        out["QueryParameters"] = value["query_parameters"]
    if "body" in value:
        out["Body"] = value["body"]
    return out


def deserialize_json(data: dict) -> InvokeRestApiRequest:
    out: InvokeRestApiRequest = {}  # type: ignore[typeddict-item]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    else:
        raise DeserializationError("InvokeRestApiRequest.path required")
    if data.get("Method") is not None:
        out["method"] = data["Method"]
    else:
        raise DeserializationError("InvokeRestApiRequest.method required")
    if data.get("QueryParameters") is not None:
        out["query_parameters"] = data["QueryParameters"]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    return out
