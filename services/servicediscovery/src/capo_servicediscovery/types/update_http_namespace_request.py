"""Generated from Smithy shape ``com.amazonaws.servicediscovery#UpdateHttpNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn
    import capo_servicediscovery.types.http_namespace_change
    import capo_servicediscovery.types.resource_id


class UpdateHttpNamespaceRequest(TypedDict, closed=True):
    id: "capo_servicediscovery.types.arn.Arn"
    """<p>The ID or Amazon Resource Name (ARN) of the namespace that you want to update.</p>"""
    updater_request_id: NotRequired[
        "capo_servicediscovery.types.resource_id.ResourceId"
    ]
    """<p>A unique string that identifies the request and that allows failed <code>UpdateHttpNamespace</code> requests to be retried without the risk of running the operation twice. <code>UpdaterRequestId</code> can be any unique string (for example, a date/timestamp).</p>"""
    namespace: "capo_servicediscovery.types.http_namespace_change.HttpNamespaceChange"
    """<p>Updated properties for the the HTTP namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHttpNamespaceRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "updater_request_id" in value:
        out["UpdaterRequestId"] = value["updater_request_id"]
    import capo_servicediscovery.types.http_namespace_change

    out["Namespace"] = (
        capo_servicediscovery.types.http_namespace_change.serialize_aws_json_1_1(
            value["namespace"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHttpNamespaceRequest:
    out: UpdateHttpNamespaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("UpdaterRequestId") is not None:
        out["updater_request_id"] = data["UpdaterRequestId"]
    if data.get("Namespace") is not None:
        import capo_servicediscovery.types.http_namespace_change

        out["namespace"] = (
            capo_servicediscovery.types.http_namespace_change.deserialize_aws_json_1_1(
                data["Namespace"]
            )
        )
    else:
        raise DeserializationError("UpdateHttpNamespaceRequest.namespace required")
    return out
